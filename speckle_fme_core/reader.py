"""
SpeckleFMEReader — FME Pluginbuilder Reader class.

Lifecycle (called by FME):
  open(datasetName, parameters)  — once before read() / readSchema()
  readSchema()                   — repeatedly during schema discovery; return FMEFeature | None
  read()                         — repeatedly during data read; return FMEFeature | None
  close()                        — after EOF or abort (may be called multiple times)
  abort()                        — before close() on error

IMPORTANT:
  - In data-read mode, open() receives EMPTY parameters — fetch all config from mappingFile.
  - close() can be called more than once; guard with self._closed.
  - readSchema() and read() are mutually exclusive per open() call.
"""

from __future__ import annotations

import fmeobjects
import pluginbuilder

from speckle_fme_core.auth import client_from_mapping_file
from speckle_fme_core.api import SpeckleFMEError, get_latest_version_id
from speckle_fme_core.schema import get_container_names, get_eav_paths
from speckle_fme_core.bundle_receive import receive


_IDENTITY_ATTRS = [
    ("speckle_application_id", "fme_varchar(256)"),
    ("speckle_type", "fme_varchar(256)"),
    ("speckle_units", "fme_varchar(32)"),
]


class SpeckleFMEReader(pluginbuilder.FMEReader):

    def __init__(self, readerTypeName, readerKeyword, mappingFile):
        super().__init__()
        self._type_name = readerTypeName
        self._keyword = readerKeyword
        self._mapping_file = mappingFile
        self._keyword_prefix = readerKeyword + "_"
        self._type_prefix = readerTypeName + "_"
        self._client = None
        self._version_id = None
        self._project_id = None
        self._model_id = None
        self._feature_iter = None
        self._closed = False
        self._log = fmeobjects.FMELogFile()

    def _fetch_param(self, name: str) -> str:
        return (
            self._mapping_file.fetchWithPrefix(
                self._keyword_prefix, self._type_prefix, name
            )
            or ""
        )

    def open(self, datasetName, parameters):
        self._client = client_from_mapping_file(
            self._mapping_file, self._keyword_prefix, self._type_prefix
        )
        self._project_id = self._fetch_param("SPECKLE_PROJECT_ID")
        self._model_id = self._fetch_param("SPECKLE_MODEL_ID")
        version_id = self._fetch_param("SPECKLE_VERSION_ID")

        if not version_id:
            version_id = get_latest_version_id(
                self._client, self._project_id, self._model_id
            )
        self._version_id = version_id
        self._log.logMessageString(
            f"Speckle: reading version {self._version_id}", fmeobjects.FME_INFORM
        )

    def readSchema(self):
        # TODO: Stage 2 — implement readSchema()
        # Use get_container_names() + get_eav_paths() to build schema features.
        return None

    def read(self):
        # TODO: Stage 4 — implement read()
        # Drive bundle_receive.receive() to yield feature data → FMEFeature
        return None

    def close(self):
        if self._closed:
            return
        self._closed = True

    def abort(self):
        pass
