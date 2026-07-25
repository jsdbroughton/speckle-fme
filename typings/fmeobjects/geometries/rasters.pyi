from fmeobjects.geometries.general import FMEGeometry

# Tile Type
FME_TILE_TYPE_FIXED: int
FME_TILE_TYPE_FIXED_MULTIPLE: int
FME_TILE_TYPE_FLEXIBLE: int

# Data Type
FME_DATA_TYPE_NULL: int
FME_DATA_TYPE_REAL64: int
FME_DATA_TYPE_REAL32: int
FME_DATA_TYPE_UINT64: int
FME_DATA_TYPE_INT64: int
FME_DATA_TYPE_UINT32: int
FME_DATA_TYPE_INT32: int
FME_DATA_TYPE_UINT16: int
FME_DATA_TYPE_INT16: int
FME_DATA_TYPE_UINT8: int
FME_DATA_TYPE_INT8: int

class FMERaster(FMEGeometry):
    pass

class FMERasterProperties:
    pass

class FMEBand:
    pass

class FMEBandProperties:
    pass

class FMEPalette:
    pass

class FMETile:
    """FME Tile Class

    FMETile is an abstract class. It cannot be created directly.
    """

    def __init__(self) -> None:
        """Initialze self. See help(type(self)) for accurate signature."""
    def getByteArray(self) -> list[bytearray]:
        """Returns a list of bytearrays where each bytearray represents the data
        values of each row of the tile.

        Returns:
            list[bytearray]: The data values of the tile.
        """
    def getDataAsStringArray(self, startRow: int, startCol: int, numRows: int, numCols: int) -> list[str]:
        """Get a list that contains values of the tiles. One string is added to
        the list for each cell in the specified area.

        If the specified area falls outside the bounds of the tile, the string
        array will not be modified. ‘startRow’, ‘startCols’, numRows’, and ‘numCols’
        should be integers greater than or equal to 0.

        Args:
          startRow (int): The starting row.
          startCol (int): The starting column.
          numRows (int): The number of rows.
          numCols (int): The number of columns.

        Returns:
          list[str]: The data as a string array.
        """
    def getDataType(self) -> int:
        """Returns the data type of the raster tile.

        Returns one of:
        - FME_DATA_TYPE_NULL
        - FME_DATA_TYPE_REAL64
        - FME_DATA_TYPE_REAL32
        - FME_DATA_TYPE_UINT64
        - FME_DATA_TYPE_INT64
        - FME_DATA_TYPE_UINT32
        - FME_DATA_TYPE_INT32
        - FME_DATA_TYPE_UINT16
        - FME_DATA_TYPE_INT16
        - FME_DATA_TYPE_UINT8
        - FME_DATA_TYPE_INT8

        Returns:
            int: Data type of a raster tile. For example:
                An FMEInt32Tile would return FME_DATA_TYPE_INT32.
                An FMERGBA64Tile would return FME_DATA_TYPE_UINT16.
                An FMEStringTile would return FME_DATA_TYPE_UINT8.
        """
    def getDataTypeBitDepth(self) -> int:
        """Returns the bit depth of the data type of the raster tile.

        Returns:
            int: The number of bits in the data type of a raster tile. For example:
                An FMEInt32Tile would return 32.
                An FMERGBA64Tile would return 16.
                An FMEStringTile would return 8.
        """
    def getInterpretation(self) -> int:
        """Returns the interpretation of the raster tile.

        Returns one of:
        - FME_INTERPRETATION_NULL
        - FME_INTERPRETATION_REAL64
        - FME_INTERPRETATION_REAL32
        - FME_INTERPRETATION_UINT64
        - FME_INTERPRETATION_INT64
        - FME_INTERPRETATION_UINT32
        - FME_INTERPRETATION_INT32
        - FME_INTERPRETATION_UINT16
        - FME_INTERPRETATION_INT16
        - FME_INTERPRETATION_UINT8
        - FME_INTERPRETATION_INT8
        - FME_INTERPRETATION_GRAY8
        - FME_INTERPRETATION_GRAY16
        - FME_INTERPRETATION_RED8
        - FME_INTERPRETATION_RED16
        - FME_INTERPRETATION_GREEN8
        - FME_INTERPRETATION_GREEN16
        - FME_INTERPRETATION_BLUE8
        - FME_INTERPRETATION_BLUE16
        - FME_INTERPRETATION_ALPHA8
        - FME_INTERPRETATION_ALPHA16
        - FME_INTERPRETATION_NULL
        - FME_INTERPRETATION_RGB24
        - FME_INTERPRETATION_RGBA32
        - FME_INTERPRETATION_RGB48
        - FME_INTERPRETATION_RGBA64
        - FME_INTERPRETATION_STRING

        Returns:
            int: The interpretation of a raster tile. For example:
                An FMERGBA64Tile would return FME_INTERPRETATION_RGBA64.
                An FMERGBA64Tile would return FME_INTERPRETATION_RGBA64.
                An FMEStringTile would return FME_INTERPRETATION_STRING.
        """
    def getInterpretationBitDepth(self) -> int:
        """Returns the bit depth of the interpretation of the raster tile.

        Returns:
            int: The number of bits in the interpretation of a raster tile. For example:
                An FMEInt32Tile would return 32.
                An FMERGBA64Tile would return 64.
                An FMEStringTile would return 8 * stringLength.
        """
    def getInterpretationNumComponents(self) -> int:
        """Returns the number of components in the interpretation of the raster tile.

        Returns:
            int: The number of components in the interpretation of a raster tile. For example:
                An FMEInt32Tile would return 1.
                An FMERGBA64Tile would return 4.
                An FMEStringTile would return 1.
        """
    def getNumCols(self) -> int:
        """Returns the number of columns in the raster tile.

        Returns:
            int: The number of columns in the raster tile.
        """
    def getNumDataTypesPerCell(self) -> int:
        """Returns the number of data types in a cell.

        Returns:
            int: The number of instances of the data type. For example:
              An FMEInt32Tile would return 1.
              An FMERGBA64Tile would return 4.
              An FMEStringTile would return stringLength.
        """
    def getNumRows(self) -> int:
        """Returns the number of rows in the raster tile.

        Returns:
            int: The number of rows in the raster tile.
        """
    def getTileByteLength(self) -> int:
        """Returns the length of the tile in bytes.

        This is equal to numRows * numCols * (interpretationBitDepth / 8)).

        Returns:
            int: The length of the tile in bytes.
        """
    def getTileNumComponents(self) -> int:
        """Returns the number of components in the tile.

        This is equal to numRows * numCols * interpretationNumComponents.

        Returns:
            int: The number of components in the tile.
        """

class FMEAlpha8Tile(FMETile):
    pass

class FMEAlpha16Tile(FMETile):
    pass

class FMEBlue8Tile(FMETile):
    pass

class FMEBlue16Tile(FMETile):
    pass

class FMEGray8Tile(FMETile):
    pass

class FMEGray16Tile(FMETile):
    pass

class FMEGreen8Tile(FMETile):
    pass

class FMEGreen16Tile(FMETile):
    pass

class FMEInt8Tile(FMETile):
    pass

class FMEInt16Tile(FMETile):
    pass

class FMEInt32Tile(FMETile):
    pass

class FMEInt64Tile(FMETile):
    pass

class FMERGB24Tile(FMETile):
    pass

class FMERGB48Tile(FMETile):
    pass

class FMERGBA32Tile(FMETile):
    pass

class FMERGBA64Tile(FMETile):
    pass

class FMEReal32Tile(FMETile):
    pass

class FMEReal64Tile(FMETile):
    pass

class FMERed8Tile(FMETile):
    pass

class FMERed16Tile(FMETile):
    pass

class FMEUInt8Tile(FMETile):
    pass

class FMEUInt16Tile(FMETile):
    pass

class FMEUInt32Tile(FMETile):
    pass

class FMEUInt64Tile(FMETile):
    pass

class FMEStringTileg(FMETile):
    pass
