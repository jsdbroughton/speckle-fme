"""
SpeckleFMEWriter — FME Pluginbuilder Writer class.

Lifecycle (called by FME):
  open(datasetName, parameters)  — once; parameters is EMPTY in single-writer mode
  write(feature)                 — repeatedly with each FMEFeature
  close()                        — commit / finalise version (may be called multiple times)
  abort()                        — before close() on error

multiFileWriter() returns False → single writer instance per translation.
One Speckle version is created per FME workspace run.
"""

from __future__ import annotations

import fmeobjects
import pluginbuilder

from speckle_fme_core.auth import client_from_mapping_file
from speckle_fme_core.bundle_publish import publish


class SpeckleFMEWriter(pluginbuilder.FMEWriter):

    def __init__(self, writerType, destKeyword, mappingFile):
        super().__init__()
        self._type_name = writerType
        self._keyword = destKeyword
        self._mapping_file = mappingFile
        self._keyword_prefix = destKeyword + "_"
        self._type_prefix = writerType + "_"
        self._client = None
        self._project_id = None
        self._model_id = None
        self._commit_message = None
        self._features: list = []
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
        self._model_id = self._fetch_param("SPECKLE_MODEL_ID") or "main"
        self._commit_message = self._fetch_param("SPECKLE_COMMIT_MESSAGE")

    def write(self, feature):
        # TODO: Stage 2 — buffer features for bundle publish
        # For large datasets, stream directly into ObjectsArtifactPipeline
        # rather than buffering all features in memory.
        self._features.append(feature)

    def close(self):
        if self._closed:
            return
        self._closed = True

        if not self._features:
            return

        # TODO: Stage 1 — call publish()
        # version_id = publish(
        #     self._client,
        #     self._project_id,
        #     self._model_id,
        #     self._features,
        #     commit_message=self._commit_message,
        #     log=self._log,
        # )
        # self._log.logMessageString(
        #     f"Speckle: published version {version_id}", fmeobjects.FME_INFORM
        # )

    def abort(self):
        self._features.clear()

    def multiFileWriter(self):
        return False
