from fmeobjects.geometries.curves import FMEArc, FMECurve, FMELine
from fmeobjects.geometries.areas import FMEArea, FMEEllipse, FMEMultiArea
from fmeobjects.geometries.general import FMEGeometry
from fmeobjects.geometries.surfaces import FMESurface
from fmeobjects.geometries.points import FMEPoint
from fmeobjects.geometries.text import FMEText

# Closing Curves in 3D
FME_CLOSE_3D_AVERAGE_MODE: int
FME_CLOSE_3D_EXTEND_MODE: int
FME_CLOSE_3D_EXTEND_OR_AVERAGE_Z_MODE: int

# Calculating Vertex Normals
BY_FACE: int

# Refine Area Type
FME_RA_PATH_CONCAT_LINES: int
FME_RA_PATH_EXTRACT_SINGLE_LINES: int
FME_RA_PATH_EXTRACT_SINGLE_ARCS: int
FME_RA_ARC_STANDARDIZE: int
FME_RA_ARC_STROKE: int
FME_RA_AREA_STANDARDIZE: int
FME_RA_LINE_REMOVE_DUPLICATE_COORDS: int
FME_RA_LINE_REMOVE_DUPLICATE_COORDS_Z: int

# Refine Curve Type
FME_RC_PATH_CONCAT_LINES: int
FME_RC_PATH_EXTRACT_SINGLE_LINES: int
FME_RC_PATH_EXTRACT_SINGLE_ARCS: int
FME_RC_ARC_STANDARDIZE: int
FME_RC_ARC_STROKE: int
FME_RC_LINE_REMOVE_DUPLICATE_COORDS: int
FME_RC_LINE_REMOVE_DUPLICATE_COORDS_Z: int

# Refine Geometry Type
FME_RG_PATH_CONCAT_LINES: int
FME_RG_PATH_EXTRACT_SINGLE_LINES: int
FME_RG_PATH_EXTRACT_SINGLE_ARCS: int
FME_RG_ARC_STANDARDIZE: int
FME_RG_ARC_STROKE: int
FME_RG_AREA_STANDARDIZE: int
FME_RG_LINE_REMOVE_DUPLICATE_COORDS: int
FME_RG_LINE_REMOVE_DUPLICATE_COORDS_Z: int
FME_RG_AGG_OR_MULTI_EXTRACT_SINGLETONS: int
FME_RG_AGG_OR_MULTI_RECURSE: int
FME_RG_AGG_CONVERT_HOMOGENEOUS_TO_MULTI: int
FME_RG_3D_CONVERT_TO_WIREFRAME: int
FME_RG_RASTER_CONVERT_TO_POLYGON: int
FME_RG_3D_CONVERT_TO_POLYGON: int
FME_RG_3D_REMOVE_VERTICAL_SEGMENTS: int
FME_RG_3D_CONVERT_VERTICAL_FACES_TO_WIREFRAME: int
FME_RG_3D_CONVERT_TO_FACE: int
FME_RG_REMOVE_NULLS: int
FME_RG_3D_AUTO_FRONT_SIDED_SURFACE: int
FME_RG_BISECT_CLOSED_ARCS: int

class FMEGeometryTools:
    """FME Geometry Tools Class

    This class provides the ability to modify FME Geometry."""

    def __init__(self) -> None: ...
    def appendCurve(self, destinationCurve: FMECurve | None, sourceCurve: FMECurve | None) -> FMECurve | None:
        """Appends the source curve to the destination curve.

        This will not merge curves but simply append them into an IFMEPath if
        necessary. If the source curve is None, nothing will be done and the
        destination curve will be returned. If the destination curve is None,
        it will be set to the source curve. If the source and destination curves
        do not have touching end points, a line will be inserted to connect them.

        Args:
            destinationCurve (FMECurve or None): The destination curve.
            sourceCurve (FMECurve or None): The source curve.

        Returns:
            (FMECurve or None): The appended curve. Note: This method returns a
                terminal geometry type of the FMECurve; i.e. one of the leaf
                classes in the FMECurve inheritance graph. For example, a
                FMEPath is returned if the geometry truly is a path.
        """
    def applyTransformationToTextureCoordinates(self, surface: FMESurface, applyOnlyIfShearExists: bool) -> None:
        """Apply the transformation matrix of the texture to the texture coordinates
        if exists and that it does not have any shear if 'applyOnlyIfShearExists' is set to true.

        Note: This method should only be called once for one surface, or else the
        transformation matrix is applied as many times as the method is called.

        Args:
            surface (FMESurface): The surface.
            applyOnlyIfShearExists (bool): If true, the transformation is only
                applied if the surface has a shear.
        """
    def calculateVertexNormals(self, repairOnlyMissing: bool, repairType: int, geom: FMEGeometry) -> None:
        """This method returns None if vertex normals are repaired on the geometry
        or if there is nothing to repair.

        If an error occurs during the repair a FMEException is thrown. Currently,
        the only valid value for repairOnlyMissing is true, and the only valid
        value for repairType is BY_FACE.

        Args:
            repairOnlyMissing (bool): Boolean indicating whether or not to repair
                only the missing vertex normals, currently, the only true is valid.
            repairType (int): Repair type, the only valid value is BY_FACE.
            geom (FMEGeometry):  The geometry to calculate the vertex normals for.
        """
    def closeArcAsEllipse(self, arc: FMEArc) -> FMEEllipse | None:
        """This routine is to see if the current arc is closed.

        A closed arc is defined as one where the start and end points are equal.
        If None is passed in, nothing will be done. The returned geometry may or
        may not be the original object that was passed in. If a different object
        is returned, the original object will be destroyed.

        Args:
            arc (FMEArc): The arc to close.

        Returns:
            (FMEEllipse or None): The Arc closed as an ellipse or None
        """
    def closeCurve(self, curve: FMECurve | None) -> FMECurve | None:
        """This checks to see if the current curve is closed. A closed curve is
        defined as one where the start and end points are equal. If necessary
        this method will add a straight segment from the end point to the start
        point to force the curve closed. If None is passed in, nothing will be
        done and None will be returned. The returned geometry may or may not be
        the original object that was passed in. If a different object is returned,
        the original object will be destroyed.

        Args:
            curve (FMECurve): The curve to close.

        Returns:
            (FMECurve or None): The closed curve. Note: This method returns a
                terminal geometry type of the FMECurve; i.e. one of the leaf
                classes in the FMECurve inheritance graph. For example, a FMEArc.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def closeCurve3D(self, curve: FMECurve | None, mode: int) -> FMECurve | None:
        """This function closes the curve in 3D if it is not already closed.

        If the curve is not 3D, it forces the curve to be 3D with default z value
        of 0.0. A closed curve is defined as one where the start and end points
        are equal in all X, Y and Z coordinates. The returned geometry may or may
        not be the original object that was passed in. If None is passed in,
        nothing will be done and None will be returned. If a different object is
        returned, the original object will be destroyed. There are 3 modes that
        the function uses in deciding how to close the curve, namely
        FME_CLOSE_3D_EXTEND_MODE, FME_CLOSE_3D_AVERAGE_MODE and
        FME_CLOSE_3D_EXTEND_OR_AVERAGE_Z_MODE.

        - In FME_CLOSE_3D_AVERAGE_MODE, the curve is closed by modifying the current
        start and end points of the curve to be the average of the two points.
        - In FME_CLOSE_3D_EXTEND_MODE, this method will add a straight segment
        from the end point to the start point to force the curve closed.
        - In FME_CLOSE_3D_EXTEND_OR_AVERAGE_Z_MODE, the curve is closed using
        the AVERAGE mode if the start and end points only differ in Z. Otherwise,
        the EXTEND MODE is used.

        Args:
            curve (FMECurve): The curve to close.
            mode (int): The FME_CloseCurve3DMode.

        Returns:
            (FMECurve or None): The closed curve. Note: This method returns a
                terminal geometry type of the FMECurve; i.e. one of the leaf
                classes in the FMECurve inheritance graph. For example, a FMEPath
                is returned if the geometry truly is a path.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def convertToLine(self, curve: FMECurve | None) -> FMELine | None:
        """Returns a line that is created from the given curve.

        If the curve is a FMELine, it will be returned. If it is a FMEArc, it will
        be stroked to a line. If the curve is a FMEPath, all segments will be
        returned as their line representations. If the given curve is None, nothing
        will be done. This throws an exception if there is an error.

        Args:
            curve (FMECurve): The curve to convert.

        Returns:
            (FMELine or None): The line representing the curve.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def createXMLFromGeometry(self, geom: FMEGeometry) -> str:
        """This routine returns an XML definition according to the geometry passed in.

        Args:
            geom (FMEGeometry): The geometry to create the XML definition from.

        Returns:
            (str): The geometry definition.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def extendToCurve(self, destinationCurve: FMECurve | None, sourceCurve: FMECurve | None) -> FMECurve | None:
        """Extends the source curve to the destination curve.

        If one curve is a line or a path with a line at its end, and the other
        curve is a line or a path with a line at its start, the matching lines
        will be merged, as long as both share the same geometry attributes. If
        the curves do not have touching end points, a line will be created to
        attach them. Appending an arc or appending to an arc will result in a
        path. If the source curve is None, nothing will be done and None will be
        returned. If the destination curve is None, it will be set to the source
        curve.

        Args:
            destinationCurve (FMECurve): The curve to extend with source curve.
            sourceCurve (FMECurve): The curve to extend the destination curve by.

        Returns:
            (FMECurve or None): The extended curve. Note: This method returns a
                terminal geometry type of the FMECurve; i.e. one of the leaf
                classes in the FMECurve inheritance graph. For example, a FMEPath
                is returned if the geometry truly is a path.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def extendToPoint(self, curve: FMECurve | None, point: FMEPoint | None) -> FMECurve | None:
        """This method will extend the given curve to the given point.

        This method will add a straight segment from the curve's end point to the
        new point. The returned geometry may or may not be the original object
        that was passed in. If a different object is returned, the original object
        will be destroyed. If the point is None, nothing will be done and None
        will be returned. If the curve is None, but the point is valid, a line
        will be returned that has one point.

        Args:
            curve (FMECurve): The curve to extend with the point or None.
            point (FMEPoint): The point to extend the curve by, or None.

        Returns:
            (FMECurve or None): The extended curve. Note: This method returns a
                terminal geometry type of the FMECurve; i.e. one of the leaf
                classes in the FMECurve inheritance graph. For example, a FMELine
                is returned if the geometry truly is a line.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def extractTextLocation(self, text: FMEText) -> FMEGeometry:
        """This routine consumes the text passed in and returns the IFMEGeometry
        that was its location.

        Args:
            text (FMEText): The text to extract the location from.

        Returns:
            (FMEGeometry): The geometry at the text's location. Note: This method
                returns a terminal geometry type of the FMEGeometry; i.e. one of
                the leaf classes in the FMEGeometry inheritance graph. For example,
                a FMELine is returned if the geometry truly is a line.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def force2D(self, geometry: FMEGeometry) -> FMEGeometry:
        """This routine forces the geometry to 2D.

        If the geometry is surface or solid, it will become 2D polygons, or
        wire-frame if the surface is vertical.

        Args:
            geometry (FMEGeometry): The geometry to force to 2D.

        Returns:
            (FMEGeometry or None): The geometry in 2D. Note: This method returns
                a terminal geometry type of the FMEGeometry; i.e. one of the leaf
                classes in the FMEGeometry inheritance graph. For example, a
                FMELine is returned if the geometry truly is a line.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getPartCount(
        self,
        geometry: FMEGeometry,
        recursive: bool,
        splitDonuts: bool,
        splitPaths: bool,
    ) -> int:
        """Return the number of parts in the geometry. For multis and aggregates,
        this is the number of parts, and for paths, the number of segments;
        otherwise it is one. If recursive is True, then aggregates' parts will
        be counted recursively.

        Args:
            geometry (FMEGeometry): aggregate or multis whose parts to count.
            recursive (bool): Boolean indicating whether or not to count recursively.
            splitDonuts (bool): Boolean indicating whether or not to split donuts.
            splitPaths (bool): Boolean indictaing whether or to split paths.

        Returns:
            (int): The number of parts in the geometry.
        """
    def join(self, firstGeom: FMEGeometry, secondGeom: FMEGeometry, aggregatable: bool) -> FMEGeometry:
        """This routine joins two geometries together.

        Options applying to joining will affect the result. Both geometries will
        be taken ownership if the result is successful. If the joining of two
        geometries doesn't make any sense, put them into an aggregate. For example:
        one ellipse and one line

        Args:
            firstGeom (FMEGeometry): The first geometry to join.
            secondGeom (FMEGeometry): The second geometry to join.
            aggregatable (bool): Boolean indictaing whether or not to combine the
                two geometries into an aggregate.

        Returns:
            (FMEGeometry): The combined geometries. Note: This method returns a
                terminal geometry type of the FMEGeometry; i.e. one of the leaf
                classes in the FMEGeometry inheritance graph. For example, a
                FMELine is returned if the geometry truly is a line.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def makeDonuts(self, multiArea: FMEMultiArea) -> FMEGeometry:
        """This routine takes in a MultiArea, extracts simple areas from it, and
        creates donuts out of them. The resulting donuts and simple areas, if any,
        are returned. The returned MultiArea may contain a mixture of donuts and
        simple areas.

        Args:
            multiArea (FMEMultiArea): The multi area to make a donut from.

        Returns:
            (FMEGeometry): The donuts and simple areas extracted form the multi
                area. Note: This method returns a terminal geometry type of the
                FMEGeometry; i.e. one of the leaf classes in the FMEGeometry
                inheritance graph. For example, a FMESimpleArea is returned if
                the geometry truly is a simple area.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def matrixTransform(
        self,
        geometry: FMEGeometry,
        m11: float,
        m12: float,
        m13: float,
        m14: float,
        m21: float,
        m22: float,
        m23: float,
        m24: float,
        m31: float,
        m32: float,
        m33: float,
        m34: float,
    ) -> FMEGeometry:
        """This method performs a 3D matrix transformation on the geometry passed in.

        The order in which parameters are passed in is important and it should be
        row wise e.g. for a matrix the order of the parameters should be m11, m12,
        m13, m14, m21, m22, m23, m24, m31, m32, m33, m34.

        |m11 m12 m13 m14|

        |m21 m22 m23 m24|

        |m31 m32 m33 m34|

        After doing the transformation, geometry is replaced with the transformed
        geometry if the method is successful. Otherwise, the matrix transform has
        failed and a FMEException is thrown.

        Args:
            geometry (FMEGeometry): The geometry to transform.

        Returns:
            (FMEGeometry): The transformed geometry. Note: This method returns a
                terminal geometry type of the FMEGeometry; i.e. one of the leaf
                classes in the FMEGeometry inheritance graph. For example, a
                FMEAggregate is returned if the geometry truly is a aggregate.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def offset(self, geometry: FMEGeometry, point: FMEPoint) -> FMEGeometry:
        """Offsets the geometry by the coords specified by 'point'.

        The returned geometry may or may not be the original object that was
        passed in. If a different object is returned, the original object will
        be destroyed.

        Args:
            geometry (FMEGeometry): The geometry to offset.
            point (FMEPoint): The point specifying the offset distance.

        Returns:
            (FMEGeometry): The offset geometry. Note: This method returns a terminal
                geometry type of the FMEGeometry; i.e. one of the leaf classes in
                the FMEGeometry inheritance graph. For example, a FMELine is
                returned if the geometry truly is a line.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def refineArea(self, area: FMEArea, refineType: int) -> FMEArea:
        """See the documentation for refineGeometry().

        Bitmask elements are defined in Refine Area Type.

        Args:
            area (FMEArea): The area to refine.
            refineType (int): One of: FME_RA_PATH_CONCAT_LINES,
                FME_RA_PATH_EXTRACT_SINGLE_LINES, FME_RA_PATH_EXTRACT_SINGLE_ARCS,
                FME_RA_ARC_STANDARDIZE, FME_RA_ARC_STROKE, FME_RA_AREA_STANDARDIZE,
                FME_RA_LINE_REMOVE_DUPLICATE_COORDS, or FME_RA_LINE_REMOVE_DUPLICATE_COORDS_Z.

        Returns:
            (FMEArea): The refined area. Note: This method returns a terminal
                geometry type of the FMEArea; i.e. one of the leaf classes in the
                FMEArea inheritance graph. For example, a FMEPolygon is returned
                if the geometry truly is a polygon.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def refineCurve(self, curve: FMECurve, refineType: int) -> FMECurve:
        """See the documentation for refineGeometry().

        Bitmask elements are defined in Refine Curve Type.

        Args:
            curve (FMECurve): The curve to refine.
            refineType (int): One of: FME_RC_PATH_CONCAT_LINES,
                FME_RC_PATH_EXTRACT_SINGLE_LINES, FME_RC_PATH_EXTRACT_SINGLE_ARCS,
                FME_RC_ARC_STANDARDIZE, FME_RC_ARC_STROKE,
                FME_RC_LINE_REMOVE_DUPLICATE_COORDS, or FME_RC_LINE_REMOVE_DUPLICATE_COORDS_Z.

        Returns:
            (FMECurve): The refined curve. Note: This method returns a terminal
                geometry type of the FMECurve; i.e. one of the leaf classes in
                the FMECurve inheritance graph. For example, a FMELine is returned
                if the geometry truly is a line.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def refineGeometry(self, geometry: FMEGeometry, refineType: int) -> FMEGeometry:
        """This routine offers a number of options to refine geometries.

        The options are defined as a bitmask whose components are defined in
        Refine Geometry Type. Options applying to curves will affect area boundaries.

        - FME_RG_AGG_CONVERT_HOMOGENEOUS_TO_MULTI: Any aggregates that could be
        represented as multis will have their parts removed and a new multi
        will be the result.
        - FME_RG_AGG_OR_MULTI_RECURSE: Elements of aggregates and multis will also
        be refined according to the same parameters.
        - FME_RG_AGG_OR_MULTI_EXTRACT_SINGLETONS: Aggregates or multis with only
        one element will have it removed and returned.
        - FME_RG_AREA_STANDARDIZE: Donuts with no holes will become polygons or
        ellipses, and polygons with arc boundaries will become ellipses.
        - FME_RG_ARC_STROKE: Arcs will be converted to lines.
        - FME_RG_ARC_STANDARDIZE: Center-point arcs will have their parameters
        adjusted so that start angle is in [0, 360) and rotation is in [0, 90].
        - FME_RG_PATH_EXTRACT_SINGLE_ARCS: Paths containing one arc (or other
        non-line segment) and no lines will be replaced by that segment.
        - FME_RG_PATH_EXTRACT_SINGLE_LINES: Paths containing one line and no arcs
        will be replaced by that line.
        - FME_RG_PATH_CONCAT_LINES: Consecutive line parts in a path will be
        combined into single lines, as long as they contain identical geometry
        attributes.
        - FME_RG_LINE_REMOVE_DUPLICATE_COORDS: Consecutive duplicate coordinates
        are removed. Arcs are unmodified. Only x and y values in the coordinates
        are used to detect duplicates.
        - FME_RG_LINE_REMOVE_DUPLICATE_COORDS_Z: Consecutive duplicate coordinates
        are removed. Arcs are unmodified. x, y, and z values in the coordinates
        are used to detect duplicates.
        - FME_RG_3D_CONVERT_TO_WIREFRAME: 3D surfaces and solids will be converted
        into wire-frames.
        - FME_RG_RASTER_CONVERT_TO_POLYGON: Rasters will be replaced with their
        polygon boundaries.
        - FME_RG_3D_CONVERT_TO_POLYGON: 3D surfaces and solids will be converted
        into areas.
        - FME_RG_3D_CONVERT_TO_FACE: 3D surfaces and solids will be converted into
        faces.
        - FME_RG_3D_REMOVE_VERTICAL_SEGMENTS: Any vertical segments that exist in
        three dimensional curves.
        - FME_RG_3D_CONVERT_VERTICAL_FACES_TO_WIREFRAME: Convert any vertical
        faces that exist in 3D surfaces and solids to wire-frames.
        - FME_RG_REMOVE_NULLS: recursively deletes any FMENull geometries.
        Container geometries such as aggregates will become empty if all they
        contained was FMENull. If the user passes in a FMENull, a FMENull will
        be returned.
        - FME_RG_3D_AUTO_FRONT_SIDED_SURFACE: will modify a surface so that it
        is front-sided, where the side selected favors the side with a non-default
        appearance or in the case of two non-default appearances, the side with
        a texture reference.
        - FME_RG_BISECT_CLOSED_ARCS

        Args:
            geometry (FMEGeometry): The geometry to refine.
            refineType (int): One of the Refine Geometry Types.

        Returns:
            (FMEGeometry): The refined geometry. Note: This method returns a terminal
                geometry type of the FMEGeometry; i.e. one of the leaf classes in
                the FMEGeometry inheritance graph. For example, a FMEPolygon is
                returned if the geometry truly is a polygon.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def rotate2D(self, geometry: FMEGeometry, center: FMEPoint, angle: float) -> FMEGeometry:
        """The angle is CCW up from the horizontal and is measured in degrees.

        The returned geometry may or may not be the original object that was
        passed in. If a different object is returned, the original object will
        e destroyed. If an error occurs an exception is thrown.

        Args:
            geometry (FMEGeometry): The geometry to rotate.
            center (FMEPoint): The center point.
            angle (float): The angle in degrees.

        Returns:
            (FMEGeometry): The rotated geometry. Note: This method returns a
                terminal geometry type of the FMEGeometry; i.e. one of the leaf
                classes in the FMEGeometry inheritance graph. For example, a
                FMESimpleArea is returned if the geometry truly is a simple area.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def scale(self, geometry: FMEGeometry, xScale: float, yScale: float, zScale: float) -> FMEGeometry:
        """The 'zscale' is ignored if geometry is 2D.

        The returned geometry may or may not be the original object that was
        passed in. If a different object is returned, the original object will
        be destroyed. If an error occurs an exception is thrown.

        Args:
            geometry (FMEGeometry): The geometry to scale.
            xScale (float): The x scale factor.
            yScale (float): The y scale factor.

        Returns:
            (FMEGeometry): The scaled geometry. Note: This method returns a
                terminal geometry type of the FMEGeometry; i.e. one of the leaf
                classes in the FMEGeometry inheritance graph. For example, a
                FMESimpleArea is returned if the geometry truly is a simple area.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setArcPrimaryRadius(self, arc: FMEArc, radius: float) -> FMEArc:
        """Sets the primary radius of an arc.

        Args:
            arc (FMECurve): The arc.
            radius (float): The radius.

        Returns:
            (FMEArc): The arc after the primary radius is set.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setArcRotation(self, arc: FMEArc, rotation: float) -> FMEArc:
        """Set the rotation on an arc object.

        All angles are CCW up from the horizontal and are measured in degrees.
        If the underlying arc is stored by bulge or by 3 points, it will become
        an arc by center point.

        Args:
            arc (FMECurve): The arc to set the rotation for.
            rotation (float): The rotation.

        Returns:
            (FMEArc): The arc after the rotation is set.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setArcSecondaryRadius(self, arc: FMEArc, radius: float) -> FMEArc:
        """Sets the secondary radius of an arc.

        Args:
            arc (FMECurve): The arc.
            radius (float): The radius.

        Returns:
            (FMEArc): The arc after the secondary radius is set.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setArcSweepAngle(self, arc: FMEArc, angle: float) -> FMEArc:
        """Sets the sweep angle of an arc.

         If the angle is a bulge arc, it is turned as an arc by center point to
         support sweep angle of 360.

        Args:
            arc (FMECurve): The arc.
            angle (float): The angle.

        Returns:
            (FMEArc): The arc after the sweep angle is set.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def splitDoubleSidedSurface(self, doubleSidedSurface: FMESurface) -> list[FMESurface]:
        """Takes a double-sided surface and splits it up into two single-sided
        surfaces of the same type.

        If the passed in geometry is actually single-sided, then None is returned
        for the side that doesn't exist. An error is returned when the function
        encounters a problem trying to split up the surface.

        Args:
            doubleSidedSurface (FMESurface): The double-sided surface.

        Returns:
            (List[FMESurface]): A List of the front and back side of doubleSidedSurface,
                in the form [frontSideSurface, backSideSurface].

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def triangulateToSurface(self, geometry: FMEGeometry) -> FMEGeometry:
        """This routine will return a FMEGeometry object with triangle faces.

        This feature can support all geometries except for FMEAggregate,
        FMECSGSolid, FMECompositeSolid and FMEMultiSolid. The output FMEGeometry
        is never None. The resulting FMEGeometry is not guaranteed to contain
        only triangles, so it is the user's responsiblity to check this. The
        geometry type of the returned FMEGeometry object depends on the type of
        input geometry:

        - If the input is a FMETriangleStrip, FMETriangleFan, or FMEFace that is
        already triangular, the resulting FMEGeometry is a copy of the input
        geometry and hence has the same geometry type as the input.
        - If the input is a sliver face, the resulting FMEGeometry is a copy of
        the original geometry.
        - If the input is a non-triangular and non-sliver Face, non-triangular
        Area, or RectangleFace, the resulting FMEGeometry is a FMECompositeSurface,
        whose components are triangular Faces. Otherwise the component is a
        FMECompositeSurface consisting of triangular Faces.
        - If the input is a CompositeSurface, the resulting FMEGeometry is a
        FMECompositeSurface. The type of each component in the resulting
        FMECompositeSurface is determined as described above.
        - If the input is a MultiSurface, the resulting FMEGeometry is a
        FMEMultiSurface. The type of each component in the resulting FMEMultiSurface
        is determined as described above.
        - If the input is a Box, Extrusion, or BRepSolid, the resulting FMEGeometry
        is a FMEBRepSolid.
        - If the input is a MultiArea, the resulting IFMEGeometry is a FMEMultiSurface.
        The type of each component in the resulting FMEMultiSurface is determined
        as described above.
        - If the input is a Mesh, the resulting FMEGeometry is a FMEMultiSurface.
        - For the case of FMEArea, the triangulation will occur with respect to
        the x- and y-coordinates, the z values are ignored, yet they will be
        retained in the output. If there are any errors an exception will be thrown.

        Args:
            geometry (FMEGeometry): The geometry to convert.

        Returns:
            (FMEGeometry): The converted geometry. Note: This method returns a
                terminal geometry type of the FMEGeometry; i.e. one of the leaf
                classes in the FMEGeometry inheritance graph. For example, a
                FMETriangleStrip is returned if the geometry truly is a triangle strip.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
