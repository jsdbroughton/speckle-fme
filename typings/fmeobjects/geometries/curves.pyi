from typing import overload
from fmeobjects.features import FMEFeature
from fmeobjects.geometries.general import FMEGeometry
from fmeobjects.geometries.geometry_mixins import TransformMixin
from fmeobjects.geometries.points import FMEPoint

from six import text_type, string_types

# No Coordinate Index
FME_NPOS32: int

# Snip Types
SNIP_DISTANCE: int
SNIP_PERCENTAGE: int
SNIP_VERTEX: int
SNIP_POINT: int

# Arc Types
FME_ARC_BY_CENTER_POINT: int
FME_ARC_BY_CENTER_POINT_START_END: int
FME_ARC_BY_BULGE: int
FME_ARC_BY_3_POINTS: int

# Mapping File Directives
kFMEStrokeMaxDeviationValue: int
kFMEDegreesPerEdge: int

class FMECurve(FMEGeometry, TransformMixin):
    """FME Curve Class

    FMECurve is an abstract class. It cannot be created directly."""

    def getAsLine(self) -> FMELine:
        """Returns the curve as a line geometry object.

        Returns:
            FMELine: A line geometry object.
        """
    def getAsLineFixedArcSamples(self, numSamples: int) -> FMELine:
        """Returns a copy of this curve as a line.

        All arcs are approximated with the number of points given by 'numSamples'.
        If 'numSamples' is 0, the number points will first be determined by the
        value of kFMEStrokeMaxDeviationValue directive in mapping file, which
        denotes the maximum deviation of the arc from the line. In the absence
        of this directive or the value of this directive is smaller than or equal
        to 0, the number points will be determined by the arc's sweep angle and
        the value of the mapping file directive kFMEDegreesPerEdge, which defaults to 5.

        Args:
            numSamples (int): The number of points to approximate the arc with.

        Returns:
            FMELine: The curve as a FMELine object.
        """
    def getEndPoint(self) -> FMEPoint | None:
        """Returns the end point of this curve.

        An error is returned and None is returned if this curve has no point to return.

        Returns:
            FMEPoint: The end point of the curve, or None if there is no point to return.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getLength(self, threeD: bool) -> float:
        """Returns the length of the curve.

        If 'threeD' is True, this returns the 3D length of the curve, otherwise
        this returns the 2D length.

        Args:
            threeD (bool): Whether to calculate the 2D or 3D length.

        Returns:
            float: The length of the curve.
        """
    def getStartPoint(self) -> FMEPoint | None:
        """Returns the start point of this curve.

        An error is returned and None is returned if this curve has no point to return.

        Returns:
            FMEPoint: The start point of the curve, or None if there is no point to return.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def isLinear(self) -> bool:
        """Returns True if and only if this curve contains only lines.

        Returns:
            bool: True if the curve contains only lines, False otherwise.
        """
    def offset(self, offsetPoint: FMEPoint) -> None: ...
    def removeDuplicates(self, checkZ: bool) -> None:
        """Removes any adjacent duplicate points.

        If 'checkZ' is True, x, y, and z coordinates are checked, otherwise only
        x and y are.

        Args:
            checkZ (bool): Whether to check the Z coordinate of the points.
        """
    def reverse(self) -> None: ...
    def rotate2D(self, center: FMEPoint, angle: float) -> None: ...
    def scale(self, xScale: float, yScale: float, zScale: float) -> None: ...
    def setEndPoint(self, point: FMEPoint) -> None:
        """Changes the existing end point of this curve.

        If there are no points on the curve, this method does nothing.

        Args:
            point (FMEPoint): The end point.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setStartPoint(self, point: FMEPoint) -> None:
        """Changes the existing start point of this curve.

        If there are no points on the curve, this method does nothing.

        Args:
            point (FMEPoint): The start point.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def snip(
        self,
        measureType: int,
        measure3D: bool,
        startLocation: float,
        endLocation: float,
    ) -> None:
        """Take a description of start and end positions.

        Either as a measured 2D/3D distance, percentage, or normalized distance
        from the beginning, or a vertex index; and chop off only the portion
        between these positions. If the start and end positions are the same,
        keep two same points.

        Args:
            measureType (int): The measure type to use. Must be on of:
                SNIP_DISTANCE, SNIP_PERCENTAGE, SNIP_VERTEX or SNIP_POINT.
            measure3D (bool): Whether to measure the 2D or 3D distance.
            startLocation (float): The start location.
            endLocation (float): The end location.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def snipByPoints(self, startPoint: FMEPoint, endPoint: FMEPoint) -> None:
        """Snip off the portion between two points.

        If these points are not on this line, replaced with nearest points which
        are exactly on the line. If the start and end point are the same, keep
        two same points.

        Args:
            startPoint (FMEPoint): The start point.
            endPoint (FMEPoint): The end point.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """

class FMEMultiCurve(FMEGeometry):
    """FME Multi-Curve Class"""

    def __init__(self, multiCurve: FMEMultiCurve) -> None:
        """Initializes a new instance of the FMEMultiCurve class.

        Args:
            multiCurve (FMEMultiCurve): The multi-curve to copy.

        Returns:
            An instance of the FMEMultiCurve class.
        """
    def appendPart(self, curve: FMECurve) -> None:
        """This appends the curve to the MultiCurve.

        If None is passed in, nothing will be appended. All curves in the
        MultiCurve will be forced to have the same dimension. If any 3D curves
        exist, all 2D curves will be converted to 3D with a default Z value of 0.0.

        Args:
            curve (FMECurve): The curve to append.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def appendParts(self, multiCurve: FMEMultiCurve) -> None:
        """This appends the MultiCurve passed in to the existing MultiCurve.

        If None is passed in, nothing will be appended.

        Args:
            multiCurve (FMEMultiCurve): The multi-curve to append.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getPartAt(self, index: int) -> FMECurve | None:
        """Returns the curve at the specified index.

        Args:
            index (int): The index of the curve to return.

        Returns:
            FMECurve: The curve at the given index. Note: This method returns a
            terminal curve type of the FMECurve; i.e. one of the leaf classes in
            the FMECurve inheritance graph. For example, a FMELine is returned
            if the curve truly is a line.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def numParts(self) -> int:
        """Returns the number of parts in the MultiCurve.

        Returns:
            int: The number of parts in the MultiCurve.
        """
    def offset(self, offsetPoint: FMEPoint) -> None:
        """Offset this geometry by the given offset point.

        Args:
            offsetPoint (FMEPoint): The point to offset the coordinates of the geometry by.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def removeLastPart(self) -> FMECurve | None:
        """This removes and returns the last curve of the MultiCurve.

        If there are no curves in the MultiCurve, it will return None.

        Returns:
            FMECurve: The last curve of the MultiCurve. Note: This method returns
                a terminal curve type of the FMECurve; i.e. one of the leaf
                classes in the FMECurve inheritance graph. For example, a FMELine
                is returned if the curve truly is a line.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def scale(self, xScale: float, yScale: float, zScale: float) -> None:
        """Scale the curve by the given scaling factors.

        Args:
            xScale (float): The X scaling factor.
            yScale (float): The Y scaling factor.
            zScale (float): The Z scaling factor.
        Raises:
            FMEException: An exception is raised if an error occurred.
        """

class FMEPath(FMECurve, TransformMixin):
    """FME Path Class

    Create an instance of a Path geometry object.

    init(): Default FMEPath constructor.

    init(path): Create a copy of the passed in Path geometry object.
    """

    @overload
    def __init__(self) -> None:
        """
        Default FMEPath constructor.

        Returns:
            An instance of the FMEPath class."""
    @overload
    def __init__(self, path: FMEPath) -> None:
        """Initializes a new instance of the FMEPath class.

        Args:
            path (FMEPath): The path to copy.

        Returns:
            An instance of the FMEPath class.
        """
    def appendPart(self, curve: FMECurve) -> None:
        """Append an entire curve.

        If the path and the curve are not connected, a new line will be inserted
        between them. If any 3D segments exist, all 2D segments will be converted
        to 3D with a default Z value of 0.0.

        Args:
            curve (FMECurve): The curve to append.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def appendPartWithSnapping(self, curve: FMECurve) -> None:
        """Append an entire segment.

        If the path and the curve are not connected, the first point on the
        curve will be moved to instead be the last point on the path.
        If any 3D segments exist, all 2D segments will be converted to 3D with a
        default Z value of 0.0.

        Args:
            curve (FMECurve): The curve to append with snapping.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def extendToPoint(self, point: FMEPoint) -> None:
        """Extend the path to the given point.

        If the point is 2D and the path is 3D, the point will be set to 3D with
        a Z value of 0.0. If the path is 2D and the point is 3D, the segments in
        the path will be set to 3D with 0.0 for Z values. If None is passed in,
        nothing will be appended.

        Args:
            point (FMEPoint): The point to be extended to.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def extendToPointXY(self, xcoord: float, ycoord: float) -> None:
        """Extend the path to the given point.

        If this method is called on a 3D line, a Z value of 0.0 will be used for
        each appended point.

        Args:
            xcoord (float): The X coordinate of the point.
            ycoord (float): The Y coordinate of the point.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def extendToPointXYZ(self, xcoord: float, ycoord: float, zcoord: float) -> None:
        """Extend the path to the given point.

         If this method is called on a 2D line, the line will be forced to 3D
         with a default Z value of 0.0.

        Args:
            xcoord (float): The X coordinate of the point.
            ycoord (float): The Y coordinate of the point.
            zcoord (float): The Z coordinate of the point.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def extendToPointsXY(self, coords: list[tuple[float, float]]) -> None:
        """Extend the path to a list of points.

        If this method is called on a 3D path, a Z value of 0.0 will be used for
        each appended point.

        Args:
            coords (list[tuple[float]]): The list of 2D points to be extended to.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def extendToPointsXYZ(self, coords: list[tuple[float, float, float]]) -> None:
        """Extend the path to a list of points.

        If this method is called on a 2D path, the path will be forced to 3D with
        a default Z value of 0.0.

        Args:
            coords (list[tuple[float]]): The list of 3D points to be extended to.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getAsLine(self) -> FMELine:
        """Returns the path as a line.

        Returns:
            FMELine: The path as a line.
        """
    def getAsLineFixedArcSamples(self, numSamples: int) -> FMELine:
        """Returns a copy of this curve as a line.

        All arcs are approximated with the number of points given by 'numSamples'.
        If 'numSamples' is 0, the number points will first be determined by the
        value of kFMEStrokeMaxDeviationValue directive in mapping file, which denotes
        the maximum deviation of the arc from the line. In the absence of this
        directive or the value of this directive is smaller than or equal to 0,
        the number points will be determined by the arc's sweep angle and the
        value of the mapping file directive kFMEDegreesPerEdge, which defaults to 5.

        Args:
            numSamples (int): The number of points to approximate the arc with.

        Returns:
            FMELine: The path as a as a FMELine object.
        """
    def getEndPoint(self) -> FMEPoint | None:
        """Returns the end point of the path.

        An error is returned and None is returned if this curve has no point to return.

        Returns:
            FMEPoint: The end point of the curve, or None if there is no point to return.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getLength(self, threeD: bool) -> float:
        """Returns the length of the path.

        If 'threeD' is True, this returns the 3D length of the curve, otherwise
        this returns the 2D length.

        Args:
            threeD (bool): Whether to calculate the 2D or 3D length.

        Returns:
            float: The length of the path.
        """
    def getPartAt(self, index: int) -> FMEArc | FMELine:
        """This returns the part of the FMEPath at the given index.

        This returns None if the index is out of range.

        Args:
            index (int): The index of the part to return.

        Returns:
            FMEArc or FMELine: The FMESegment at the given index. Returns the
                terminal geometry of the FMESegment, either a FMEArc or FMELine.
        """
    def getStartPoint(self) -> FMEPoint | None:
        """Returns the start point of the path.

        An error is returned and None is returned if this curve has no point to return.

        Returns:
            FMEPoint: The start point of the curve, or None if there is no point to return.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def isClosed(self, threeD: bool) -> bool:
        """Returns True if the start and end points have identical coordinate values.

        If 'threeD' is True, the z coordinate of the start and end points will be
        compared. This does not take measures into consideration.

        Args:
            threeD (bool): Whether to compare the z coordinate value.

        Returns:
            bool: True if the start and end point have identical coordinate
                values, False otherwise.
        """
    def isLinear(self) -> bool:
        """Returns True if and only if this curve contains only lines.

        Returns:
            bool: True if the curve contains only lines, False otherwise.
        """
    def numParts(self) -> int:
        """This returns the number of FMESegment that make up this path.

        Returns:
            int: The number of FMESegment that are used to make the FMEPath.
        """
    def offset(self, offsetPoint: FMEPoint) -> None: ...
    def removeDuplicates(self, checkZ: bool) -> None:
        """Remove duplicate points from the path.

        If 'checkZ' is True, the z coordinate of the points will be compared.

        Args:
            checkZ (bool): Whether to compare the z coordinate value.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def removeEndPart(self) -> FMEArc | FMELine:
        """This removes the end FMESegment of the path.

        If there are no segments in the FMEPath, None is returned.

        Returns:
            FMEArc or FMELine: The end FMESegment of the path, or None if there
                are no segments in the FMEPath.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def reverse(self) -> None: ...
    def rotate2D(self, center: FMEPoint, angle: float) -> None: ...
    def scale(self, xScale: float, yScale: float, zScale: float) -> None: ...
    def setEndPoint(self, point: FMEPoint) -> None:
        """Changes the existing end point of this curve.

        If there are no points on the curve, this method does nothing.

        Args:
            point (FMEPoint): The end point to set.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setStartPoint(self, point: FMEPoint) -> None:
        """Changes the existing start point of this curve.

        If there are no points on the curve, this method does nothing.

        Args:
            point (FMEPoint): The start point to set.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def snip(
        self,
        measureType: int,
        measure3D: bool,
        startLocation: float,
        endLocation: float,
    ) -> None:
        """Take a description of start and end positions.

        (either as a measured 2D/3D distance, percentage, or normalized distance
        from the beginning, or a vertex index), and chop off only the portion
        between these positions. If the start and end positions are the same,
        keep two same points.

        Args:
            measureType (int): The measure type to use. Must be on of:
                SNIP_DISTANCE, SNIP_PERCENTAGE, SNIP_VERTEX or SNIP_POINT.
            measure3D (bool): Whether to measure the 2D or 3D distance.
            startLocation (float): The start location to snip at.
            endLocation (float): The end location to snip at.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def snipByPoints(self, startPoint: FMEPoint, endPoint: FMEPoint) -> None:
        """Snip off the portion between two points.

        If these points are not on this line, replaced with nearest points which
        are exactly on the line. If the start and end point are the same, keep
        two same points.

        Args:
            startPoint (FMEPoint): The start point to snip at.
            endPoint (FMEPoint): The end point to snip at.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """

class FMESegment(FMECurve):
    """FME Segment Class

    FMESegment is an abstract class. It cannot be created directly."""

    def getAsLine(self) -> FMELine:
        """Returns the segment as a line.

        Returns:
            FMELine: The segment as a line.
        """
    def getAsLineFixedArcSamples(self, numSamples: int) -> FMELine:
        """Returns a copy of this curve as a line.

        All arcs are approximated with the number of points given by 'numSamples'.
        If 'numSamples' is 0, the number points will first be determined by the
        value of kFMEStrokeMaxDeviationValue directive in mapping file, which
        denotes the maximum deviation of the arc from the line. In the absence
        of this directive or the value of this directive is smaller than or equal
        to 0, the number points will be determined by the arc's sweep angle and
        the value of the mapping file directive kFMEDegreesPerEdge, which defaults to 5.

        Args:
            numSamples (int): The number of points to approximate the arc with.

        Returns:
            FMELine: The segment as a line.
        """
    def getEndPoint(self) -> FMEPoint | None:
        """Returns the end point of this curve.

        An error is returned and None is returned if this curve has no point to return.

        Returns:
            FMEPoint or None: The end point of the segment.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getLength(self, threeD: bool) -> float:
        """Returns the length of this curve.

        If 'threeD' is True, this returns the 3D length of the curve, otherwise
        this returns the 2D length.

        Args:
            threeD (bool): Whether to calculate the 2D or 3D length.

        Returns:
            float: The length of the segment.
        """
    def getStartPoint(self) -> FMEPoint | None:
        """Returns the start point of this curve.

        An error is returned and None is returned if this curve has no point to return.

        Returns:
            FMEPoint or None: The start point of the segment.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def isClosed(self, threeD: bool) -> bool:
        """Returns True if the start and end points have identical coordinate values.

        If 'threeD' is True, the z coordinate of the start and end points will be
        compared. This does not take measures into consideration.

        Args:
            threeD (bool): Whether to compare the z coordinate value.

        Returns:
            bool: True if the start and end point have identical coordinate
                values, False otherwise.
        """
    def isLinear(self) -> bool:
        """Returns True if and only if this curve contains only lines.

        Returns:
            bool: True if the curve contains only lines, False otherwise.
        """
    def offset(self, offsetPoint: FMEPoint) -> None: ...
    def removeDuplicates(self, checkZ: bool) -> None:
        """Removes any adjacent duplicate points.

        If 'checkZ' is True, x, y, and z coordinates are checked, otherwise
        only x and y are.

        Args:
            checkZ (bool): Whether to check the z coordinate value.
        """
    def reverse(self) -> None: ...
    def rotate2D(self, centre: FMEPoint, angle: float) -> None: ...
    def scale(self, xScale: float, yScale: float, zScale: float) -> None: ...
    def setEndPoint(self, point: FMEPoint) -> None:
        """Changes the existing end point of this curve.

        If there are no points on the curve, this method does nothing.

        Args:
            point (FMEPoint): The point to set at the end of the curve.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setStartPoint(self, point: FMEPoint) -> None:
        """Changes the existing start point of this curve.

        If there are no points on the curve, this method does nothing.

        Args:
            point (FMEPoint): The point to set at the start of the curve.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def snip(
        self,
        measureType: int,
        measure3D: bool,
        startLocation: float,
        endLocation: float,
    ) -> None:
        """Take a description of start and end positions

        (either as a measured 2D/3D distance, percentage, or normalized distance
        from the beginning, or a vertex index), and chop off only the portion
        between these positions. If the start and end positions are the same,
        keep two same points.

        Args:
            measureType (int): The measure type to use. Must be on of:
                SNIP_DISTANCE, SNIP_PERCENTAGE, SNIP_VERTEX or SNIP_POINT.
            measure3D (bool): Whether to measure the 2D or 3D distance.
            startLocation (float): The start location to snip at.
            endLocation (float): The end location to snip at.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def snipByPoints(self, startPoint: FMEPoint, endPoint: FMEPoint) -> None:
        """Snip off the portion between two points.

        If these points are not on this line, replaced with nearest points which
        are exactly on the line. If the start and end point are the same, keep
        two same points.

        Args:
            startPoint (FMEPoint): The start point to snip at.
            endPoint (FMEPoint): The end point to snip at.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """

class FMESegmentIterator:
    """FME SegmentIterator Class"""

class FMELine(FMESegment):
    """FME Line Class"""

    @overload
    def __init__(self, is3D: bool) -> None:
        """Constructs a 3D line if 'is3D' is True, otherwise a 2D line is created.

        Args:
            is3D (bool): The value to set the line’s dimension.

        Returns:
            An instance of a Line Geometry object
        """
    @overload
    def __init__(self, points: list[tuple[float]]) -> None:
        """Constructs a line from a list of points.

        Args:
            points (list[tuple[float]]): The list of points to set to the line.
                The points are represented as (x, y) or (x, y, z) tuples

        Returns:
            An instance of a Line Geometry object
        """
    @overload
    def __init__(self, line: FMELine) -> None:
        """Constructs a line from another line.

        Args:
            line (FMELine): The line to copy

        Returns:
            An instance of a Line Geometry object
        """
    def appendLine(self, line: FMELine) -> None:
        """Appends 'line' to the end of the existing line.

        If the existing line has no coordinates, it will have its geometry
        dimension set based on the first append call made. This line's points
        will be forced to have a consistent dimension. If a 2D line is appended
        to a 3D line, the 2D line will be changed to 3D with a Z value of 0.0.
        If a 3D line is appended to a 2D line, the 2D line will be changed to
        3D with 0.0 for all Z values. The appended line will be forced to have
        consistent measures. Any unspecified measure values will be set to None.

        Args:
            line (FMELine): The line to append
        """
    def appendPoint(self, point: FMEPoint | tuple[float, float, float]) -> None:
        """Appends 'point' to the end of the existing line.

        Lines with no coordinates will have their dimension set based on the
        first append call made. The line's points will be forced to have a
        consistent dimension. If a 2D point is appended to a 3D line, the point
        will be changed to 3D with a Z value of 0.0. If a 3D point is appended
        to a 2D line, the line will be changed to 3D with 0.0 for all Z values.
        The points will be forced to have consistent measures. Any unspecified
        measure values will be set to None. Nothing is appended if None is passed in.

        Args:
            point (FMEPoint or tuple): The point to append

        Raises:
            FMEException: An exception is raised if an error occurs.
        """
    def appendPoints(self, points: list[FMEPoint]) -> None:
        """Appends 'points' to the end of the existing line.

        Lines with no coordinates will have their geometry dimension set based
        on the first append call made. If this method is called on a 3D line, a
        Z value of 0.0 will be used for each appended point. If this method is
        called on a 2D line, the line will be forced to 3D with a default Z value
        of 0.0. Because this method does not specify measure values, a value of
        None will be used for each point for any existing measures.

        Args:
            points (list[FMEPoint]): The list of points to append

        Raises:
            FMEException: An exception is raised if an error occurs.
        """
    def getAsLine(self) -> FMELine:
        """Returns the curve as a line.

        Returns:
            (FMELine): The curve as a FMELine object.
        """
    def getAsLineFixedArcSamples(self, numSamples: int) -> FMELine:
        """Returns a copy of this curve as a line.

        All arcs are approximated with the number of points given by 'numSamples'.
        If 'numSamples' is 0, the number points will first be determined by the
        value of kFMEStrokeMaxDeviationValue directive in mapping file, which
        denotes the maximum deviation of the arc from the line. In the absence
        of this directive or the value of this directive is smaller than or equal
        to 0, the number points will be determined by the arc's sweep angle and
        the value of the mapping file directive kFMEDegreesPerEdge, which defaults to 5.

        Args:
            numSamples (int): The number of points to approximate the arc with.

        Returns:
            (FMELine): The curve as a FMELine object.
        """
    def getEndPoint(self) -> FMEPoint | None:
        """Returns the end point of the line.

        An error is returned and None is returned if this curve has no point to return.

        Returns:
            (FMEPoint or None): The end point of the line.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getLength(self, threeD: bool) -> float:
        """Returns the length of the line.

        If 'threeD' is True, this returns the 3D length of the curve,
        otherwise this returns the 2D length.

        Args:
            threeD (bool): Whether to calculate the 2D or 3D length.

        Returns:
            (float): The length of the line.
        """
    def getPointAt(self, index: int) -> FMEPoint:
        """Gets the point at the specified 'index'.

        An error is returned if the index is out of range.

        Args:
            index (int): The index of the point to return.

        Returns:
            (FMEPoint): The point at the given index.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getPoints(self) -> list[FMEPoint]:
        """Gets the points of the line as a list of FMEPoint objects.

        An exception is raised if an error occurred getting a point from the line.

        Returns:
            (list[FMEPoint]): The points of the line.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getStartPoint(self) -> FMEPoint | None:
        """Returns the start point of the line.

        An error is returned and None is returned if this curve has no point to return.

        Returns:
            (FMEPoint or None): The start point of the line.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def indexOfCoord(self, coord: tuple[float, float, float]) -> int:
        """Returns the index of the first coordinate defined within the tuple 'coord',
        or FME_NPOS32 if no such coordinate is found.

        Args:
            coord (tuple): The z tuple containing coordinate whose index to search.

        Returns:
            (int): The index of the supplied coordinate,
                or FME_NPOS32 if no such coordinate exists.
        """
    def insertPointAtIndex(self, point: FMEPoint, index: int) -> None:
        """Inserts a point at the specified 'index'.

        All points from that index on will be shifted to allow room for the new
        point. Any new measures added to the point will be set a default of None.

        Args:
            point (FMEPoint): The point to insert.
            index (int): The index of the point to remove.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def isClosed(self, threeD: bool) -> bool:
        """Returns True if the start and end points have identical coordinate values.
        If 'threeD' is True, the z coordinate of the start and end points will
        be compared. This does not take measures into consideration.

        Args:
            threeD (bool): Whether to compare the z coordinate value.

        Returns:
            (bool): True if the start and end point have identical coordinate values, False otherwise.
        """
    def isLinear(self) -> bool:
        """Returns True if and only if this curve contains only lines.

        Returns:
            (bool): True if the curve contains only lines, False otherwise.
        """
    def numPoints(self) -> int:
        """Returns the number of points in the line.

        Returns:
            (int): The number of points in the line.
        """
    def offset(self, offsetPoint: FMEPoint) -> None:
        """Offsets the line by the distance from the start point to the supplied point.

        The offset point is the point from which the line will be offset.
        The offset point will be removed from the line.

        Args:
            offsetPoint (FMEPoint): The point from which the line will be offset.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def removeDuplicates(self, checkZ: bool) -> None:
        """Removes duplicate points from the line.

        If 'checkZ' is True, the z coordinate of the points will be compared.
        This does not take measures into consideration.

        Args:
            checkZ (bool): Whether to compare the z coordinate value.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def removePointAt(self, index: int) -> FMEPoint | None:
        """Removes the point at the specified 'index' and returns.

        Null is returned if the index is out of range.

        Args:
            index (int): The index of the point to remove.

        Returns:
            (FMEPoint or None): The point removed, or None if the index is out of range.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def reset(self, coords: list[tuple[float, float, float]]) -> None:
        """Resets the coordinates to an 'empty' state.

        It does not alter the geometry dimension, but it does remove all measures.
        If 'coords' is supplied, then this method sets the line's coordinates to
        the values in the supplied 'coords' list. None zCoord values will result
        in a 2D line, otherwise a 3D line is created. This method removes all measures.

        Args:
            coords (list[tuple]): (Optional) The list of coordinate tuples to
                add after the reset.
        """
    def reverse(self) -> None:
        """Reverses the order of the points in the line."""
    def rotate2D(self, centre: FMEPoint, angle: float) -> None:
        """Rotate the curve counterclockwise around the 'center' point by the
        specified 'angle' (in degrees).

        The angle is specified in radians.

        Args:
            centre (FMEPoint): The centre of the rotation.
            angle (float): The angle of the rotation.
        """
    def scale(self, xScale: float, yScale: float, zScale: float) -> None:
        """Scales the line by the supplied 'xScale', 'yScale' and 'zScale'.

        Args:
            xScale (float): The x scale factor.
            yScale (float): The y scale factor.
            zScale (float): (optional) The z scale factor.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setEndPoint(self, point: FMEPoint) -> None:
        """Sets the end point of the line.

        Args:
            point (FMEPoint): The point to set as the end point.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setPointAt(self, index: int, point: FMEPoint) -> None:
        """Sets 'point' at the specified index.

        The line's points will be forced to have a consistent dimension. If any
        points are 3D, they all must be. A Z value of 0.0 is used when converting
        from a 2D point to a 3D point. The points will be forced to have
        consistent measures. Any unspecified measure values will be set to None.
        An error is returned if the index is out of range.

        Args:
            index (int): The index of the point to set.
            point (FMEPoint): The point to set.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setStartPoint(self, point: FMEPoint) -> None:
        """Sets the start point of the line.

        Args:
            point (FMEPoint): The point to set as the start point.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def snip(
        self,
        measureType: int,
        measure3D: bool,
        startLocation: float,
        endLocation: float,
    ) -> None:
        """Take a description of start and end positions

        (either as a measured 2D/3D distance, percentage, or normalized distance
        from the beginning, or a vertex index), and chop off only the portion
        between these positions. If the start and end positions are the same,
        keep two same points.

        Args:
            measureType (int): The measure type to use. Must be on of:
                SNIP_DISTANCE, SNIP_PERCENTAGE, SNIP_VERTEX or SNIP_POINT.
            measure3D (bool): Whether to measure the 2D or 3D distance.
            startLocation (float): The location at which to split the line.
            endLocation (float): The location at which to split the line.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def snipByPoints(self, startPoint: FMEPoint, endPoint: FMEPoint) -> None:
        """Snip off the portion between two points.

        If these points are not on this line, replaced with nearest points which
        are exactly on the line. If the start and end point are the same,
        keep two same points.

        Args:
            startPoint (FMEPoint): The start point.
            endPoint (FMEPoint): The end point.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """

class FMEArc(FMESegment):
    """FME Arc Class"""

    @overload
    def __init__(self, threePoints: tuple[FMEPoint, FMEPoint, FMEPoint]) -> None:
        """Creates an arc using the 3 points contained in the tuple.

        If 'startPoint' and 'endPoint' (threePoints[0] and threePoints[2]) and
        are equal, then the arc will be coincident with the circle whose center
        point is midway between startPoint and midpoint (threePoints[0] and threePoints[1]).

        Args:
            threePoints (tuple[FMEPoint]): The tuple containing 3 points to create
                the arc in the form (startPoint, midPoint, endPoint).

        Returns:
            (FMEArc): An instance of an Arc Geometry object.
        """
    @overload
    def __init__(self, twoPoints: tuple[FMEPoint, FMEPoint], bulge: float) -> None:
        """Creates an arc using the 2 points contained in the tuple, and the supplied 'bulge' value.

        All angles are CCW up from the horizontal, and are measured in degrees.

        Args:
            twoPoints (tuple[FMEPoint]): The tuple containing 2 points to create
                the arc in the form (startPoint, endPoint).
            bulge (float): The bulge value for the arc to be created.

        Returns:
            (FMEArc): An instance of an Arc Geometry object.
        """
    @overload
    def __init__(
        self,
        centrePoint: FMEPoint,
        rotation: float,
        primaryRadius: float,
        secondaryRadius: float,
        startAngle: float,
        sweepAngle: float,
    ) -> None:
        """Creates an arc using the center point supplied, along with the
        supplied radii and angles.

        Measures on the center point will be ignored. All angles are CCW up from
        the horizontal, and are measured in degrees.

        Args:
            centrePoint (FMEPoint): The centre point of the arc.
            rotation (float): The rotation angle of the arc.
            primaryRadius (float): The radius of the arc.
            secondaryRadius (float): The secondary radius of the arc.
            startAngle (float): The start angle of the arc.
            sweepAngle (float): The sweep angle of the arc.

        Returns:
            (FMEArc): An instance of an Arc Geometry object.
        """
    @overload
    def __init__(
        self,
        centerPoint: FMEPoint,
        rotation: float,
        primaryRadius: float,
        secondaryRadius: float,
        startAngle: float,
        sweepAngle: float,
        startPoint: FMEPoint,
        endPoint: FMEPoint,
    ) -> None:
        """Creates an arc using the center point supplied, along with the
        supplied radii, angles, and points.

        All angles are CCW up from the horizontal, and are measured in degrees.

        Args:
            centrePoint (FMEPoint): The centre point of the arc.
            rotation (float): The rotation angle of the arc.
            primaryRadius (float): The radius of the arc.
            secondaryRadius (float): The secondary radius of the arc.
            startAngle (float): The start angle of the arc.
            sweepAngle (float): The sweep angle of the arc.
            startPoint (FMEPoint): (optional) The start point of the arc.
            endPoint (FMEPoint): (optional) The end point of the arc.

        Returns:
            (FMEArc): An instance of an Arc Geometry object.
        """
    @overload
    def __init__(
        self,
        twoPoints: tuple[FMEPoint, FMEPoint],
        radius: float,
        counterClockwise: bool,
    ) -> None:
        """Creates an arc using the 2 points contained in the tuple, and the
        supplied 'radius' and points.

        startPoint and endPoint (twoPoints[0] and twoPoints[1]) must not be None.

        Args:
            twoPoints (tuple[FMEPoint]): The tuple containing 2 points to create
                the arc in the form (startPoint, endPoint).
            radius (float): The radius of the arc to be created.
            counterClockwise (bool): Whether the arc is to be drawn counter-clockwise.

        Returns:
            (FMEArc): An instance of an Arc Geometry object.
        """
    @overload
    def __init__(self, arc: FMEArc) -> None:
        """Creates an arc using the supplied arc.

        Args:
            arc (FMEArc): The arc to be copied.

        Returns:
            (FMEArc): An instance of an Arc Geometry object.
        """
    def bisectArc(self) -> FMEPath:
        """BReturns an equivalent path consisting of two smaller arcs.

        These two arcs do not necessarily have equal length.

        Returns:
            (FMEPath): An equivalent path consisting of two smaller arcs.
        """
    def convertToArcBy3Points(self) -> None:
        """Converts the arc to an arc by 3 points.

        If the arc is not circular (isCircular() returns False), then the arc
        cannot be converted to arc by 3 points, and an error is returned.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def convertToArcByBulge(self) -> None:
        """Converts the arc to an arc by bulge.

        If the arc is not circular (isCircular() returns False), then the arc
        cannot be converted to arc by bulge, and an error is returned.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def convertToArcByCenterPoint(self) -> None:
        """Converts the arc to an arc by center point.

        If the arc cannot be converted, then an error is returned.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getAsLine(self) -> FMELine:
        """Returns an equivalent line.

        Returns:
            (FMELine): An equivalent line.
        """
    def getAsLineFixedArcSamples(self, numSamples: int) -> FMELine:
        """Returns a copy of this curve as a line.

        All arcs are approximated with the number of points given by 'numSamples'.
        If 'numSamples' is 0, the number points will first be determined by the
        value of kFMEStrokeMaxDeviationValue directive in mapping file, which
        denotes the maximum deviation of the arc from the line. In the absence
        of this directive or the value of this directive is smaller than or equal
        to 0, the number points will be determined by the arc's sweep angle and
        the value of the mapping file directive kFMEDegreesPerEdge, which defaults to 5.

        Args:
            numSamples (int): The number of points to be used to approximate the arc.

        Returns:
            (FMELine): An equivalent line.
        """
    def getBulge(self) -> float:
        """Returns the bulge value of the arc.

        An error is returned if an error occurs.

        Returns:
            (float): The bulge value of the arc.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getCenterPoint(self) -> FMEPoint:
        """Returns the center point of the arc.

        An error is returned if an error occurs.

        Returns:
            (FMEPoint): The center point of the arc.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getEndPoint(self) -> FMEPoint | None:
        """Returns the end point of the arc.

        An error is returned and None is returned if this curve has no point to return.

        Returns:
            (FMEPoint): The end point of the arc.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getLength(self, threeD: bool) -> float:
        """Returns the length of the arc.

        If 'threeD' is True, this returns the 3D length of the curve, otherwise
        this returns the 2D length.

        Args:
            threeD (bool): Whether to calculate the length in 3D.

        Returns:
            (float): The length of the arc.
        """
    def getMidpoint(self) -> FMEPoint:
        """Returns mid point, which will be interpolated halfway along the arc if
        the underlying storage is not by 3 points.

        If an arc is elliptical, an error is returned.

        Returns:
            (FMEPoint): The midpoint of the arc.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getPrimaryRadius(self) -> float:
        """Returns the primary radius of the arc.

        Returns:
            (float): The primary radius of the arc.
        """
    def getPropertiesAs3Points(self) -> tuple[FMEPoint]:
        """Returns the arc geometry as a tuple of three points.

        If the arc is elliptical, an error is returned.

        The structure of the tuple returned is as follows:
            (startPoint, midPoint, endPoint).

        Returns:
            (tuple[FMEPoint]): The arc geometry as three points.
        """
    def getPropertiesAsBulge(self) -> tuple[FMEPoint, FMEPoint, float]:
        """Returns the arc geometry as a tuple of three points and a bulge.

        If the arc is elliptical, an error is returned.

        The structure of the tuple returned is as follows:
            (startPoint, endPoint, bulge).

        Returns:
            (tuple[FMEPoint, FMEPoint, float]): The arc geometry as three points
                and a bulge.
        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getPropertiesAsCentered(
        self,
        withEnds: bool,
    ) -> tuple[FMEPoint, float, float, float, float, float, FMEPoint, FMEPoint] | tuple[
        FMEPoint, float, float, float, float, float
    ]:
        """Returns the arc properties.

        If 'withEnds' is True, the end points will be computed and returned.
        Note that measures are only stored on the end points. All angles are CCW
        up from the horizontal, and rotation is measured in degrees. Also, 'startAngle'
        and 'sweepAngle' aren't angles. Refer to the @Arc (function) in the
        FME Functions and Factories manual for a detailed definition of 'startAngle'.

        The structure of the tuple returned if 'withEnds' is True is as follows:
            (centerPoint, rotation, primaryRadius, secondaryRadius,
            startAngle, sweepAngle, startPoint, endPoint).

        The structure of the tuple returned if 'withEnds' is False is as follows:
            (centerPoint, rotation, primaryRadius, secondaryRadius,
            startAngle, sweepAngle).

        Returns:
            (tuple[FMEPoint, float, float, float, float, FMEPoint, FMEPoint]):
                The arc geometry as a centered point definition.
        """
    def getRotation(self) -> float:
        """Returns the rotation of the arc.

        All angles are CCW up from the horizontal, and are measured in degrees.

        Returns:
            (float): The rotation of the arc.
        """
    def getSecondaryRadius(self) -> float:
        """Returns the secondary radius of the arc.

        Returns:
            (float): The secondary radius of the arc.
        """
    def getStartAngle(self) -> float:
        """Returns the start angle of the arc.

        All angles are CCW up from the horizontal.

        Note: 'startAngle' isn't an angle. Refer to the @Arc (function) in the
        FME Functions and Factories manual for a detailed definition of startAngle.

        Returns:
            (float): The start angle of the arc.
        """
    def getStartPoint(self) -> FMEPoint | None:
        """Returns the start point of the arc.

        An error is returned and None is returned if this curve has no point to return.

        Returns:
            (FMEPoint): The start point of the arc.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getSweepAngle(self) -> float:
        """Returns the sweep angle of the arc.

        All angles are CCW up from the horizontal.

        Note: 'startAngle' isn't an angle. Refer to the @Arc (function) in the
        FME Functions and Factories manual for a detailed definition of startAngle.

        Returns:
            (float): The sweep angle of the arc.
        """
    def hasExplicitEndpoints(self) -> bool:
        """This returns True if the arc's end points have been explicitly set, and False otherwise.

        getPropertiesAsCentered() method can calculate the end points if none
        have been specified by setting the 'withEnds' parameter to True. If this
        is not desired, hasExplicitEndpoints can be called first to determine
        whether the 'withEnds' parameter should be set to True or False.

        Returns:
            (bool): Whether the arc has explicit endpoints.
        """
    def isCW(self) -> bool:
        """Returns True if the arc is clockwise, and False otherwise.

        Returns:
            (bool): Whether the arc is clockwise.
        """
    def isCircular(self) -> bool:
        """Returns True if the arc is circular, and False otherwise.

        Returns:
            (bool): Whether the arc is circular.
        """
    def isClosed(self, threeD: bool) -> bool:
        """Returns True if the start and end points have identical coordinate values.

        If 'threeD' is True, the z coordinate of the start and end points will
        be compared. This does not take measures into consideration.

        Returns:
            (bool): True if the start and end point have identical coordinate values,
                False otherwise.
        """
    def isLinear(self) -> bool:
        """Returns True if and only if this curve contains only lines.

        Returns:
            (bool): True if the curve contains only lines, False otherwise.
        """
    def offset(self, offsetPoint: FMEPoint) -> None:
        """Offset the arc by the specified point.

        Args:
            offsetPoint (FMEPoint): The point to offset the arc by.
        """
    def optimalArcTypeRetrieval(self) -> int:
        """Returns the arc type
            (FME_ARC_BY_CENTER_POINT, FME_ARC_BY_CENTER_POINT_START_END,
            FME_ARC_BY_BULGE, or FME_ARC_BY_3_POINTS)
          whose parameters that define the arc can be retrieved most efficiently and accurately.

        Returns:
            (int): The arc type.
        """
    def removeDuplicates(self, checkZ: bool) -> None:
        """Removes any adjacent duplicate points.

        If 'checkZ' is True, x, y, and z coordinates are checked, otherwise only x and y are.

        Args:
            checkZ (bool): Whether to check z coordinates.
        """
    def reverse(self) -> None:
        """This reverses the order of the curve's points."""
    def rotate2D(self, centre: FMEPoint, angle: float) -> None:
        """Rotates the arc by the specified angle about the specified point.

        Args:
            centre (FMEPoint): The point to rotate the arc about.
            angle (float): The angle to rotate the arc by.
        """
    def scale(self, xScale: float, yScale: float, zScale: float) -> None:
        """Scales the arc by the specified factors.

        Args:
            xScale (float): The x scale factor.
            yScale (float): The y scale factor.
            zScale (float): (optional) The z scale factor. Default value is 1.0

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setCenterPoint(self, centerPoint: FMEPoint) -> None:
        """Sets the center point of the arc.

        The arc is converted to an arc by center point as a result of this method.

        Args:
            centerPoint (FMEPoint): The center point to set on the arc.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setEndPoint(self, point: FMEPoint) -> None:
        """Changes the existing end point of this curve.

        If there are no points on the curve, this method does nothing.

        Args:
            point (FMEPoint): The end point to set on the arc.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setMidPoint(self, midPoint: FMEPoint) -> None:
        """Sets the midpoint of the arc.

        It only sets the midpoint if the arc can be successfully converted to
        an arc by mid point.

        Args:
            midPoint (FMEPoint): The mid point to set on the arc.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setPrimaryRadius(self, primaryRadius: float) -> None:
        """Sets the primary radius of the arc.

        The arc is converted to an arc by center point before setting the primary radius.

        Args:
            primaryRadius (float): The primary radius of the arc.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setRotation(self, rotation: float) -> None:
        """Sets the rotation of the arc.

        The arc is converted to an arc by center point before setting the rotation.

        Args:
            rotation (float): The rotation of the arc.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setSecondaryRadius(self, secondaryRadius: float) -> None:
        """Sets the secondary radius of the arc.

        The arc is converted to an arc by center point before setting the secondary radius.

        Args:
            secondaryRadius (float): The secondary radius of the arc.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setStartAngle(self, startAngle: float) -> None:
        """Sets the start angle of the arc, measured counter-clockwise up from the horizontal.

        Note: 'startAngle' is a t angle. Refer to the @Arc (function) in the
        FME Functions and Factories manual for a detailed definition of 'startAngle'.

        Args:
            startAngle (float): The start angle to set on the arc.
        """
    def setStartPoint(self, point: FMEPoint) -> None:
        """Changes the existing start point of this curve.

        If there are no points on the curve, this method does nothing.

        Args:
            point (FMEPoint): The start point to set on the arc.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setSweepAngle(self, sweepAngle: float) -> None:
        """Sets the sweep angle of the arc, measured counter-clockwise up from the horizontal.

        Note: 'sweepAngle' is a t angle. The arc is first converted to an arc by
        center point before the 'sweepAngle' is set. Refer to the @Arc (function)
        in the FME Functions and Factories manual for a detailed definition of 'sweepAngle'.

        Args:
            sweepAngle (float): The sweep angle to set on the arc.
        """
    def snip(
        self,
        measureType: int,
        measure3D: bool,
        startLocation: float,
        endLocation: float,
    ) -> None:
        """Take a description of start and end positions

        (either as a measured 2D/3D distance, percentage, or normalized distance
        from the beginning, or a vertex index), and chop off only the portion
        between these positions. If the start and end positions are the same,
        keep two same points.

        Args:
            measureType (int): The measure type to use. Must be on of:
                SNIP_DISTANCE, SNIP_PERCENTAGE, SNIP_VERTEX or SNIP_POINT.
            measure3D (bool): Whether to measure the 2D or 3D distance.
            startLocation (float): The start location.
            endLocation (float): The end location.
        """
    def snipByPoints(self, startPoint: FMEPoint, endPoint: FMEPoint) -> None:
        """Snip off the portion between two points.

        If these points are not on this line, replaced with nearest points which
        are exactly on the line. If the start and end point are the same,
        keep two same points.

        Args:
            startPoint (FMEPoint): The start point.
            endPoint (FMEPoint): The end point.
        """

class FMEOrientedArc(FMESegment):
    """FME Oriented Arc Class"""

    @overload
    def __init__(
        self,
        arc: FMEArc,
        startCoord: tuple[float, float, float] | None,
        endCoord: tuple[float, float, float] | None,
        transformationMatrix: list[list[float]],
    ) -> None:
        """Creates an oriented arc using an arc, a start coordinate, a end coordinate, and a transformation matrix.

        The startCoord and endCoord are optional and can be specified as None.

        The transformation matrix can be used to place the oriented arc in a
        custom orientation and location as follows:

            Pick three orthogonal unit vectors V1, V2, V3 which represents the
            X, Y, and Z axes of the orientation, and a vector v4 that represents
            the offset of the arc. Then, the transformation matrix is of the
            form: [[V1x,V1y,V1z,0x],[V2x,V2y,V2z,0x],[V3x,V3y,V3z,0x],[0,0,0,1]]

            The matrix can be any kind of affine transformation matrix. Only
            three rows are expected in the input array, as a bottom row of
            [ 0 0 0 1 ] is assumed. The end result of this call will be forced
            to 3D if the input arc is 3D.

        Args:
            arc (FMEArc): The arc to use for creating the oriented arc.
            startCoord (tuple[float,float,float] or None): The start coordinate
                of the oriented arc in the form (x, y, z). The z is not required
                and will be ignored when the input arc is 2D. This is optional
                and can be specified as None.
            endCoord (tuple[float,float,float] or None): The end coordinate of
                the oriented arc in the form (x, y, z). The z is not required
                and will be ignored when the input arc is 2D. This is optional
                and can be specified as None.
            transformationMatrix (list[list[float]]): The transformation matrix
                to apply to the created oriented arc, formatted [[dddd][dddd][dddd]].
                Only three rows are expected in the input array, as a bottom row
                of [ 0 0 0 1 ] is assumed.

        Returns:
            (FMEOrientedArc): The oriented arc.
        """
    @overload
    def __init__(self, orientedArc: FMEOrientedArc) -> None:
        """Creates an oriented arc using an oriented arc.

        Args:
            orientedArc (FMEOrientedArc): The oriented arc to use for creating the oriented arc.

        Returns:
            (FMEOrientedArc): The oriented arc.
        """
    def boundingBox(self) -> tuple[tuple[float]]: ...
    def boundingCube(self) -> tuple[tuple[float]]: ...
    def bounds(self) -> tuple[FMEPoint]: ...
    def clearMeasures(self) -> None: ...
    def copyAttributesFromFeature(
        self,
        sourceFeature: FMEFeature,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyNameFromGeometry(self, sourceGeometry: FMEGeometry) -> None: ...
    def copyTraitsFromGeometry(
        self,
        sourceGeometry: FMEGeometry,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyTraitsToFeature(
        self, destFeature: FMEFeature, overwriteExisting: bool, regexp: str, prefix: str
    ) -> None: ...
    def deleteName(self) -> bool: ...
    def force2D(self) -> None: ...
    def force3D(self, newZ: float) -> None: ...
    def getArcInLocalCoordinates(self) -> FMEArc:
        """Returns the FMEArc contained within this oriented arc, in local coordinates.

        Returns:
            (FMEArc): The arc in local coordinates.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getArea(self) -> float: ...
    def getAsLine(self) -> FMELine: ...
    def getAsLineFixedArcSamples(self, numSamples: int) -> FMELine: ...
    def getEndPoint(self) -> FMEPoint | None: ...
    def getLength(self, threeD: bool) -> float: ...
    def getMeasureNames(self) -> tuple[str]: ...
    def getMeasureValues(self, measureName: str) -> tuple[float]:
        """Returns the values of the specified measures.

        Args:
            measureName (str): The name of the measure to get the values of.

        Returns:
            (tuple[float]): The values of the specified measures.

        Raise:
            FMEException: An exception is raised if an error occurred.
        """
    def getName(self) -> text_type | None: ...
    def getStartPoint(self) -> FMEPoint | None: ...
    def getTrait(self, traitName: str) -> text_type | None: ...
    def getTraitNullMissingAndType(self, traitName: str) -> tuple[bool, bool, int]: ...
    def getTraitType(self, traitName: str) -> int: ...
    def getTransformationMatrix(self) -> list[list[float]]:
        """Gets this oriented arc's transformation matrix.

        If the oriented arc does not have such a matrix, an identity matrix is
        returned. Only the top three rows of the matrix will be returned, as the
        bottom row is always [ 0 0 0 1 ].

        Returns:
            (list[list[float]]): The oriented arc's transformation matrix,
                formatted [[dddd][dddd][dddd]].
        """
    def hasMeasures(self) -> bool: ...
    def hasName(self) -> bool: ...
    def hasTrandformationMatrix(self) -> bool:
        """Returns True if this oriented arc has a transformation matrix.

        Returns:
            (bool): True if this oriented arc has a transformation matrix.
        """
    def is3D(self) -> bool: ...
    def isClosed(self, threeD: bool) -> bool: ...
    def isCollection(self) -> bool: ...
    def isLinear(self) -> bool: ...
    def measureExists(self, measureName: str) -> bool: ...
    def offset(self, offsetPoint: FMEPoint) -> None: ...
    def removeDuplicates(self, checkZ: bool) -> None: ...
    def removeMeasure(self, measureName: str) -> None: ...
    def removeTraits(self, regexp: str) -> None: ...
    def removeTransformationMatrix(self) -> None:
        """Removes this oriented arc's transformation matrix."""
    def renameMeasure(self, oldMeasureName: str, newMeasureName: str) -> None: ...
    def reverse(self) -> None: ...
    def rotate2D(self, centre: FMEPoint, angle: float) -> None: ...
    def scale(self, xScale: float, yScale: float, zScale: float) -> None: ...
    def setArc(self, arc: FMEArc, transformationMatrix: list[list[float]]) -> None:
        """Sets the arc of this oriented arc.

        The input arc should be planar. The existing arc will be replaced and
        the transformation matrix will be reset to the given value. To leave the
        transformation matrix in place and modify the arc's local coordinates only,
        use setArcInLocalCoordinates(). If the input arc is None, then an exception
        will be raised.

        Args:
            arc (FMEArc): The arc to use for creating the oriented arc.
            transformationMatrix (list[list[float]]): The transformation matrix
                to apply to the created oriented arc, formatted [[dddd][dddd][dddd]].
                Only three rows are expected in the input array, as a bottom row
                of [ 0 0 0 1 ] is assumed.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setArcInLocalCoordinate(self, arc: FMEArc) -> None:
        """Sets the arc of this oriented arc.

        The input arc should be planar. If the input arc is None, then an exception
        will be raised.

        Args:
            arc (FMEArc): The arc to set on this oriented arc.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setEndPoint(self, point: FMEPoint) -> None: ...
    def setName(self, name: text_type) -> None: ...
    def setStartPoint(self, point: FMEPoint) -> None: ...
    def setTrait(
        self,
        traitName: str,
        traitValue: bool | int | float | text_type | bytearray | bytes,
    ) -> None: ...
    def setTraitNullWithType(self, traitName: str, traitType: int) -> None: ...
    def setTransformationMatrix(self, transformationMatrix: list[list[float]]) -> None:
        """Sets this oriented arc's transformation matrix.

        Only the top three rows of the matrix will be used, as the bottom row is
        always [ 0 0 0 1 ].

        Args:
            transformationMatrix (list[list[float]]): The transformation matrix
                to apply to the oriented arc, formatted [[dddd][dddd][dddd]].
                Only three rows are expected in the input array, as a bottom row
                of [ 0 0 0 1 ] is assumed.
        """
    def snip(
        self,
        measureType: int,
        measure3D: bool,
        startLocation: float,
        endLocation: float,
    ) -> None: ...
    def snipByPoints(self, startPoint: FMEPoint, endPoint: FMEPoint) -> None: ...

class FMEClothoid(FMESegment):
    """FME Clothoid Class"""

    @overload
    def __init__(
        self,
        startPoint: FMEPoint,
        endPoint: FMEPoint,
        transformationMatrix: list[list[float]],
        localStartCoord: tuple[float, float, float],
        localEndZ: float,
        startDirection: float,
        startCurvature: float,
        endCurvature: float,
        localLength: float,
    ) -> None:
        """
        Creates a clothoid.

        The startPoint and endPoint are optional and can be specified as None.

        The transformation matrix can be used to place the clothoid in a custom
        orientation and location as follows:

            Pick three orthogonal unit vectors V1, V2, V3 which represents the
            X, Y, and Z axes of the orientation, and a vector v4 that represents
            the offset of the arc. Then, the transformation matrix is of the
            form: [[V1x,V1y,V1z,0x],[V2x,V2y,V2z,0x],[V3x,V3y,V3z,0x],[0,0,0,1]]

            The matrix can be any kind of affine transformation matrix. Only
            three rows are expected in the input array, as a bottom row of
            [ 0 0 0 1 ] is assumed.

        Args:
            startPoint (FMEPoint): The start point of the clothoid. It is optional
                and can be specified as None.
            endPoint (FMEPoint): The end point of the clothoid. It is optional
                and can be specified as None.
            transformationMatrix (list[list[float]]): The transformation matrix
                to apply to the created clothoid, formatted [[dddd][dddd][dddd]].
                Only three rows are expected in the input array, as a bottom
                row of [ 0 0 0 1 ] is assumed.
            localStartCoord (tuple[float, float, float]):  The XYZ (in local
                coordinates) of the clothoid's start coordinate in the form (x, y, z).
            localEndZ (float): The elevation (in local coordinates) of the
                clothoid's end coordinate.
            startDirection (float): The start angle (in degrees of the local
                coordinates) of the clothoid.
            startCurvature (float): The start curvature (in local coordinates) of the clothoid.
            endCurvature (float): The end curvature (in local coordinates) of the clothoid.
            localLength (float): The length (in local coordinates) of the clothoid.

        Returns:
            (FMEClothoid): The created clothoid.
        """
    @overload
    def __init__(safe, clothoid: "FMEClothoid") -> None:
        """
        Creates a clothoid from another clothoid.

        Args:
            clothoid (FMEClothoid): The clothoid to copy.

        Returns:
            (FMEClothoid): The created clothoid.
        """
    def boundingBox(self) -> tuple[tuple[float]]: ...
    def boundingCube(self) -> tuple[tuple[float]]: ...
    def bounds(self) -> tuple[FMEPoint]: ...
    def clearMeasures(self) -> None: ...
    def copyAttributesFromFeature(
        self,
        sourceFeature: FMEFeature,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyNameFromGeometry(self, sourceGeometry: FMEGeometry) -> None: ...
    def copyTraitsFromGeometry(
        self,
        sourceGeometry: FMEGeometry,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def copyTraitsToFeature(
        self, destFeature: FMEFeature, overwriteExisting: bool, regexp: str, prefix: str
    ) -> None: ...
    def deleteName(self) -> bool: ...
    def force2D(self) -> None: ...
    def force3D(self, newZ: float) -> None: ...
    def getArea(self) -> float: ...
    def getAsLine(self) -> FMELine: ...
    def getAsLineFixedArcSamples(self, numSamples: int) -> FMELine: ...
    def getEndCurvature(self) -> float:
        """
        Returns the end curvature (in local coordinates) of the clothoid.

        Returns:
            (float): The end curvature (in local coordinates) of the clothoid.
        """
    def getEndPoint(self) -> FMEPoint: ...
    def getLength(self, threeD: bool) -> float: ...
    def getLocalEndZ(self) -> float:
        """Returns the elevation (in local coordinates) of the clothoid's end coordinate.

        If the clothoid is 2D, the z value will be given as NaN.

        Returns:
            (float): The elevation (in local coordinates) of the clothoid's end
                coordinate.
        """
    def getLocalLength(self) -> float: ...
    def getLocalStartCoordXY(self) -> tuple[float, float]:
        """
        Returns the XY (in local coordinates) of the clothoid's start coordinate.

        Returns:
            (tuple[float,float]): The XY (in local coordinates) of the clothoid's start coordinate.
        """
    def getLocalStartCoordXYZ(self) -> tuple[float, float, float]:
        """
        Returns the XYZ (in local coordinates) of the clothoid's start coordinate.

        Returns:
            (tuple[float,float,float]): The XYZ (in local coordinates) of the clothoid's start coordinate.
        """
    def getMeasureNames(self) -> tuple[str]: ...
    def getMeasureValues(self, measureName: str) -> tuple[float, float]:
        """
        Returns the values of the specified measure.

        Args:
            measureName (str): The name of the measure.

        Returns:
            (tuple[float,float]): The values of the named measure in the form
                (start_point_value, end_point_value)
        """
    def getName(self) -> text_type | None: ...
    def getStartCurvature(self) -> float:
        """
        Returns the start curvature (in local coordinates) of the clothoid.

        Returns:
            (float): The start curvature (in local coordinates) of the clothoid.
        """
    def getStartDirection(self) -> float:
        """
        Returns the start angle (in degrees of the local coordinates) of the clothoid.

        Returns:
            (float): The start angle (in degrees of the local coordinates) of the clothoid.
        """
    def getStartPoint(self) -> FMEPoint | None: ...
    def getTrait(
        self, traitName: str
    ) -> bool | int | float | string_types | bytearray | bytes | None: ...  # type: ignore
    def getTraitNames(self) -> tuple[str]: ...
    def getTraitNullMissingAndType(self, traitName: str) -> tuple[bool, bool, int]: ...
    def getTraitType(self, traitName: str) -> int: ...
    def getTransformationMatrix(self) -> list[list[float]]:
        """Gets this clothoid's transformation matrix.

        If the clothoid does not have such a matrix, an identity matrix is returned.
        Only the top three rows of the matrix will be returned, as the bottom row
        is always [ 0 0 0 1 ].

        Returns:
          (list[list[float]]): The transformation matrix of the clothoid.
        """
    def hasMeasures(self) -> bool: ...
    def hasName(self) -> bool: ...
    def hasTransformationMatrix(self) -> bool:
        """
        Returns True if the clothoid has a transformation matrix.

        Returns:
            (bool): True if the clothoid has a transformation matrix.
        """
    def is3D(self) -> bool: ...
    def isClosed(self, threeD: bool) -> bool: ...
    def isCollection(self) -> bool: ...
    def isLinear(self) -> bool: ...
    def measureExists(self, measureName: str) -> bool: ...
    def offset(self, offsetPoint: FMEPoint) -> None: ...
    def removeDuplicates(self, checkZ: bool) -> None: ...
    def removeMeasure(self, measureName: str) -> None: ...
    def removeTraits(self, regexp: str) -> None: ...
    def removeTransformationMatrix(self) -> None:
        """Removes the transformation matrix of the clothoid."""
    def renameMeasure(self, oldMeasureName: str, newMeasureName: str) -> None: ...
    def reverse(self) -> None: ...
    def rotate2D(self, centre: FMEPoint, angle: float) -> None: ...
    def scale(self, xScale: float, yScale: float, zScale: float) -> None: ...
    def setEndCurvature(self, endCurvature: float) -> None:
        """
        Sets the end curvature (in local coordinates) of the clothoid.

        This will recompute the end point.

        Args:
            endCurvature (float): The end curvature (in local coordinates) of the clothoid.
        """
    def setEndPoint(self, point: FMEPoint) -> None: ...
    def setLength(self, localLength: float) -> None:
        """
        Sets the length (in local coordinates) of the clothoid.

        This will recompute the end point.

        Args:
            localLength (float): The length (in local coordinates) of the clothoid.
        """
    def setLocalEndZ(self, localEndZ: float) -> None:
        """
        Sets the elevation (in local coordinates) of the clothoid's end coordinate.

        Args:
            localEndZ (float): The elevation (in local coordinates) of the clothoid's end
                coordinate.
        """
    def setLocalStartCoordXY(self, xCoord: float, yCoord: float) -> None:
        """
        Sets the XY (in local coordinates) of the clothoid's start coordinate.

        This will recompute the end point.

        Args:
            xCoord (float): The X coordinate (in local coordinates) of the clothoid's start coordinate.
            yCoord (float): The Y coordinate (in local coordinates) of the clothoid's start coordinate.
        """
    def setLocalStartCoordXYZ(self, xCoord: float, yCoord: float, zCoord: float) -> None:
        """
        Sets the XYZ (in local coordinates) of the clothoid's start coordinate.

        This will recompute the end point.

        Args:
            xCoord (float): The X coordinate (in local coordinates) of the clothoid's start coordinate.
            yCoord (float): The Y coordinate (in local coordinates) of the clothoid's start coordinate.
            zCoord (float): The Z coordinate (in local coordinates) of the clothoid's start coordinate.
        """
    def setMeasure(self, measureName: str, startPointValue: float, endPointValue: float) -> None:
        """
        Assign the given values to the specified measure. This will create the measure if it doesn't already exist.

        Args:
            measureName (str): The name of the measure.
            startPointValue (float): The value of the measure at the start point.
            endPointValue (float): The value of the measure at the end point.
        """
    def setName(self, name: text_type) -> None: ...
    def setStartCurvature(self, startCurvature: float) -> None:
        """
        Sets the start curvature (in local coordinates) of the clothoid.

        This will recompute the end point.

        Args:
            startCurvature (float): The start curvature (in local coordinates) of the clothoid.
        """
    def setStartDirection(self, startDirection: float) -> None:
        """
        Sets the start angle (in degrees of the local coordinates) of the clothoid.

        This will recompute the end point.

        Args:
            startDirection (float): The start angle (in degrees of the local coordinates) of the clothoid.
        """
    def setStartPoint(self, point: FMEPoint) -> None:
        """
        Changes the existing start point of this curve.

        If there are no points on the curve, this method does nothing.

        Args:
            point (FMEPoint): The start point of the clothoid.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setTrait(
        self,
        traitName: str,
        traitValue: bool | int | float | text_type | bytearray | bytes,
    ) -> None: ...
    def setTraitNullWithType(self, traitName: str, traitType: int) -> None: ...
    def setTransformationMatrix(self, transformationMatrix: list[list[float]]) -> None:
        """
        Sets this clothoid's transformation matrix, replacing the existing matrix if it exists.

        Only three rows are expected in the input array, as a bottom row of
        [ 0 0 0 1 ] is assumed.

        Args:
            transformationMatrix (list[list[float]]): The transformation matrix,
                formatted [[dddd][dddd][dddd]].
        """
    def snip(
        self,
        measureType: int,
        measure3D: bool,
        startLocation: float,
        endLocation: float,
    ) -> None: ...
    def snipByPoints(self, startPoint: FMEPoint, endPoint: FMEPoint) -> None: ...
