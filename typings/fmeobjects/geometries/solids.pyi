# CSG Solid Operations
from typing import overload
from fmeobjects.features import FMEFeature
from fmeobjects.geometries.general import FMEGeometry
from fmeobjects.geometries.curves import FMEMultiCurve
from fmeobjects.geometries.geometry_mixins import (
    AppearanceMixin,
    OrientMixin,
    TransformMixin,
)
from fmeobjects.geometries.points import FMEPoint
from fmeobjects.geometries.surfaces import FMEFace, FMESurface

from six import text_type, string_types

FME_CSG_UNION: int
FME_CSG_DIFFERENCE: int
FME_CSG_INTERSECTION: int
FME_CSG_NONE: int

class FMESolidIterator:
    """FME Solid Iterator Class

    FMESolidIterator should not be constructed directly. Instead, use the iterator
    semantics of FMEMultiSolid to get an FMESolidIterator which can be used to
    iterate over its geometries."""

    def __init__(self) -> None:
        """Initialize self. See help(type(self)) for accurate signature."""

class FMESimpleSolidIterator:
    """FME Simple Solid Iterator Class

    FMESimpleSolidIterator should not be constructed directly. Instead, use the
    iterator semantics of FMEMCompositeSolid to get an FMESimpleSolidIterator which can be
    used to iterate over its geometries."""

    def __init__(self) -> None:
        """Initialize self. See help(type(self)) for accurate signature."""

class FMECSGSolidIterator:
    """FME CSG Solid Iterator Class

    FMECSGSolidIterator should not be constructed directly. Instead, use the iterator
    semantics of FMECSGSolid to get an FMECSGSolidIterator which can be used to
    iterate over its geometries."""

    def __init__(self) -> None:
        """Initialize self. See help(type(self)) for accurate signature."""
    def getOperator(self) -> int:
        """This method returns a valid CSG Boolean Operator if isLeaf() returns True.

        This method returns FME_CSG_NONE if isLeaf() returns False.

        Returns:
            int: Returns a valid CSG Boolean Operator.
        """
    def getPartInLocalCoordinates(self) -> FMESolid | None:
        """This method returns the same solid as next() but if the CSG solid has
        a transformation matrix, the matrix is NOT applied to the leaf solid when
        returned.

        This method must be called after next().

        Returns:
            FMESolid: Returns the solid at the current node in local coordinates.
        """
    def isBranch(self) -> bool:
        """This method returns True if the iterator reaches a branch node in the
        CSG solid tree structure and if next() was called a Stop iteration
        exception would be thrown. This method returns False if the iterator is
        at a leaf node.

        Returns:
            bool: Returns True if the iterator reaches a branch node and false otherwise.
        """
    def isLeftLeaf(self) -> bool:
        """This method returns True if the iterator is at a left leaf node in the
        CSG solid tree structure. This method returns False if the iterator is
        at a branch node.

        Returns:
            bool: Returns True if the iterator is at a left leaf node and false otherwise.
        """
    def isRightLeaf(self) -> bool:
        """This method returns True if the iterator is at a right leaf node in the
        CSG solid tree structure. This method returns False if the iterator is
        at a branch node.

        Returns:
            bool: Returns True if the iterator is at a right leaf node and false otherwise.
        """

class FMESolid(FMEGeometry):
    """FME Solid Class

    FMESolid is an abstract class. It cannot be created directly."""

    def __init__(self) -> None:
        """Initialize self. See help(type(self)) for accurate signature."""

class FMEMultiSolid(FMEGeometry, AppearanceMixin, TransformMixin):
    """FME Multi Solid Class"""

    @overload
    def __init__(self) -> None:
        """Default FMEMultiSolid constructor.

        Returns:
            FMEMultiSolid: An instance of MultiSolid geometry object.
        """
    @overload
    def __init__(self, multiSolid: FMEMultiSolid) -> None:
        """Create a copy of the given multiSolid.

        Returns:
            FMEMultiSolid: An instance of MultiSolid geometry object.
        """
    def appendPart(self, solid: FMESolid) -> None:
        """This appends the MultiSolid passed in to the MultiSolid. If None is
        passed in, nothing will be appended.

        Args:
            solid (FMESolid): A solid to append to the multiSolid.

        Raises:
            FMException: An exception is raised if an error occurs.
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
    def getAppearanceReference(self, front: bool) -> int: ...
    def getArea(self) -> float: ...
    def getAsWireFrame(self) -> FMEMultiCurve | None:
        """Returns the wireframe of the MultiSolid as a FMEMultiCurve.

        None is returned if a wireframe cannot be generated.

        Returns:
            FMEMultiCurve: Returns the solid as a wireframe.
        """
    def getMeasureNames(self) -> tuple[str]: ...
    def getName(self) -> text_type | None: ...
    def getPartAt(self, index: int) -> FMESolid | None:
        """Returns the solid at the given index.

        Args:
            index (int): The index of the solid to return.

        Returns:
            FMESolid: The solid at the given index. Note: This method returns a
                terminal solid type of the FMESolid; i.e. one of the leaf classes
                in the FMESolid inheritance graph. For example, a FMELine is
                returned if the solid truly is a line.

        Raises:
            FMException: An exception is raised if an error occurs.
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
    def measureExists(self, measureName: str) -> bool: ...
    def numParts(self) -> int:
        """Returns the number of parts in the MultiSolid.

        Returns:
            int: The number of parts in the MultiSolid.
        """
    def offset(self, offsetPoint: FMEPoint) -> None: ...
    def removeLastPart(self) -> FMESolid | None:
        """This removes and returns the last solid of the MultiSolid.

        If there are no solids in the MultiSolid, it will return None.

        Returns:
            FMESolid: The last solid of the MultiSolid. Note: This method returns
                a terminal solid type of the FMESolid; i.e. one of the leaf classes
                in the FMESolid inheritance graph. For example, a FMELine is
                returned if the solid truly is a line.

        Raises:
            FMException: An exception is raised if an error occurs.
        """
    def removeMeasure(self, measureName: str) -> None: ...
    def removeTraits(self, regexp: str) -> None: ...
    def renameMeasure(self, oldMeasureName: str, newMeasureName: str) -> None: ...
    def resolvePartDefaults(self) -> None:
        """Recursively resolves parts with default appearances by replacing these
        defaults with the inherited appearance references stored by the parent
        geometry, if such a value exists. The nearest non-default ancestor value
        will be used to set the default appearances on the part.
        """
    def rotate2D(self, center: FMEPoint, angle: float) -> None: ...
    def scale(self, xScale: float, yScale: float, zScale: float) -> None: ...
    def setAppearanceReference(self, appearanceRef: int, front: bool) -> None: ...
    def setName(self, name: text_type) -> None: ...
    def setTrait(
        self,
        traitName: str,
        traitValue: bool | int | float | text_type | bytearray | bytes,
    ) -> None: ...
    def setTraitNullWithType(self, traitName: str, traitType: int) -> None: ...

class FMESimpleSolid(FMESolid):
    """FME Simple Solid Class

    FMESimpleSolid is an abstract class. It cannot be created directly."""

    def __init__(self) -> None:
        """Initialize self. See help(type(self)) for accurate signature."""

class FMECompositeSolid(FMESolid, AppearanceMixin, TransformMixin, OrientMixin):
    """FME Composite Solid Class"""

    @overload
    def __init__(self) -> None:
        """Default FMECompositeSolid constructor.

        Returns:
            FMEBox: An instance of a Composite Solid geometry object.
        """
    @overload
    def __init__(self, compositeSolid: FMECompositeSolid) -> None:
        """Create a copy of the passed in Composite Solid geometry object.

        Args:
            compositeSolid (FMECompositeSolid): The Composite Solid geometry
                object to create a copy of.

        Returns:
            FMECompositeSolid: Returns:	An instance of a Composite Solid geometry object.
        """
    def appendPart(self, solid: FMESimpleSolid) -> None:
        """Appends a simple solid to the end of this composite solid.

        A None input is ignored.

        Args:
            solid (FMESolid):  The simple solid to be appended.

        Raises:
            FMException: An exception is raised if an error occurs.
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
    def getAppearanceReference(self, front: bool) -> int: ...
    def getArea(self) -> float: ...
    def getAsWireFrame(self) -> FMEMultiCurve | None:
        """Returns the wireframe of the solid as a FMEMultiCurve.

        None is returned if a wireframe cannot be generated.

        Returns:
            FMEMultiCurve: The wireframe representation of this solid.
        """
    def getMeasureNames(self) -> tuple[str]: ...
    def getName(self) -> text_type | None: ...
    def getPartAt(self, index: int) -> FMESimpleSolid | None:
        """Returns the solid at the index specified, or returns None if the index is out of range.

        Returns:
            FMESimpleSolid: The solid at the specified index.

        Raises:
            FMException: An exception is raised if an error occurs.
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
    def isOriented(self, orientation: int) -> bool: ...
    def measureExists(self, measureName: str) -> bool: ...
    def numParts(self) -> int:
        """Returns the number of simple solids that are contained in this composite.

        Returns:
            int: The number of parts in the solid.

        Raises:
            FMException: An exception is raised if an error occurs.
        """
    def orient(self, orientation: int) -> None: ...
    def removeEndPart(self) -> FMESimpleSolid | None:
        """Removes the last simple solid of this composite solid.

        If there are no solids in this composite, this method will return None.

        Returns:
            FMESimpleSolid: The last part of the solid.

        Raises:
            FMException: An exception is raised if an error occurs.
        """
    def removeMeasure(self, measureName: str) -> None: ...
    def removeTraits(self, regexp: str) -> None: ...
    def renameMeasure(self, oldMeasureName: str, newMeasureName: str) -> None: ...
    def reorient(self) -> None: ...
    def resolvePartDefaults(self) -> None:
        """Recursively resolves parts with default appearances by replacing these
        defaults with the inherited appearance references stored by the parent
        geometry, if such a value exists. The nearest non-default ancestor value
        will be used to set the default appearences on the part."""
    def reverse(self) -> None: ...
    def rotate2D(self, center: tuple[float], angle: float) -> None: ...
    def scale(self, xScale: float, yScale: float, zScale: float) -> None: ...
    def setAppearanceReference(self, appearanceRef: int, front: bool) -> None: ...
    def setName(self, name: text_type) -> None: ...
    def setTrait(
        self,
        traitName: str,
        traitValue: bool | int | float | text_type | bytearray | bytes,
    ) -> None: ...
    def setTraitNullWithType(self, traitName: str, traitType: int) -> None: ...

class FMEBox(FMESimpleSolid, AppearanceMixin, TransformMixin, OrientMixin):
    """FME Box Class"""

    @overload
    def __init__(self) -> None:
        """Default FMEBox constructor.

        Returns:
            FMEBox: An instance of a Box =geometry object.
        """
    @overload
    def __init__(self, coords: tuple[float, float, float, float, float, float]) -> None:
        """Creates a box consisting of the tuple of doubles passed in.

        Args:
            coords: (tuple[double]): The tuple of doubles to set to the box.
                The coords are represented as a tuple of
                (firstX, firstY, firstZ, secondX, secondY, secondZ).

        Returns:
            FMEBox: An instance of a Box Geometry object.
        """
    @overload
    def __init__(
        self,
        coords: tuple[float, float, float, float, float, float],
        matrix: list[list[float]],
    ) -> None:
        """Creates a box consisting of the tuple of doubles passed in.

        With the specified transformation matrix.

        Args:
            coords: (tuple[double]): The tuple of doubles to set to the box.
                The coords are represented as a tuple of
                (firstX, firstY, firstZ, secondX, secondY, secondZ).
            matrix: (tuple[double]): transformation matrix applied to the box,
                formatted [[dddd][dddd][dddd]].

        Returns:
            FMEBox: An instance of a Box Geometry object.
        """
    @overload
    def __init__(self, box: FMEBox) -> None:
        """Creates a box from another box.

        Args:
            box: (FMEBox): The box to copy.

        Returns:
            FMEBox: An instance of a Box Geometry object.
        """
    def getAppearanceReference(self, front: bool) -> int: ...
    def getAsBRepSolid(self) -> FMEBRepSolid:
        """Returns the box as a BRepSolid.

        Returns:
            FMEBRepSolid: The BRepSolid of this box.
        """
    def getAsExtrusion(self) -> FMEExtrusion:
        """Returns the box as an Extrusion.

        Returns:
            FMEExtrusion: The Extrusion representation of this box.
        """
    def getAsWireFrame(self) -> FMEMultiCurve | None:
        """Returns the wireframe of the solid as a FMEMultiCurve.

        None is returned if a wireframe cannot be generated.

        Returns:
            FMEWireFrame: The wireframe of the solid as a FMEMultiCurve.
        """
    def getCenterPointXYZ(self) -> tuple[float, float, float]:
        """Returns the center point of the box.

        Returns:
            tuple[float,float,float]: A tuple of the center point's x, y and z
                coordinates consecutively, formatted (x, y, z).
        """
    def getLocalFirstPointXYZ(self) -> tuple[float, float, float]:
        """Gets the coordinates of the first point of this box, prior to transformation.

        Returns:
            tuple[float,float,float]: A tuple of the first point's x, y and z
                coordinates consecutively, formatted (x, y, z).
        """
    def getLocalHeight(self) -> float:
        """Gets the height of this box, prior to transformation.

        Returns:
            float: The height of this box.
        """
    def getLocalLength(self) -> float:
        """Gets the length of this box, prior to transformation.

        Returns:
            float: The length of this box.
        """
    def getLocalMaxPoint(self) -> FMEPoint:
        """Gets the maximum point of this box, prior to transformation.

        Returns:
            FMEPoint: The upper point of this box's bounds.
        """
    def getLocalMinPoint(self) -> FMEPoint:
        """Gets the minimum point of this box, prior to transformation.

        Returns:
            FMEPoint: The lower point of this box's bounds.
        """
    def getLocalSecondPointXYZ(self) -> tuple[float, float, float]:
        """Gets the coordinates of the second point of this box, prior to transformation.

        Returns:
            tuple[float,float,float]: A tuple of the second point's x, y and z
                coordinates consecutively, formatted (x, y, z).
        """
    def getLocalSize(self) -> tuple[float, float, float]:
        """Gets the dimensions of this box, prior to transformation.

        The x-, y-, and z-directions correspond to length, width, and height,
        respectively.

        Returns:
            tuple[float,float,float]: A tuple of the box's length, width and height respectively.
        """
    def getLocalWidth(self) -> float:
        """Gets the width of this box, prior to transformation.

        Returns:
            float: The width of this box.
        """
    def getTransformationMatrix(self) -> list[list[float]]:
        """Gets this box's transformation matrix.

        If the box does not have such a matrix, an identity matrix is returned.
        Only the top three rows of the matrix will be returned, as the bottom
        row is always [ 0 0 0 1 ].

        Returns:
            list[list[float]]: The box's tranformation matrix, formatted [[dddd][dddd][dddd]].
        """
    def hasTransformationMatrix(self) -> bool:
        """Returns whether this box has a transformation matrix.

        Returns:
            bool: True if this box has a transformation matrix, False otherwise.
        """
    def isOriented(self, orientation: int) -> bool: ...
    def offset(self, offsetPoint: FMEPoint) -> FMEBox: ...
    def orient(self, orientation: int) -> FMEBox: ...
    def removeTransformationMatrix(self) -> None:
        """Removes this box's transformation matrix."""
    def reorient(self) -> None: ...
    def reverse(self) -> None: ...
    def rotate2D(self, centerPoint: FMEPoint, angle: float) -> None: ...
    def scale(self, xScale: float, yScale: float, zScale: float) -> None: ...
    def setApperanceReference(self, apperanceReference: int, front: bool) -> None: ...
    def setLocalFirstPointXYZ(self, x: float, y: float, z: float) -> None:
        """Sets the coordinates of the first point of this box, prior to transformation.

        Args:
            x: (float): The x coordinate of the first point.
            y: (float): The y coordinate of the first point.
            z: (float): The z coordinate of the first point.

        Raises:
            FMEException: An exception is raised if an error ocurred.
        """
    def setLocalSecondPointXYZ(self, x: float, y: float, z: float) -> None:
        """Sets the coordinates of the second point of this box, prior to transformation.

        Args:
            x: (float): The x coordinate of the second point.
            y: (float): The y coordinate of the second point.
            z: (float): The z coordinate of the second point.

        Raises:
            FMEException: An exception is raised if an error ocurred.
        """
    def setTransformationMatrix(self, matrix: list[list[float]]) -> None:
        """Sets this box's transformation matrix.

        Replacing the existing matrix if it exists. Only three rows are expected
        in the input array, as a bottom row of [ 0 0 0 1 ] is assumed.

        Args:
            matrix: (list[list[float]]): The transformation matrix, formatted [[dddd][dddd][dddd]].
        """

class FMECSGSolid(FMESimpleSolid):
    pass

class FMEExtrusion(FMESimpleSolid, AppearanceMixin, TransformMixin, OrientMixin):
    """FME Extrusion Class"""

    @overload
    def __init__(
        self,
        face: FMEFace,
        extrusionVector: tuple[float, float, float],
    ) -> None:
        """Creates an extrusion by a face and extrusion vector.

        Args:
            face: (FMESurface): A face representing the base of the extrusion.
            extrusionVector: (tuple[float,float,float]): The extrusion vector as an (x, y, z) tuple.
        """
    @overload
    def __init__(self, extrusion: FMEExtrusion) -> None:
        """Creates an extrusion by an existing extrusion.

        Args:
            extrusion: (FMEExtrusion): An existing extrusion to copy.
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
    def getAppearanceReference(self, front: bool) -> int: ...
    def getArea(self) -> float: ...
    def getAsBRepSolid(self) -> FMEBRepSolid:
        """Returns a boundary-representation solid of this extrusion.

        Returns:
            FMEBRepSolid: The solid as a BRepSolid.
        """
    def getAsWireFrame(self) -> FMEMultiCurve | None:
        """Returns the wireframe of the solid as a FMEMultiCurve.

        None is returned if a wireframe cannot be generated.

        Returns:
            FMEMultiCurve: The wire-frame representation of this extrusion.
        """
    def getBaseAsFace(self) -> FMEFace:
        """Gets the base of this extrusion solid as a face.

        Returns:
            FMEFace: The base face of this extrusion.
        """
    def getEndCapAsFace(self) -> FMEFace:
        """Gets the end cap of this extrusion solid as a face.

        Returns:
            FMEFace: The end cap face of this extrusion.
        """
    def getExtrusionVectorXYZ(self) -> tuple[float, float, float]:
        """Gets the extrusion vector of this extrusion solid.

        Returns:
            tuple[float,float,float]: The extrusion vector as an (x, y, z) tuple.
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
    def isCollection(self) -> bool: ...
    def isOriented(self, orientation: int) -> bool: ...
    def measureExists(self, measureName: str) -> bool: ...
    def offset(self, offsetPoint: FMEPoint) -> None: ...
    def orient(self, orientation: int) -> None: ...
    def removeMeasure(self, measureName: str) -> None: ...
    def removeTraits(self, regexp: str) -> None: ...
    def renameMeasure(self, oldMeasureName: str, newMeasureName: str) -> None: ...
    def reorient(self) -> None: ...
    def reverse(self) -> None: ...
    def rotate2D(self, center: FMEPoint, angle: float) -> None: ...
    def scale(self, xScale: float, yScale: float, zScale: float) -> None: ...
    def setAppearanceReference(self, appearanceRef: int, front: bool) -> None: ...
    def setBase(self, base: FMEFace) -> None:
        """Sets the base of this extrusion solid as the specified face.

        Any existing base that exists in this solid will be replaced. By setting
        the base, the surface normals automatically adjust so that all normals
        are pointing away from the extrusion. If None is passed in, an error will
        result.

        Args:
            base: (FMEFace): The base of the FMEExtrusion as a face.

        Raises:
            FMEException: An exception is raised if an error ocurred.
        """
    def setExtrusionVectorXYZ(self, x: float, y: float, z: float) -> None:
        """Sets the extrusion vector of this extrusion solid.

        Args:
            x: (float): The x-component of the extrusion vector.
            y: (float): The y-component of the extrusion vector.
            z: (float): The z-component of the extrusion vector.
        """
    def setName(self, name: text_type) -> None: ...
    def setTrait(
        self,
        traitName: str,
        traitValue: bool | int | float | text_type | bytearray | bytes,
    ) -> None: ...
    def setTraitNullWithType(self, traitName: str, traitType: int) -> None: ...

class FMEBRepSolid(FMESimpleSolid, AppearanceMixin, TransformMixin, OrientMixin):
    """FME BRepSolid Class"""

    @overload
    def __init__(self) -> None:
        """Create an instance of a BRepSolid geometry object"""
    @overload
    def __init__(self, outerSurface: FMESurface) -> None:
        """Creates a new BRepSolid geometry object. The surface passed in is used
        to define the outer surface of the BRepSolid.

        Args:
            outerSurface: (FMESurface): The outer surface as a surface.

        Returns:
            FMEBRepSolid: The new BRepSolid object.
        """
    @overload
    def __init__(self, brepsolid: FMEBRepSolid) -> None:
        """Create a copy of the passed in BRepSolid geometry object.

        Args:
            brepsolid: (FMEBRepSolid): The BRepSolid geometry object to create a copy of.

        Returns:
            FMEBRepSolid: An instance of a BRepSolid Geometry object.
        """
    def addInnerSurface(self, surface: FMESurface) -> None:
        """Adds a new inner surface to the BRepSolid.

        If None is passed in, this solid will not be modified.

        Args:
            surface: (FMESurface): The surface to add to the boundary-representation solid.
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
    def createBRepSolidCopy(self) -> FMEBRepSolid:
        """This routine returns a copy of the given BRepSolid geometry object.

        If there are any errors, an exception is raised.

        Returns:
            FMEBRepSolid: The new BRepSolid object.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def deleteName(self) -> bool: ...
    def force2D(self) -> None: ...
    def force3D(self, newZ: float) -> None: ...
    def getAppearanceReference(self, front: bool) -> int: ...
    def getArea(self) -> float: ...
    def getAsWireframe(self) -> FMEMultiCurve | None:
        """Returns the outer wireframe of the solid.

        If the solid is not a closed solid, None is returned.

        Returns:
            FMEMultiCurve: The outer wireframe of the solid.
        """
    def getInnerSurfaceAt(self, index: int) -> FMESurface | None:
        """Returns the inner surface at the specified index.

        If the index is out of bounds, None is returned.

        Args:
            index: (int): The index of the inner surface to return.

        Returns:
            FMESurface: The inner surface at the specified index.
        """
    def getMeasureNames(self) -> tuple[str]: ...
    def getName(self) -> text_type | None: ...
    def getOuterSurface(self) -> FMESurface | None:
        """Returns the outer surface of the solid.

        If the solid is not a closed solid, None is returned.

        Returns:
            FMESurface: The outer surface of the solid.
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
    def isOriented(self, orientation: int) -> bool: ...
    def measureExists(self, measureName: str) -> bool: ...
    def numInnerSurfaces(self) -> int:
        """Returns the number of inner surfaces in the solid.

        Returns:
            int: The number of inner surfaces in the solid.
        """
    def offset(self, offsetPoint: FMEPoint) -> None: ...
    def orient(self, orientation: int) -> None: ...
    def removeLastInnerSurface(self) -> FMESurface | None:
        """Removes the last inner surface of this boundary-representation solid.

        If there are no inner surfaces in this solid, this method will return None.

        Returns:
            FMESurface: The last inner surface of the BRepSolid or none.
                Note: This method returns a terminal geometry type of the
                FMESurface; i.e. one of the leaf classes in the FMESurface
                inheritance graph. For example, a FMEFace is returned if the
                geometry truly is a face.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def removeMeasure(self, measureName: str) -> None: ...
    def removeTraits(self, regexp: str) -> None: ...
    def renameMeasure(self, oldMeasureName: str, newMeasureName: str) -> None: ...
    def reorient(self) -> None: ...
    def resolvePartDefaults(self) -> None:
        """Recursively resolves surface parts with default appearances by replacing
        these defaults with the inherited appearance references stored by the
        parent surface, if such a value exists. The nearest non-default ancestor
        value will be used to set the default appearances on the part."""
    def reverse(self) -> None: ...
    def rotate2D(self, center: FMEPoint, angle: float) -> None: ...
    def scale(self, xScale: float, yScale: float, zScale: float) -> None: ...
    def setAppearanceReference(self, appearanceRef: int, front: bool) -> None: ...
    def setName(self, name: text_type) -> None: ...
    def setOuterSurface(self, outerSurface: FMESurface) -> None:
        """Sets the outer surface of this boundary-representation solid as the
        specified FMESurface passed in.

        The outer surface of a boundary-representation solid must exist. Thus,
        if None is passed in, an error will result.

        Args:
            outerSurface: (FMESurface): The outer surface of this solid.

        Raises:
            FMEException: AAn exception is raised if an error occurred, or None is passed in.
        """
    def setTrait(
        self,
        traitName: str,
        traitValue: bool | int | float | text_type | bytearray | bytes,
    ) -> None: ...
    def setTraitNullWithType(self, traitName: str, traitType: int) -> None: ...
