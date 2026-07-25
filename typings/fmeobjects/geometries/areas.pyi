from typing import overload
from fmeobjects.features import FMEFeature
from fmeobjects.geometries.curves import FMEArc, FMECurve, FMELine, FMEPath
from fmeobjects.geometries.general import FMEGeometry
from fmeobjects.geometries.points import FMEPoint

from six import text_type, string_types

FME_LEFT_HAND_RULE: int
FME_RIGHT_HAND_RULE: int

class FMESimpleAreaIterator:
    """FME Simple Area Iterator Class

    FMESimpleAreaIterator should not be constructed directly. Instead, use the
    iterator semantics of FMEDonut to get an FMESimpleAreaIterator which can be
    used to iterate over its geometries."""

class FMEAreaIterator:
    """FME Area Iterator Class

    FMEAreaIterator should not be constructed directly. Instead, use the
    iterator semantics of FMEMultiArea to get an FMEAreaIterator which can be
    used to iterate over its geometries."""

class FMEArea(FMEGeometry):
    """FME Area Class

    FMEArea is an abstract class. It cannot be created directly.
    """

    def __init__(self) -> None:
        """Initialize self. See help(type(self)) for accurate signature."""
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
    def getMeasureNames(self) -> tuple[str]: ...
    def getName(self) -> text_type | None: ...
    def getTrait(
        self, traitName: str
    ) -> bool | int | float | string_types | bytearray | bytes | None: ...  # type: ignore
    def getTraitNames(self) -> tuple[str]: ...
    def getTraitNullMissingAndType(self, traitName: str) -> tuple[bool, bool, int]: ...
    def getTraitType(self, traitName: str) -> int: ...
    def hasMeasures(self) -> bool: ...
    def is3D(self) -> bool: ...
    def isBoundaryLinear(self) -> bool:
        """Returns True if the outer boundary (and inner boundaries in the case
        of FMEDonut) of this area contains FMELine only.

        Returns:
            (bool): Whether the area's boundaries contain only lines.
        """
    def isCollection(self) -> bool: ...
    def isConvex(self) -> bool:

        """Determines if area is convex.

        The polygon making up the area is convex if all internal angles are less
        than 180 degrees and it's not self-intersecting. Imperfectly planar 3D
        polygons are tolerated.

        Returns:
            (bool): Whether the area is convex.
        """
    def isInPlane(
        self,
        tolerance: float,
        normalVector: tuple[float, float, float],
        valD: float,
        recalculateD: bool,
    ) -> tuple[bool, tuple[float, float, float], float]:
        """Works similarly to isPlanar(), but checks planarity with respect to
        given normal or given plane (if plane equation D is specified - see below).

        If given normal is the zero vector, the normal used to check the planarity
        is computed using Newell's method as in isPlanar(). valD is a reference
        to a value of D in the plane equation AX + BY + CZ = D. It can be used to
        make sure that multiple pieces lie in the same plane. If 'recalculateD'
        is set to False, the passed in value of D will be used in the calculation.
        If 'recalcualteD' is set to True, the passed in value is ignored and is
        instead automatically calculated (and returned in the second position of
        the returned tuple). A useful calling pattern for ensuring co-planarity
        is to get valD computed on the first call to the function setting
        recalculateD to True, and then use this value for future calls with
        recalculateD to False.

        Args:
            tolerance (float): The tolerance to check against.
            normalVector (tuple[float, float, float]): The normal used to check the planarity.
            valD (float): The value D from 'AX + BY + CZ = D'.
            recalculateD (bool): Whether to recalculate 'D' or not.

        Returns:
            (bool, tuple[float, float, float], float): A tuple containing a
                boolean, tuple, and float representing:
                1) Whether or not the area is in plane;
                2) The normal vector returned; and
                3) The value 'D'.
                Note: If recalculateD is False, the tuple returned will only
                contain the boolean and vector tuple (i.e. 'valD' is not returned).
        """
    def isOriented(self, rightOrLeft: int) -> bool:
        """This returns True if the geometry has the specified orientation.

        Args:
          rightOrLeft (int):The orientation to check the FMEArea for.

        Returns:
          (bool): Whether the area has the specified orientation.
        """
    def isPlanar(self, tolerance: float) -> bool:
        """Returns True if this is planar within the given tolerance, and False otherwise.

        The planarity condition is computed by the following algorithm. The
        normal vector <A, B, C> is determined by the vertices of this area using
        Newell's method. For the first point (x', y', z') of this area, we
        compute D' = Ax' + By' + Cz'. Then, this area is planar if and only if
        every subsequent point (x, y, z) of this area gives a D = Ax + By + Cz,
        that is within the tolerance amount of D'. That is, | D - D' | <= tolerance.

        If the specified tolerance is negative, then this method always returns True.

        Args:
            tolerance (float): The tolerance to check against.

        Returns:
            (bool): Whether the area is planar within the tolerance supplied.
        """
    def measureExists(self, measureName: str) -> bool: ...
    def offset(self, offsetPoint: FMEPoint) -> None:
        """Offsets the area by the coords specified by 'offsetPoint'.

        Raises:
            FMEException: An exception is raised if an error occurred
        """
    def orient(self, rightOrLeft: int) -> None:
        """Orients the area to the specified right or left.

        Args:
          rightOrLeft (int): The orientation to set on the FMEArea.
        """
    def removeDuplicates(self, checkZ: bool) -> None:
        """Removes any adjacent duplicate points.

        If 'checkZ' is True, x, y, and z coordinates are checked, otherwise
        only x and y are.

        Args:
          checkZ (bool): Whether to check Z values.
        """
    def removeMeasure(self, measureName: str) -> None: ...
    def removeTraits(self, regexp: str) -> None: ...
    def renameMeasure(self, oldMeasureName: str, newMeasureName: str) -> None: ...
    def reverse(self) -> None:
        """This reverses the order of the area's points."""
    def rotate2D(self, centre: FMEPoint, angle: float) -> None:
        """Rotate the area counterclockwise around the 'center' point by the
        specified 'angle' (in degrees).

        Args:
          centre (FMEPoint): The centre of rotation.
          angle (float): The angle to rotate by.
        """
    def scale(self, xScale: float, yScale: float, zScale: float) -> None:
        """Scales the area by the specified x, y, and z scales.

        Args:
          xScale (float): The x scale factor.
          yScale (float): The y scale factor.
          zScale (float): The z scale factor.

        Raises:
          FMEException: An exception is raised if an error occurred.
        """
    def setName(self, name: text_type) -> None: ...
    def setTrait(
        self,
        traitName: str,
        traitValue: bool | int | float | text_type | bytearray | bytes,
    ) -> None: ...
    def setTraitNullWithType(self, traitName: str, traitType: int) -> None: ...

class FMEMultiArea(FMEGeometry):
    """FME MultiArea class."""

    @overload
    def __init__(self) -> None:
        """Default FMEMultiArea constructor.

        Returns:
          (FMEMultiArea): An instance of a MultiArea geometry object.
        """
    @overload
    def __init__(self, multiArea: FMEMultiArea) -> None:
        """Create a copy of the passed in Multi-Area geometry object..

        Args:
          multiArea (FMEMultiArea): An instance of a MultiArea geometry object.

        Returns:
          (FMEMultiArea): An instance of a MultiArea geometry object.
        """
    def appendPart(self, area: FMEArea) -> None:
        """This appends the area to the MultiArea.

        If None is passed in, nothing will be appended. All areas in the MultiArea
        will be forced to have the same dimension. If any 3D areas exist, all 2D
        areas will be converted to 3D with a default Z value of 0.0.

        Args:
          area (FMEArea): The area to append to the MultiArea.

        Raise:
          FMEException: An exception is raised if an error occurred.
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
    def getMeasureNames(self) -> tuple[str]: ...
    def getName(self) -> text_type | None: ...
    def getPartAt(self, index: int) -> FMEArea | None:
        """Returns the area at the specified index.

        Args:
          index (int): The index of the area to return.

        Returns:
          (FMEArea): The area at the given index. Note: This method returns a
              terminal area type of the FMEArea; i.e. one of the leaf classes in
              the FMEArea inheritance graph. For example, a FMEPolygon is returned
              if the area truly is a polygon.
        """
    def getTrait(
        self, traitName: str
    ) -> bool | int | float | string_types | bytearray | bytes | None: ...  # type: ignore
    def getTraitNames(self) -> tuple[str]: ...
    def getTraitNullMissingAndType(self, traitName: str) -> tuple[bool, bool, int]: ...
    def getTraitType(self, traitName: str) -> int: ...
    def hasMeasures(self) -> bool: ...
    def hasName(self) -> bool: ...
    def is3D(self) -> bool: ...
    def isCollection(self) -> bool: ...
    def isInPlane(
        self,
        tolerance: float,
        normalVector: tuple[float, float, float],
        valD: float,
        recalculateD: bool,
    ) -> tuple[bool, tuple[float, float, float], float]:
        """Works similarly to isPlanar(), but checks planarity with respect to
        given normal or given plane (if plane equation D is specified - see below).

        If given normal is the zero vector, the normal used to check the planarity
        is computed using Newell's method as in isPlanar(). valD is a reference
        to a value of D in the plane equation AX + BY + CZ = D. It can be used to
        make sure that multiple pieces lie in the same plane. If 'recalculateD'
        is set to False, the passed in value of D will be used in the calculation.
        If 'recalcualteD' is set to True, the passed in value is ignored and is
        instead automatically calculated (and returned in the second position of
        the returned tuple). A useful calling pattern for ensuring co-planarity
        is to get valD computed on the first call to the function setting
        recalculateD to True, and then use this value for future calls with
        recalculateD to False.

        Args:
          tolerance (float): The tolerance to check against.
          normalVector (tuple[float]): The normal used to check the planarity.
          valD (float): The value of D in the plane equation AX + BY + CZ = D.
          recalculateD (bool): Whether to recalculate D.

        Returns:
          (bool, tuple[float], float): A tuple containing the following:
            - (bool): True if the area is in plane.
            - (tuple[float, float, float]): The normal vector of the plane.
            - (float): The value of D in the plane equation AX + BY + CZ = D.
        """
    def isPlanar(self, tolerance: float) -> bool:
        """Returns True if this is planar within the given tolerance, and False otherwise.

        The planarity condition is computed by the following algorithm. The normal
        vector <A, B, C> is determined by the vertices of this area using Newell's
        method. For the first point (x', y', z') of this area, we
        compute D' = Ax' + By' + Cz'. Then, this area is planar if and only if
        every subsequent point (x, y, z) of this area gives a D = Ax + By + Cz,
        that is within the tolerance amount of D'. That is, | D - D' | <= tolerance.

        Args:
          tolerance (float): The tolerance to check against.

        Returns:
          (bool): Whether the multiarea is planar within the tolerance supplied.
        """
    def measureExists(self, measureName: str) -> bool: ...
    def numParts(self) -> int:
        """This returns the number of areas that make up this MultiArea.

        Returns:
          (int): The number of parts in this MultiArea.
        """
    def offset(self, offsetPoint: FMEPoint) -> None:
        """This offsets the MultiArea by the specified point.

        Args:
          offsetPoint (FMEPoint): The point to offset the MultiArea by.

        Raise:
          FMEException: An exception is raised if an error occurred.
        """
    def removeLastPart(self) -> FMEArea | None:
        """This removes and returns the last area of the MultiArea.

        If there are no areas in the MultiArea, it will return None.

        Returns:
          (FMEArea): The last area of the MultiArea. Note: This method returns a
          terminal area type of the FMEArea; i.e. one of the leaf classes in the
          FMEArea inheritance graph. For example, a FMEPolygon is returned if the
          area truly is a polygon.

        Raise:
          FMEException: An exception is raised if an error occurred.
        """
    def removeMeasure(self, measureName: str) -> None: ...
    def removeTraits(self, regexp: str) -> None: ...
    def renameMeasure(self, oldMeasureName: str, newMeasureName: str) -> None: ...
    def rotate2D(self, center: FMEPoint, angle: float) -> None:
        """Rotates the MultiArea about the specified point by the specified angle.

        Args:
          center (FMEPoint): The point to rotate about.
          angle (float): The angle to rotate by.

        Raise:
          FMEException: An exception is raised if an error occurred.
        """
    def scale(self, xScale: float, yScale: float, zScale: float) -> None:
        """Scales the MultiArea by the specified factors.

        Args:
          xScale (float): The x-scale factor.
          yScale (float): The y-scale factor.
          zScale (float): The z-scale factor.

        Raise:
          FMEException: An exception is raised if an error occurred.
        """
    def setName(self, name: text_type) -> None: ...
    def setTrait(
        self,
        traitName: str,
        traitValue: bool | int | float | text_type | bytearray | bytes,
    ) -> None: ...
    def setTraitNullWithType(self, traitName: str, traitType: int) -> None: ...

class FMEDonut(FMEArea):
    """FME Donut Class"""

    @overload
    def __init__(self, outerBoundary: FMESimpleArea) -> None:
        """Creates a new Donut geometry object.

        The simple area passed in is used to define the outer boundary of the donut.

        Args:
          outerBoundary (FMESimpleArea): The simple area defining the outer boundary of the donut.

        Returns:
          (FMEDonut): The newly created Donut geometry object.
        """
    @overload
    def __init__(self, outerBoundary: FMECurve) -> None:
        """Creates a new Donut geometry object.

        The curve passed in is used to define the outer boundary of the donut.

        Args:
          outerBoundary (FMECurve): The outer boundary as a curve.

        Returns:
          (FMEDonut): The newly created Donut geometry object.
        """
    @overload
    def __init__(self, donut: FMEDonut) -> None:
        """Create a copy of the passed in Donut geometry object.

        Args:
          donut (FMEDonut): The Donut geometry object to create a copy of.

        Returns:
          (FMEDonut): The newly created Donut geometry object.
        """
    def addInnerBoundaryCurve(self, innerBoundary: FMECurve) -> None:
        """If the inner boundary being added has a different dimension than the
        other boundaries, anything 2D will be forced to 3D.

        Note that the default Z value is 0.0 when forcing 2D geometry to 3D. If
        the curve is not closed, the closure will be assumed as a straight line
        from the start point to the end point. If the 'innerBoundary' being added
        is None, nothing will be done.

        Args:
          innerBoundary (FMECurve): The curve defining the inner boundary.

        Raise:
          FMEException: An exception is raised if an error occurred.
        """
    def addInnerBoundarySimpleArea(self, innerBoundary: FMESimpleArea) -> None:
        """Adds a simple area as an inner boundary.

        If the inner boundary being added has a different dimension than the other
        boundaries, anything 2D will be forced to 3D. Note that the default Z value
        is 0.0 when forcing 2D geometry to 3D. If the 'innerBoundary' being added
        is None, nothing will be done.

        Args:
          innerBoundary (FMESimpleArea): The simple area defining the inner boundary.

        Raise:
          FMEException: An exception is raised if an error occurred.
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
    def getInnerBoundaryAsCurveAt(self, index: int) -> FMEPath | FMEArc | FMELine | None:
        """Retrieves the inner boundary at the specified index.

        If the index is out of bounds, it will return None.

        Args:
          index (int): The index of the inner boundary to retrieve.

        Returns:
          (FMEPath or FMEArc or FMELine or None): The inner boundary as a FMECurve,
          or None if the specified index is greater than the number of inner
          boundaries. Returns the terminal geometry of the FMECurve, either a
          FMEPath, FMEArc or FMELine.

        Raises:
          FMEException: An exception is raised if an error occurred.
        """
    def getInnerBoundarAsSimpleAreaAt(self, index: int) -> FMEPolygon | FMEEllipse | None:
        """Retrieves the inner boundary at 'index' as a FMESimpleArea.

        Args:
          index (int): The index of the inner boundary to retrieve.

        Returns:
          (FMESimpleArea or None):The inner boundary as a FMESimpleArea, or None
          if the specified index is greater than the number of inner boundaries.
          Returns the terminal geometry of the FMESimpleArea, either a FMEPolygon
          or a FMEEllipse.

        Raises:
          FMEException: An exception is raised if an error occurred.
        """
    def getMeasureNames(self) -> tuple[str]: ...
    def getName(self) -> text_type | None: ...
    def getOuterBoundaryAsCurve(self) -> FMEPath | FMEArc | FMELine:
        """Retrieves the outer boundary as a FMECurve.

        Returns:
          (FMEPath, FMEArc or FMELine): The inner boundary as a FMECurve. Returns
              the terminal geometry of the FMECurve, either a FMEPath, FMEArc or
              FMELine.

        Raises:
          FMEException: An exception is raised if an error occurred.
        """
    def getOuterBoundaryAsSimpleArea(self) -> FMEPolygon | FMEEllipse:
        """Retrieves the outer boundary as a FMESimpleArea.

        Returns:
          (FMEPolygon or FMEEllipse): The outer boundary as a FMESimpleArea.
              Returns the terminal geometry of the FMESimpleArea, either a
              FMEPolygon or a FMEEllipse.

        Raises:
          FMEException: An exception is raised if an error occurred.
        """
    def getTrait(
        self, traitName: str
    ) -> bool | int | float | string_types | bytearray | bytes | None: ...  # type: ignore
    def getTraitNames(self) -> tuple[str]: ...
    def getTraitNullMissingAndType(self, traitName: str) -> tuple[bool, bool, int]: ...
    def getTraitType(self, traitName: str) -> int: ...
    def hasMeasures(self) -> bool: ...
    def hasName(self) -> bool: ...
    def is3D(self) -> bool: ...
    def isBoundaryLinear(self) -> bool: ...
    def isCollection(self) -> bool: ...
    def isConvex(self) -> bool: ...
    def isInPlane(
        self,
        tolerance: float,
        normalVector: tuple[float, float, float],
        valD: float,
        recalculateD: bool,
    ) -> tuple[bool, tuple[float, float, float], float]: ...
    def isOriented(self, rightOrLeft: int) -> bool: ...
    def isPlanar(self, tolerance: float) -> bool: ...
    def measureExists(self, measureName: str) -> bool: ...
    def numInnerBoundaries(self) -> int:
        """Returns the number of inner boundaries.

        Returns:
          (int): The number of inner boundaries.

        Raises:
          FMEException: An exception is raised if an error occurred.
        """
    def offset(self, offsetPoint: FMEPoint) -> None: ...
    def orient(self, rightOrLeft: int) -> None: ...
    def removeDuplicates(self, checkZ: bool) -> None: ...
    def removeLastInnerBoundaryAsCurve(self) -> FMEPath | FMEArc | FMELine:
        """Removes and returns the last inner boundary as a FMECurve.

        Returns:
          (FMEPath, FMEArc or FMELine): The last inner boundary as a FMESimpleArea.
              Returns the terminal geometry of the FMESimpleArea, either a
              FMEEllipse, or FMEPolygon.

        Raises:
          FMEException: An exception is raised if an error occurred.
        """
    def removeMeasure(self, measureName: str) -> None: ...
    def removeTraits(self, regexp: str) -> None: ...
    def renameMeasure(self, oldMeasureName: str, newMeasureName: str) -> None: ...
    def reverse(self) -> None: ...
    def rotate2D(self, centre: FMEPoint, angle: float) -> None: ...
    def scale(self, xScale: float, yScale: float, zScale: float) -> None: ...
    def setName(self, name: text_type) -> None: ...
    def setOuterBoundaryCurve(self, outerBoundary: FMECurve) -> None:
        """Sets the outer boundary as a FMECurve.

        If the curve is not closed, the closure will be assumed as a straight line
        from the start point to the end point. If the new outer boundary has a
        different dimension than the inner boundaries, everything will be forced
        to 3D. Note that the default Z value is 0.0 when forcing 2D geometry to
        3D. This will return an error if the outerBoundary passed in is invalid
        or None.

        Args:
          outerBoundary (FMECurve): The curve to set as the outer boundary.

        Raises:
          FMEException: An exception is raised if an error occurred.
        """
    def setOuterBoundarySimpleArea(self, outerBoundary: FMESimpleArea) -> None:
        """Sets the outer boundary as a FMESimpleArea.

        Sets the outer boundary of the donut. If the new outer boundary has a
        different dimension than the inner boundaries, everything will be forced
        to 3D. Note that the default Z value is 0.0 when forcing 2D geometry to 3D.

        Args:
          outerBoundary (FMESimpleArea): The simple area to set as the outer
              boundary.

        Raises:
          FMEException: An exception is raised if an error occurred.
        """
    def setTrait(
        self,
        traitName: str,
        traitValue: bool | int | float | text_type | bytearray | bytes,
    ) -> None: ...
    def setTraitNullWithType(self, traitName: str, traitType: int) -> None: ...

class FMESimpleArea(FMEArea):
    """FME Simple Area Clas

    FMESimpleArea is an abstract class. It cannot be created directly."""

    def __init__(self) -> None:
        """Initialize self. See help(type(self)) for accurate signature."""
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
    def getBoundaryAsCurve(self) -> FMEPath | FMEArc | FMELine:
        """Returns the curve that defines the boundary of the area.

        Returns:
          (FMEPath, FMEArc or FMELine): Returns the curve that defines the
              boundary of the area.
        """
    def getMeasureNames(self) -> tuple[str]: ...
    def getName(self) -> text_type | None: ...
    def getTrait(
        self, traitName: str
    ) -> bool | int | float | string_types | bytearray | bytes | None: ...  # type: ignore
    def getTraitNames(self) -> tuple[str]: ...
    def getTraitNullMissingAndType(self, traitName: str) -> tuple[bool, bool, int]: ...
    def getTraitType(self, traitName: str) -> int: ...
    def hasMeasures(self) -> bool: ...
    def hasName(self) -> bool: ...
    def is3D(self) -> bool: ...
    def isBoundaryLinear(self) -> bool: ...
    def isCollection(self) -> bool: ...
    def isConvex(self) -> bool: ...
    def isInPlane(
        self,
        tolerance: float,
        normalVector: tuple[float, float, float],
        valD: float,
        recalculateD: bool,
    ) -> tuple[bool, tuple[float, float, float], float]: ...
    def isOriented(self, rightOrLeft: int) -> bool: ...
    def isPlanar(self, tolerance: float) -> bool: ...
    def measureExists(self, measureName: str) -> bool: ...
    def offset(self, offsetPoint: FMEPoint) -> None: ...
    def orient(self, rightOrLeft: int) -> None: ...
    def removeDuplicates(self, checkZ: bool) -> None: ...
    def removeMeasure(self, measureName: str) -> None: ...
    def removeTraits(self, regexp: str) -> None: ...
    def renameMeasure(self, oldMeasureName: str, newMeasureName: str) -> None: ...
    def reverse(self) -> None: ...
    def rotate2D(self, centre: FMEPoint, angle: float) -> None: ...
    def scale(self, xScale: float, yScale: float, zScale: float) -> None: ...
    def setName(self, name: text_type) -> None: ...
    def setTrait(
        self,
        traitName: str,
        traitValue: bool | int | float | text_type | bytearray | bytes,
    ) -> None: ...
    def setTraitNullWithType(self, traitName: str, traitType: int) -> None: ...

class FMEEllipse(FMESimpleArea):
    """FME Ellipse Class"""

    @overload
    def __init__(self, boundary: FMEArc) -> None:
        """This routine creates a new Ellipse geometry object from the passed in arc boundary.

        If this arc is not closed, the closure will be assumed as a complete
        continuation of the arc where the end point is 360 degrees from the the
        start point.

        Args:
          boundary (FMEArc): The boundary as an arc.

        Returns:
          (FMEEllipse): An instance of the FMEEllipse geometry object.

        Raises:
          FMEException: An exception is raised if an error occurred.
        """
    @overload
    def __init__(
        self,
        centerPoint: FMEPoint,
        primaryRadius: float,
        secondaryRadius: float,
        rotation: float,
        orientation: int,
    ) -> None:
        """This routine creates a new Ellipse geometry object using the passed in values.

        Args:
          centerPoint (FMEPoint): The center point of the ellipse.
          primaryRadius (float): The primary radius of the ellipse.
          secondaryRadius (float): The secondary radius of the ellipse.
          rotation (float): The rotation of the ellipse.
          orientation (int): The orientation rule. Must be either
              FME_RIGHT_HAND_RULE or FME_LEFT_HAND_RULE.

        Returns:
          (FMEEllipse): An instance of the FMEEllipse geometry object.

        Raises:
          FMEException: An exception is raised if an error occurred.
        """
    @overload
    def __init__(self, ellipse: FMEEllipse) -> None:
        """This routine creates a new Ellipse geometry object from the passed in ellipse.

        Args:
          ellipse (FMEEllipse): The ellipse to copy.

        Returns:
          (FMEEllipse): An instance of the FMEEllipse geometry object.
        """
    @overload
    def __init__(self) -> None:
        """This routine creates a new Ellipse geometry object.

        Returns:
          (FMEEllipse): An instance of the FMEEllipse geometry object.
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
    def getAsLine(self) -> FMELine | None:
        """Returns the ellipse as a line.

        Returns:
          (FMELine): The line representing the ellipse or None if the ellipse
              cannot be returned as a line.
        """
    def getBoundaryAsArc(self) -> FMEArc | None:
        """Returns the ellipse as an arc.

        Returns:
          (FMEArc): The arc representing the ellipse or None if the ellipse
              cannot be returned as an arc.
        """
    def getBoundaryAsCurve(self) -> FMEPath | FMEArc | FMELine:
        """Returns the ellipse as a curve.

        Returns:
          (FMEPath or FMEArc or FMELine): The curve representing the ellipse.
        """
    def getMeasureNames(self) -> tuple[str]: ...
    def getName(self) -> text_type | None: ...
    def getPrimaryRadius(self) -> float:
        """This gets the primary radius of the ellipse.

        All angles are CCW up from the horizontal and are measured in degrees.

        Returns:
          (float): The primary radius of the ellipse.
        """
    def getRotation(self) -> float:
        """This gets the rotation of the ellipse.

        All angles are CCW up from the horizontal and are measured in degrees.

        Returns:
          (float): The rotation of the ellipse.
        """
    def getSecondaryRadius(self) -> float:
        """This gets the secondary radius of the ellipse.

        All angles are CCW up from the horizontal and are measured in degrees.

        Returns:
          (float): The secondary radius of the ellipse.
        """
    def getTrait(
        self, traitName: str
    ) -> bool | int | float | string_types | bytearray | bytes | None: ...  # type: ignore
    def getTraitNames(self) -> tuple[str]: ...
    def getTraitNullMissingAndType(self, traitName: str) -> tuple[bool, bool, int]: ...
    def getTraitType(self, traitName: str) -> int: ...
    def hasMeasures(self) -> bool: ...
    def hasName(self) -> bool: ...
    def is3D(self) -> bool: ...
    def isBoundaryLinear(self) -> bool: ...
    def isCollection(self) -> bool: ...
    def isConvex(self) -> bool: ...
    def isInPlane(
        self,
        tolerance: float,
        normalVector: tuple[float, float, float],
        valD: float,
        recalculateD: bool,
    ) -> tuple[bool, tuple[float, float, float], float]: ...
    def isOriented(self, rightOrLeft: int) -> bool: ...
    def isPlanar(self, tolerance: float) -> bool: ...
    def measureExists(self, measureName: str) -> bool: ...
    def offset(self, offsetPoint: FMEPoint) -> None: ...
    def orient(self, rightOrLeft: int) -> None: ...
    def removeDuplicates(self, checkZ: bool) -> None: ...
    def removeMeasure(self, measureName: str) -> None: ...
    def removeTraits(self, regexp: str) -> None: ...
    def renameMeasure(self, oldMeasureName: str, newMeasureName: str) -> None: ...
    def reverse(self) -> None: ...
    def rotate2D(self, centre: FMEPoint, angle: float) -> None: ...
    def scale(self, xScale: float, yScale: float, zScale: float) -> None: ...
    def setBoundary(self, boundary: FMEArc) -> None:
        """This sets the curve that defines the boundary of the ellipse.

        If this arc is not closed, the closure will be assumed as a complete
        continuation of the arc where the end point is 360 degrees from the the
        start point. If an error occurs, an exception is thrown.

        Args:
          boundary (FMEArc): The new boundary of the ellipse.

        Raises:
          FMEException: An exception is raised if an error occurred.
        """
    def setName(self, name: text_type) -> None: ...
    def setPrimaryRadius(self, radius: float) -> None:
        """This sets the primary radius of the ellipse.

        All angles are CCW up from the horizontal and are measured in degrees.

        Args:
          radius (float): The new primary radius of the ellipse.
        """
    def setSecondaryRadius(self, radius: float) -> None:
        """This sets the secondary radius of the ellipse.

        All angles are CCW up from the horizontal and are measured in degrees.

        Args:
          radius (float): The new secondary radius of the ellipse.
        """
    def setTrait(
        self,
        traitName: str,
        traitValue: bool | int | float | text_type | bytearray | bytes,
    ) -> None: ...
    def setTraitNullWithType(self, traitName: str, traitType: int) -> None: ...

class FMEPolygon(FMESimpleArea):
    """FME Polygon Class"""

    @overload
    def __init__(self, boundary: FMECurve) -> None:
        """Create an instance of a Polygon geometry object.

        The curve passed in, 'boundary', is used to define the boundary of the polygon.

        Args:
          boundary (FMECurve): The boundary as a curve.

        Returns:
          (FMEPolygon): The new polygon.
        """
    @overload
    def __init__(self, polygon: FMEPolygon) -> None:
        """Create a copy of the passed in Polygon geometry object.

        Args:
          polygon (FMEPolygon): The polygon.

        Returns:
          (FMEPolygon): The new polygon.
        """
    @overload
    def __init__(self) -> None:
        """Initialize self. See help(type(self)) for accurate signature."""
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
    def getBoundaryAsCurve(self) -> FMEPath | FMEArc | FMELine: ...
    def getMeasureNames(self) -> tuple[str]: ...
    def getName(self) -> text_type | None: ...
    def getTrait(
        self, traitName: str
    ) -> bool | int | float | string_types | bytearray | bytes | None: ...  # type: ignore
    def getTraitNames(self) -> tuple[str]: ...
    def getTraitNullMissingAndType(self, traitName: str) -> tuple[bool, bool, int]: ...
    def getTraitType(self, traitName: str) -> int: ...
    def hasMeasures(self) -> bool: ...
    def hasName(self) -> bool: ...
    def is3D(self) -> bool: ...
    def isBoundaryLinear(self) -> bool: ...
    def isCollection(self) -> bool: ...
    def isConvex(self) -> bool: ...
    def isInPlane(
        self,
        tolerance: float,
        normalVector: tuple[float, float, float],
        valD: float,
        recalculateD: bool,
    ) -> tuple[bool, tuple[float, float, float], float]: ...
    def isOriented(self, rightOrLeft: int) -> bool: ...
    def isPlanar(self, tolerance: float) -> bool: ...
    def measureExists(self, measureName: str) -> bool: ...
    def offset(self, offsetPoint: FMEPoint) -> None: ...
    def orient(self, rightOrLeft: int) -> None: ...
    def removeDuplicates(self, checkZ: bool) -> None: ...
    def removeMeasure(self, measureName: str) -> None: ...
    def removeTraits(self, regexp: str) -> None: ...
    def renameMeasure(self, oldMeasureName: str, newMeasureName: str) -> None: ...
    def reverse(self) -> None: ...
    def rotate2D(self, centre: FMEPoint, angle: float) -> None: ...
    def scale(self, xScale: float, yScale: float, zScale: float) -> None: ...
    def setBoundary(self, boundary: FMECurve) -> None: ...
    def setName(self, name: text_type) -> None: ...
    def setTrait(
        self,
        traitName: str,
        traitValue: bool | int | float | text_type | bytearray | bytes,
    ) -> None: ...
    def setTraitNullWithType(self, traitName: str, traitType: int) -> None: ...
