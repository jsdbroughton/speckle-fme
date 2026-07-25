from typing import overload
from fmeobjects.geometries.general import FMEGeometry

class FMEPointIterator:
    """FME Point Iterator Class"""

    def __init__(self) -> None:
        """Initialize self. See help(type(self)) for accurate signature."""

class FMEPoint(FMEGeometry):
    """FME Point Class"""

    @overload
    def __init__(self, x: float, y: float, z: float) -> None:
        """Creates a point with the given xyz coordinates.

        Args:
            x (float): The x coordinate of the point.
            y (float): The y coordinate of the point.
            z (float): The z coordinate of the point.


        Returns:
          (FMEPoint): An instance of a Point Geometry object.
        """
    @overload
    def __init__(self, point: FMEPoint) -> None:
        """Creates a point from an existing point.

        Args:
            point (FMEPoint): The Point geometry object to create a copy of.


        Returns:
          (FMEPoint): An instance of a Point Geometry object.
        """
    def equalCoordinate(self, point: FMEPoint, checkZ: bool) -> bool:
        """Returns True if the two points have the identical coordinate.

        Z coordinate values are checked only if 'checkZ' is True.
        Measures are not compared.

        Args:
            point (FMEPoint): The Point geometry object to compare with.
            checkZ (bool): If True, the z coordinate is also checked.


        Returns:
          (bool): True if the coordinates are equal, False otherwise.
        """
    def equalOrientation(self, point: FMEPoint) -> bool:
        """Returns True if the two points have identical rotations.

        Measures are not compared.

        Args:
            point (FMEPoint): The Point geometry object to compare with.


        Returns:
          (bool): True if the two points have identical rotations, False otherwise.
        """
    def equals(self, point: FMEPoint) -> bool:
        """Returns True if the two points have the identical coordinate and measures.

        Args:
            point (FMEPoint): The Point geometry object to compare with.


        Returns:
          (bool): True if the two points have identical coordinate and measures,
          False otherwise.
        """
    def getXYZ(self) -> tuple[float]:
        """Returns the xyz coordinates of the point.

        0.0 is returned for the z value if the point is 2D.

        Returns:
          (tuple[float]): The xyz coordinates of the point.
        """
    def offset(self, offsetPoint: FMEPoint) -> None:
        """Offsets the geometry by the coords specified by 'offsetPoint'.

        Args:
            offsetPoint (FMEPoint): The offset point.

        Raises:
          FMEException: An exception is raised if an error occurs.
        """
    def reset(self, point: FMEPoint) -> None:
        """Set the coordinate and measure values to the values in the given point.

        The point is forced to 3D if necessary. All existing measures are lost.

        Args:
            point (FMEPoint): The point to reset the coordinate and measure values to.
        """
    def rotate2D(self, center: FMEPoint, angle: float) -> None:
        """Rotates the point around the given center.

        Args:
            center (FMEPoint): The center of rotation.
            angle (float): The angle to rotate by. The angle is counter-clockwise
            up from the horizontal, and measured in degrees.

        Raises:
          FMEException: An exception is raised if an error occurs.
        """
    def scale(self, xScale: float, yScale: float, zScale: float) -> None:
        """zScale is ignored if geometry is 2D.

        Args:
            xScale (float): The x scale factor.
            yScale (float): The y scale factor.
            zScale (float): (Optional) The z scale factor.

        Raises:
          FMEException: An exception is raised if an error occurs.
        """
    def setMeasure(self, measureValue: float, measureName: str) -> None:
        """Sets the value of the default measure.

        Or creates the default measure if it doesn't exist. If a 'measureName'
        is supplied, this method sets the value of the named measure, or creates
        the measure if it doesn't exist.

        Args:
            measureValue (float): The measure value.
            measureName (str):  (Optional) The name of the measure whose value
                is to be set, or created.
        """
    def setX(self, newX: float) -> None:
        """Sets the x coordinate of the point.

        Args:
            newX (float): The new x coordinate.
        """
    def setY(self, newY: float) -> None:
        """Sets the y coordinate of the point.

        Args:
            newY (float): The new y coordinate.
        """
    def setZ(self, newZ: float) -> None:
        """Sets the z coordinate of the point.

        Args:
            newZ (float): The new z coordinate.
        """
    def setXYZ(self, newX: float, newY: float, newZ: float) -> None:
        """Sets the xyz coordinates of the point.

        Args:
            newX (float): The new x coordinate.
            newY (float): The new y coordinate.
            newZ (float): (Optional) The new z coordinate.
        """
    def setXYZAsTuple(self, point: tuple[float]) -> None:
        """Set the coordinate value as a tuple.

        The point is forced to 3D if necessary.

        Args:
            point (tuple[float]): The new xyz coordinates.
        """

class FMEMultiPoint(FMEGeometry):
    """FME Multi-Point Class"""

    def __init__(self, multiPoint: FMEMultiPoint) -> None:
        """Creates a Multi-Point geometry from an existing Multi-Point geometry.

        Args:
            multiPoint (FMEMultiPoint): The Multi-Point geometry object to create a copy of.

        Returns:
            (FMEMultiPoint): An instance of a Multi-Point Geometry object.
        """
    def appendPart(self, point: FMEPoint) -> None:
        """This appends the point to the multi point.

        If None is passed in, nothing will be appended. All points in the multi
        point will be forced to have the same dimension. If any 3D points exist,
        all 2D points will be converted to 3D with a default Z value of 0.0.

        Args:
            point (FMEPoint): The point to append.

        Raises:
          FMEException: An exception is raised if an error occurs.
        """
    def appendParts(self, multiPoint: FMEMultiPoint) -> None:
        """This appends the multi point passed in to the multi point.

        If None is passed in, nothing will be appended.

        Args:
            multiPoint (FMEMultiPoint): The multi point to append.

        Raises:
          FMEException: An exception is raised if an error occurs.
        """
    def numParts(self) -> int:
        """Returns the number of parts in the multi point.

        Returns:
          (int): The number of parts in the multi point.
        """
    def offset(self, offsetPoint: FMEPoint) -> None:
        """Offsets the geometry by the coords specified by 'offsetPoint'.

        Args:
            offsetPoint (FMEPoint): The offset point.

        Raises:
          FMEException: An exception is raised if an error occurs.
        """
    def removeLastPart(self) -> FMEPoint | None:
        """This removes and returns the last point of the multi point.

        If there are no points in the multi point, it will return None.

        Returns:
          (FMEPoint or None): The removed point or None if no parts exist.

        Raises:
          FMEException: An exception is raised if an error occurs.
        """
    def scale(self, xscale: float, yscale: float, zscale: float) -> None:
        """Applies a scale factor to the multi point.

        zscale is ignored if geometry is 2D.

        Args:
            xscale (float): The x scale factor.
            yscale (float): The y scale factor.
            zscale (float): The z scale factor.

        Raises:
          FMEException: An exception is raised if an error occurs.
        """
