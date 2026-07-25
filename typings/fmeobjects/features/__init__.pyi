from typing import Any, overload

from fmeobjects.geometries.general import FMEGeometry

class FMEFeature:
    """FME Feature Class"""

    @overload
    def __init__(self) -> None:
        """Default FMEFeature constructor

        Returns:
            FMEFeature: An instance of a Feature object."""
    @overload
    def __init__(self, feature: FMEFeature) -> None:
        """Creat a copy of the passed in Feature object.

        Args:
            feature (FMEFeature): The feature to copy.

        Returns:
            FMEFeature: An instance of a Feature object."""
    def addCoordinate(self, x: float, y: float, z: float = ...) -> None:
        """Add a coordinate to the part.

        If the feature is two-dimensional, any provided third coordinate is ignored.

        Args:
            x (float): The x coordinate.
            y (float): The y coordinate.
            z (float): The z coordinate.
        """
    def addCoordinates(self, coordinates: list[tuple[float, float, float]]) -> None:
        """Adds coordinates onto the feature.

        Missing values are replaced by 0. If the feature is two-dimensional, any provided third coordinate is ignored.

        Args:
            coordinates (list[tuple[float,float,float]]): The list of coordinates.
        """
    def boundingBox(self) -> list[list[float]]:
        """Get the bounding box of the feature.

        Returns:
            (list[list[float]]): The bounding box of the feature, in the
                form ((minx, miny), (maxx, maxy)).

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def boundingCube(
        self,
    ) -> tuple[tuple[float, float, float], tuple[float, float, float]]:
        """Get the bounding cube of the feature.

        Returns:
            (tuple[tuple[float,float,float],tuple[float,float,float]]): The bounding
                cube of the feature, in the form ((minx, miny, minz), (maxx, maxy, maxz)).

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def buffer(self, width: float, sampleAngle: float) -> None:
        """This method generates a buffer around the feature.

        The features geometry is replaced by the new buffer geometry. If the feature
        is an area feature then the buffer is only generated on the outside (and
        inside holes) of the feature.

        Args:
            width (float): The number of ground units to buffer around the feature.
            sampleAngle (float): The sampling angle. If 5 then there is a vertex
                on the buffer every 5 degrees.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def buildAggregateFeat(self, featureList: list[FMEFeature]) -> None:
        """Build an aggregate feature from a list of features.

        Args:
            featureList (list[FMEFeature]): The list of features to aggregate.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def changeCase(self, changeOpt: int, matchExp: str | list[str], caseTpe: int) -> None:
        """Change the letter case of attribute names and values.

        Args:
            changeOpt (int): The change option.
            matchExp (str or list[str]): The match expression.
            caseTpe (int): The new case to change the letters of the attribute
                names and values to.

                Must be one of:
                - FME_UPPERCASE
                - FME_LOWERCASE
                - FME_TITLECASE
                - FME_FULLTITLECASE
        Raise:
            FMEException: An exception is raised if an error occurred.
        """
    def chopUp(self, vertexThreshold: int) -> bool:
        """Convert a feature into an aggregate where each member of the aggregate
        has fewer than the threshold number of vertices.

        If the feature was an area based feature, it will do area chopping,
        subdividing the area so that no area piece has more than the number of
        vertices.

        If the feature was linear, then the line is broken into chunks that meet
        the size criteria.

        Args:
            vertexThreshold (int): The threshold number of vertices.

        Returns:
            bool: True if the feature was chopped up, False otherwise.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def cloneAttributes(self) -> FMEFeature:
        """Create a new FMEFeature with only the attributes of this one copied over.

        Returns:
            FMEFeature: A new FMEFeature with the same attributes as the original.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def convertAnyArcToPoints(
        self,
        center: tuple[float, float],
        semiPrimaryAxis: float,
        semiSecondaryAxis: float,
        origNumSamps: int,
        startAngle: float,
        sweepAngle: float,
        rotation: float,
    ) -> None:
        """Strokes an arc feature to be a points.

        Args:
            center (tuple[float,float]): The center of the arc.
            semiPrimaryAxis (float): The semi-primary axis of the arc.
            semiSecondaryAxis (float): The semi-secondary axis of the arc.
            origNumSamps (int): The number of samples to use.
            startAngle (float): The start angle of the arc.
            sweepAngle (float): The sweep angle of the arc.
            rotation (float): The rotation of the arc.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def convertArcToPointUseAttributes(self) -> None:
        """Return the bounding cube of the feature in the format ((min x, min y,
        min z), (max x, max y, max z)) Strokes an arc feature to be a polygon or
        line. The parameters used to stroke the arc or ellipse are retrieved from
        the related attributes. Arcs with a sweep angle of 360 degrees will be
        converted into a polygon.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def convertArcToPoints(
        self,
        center: tuple[float, float],
        semiPrimaryAxis: float,
        semiSecondaryAxis: float,
        origNumSamps: int,
        startAngle: float,
        sweepAngle: float,
        rotation: float,
    ) -> None:
        """Strokes an arc feature to be a polygon or line.

        Args:
            center (tuple[float,float]): The center of the arc.
            semiPrimaryAxis (float): The semi-primary axis of the arc.
            semiSecondaryAxis (float): The semi-secondary axis of the arc.
            origNumSamps (int): The number of samples to use.
            startAngle (float): The start angle of the arc.
            sweepAngle (float): The sweep angle of the arc.
            rotation (float): The rotation of the arc.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def convertPointsToArc(self, radiusAttrName: str, startAngleAttrName: str, sweepAngleAttrName: str) -> None:
        """Converts the feature into a point feature with attributes required to
        define it as an arc. If the feature has more than 3 points, the arc is
        approximated.

        Args:
            radiusAttrName (str): The attribute name of the radius.
            startAngleAttrName (str): The attribute name of the start angle.
            sweepAngleAttrName (str): The attribute name of the sweep angle.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def deserialize(self, buffer: bytearray, parameters: dict[str, str]) -> bool:
        """Restore the state of the FMEFeature from the specified buffer.

        Args:
            buffer (bytearray): The buffer from which the state of the feature is
                restored from.
            parameters (dict[str,str]): (Optional) Possible name-value pairs are:

                - kFME_FeatureDeserializeOption:
                    - kFME_FeatureDeserializeReset: (Default) Reset the original
                    feature before restoring the state of the FMEFeature.
                    - kFME_FeatureDeserializeMerge: When restoring the state of
                    the FMEFeature, the original feature will NOT be reset; the
                    original information in the feature will be preserved when
                    there is no corresponding information in the buffer. Attributes,
                    geometry, coordinate system information, etc. taken from the
                    buffer will overwrite such information on the feature if necessary.
                - kFME_FeatureDeserializeSidecarBasename:
                    File from which to read extra geometry data: The path and
                    basename (not including file extension) from which additional
                    data will be read for some geometries (raster, point cloud).
                    If this option is not specified for those geometries, they
                    may return an error when data is requested (e.g. when writing
                    out a raster).

        Returns:
            bool: True on success, False otherwise.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def exportGeometryToOGCWKB(self, version: int) -> bytearray | bytes | None:
        """Convert the geometry of the feature to the OGC Well Known Binary format.

        Args:
            version (int): Optional) The OGC Version to use. Must be one of:
                - ogcvOneDotOne (default)
                - ogcvOneDotTwo
                - ogcvPostGISPreOneDotZero
                - ogcvPostGISOneDotZero
                - ogcvPostGISOneWithSQLMM3

        Returns:
            bytearray or bytes or None: A buffer representing the geometry of the
                feature converted to the OGCWKB.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def exportGeometryToOGCWKT(self, version: int) -> str:
        """Convert the geometry of the feature to the OGC Well Known Text format.

        Args:
            version (int): Optional) The OGC Version to use. Must be one of:
                - ogcvOneDotOne (default)
                - ogcvOneDotTwo
                - ogcvPostGISPreOneDotZero
                - ogcvPostGISOneDotZero
                - ogcvPostGISOneWithSQLMM3

        Returns:
            str: A string representing the geometry of the feature converted
                to the OGCWKT.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def generatePointInPolygon(self, pretty: bool) -> tuple[float, float, float]:
        """Generate a point somewhere inside the polygon.

        If the feature is 3D, the Z value is calculated to be the average of all
        points on the feature.

        Args:
            pretty (bool): (Optional) Generate a point that has a more central
                position, however more computational time may be required (default
                is False).

        Returns:
            tuple[float,float,float]: A point somewhere inside the polygon.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getAllAttributeNames(self) -> list[str]:
        """This method returns a complete, exhaustive list of all the attribute
        names present in the feature.

        Returns:
            list[str]: A list of all attribute names.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getAllCoordinates(self) -> list[tuple[float, float, float]]:
        """Get all the coordinates in this feature.

        Returns a list of coordinates, each as a tuple of floats.

        Returns:
            list[tuple[float,float,float]]: A list of all coordinates.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getAttribute(
        self,
        attrName: str,
        desiredType: type = str,
        fallback: bool | int | float | str | bytes | bytearray | list[Any] | None = "",  # ignore
    ) -> bool | int | float | str | bytes | bytearray | list[Any] | None:
        """Get the value of an attribute.

        Args:
            attrName (str): The name of the attribute.
            desiredType (type): (Optional) The desired type for the attribute value
                to be returned as. Possible values are bool, int, float, str, bytes,
                bytearray, and list.
            fallback (bool): (Optional) If specified, this value is returned
                instead of raising FMEException on conversion failures.

        Returns:
            bool or int or float or str or bytes or bytearray or list[Any] or None:
                The value of the attribute.

        Raises:
            FMEException: An exception is raised if there was a problem in retrieving
                the attribute value.
        """
    def getAttributeAsType(
        self, attrName: str, attrType: int, fallback: Any
    ) -> bool | int | float | str | list[str] | bytearray | list[bytearray] | bytes | list[bytes] | None:
        """[DEPRECATED] Get the value of the named attribute, casted to the specified
        FME type, then to an appropriate python type.

        An optional third parameter can be specified to be returned as a fallback
        in case type conversion fails.

        Example: getAttributeAsType(“output_file_type”, fmeobjects.FME_ATTR_STRING, “png”)

        The enum value fmeobjects.FME_ATTR_UNDEFINED can be used to retrieve a list
        object. If used to try and get a single attribute as a list, or a list as
        a single type, there is automatic conversion failure.

        A return of None indicates the attribute does not exist.

        Args:
            attrName (str): The name of the attribute.
            attrType (int): The type of the attribute.
            fallback (Any): (Optional) If specified, this value is returned instead
                of raising FMEException on conversion failures.

        Returns:
            bool or int or float or str or bytes or bytearray or list[Any] or None:
                The value of the attribute.

        Raises:
            FMEException: An exception is raised if there was a problem in retrieving
                or converting the attribute value.
        """
    def getAttributeNullMissingAndType(self, attributeName: str) -> tuple[bool, bool, int]:
        """[DEPRECATED] This method returns a tuple of a boolean indicating if the
        attribute is null, a boolean indicating if the attribute is missing, and
        an integer representing the type of the attribute.

        The first boolean is True if attributeName maps to a null attribute value
        on the feature. Otherwise it is False. The second boolean is True if
        attributeName maps to no value on the feature. Otherwise it is False. If
        the attribute is absent, FME_ATTR_UNDEFINED is returned for the type,
        otherwise the attribute type is returned.

        Args:
            attributeName (str): The name of the attribute.

        Returns:
            tuple[bool, bool, int]: A tuple of 2 boolean values and an integer.
                The first boolean indicating whether or not the value of the
                attribute is null, the second boolean indicating whether or not
                the attribute is missing, and the integer representing the
                attribute type. Attribute type int values are represented by the
                constants FME_ATTR_UNDEFINED, FME_ATTR_BOOLEAN, FME_ATTR_INT8,
                FME_ATTR_UINT8, FME_ATTR_INT16, FME_ATTR_UINT16, FME_ATTR_INT32,
                FME_ATTR_UINT32, FME_ATTR_REAL32, FME_ATTR_REAL64, FME_ATTR_REAL80,
                FME_ATTR_STRING, FME_ATTR_ENCODED_STRING, FME_ATTR_INT64,
                or FME_ATTR_UINT64."""
    def getAttributeType(self, attrName: str) -> int:
        """Get the type of the named attribute.

        Args:
            attrName (str): The name of the attribute.

        Returns:
            int: The type of the attribute. Attribute type int values are
                represented by the constants FME_ATTR_UNDEFINED, FME_ATTR_BOOLEAN,
                FME_ATTR_INT8, FME_ATTR_UINT8, FME_ATTR_INT16, FME_ATTR_UINT16,
                FME_ATTR_INT32, FME_ATTR_UINT32, FME_ATTR_REAL32, FME_ATTR_REAL64,
                FME_ATTR_REAL80, FME_ATTR_STRING, FME_ATTR_ENCODED_STRING,
                FME_ATTR_INT64, or FME_ATTR_UINT64."""
    def getCoordSys(self) -> str:
        """Get the coordinate system of the feature.

        Returns:
            str: The coordinate system of the feature.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getCoordinate(self, index: int) -> tuple[float, float, float]:
        """Access the feature's individual coordinates by index.

        The index must be in the range 0 .. ( numCoords() - 1).

        Args:
            index (int): The index of the coordinate.

        Returns:
            tuple[float,float, float]: The coordinate at the specified index.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getDimension(self) -> int:
        """Get the dimension of the feature.

        Returns either FME_TWO_D or FME_THREE_D

        Returns:
            int: The dimension of the feature."""
    def getDonutParts(self) -> list[FMEFeature]:
        """Break a donut feature into its constituent parts. The first part is
        the outer shell of the donut polygon, and the following parts are the
        holes. All of the parts have the same attributes and feature type as the
        original feature.

        Returns:
            list[FMEFeature]: The donut parts of the feature.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getFeatureType(self) -> str:
        """Get the feature type of the feature.

        Returns:
            str: The feature type of the feature."""
    def getGeometry(self) -> FMEGeometry:
        """Get the geometry of the feature.

        Returns:
            FMEGeometry: The geometry of the feature. Note: This method returns
                a terminal geometry type of the FMEGeometry; i.e. one of the leaf
                classes in the FMEGeometry inheritance graph. For example, a
                FMEPoint is returned if the geometry truly is a point."""
    def getGeometryType(self) -> int:
        """Get the geometry type of the feature.

        Returns:
            int: The geometry type of the feature. Returns one of FME_GEOM_UNDEFINED,
            FME_GEOM_POINT, FME_GEOM_LINE, FME_GEOM_POLYGON, FME_GEOM_DONUT,
            FME_GEOM_PIP, or FME_GEOM_AGGREGATE."""
    def getSequencedAttributeNames(self) -> list[str]:
        """This method gets a list of sequenced attribute names in the order they
        were added to the feature.

        The attrNames list is only populated for schema features. The list will
        not contain sequenced attribute names for data features.

        Returns:
            list[str]: The names of the attributes in the feature."""
    def hasGeometry(self) -> bool:
        """[DEPRECATED] Check if the feature has a geometry.

        Returns:
            bool: True if the feature has a geometry, False otherwise."""
    def hasRichGeometry(self) -> bool:
        """Determine if the feature has geometry that takes advantage of the new
        geometry technology.

        Returns:
            bool: True if the feature's geometry takes advantage of the new
                geometry technology, and False otherwise."""
    def importGeometryFromOGCWKB(self, ogcwkb: bytearray) -> None:
        """Set the geometry of the feature to be that specified in the OGC Well
        Known Binary format. If the feature has geometry, then the geometry is
        replaced.

        Args:
            ogcwkb (bytearray): Specifies the geometry of the feature.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def importGeometryFromWKT(self, ogcwkt: str) -> None:
        """Set the geometry of the feature to be that specified in the Well
        Known Text format. If the feature has geometry, then the geometry is
        replaced.

        Args:
            ogcwkt (str): Specifies the geometry of the feature.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def interpolateSpline(self, numPointsPerSegment: int, calcPhantomPoints: bool) -> None:
        """Perform interpolation on the feature.

        Args:
            numPointsPerSegment (int): The number of points per segment.
            calcPhantomPoints (bool): If True, phantom points are calculated.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def isAttributeMissing(self, attributeName: str) -> bool:
        """This method returns a boolean indicating if the attribute name maps to
        no value on the feature.

        Args:
            attributeName (str): The name of the attribute.

        Returns:
            bool: True if the attribute is missing, False otherwise.
        """
    def isAttributeNull(self, attributeName: str) -> bool:
        """This method returns a boolean indicating if the attribute name maps to
        a null value on the feature.

        Args:
            attributeName (str): The name of the attribute.

        Returns:
            bool: True if the attribute is null, False otherwise.
        """
    def makeDonuts(self, featureList: list[FMEFeature]) -> None:
        """Construct a donut polygon from the list of features provided. If multiple
        donut polygons are formed then the resulting geometry is an aggregate of
        these donuts.

        Args:
            featureList (list[FMEFeature]): The list of features to make the donut from.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def matrixTransform(self, matrix: list[list[float]]) -> None:
        """Transform the feature using a matrix.

        Args:
            matrix ((float, float), (float, float)) or
                ((float, float, float), (float, float, float), (float, float, float))):
                    The matrix to transform the feature with.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def mergeAttribute(self, destFeature: FMEFeature) -> None:
        """Set the featureType and attributes of the feature passed in from the
        current feature, but ONLY if those attributes are not already present.

        The geometry is not touched. The original attributes on the destFeature
        are not lost.

        Args:
            destFeature (FMEFeature):  The original feature to set featureType
                and attributes on.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def numCoords(self) -> int:
        """Get the number of coordinates in the feature.

        We recommend limited use of this method since it returns numVertices() +
        numParts() for multi-part features. A true vertex count will be returned
        by numVertices().

        Returns:
            int: The number of coordinates in the feature."""
    def numParts(self, flatten: bool, splitDonuts: bool) -> int:
        """Get the number of parts in the feature.

        Args:
            flatten (bool):  If flatten is True, then return the number of primitive
                parts drilling down into sub aggregates. If flatten is False then
                it returns the number of high level parts with some parts potentially
                being aggregates.
            splitDonuts (bool): If splitDonuts is True, each ring of a donut will
                count as a separate part.

        Returns:
            int: The number of parts in the feature."""
    def numVertices(self) -> int:
        """Get the number of vertices that make up the geometry of the feature
        Multi-part (aggregate) geometries are handled properly.

        For simple geometries, the same value is returned as in numCoords()

        Returns:
            int: The number of vertices in the feature."""
    def offset(self, x: float, y: float, z: float) -> None:
        """Offset the feature by the specified amount.

        Args:
            x (float): The amount to offset the feature in the x direction.
            y (float): The amount to offset the feature in the y direction.
            z (float): The amount to offset the feature in the z direction.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def orient(self, rule: int) -> int:
        """Optionally set and get the orientation rule of the feature.

        This descends into aggregates and orients any polygons or donuts found.
        Geometries other than polygons or donuts are left unchanged.

        Args:
            rule (int): (Optional) If the parameter is not supplied, the orientation
                is not changed. If the rule is supplied, the feature is adjusted
                so that rule is followed.

                With the right hand rule, the area of the polygon is always on the
                right and the coordinates of the outer boundary are in the clockwise
                direction, and for any holes they are counterclockwise.

        Returns:
            int: The orientation rule of the feature.
        """
    def outerShell(self) -> None:
        """Set the geometry of the feature to be just its outer shell. This has
        no effect on non-area features.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def performFunction(self, functionSpecification: str) -> str:
        """Call an FME function on the feature. See the FME Factory and Function
        Documentation for formatting and the list of supported functions. It may
        not support newer FME functions. Functions that are not supported will
        produce an error message indicating that the function is not recognized.
        The function string passed in to this function follows the syntax of the
        documentation exactly.

        i.e. feature.performFunction('@Count()')

        Note that no spaces should be present between any parameters of the function,
        or between the function name and the '('. Additionally, do not call this
        method during a writer's close() method.

        Args:
            functionSpecification (str): The function specification.

        Returns:
            str: The result of the function.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def processFeature(self, featureList: list[FMEFeature], paramList: list[str]) -> None:
        """Perform some general processing operation on a list of features.

        The operation performed is governed by the contents of paramList.

        Args:
            featureList (list[FMEFeature]): The list of features to process.
            paramList (list[str]): The first entry in the array determines the
                type of operation.

                The following types of operations are supported:

                - kFME_ConvertToArea: The contents of the feature list are assumed
                to be a collection of lines. These lines are then formed into
                polygons. The polygons which result are turned into donuts and
                aggregated. Any holes are themselves dropped from the result. The
                single resulting area geometry is applied to the current feature.
                - kFME_PolygonDissolve: The contents of the feature list are
                assumed to be a collection of polygons. If there are non-polygon
                features, then they will be filtered out. The collection of polygon
                features will be dissolved and the result will be applied to the
                current feature. Dissolved polygons are those polygons formed when
                shared edges between adjacent polygons are removed. This operation
                assumes that all input polygons are properly noded, a vertex is
                present at each intersection point, and that polygons are not
                overlapping.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def removeAttribute(self, attrName: str) -> None:
        """Remove an attribute from the feature.

        Args:
            attrName (str): The name of the attribute to remove."""
    def removeAttrsWithPrefix(self, attrPrefix: str) -> None:
        """Remove all attributes from the feature that have a name that starts
        with the specified prefix.

        Args:
            attrPrefix (str): The prefix to remove."""
    def removeGeometry(self) -> FMEGeometry:
        """Remove and return the feature's geometry.

        The feature loses its geometry and it can no longer be accessed.

        Returns:
            FMEGeometry: The geometry of the feature. Note: This method returns
                a terminal geometry type of the FMEGeometry; i.e. one of the leaf
                classes in the FMEGeometry inheritance graph. For example, a
                FMEPoint is returned if the geometry truly is a point."""
    def removeTraits(self, regexp: str) -> None:
        """Remove all traits from the feature that match the specified regular
        expression.

        Args:
            regexp (str): (Optional) All traits matching this regular expression
                are removed. If no expression is supplied, all traits are removed."""
    def reproject(self, coordSys: str) -> None:
        """Reproject the feature from its current coordinate system to that specified.

        If the feature has no coordinate system specified then this has the same
        effect as the setCoordSys method.

        Args:
            coordSys (str): The coordinate system to set on the feature.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def resetCoords(self) -> None:
        """Reset the number of coordinates in the feature to 0."""
    def resetFeature(self) -> None:
        """Reset (clear) all the attributes and geometry of the feature.

        It results in a fresh clean feature.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def rotate2D(self, origin: tuple[float, float], angle: float) -> None:
        """Rotate the feature counterclockwise around the origin point by the
        specified angle (in degrees).

        Args:
            origin (tuple[float, float]): The origin of the rotation.
            angle (float): The angle (in degrees) which to rotate the feature in
                the counterclockwise direction.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def scale(self, x: float, y: float, z: float) -> None:
        """Scale the feature by the specified amount.  (2D or 3D)

        Args:
            x (float): The amount to scale the feature in the x direction.
            y (float): The amount to scale the feature in the y direction.
            z (float): (Optional) The value to scale z by. (Default value is 1.0)

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def serialize(self, parameters: dict[str, str]) -> bytearray | bytes | None:
        """Write the state of the FMEFeature to a string buffer.

        Args:
            parameters (dict[str,str]): (Optional) Possible name-value pairs are:

                - kFME_FeatureSerializeOption:
                    - kFME_FeatureFullFeature: (Default) Serialize the full full
                    feature.
                    - kFME_FeatureGeometry: Serialize the geometry portion of a
                    feature only. This includes coordinates, coordinate system,
                    and geometry attributes.
                - kFME_FeatureSerializeExcludeAttr:
                    - Attribute names to exclude: The names of the attributes to
                    exclude when doing feature serialization. The value can be a
                    single string or a list.
                - kFME_FeatureSerializeSidecarBasename:
                    - File in which to store extra geometry data: The path and
                    basename (not including file extension) to which additional
                    data will be written for some geometries (raster, point cloud).
                    If this option is not specified for those geometries, the
                    extra data will not be written.

        Returns:
            bytearray or bytes or None: The serialized feature.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setAttribute(
        self,
        attrName: str,
        attrValue: bool | int | str | list[str] | float | bytearray | list[bytearray] | bytes | list[bytes],
    ) -> None:
        """Set the value of an attribute.

        If the attribute already exists, it will be overwritten. The following
        type numeric mappings are used:
            PyInt ==> FME_Int32
            PyFloat ==> FME_Real64
            PyLong ==> FME_Int64

        Binary values are to be specified as bytes or bytearray values.

        If an attribute value of None is specified, the attribute value will be
        set as an empty string. To set a null attribute, use setAttributeNullWithType.

        For a list attribute, if the attribute already exists and contains more
        elements than the new list, the resulting list will be made up of the new
        list elements plus the old list elements that were not overwritten. Call
        removeAttribute first to avoid this behavior.

        Args:
            attrName (str): The name of the attribute to set.
            attrValue (bool or int or str or list[str] or float or bytearray or
                list[bytearray] or bytes or list[bytes]): The value of the attribute.
        """
    def setAttributeNullWithType(self, attrName: str, attrType: int) -> None:
        """This method supplies a null attribute with a type to the feature.

        If an attribute with the same name already exists, it is overwritten.

        Attribute type must be one of: FME_ATTR_UNDEFINED, FME_ATTR_BOOLEAN,
        FME_ATTR_INT8, FME_ATTR_UINT8, FME_ATTR_INT16, FME_ATTR_UINT16,
        FME_ATTR_INT32, FME_ATTR_UINT32, FME_ATTR_REAL32, FME_ATTR_REAL64,
        FME_ATTR_REAL80, FME_ATTR_STRING, FME_ATTR_ENCODED_STRING,
        FME_ATTR_INT64 or FME_ATTR_UINT64.

        Args:
            attrName (str): The name of the attribute to set.
            attrType (int): An integer representing the attribute type.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setCoordSys(self, coordSys: str) -> None:
        """Set the coordinate system of the feature.

        Args:
            coordSys (str): The coordinate system to set on the feature.
        """
    def setDimension(self, dimension: int) -> None:
        """Set the dimension of the feature.

        Dimension must either be FME_TWO_D or FME_THREE_D

        Args:
            dimension (int): The dimension to set on the feature.
        """
    def setFeatureType(self, featureType: str) -> None:
        """This method sets the feature type of the FMEFeature.

        The feature type is often also called the “class” or “category” of the
        feature. The feature type set on a feature through this method will change
        as the feature is routed through a translation pipeline.

        Args:
            featureType (str): The feature type to set on the feature.
        """
    def setGeometry(self, geometry: FMEGeometry) -> None:
        """Set the geometry of the feature.

        Any existing geometry on the feature is overwritten.

        Args:
            geometry (FMEGeometry): The geometry to set on the feature.
        """
    def setGeometryType(self, geomType: int) -> None:
        """Set the feature's classic geometry type.

        geomType must one of: FME_GEOM_UNDEFINED, FME_GEOM_POINT, FME_GEOM_LINE,
        FME_GEOM_POLYGON, FME_GEOM_DONUT, FME_GEOM_PIP, or FME_GEOM_AGGREGATE.

        Args:
            geomType (int): The geometry to set on the feature.
        """
    def setSequencedAttribute(self, attrName: str, attrValue: str | list[str]) -> None:
        """Supply a new attribute for the feature, but in such a way that the sequence
        is remembered.

        This is needed for schema features, to preserve the order of attributes.

        For a list attribute, if the attribute already exists and contains more
        elements than the new list, the resulting list will be made up of the new
        list elements plus the old list elements that were not overwritten. Call
        removeAttribute first to avoid this behavior.

        Args:
            attrName (str): The name of the attribute to set.
            attrValue (str or list[str]): The value of the attribute.
        """
    def splitAggregate(self, recurse: bool) -> list[FMEFeature]:
        """Split up an aggregate feature into pieces, all of which have the same
        attributes and feature type. If the recurse flag is True, all aggregates
        within the aggregate are also split recursively, so no aggregates are ever
        returned as pieces. This method will only return points, lines, polygons,
        and null geometries (and possibly aggregates if recurse is False). All
        other geometries will be converted to these when split.

        Args:
            recurse (bool): (Optional) Whether to recursively split the aggregate
            until no aggregates remain. (Default value is False)

        Returns:
            list[FMEFeature]: A list of features resulting from the splitting of the original aggregate.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """

class FMEPartIterator:
    """FME Part Iterator Class

    FMEPartIterator should not be constructed directly. Instead, use the
    iterator semantics of FMEFeature to get an FMEPartIterator which can be used
    to iterate over its parts."""

    def __init__(self) -> None:
        """Initialize self. See help(type(self)) for accurate signature."""
    def dimension(self) -> int:
        """Get the part's dimension. Returns either FME_TWO_D or FME_THREE_D.

        Returns:
            (int): The dimension of the part.
        """
    def getAllCoordinates(self) -> list[tuple[float]]:
        """Get all the part's coordinates in a list. Each coordinate is a tuple.

        All returned tuples have the same dimension as the part.

        Returns:
            (list[list[float]]): A list of the part's coordinates.
        """
    def getCoordinate(self, index: int) -> tuple[float]:
        """Get the coordinate at the specified index.

        The dimension of the tuple equals the dimension of the part.

        Args:
            index (int): The index at which the coordinate is retrieved.

        Returns:
            (tuple[float]): The coordinate at the given index.
        """
    def numVertices(self) -> int:
        """Get the number of vertices.

        Returns:
            (int): The number of vertices in the part.
        """

# Attribute types
FME_ATTR_BOOLEAN: int
FME_ATTR_ENCODED_STRING: int
FME_ATTR_INT16: int
FME_ATTR_INT32: int
FME_ATTR_INT64: int
FME_ATTR_INT8: int
FME_ATTR_LIST: int
FME_ATTR_REAL32: int
FME_ATTR_REAL64: int
FME_ATTR_REAL80: int
FME_ATTR_STRING: int
FME_ATTR_UINT16: int
FME_ATTR_UINT32: int
FME_ATTR_UINT64: int
FME_ATTR_UINT8: int
FME_ATTR_UNDEFINED: int

# Classic geometry types
FME_GEOM_AGGREGATE: int
FME_GEOM_DONUT: int
FME_GEOM_LINE: int
FME_GEOM_PIP: int
FME_GEOM_POINT: int
FME_GEOM_POLYGON: int
FME_GEOM_UNDEFINED: int

# Attribute casing: int
FME_NAME: int
FME_VALUE: int
FME_NAME_VAL: int
FME_ATTR_LIST: int
FME_UPPERCASE: int
FME_LOWERCASE: int
FME_TITLECASE: int
FME_FULLTITLECASE: int

# Dimensions
FME_TWO_D: int
FME_THREE_D: int

# Core format attributes
kFMEBasename: int
kFMEDataset: int

# OGC versions
ogcvOneDotOne: int
ogcvOneDotTwo: int
ogcvPostGISOneDotZero: int
ogcvPostGISOneWithSQLMM3: int
ogcvPostGISPreOneDotZero: int

# Serialize Options
kFME_FeatureSerializeOption: int
kFME_FeatureFullFeature: int
kFME_FeatureGeometry: int
kFME_FeatureSerializeExcludeAttr: int
kFME_FeatureSerializeSidecarBasename: int

# Deserialize Options: int
kFME_FeatureDeserializeOption: int
kFME_FeatureDeserializeReset: int
kFME_FeatureDeserializeMerge: int
kFME_FeatureDeserializeSidecarBasename: int

# General Processing Operations
kFME_ConvertToArea: int
kFME_PolygonDissolve: int

kFMEFeatureTypeAttr: str
"""fme_feature_type"""
