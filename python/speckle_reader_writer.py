"""
FME plugin entry point for the Speckle Format Reader/Writer.

FME calls FME_createReader / FME_createWriter at startup to instantiate the
reader and writer classes. Both classes live in speckle_fme_core.

See:
  https://docs.safe.com/fme/html/fmepython/api/pluginbuilder.html
"""

from speckle_fme_core.reader import SpeckleFMEReader
from speckle_fme_core.writer import SpeckleFMEWriter


def FME_createReader(readerTypeName, readerKeyword, mappingFile):
    return SpeckleFMEReader(readerTypeName, readerKeyword, mappingFile)


def FME_createWriter(writerType, destKeyword, mappingFile):
    return SpeckleFMEWriter(writerType, destKeyword, mappingFile)
