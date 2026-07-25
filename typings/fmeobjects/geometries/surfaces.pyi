from typing import overload
from fmeobjects.features import FMEFeature
from fmeobjects.geometries.areas import FMEArea
from fmeobjects.geometries.curves import FMECurve, FMELine, FMEMultiCurve
from fmeobjects.geometries.general import FMEGeometry
from fmeobjects.geometries.points import FMEPoint
from fmeobjects.geometries.geometry_mixins import (
    AppearanceMixin,
    OrientMixin,
    TransformMixin,
)

from six import string_types, text_type

class FMESurface(FMEGeometry, AppearanceMixin, OrientMixin, TransformMixin):
    """FME Surface Class

    FMESurface is an abstract class. It cannot be created directly.
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
    def deleteSide(self, front: bool) -> bool:
        """This method deletes the side specified by 'front' and indicates
        whether or not it existed before being deleted.

        Args:
            front (bool): If True then the front side will be deleted, otherwise
                the back side will be deleted.

        Returns:
            (bool): Returns True if the side existed before being deleted and
                returns False if it didn’t exist.
        """
    def force2D(self) -> None: ...
    def force3D(self, newZ: float) -> None: ...
    def getAppearanceReference(self, front: bool) -> int: ...
    def getArea(self) -> float: ...
    def getAsWireFrame(self) -> FMEMultiCurve | None:
        """Returns the wireframe of the surface as a FMEMultiCurve.

        None is returned if a wireframe cannot be generated.

        Returns:
            (FMEMultiCurve): The wireframe of the surface as a FMEMultiCurve.
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
    def isInPlane(
        self,
        tolerance: float,
        normalVector: tuple[float, float, float],
        valD: float,
        recalculateD: bool,
    ) -> tuple[bool, tuple[float, float, float], float]:
        """Works similarly to isPlanar(), but checks planarity with respect to
        given normal or given plane.

        If given normal is the zero vector, the normal used to check the
        planarity is computed using Newell's method as in isPlanar(). valD is a
        reference to a value of D in the plane equation AX + BY + CZ = D. It can
        be used to make sure that multiple pieces lie in the same plane. If
        'recalculateD' is set to False, the passed in value of D will be used in
        the calculation. If 'recalcualted' is set to True, the passed in value
        is ignored and is instead automatically calculated (and returned in the
        second position of the returned tuple). A useful calling pattern for
        ensuring co-planarity is to get valD computed on the first call to the
        function setting 'recalculateD' to True, and then use this value for
        future calls with 'recalculateD' to False.

        Args:
            tolerance (float): The tolerance to check against.
            normalVector (tuple[float,float,float]): The normal used to check
                the planarity.
            valD (float): The value D from 'AX + BY + CZ = D'.
            recalculateD (bool): Whether to recalculate 'D' or not.

        Returns:
            (tuple[bool, tuple, float]): A tuple containing a boolean, tuple, and
            float representing:
            - 1) Whether or not the surface is in plane;
            - 2) The normal vector returned; and
            - 3) The value 'D'. Note: If recalculateD is False, the tuple returned
            will only contain the boolean and vector tuple (i.e. 'valD' is not returned).
        """
    def isOriented(self) -> bool: ...
    def isPlanar(self, tolerence: float) -> bool:
        """Check if this geometry is planar.

        Returns True if this is planar within the given tolerance, and False
        otherwise.

        The planarity condition is computed by the following algorithm. The
        normal vector <A, B, C> is determined by the vertices of this surface
        using Newell's method. For the first point (x', y', z') of this surface,
        we compute D' = Ax' + By' + Cz'. Then, this surface is planar if and
        only if every subsequent point (x, y, z) of this surface gives a
        D = Ax + By + Cz, that is within the tolerance amount of D'. That is,
        | D - D' | <= tolerance.

        If the specified tolerance is negative, then this method always returns True.

        Args:
            tolerence (float): The tolerance to check against.

        Returns:
            (bool): Whether the surface is planar within the tolerance supplied.
        """
    def measureExists(self, measureName: str) -> bool: ...
    def offset(self, offsetPoint: FMEPoint) -> None: ...
    def orient(self) -> None: ...
    def removeMeasure(self, measureName: str) -> None: ...
    def removeTraits(self, regexp: str) -> None: ...
    def renameMeasure(self, oldMeasureName: str, newMeasureName: str) -> None: ...
    def reorient(self) -> None: ...
    def reverse(self) -> None: ...
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
    def sideExists(self, front: bool) -> bool:
        """This method checks whether the side specified by 'front' exists.

        Args:
            front (bool):  If 'front' is true then the front side will be checked
                otherwise the back side will be checked.

        Returns:
            (bool): Returns True if the side exists and False otherwise.
        """

class FMEMultiSurface(FMEGeometry, AppearanceMixin, TransformMixin):
    """FME MultiSurface Class"""

    @overload
    def __init__(self) -> None:
        """Default FMEMultiSurface constructor.

        Returns:
            (FMEMultiSurface): A new instance of the FMEMultiSurface class.
        """
    @overload
    def __init__(self, multiSurface: FMEMultiSurface) -> None:
        """Create a copy of the passed in MultiSurface geometry object.

        Args:
            multiSurface (FMEMultiSurface): The MultiSurface geometry object to
            create a copy of.

        Returns:
            (FMEMultiSurface): A new instance of the FMEMultiSurface class.
        """
    def appendPart(self, surface: FMESurface) -> None:
        """This appends the surface to the MultiSurface.

        If None is passed in, nothing will be appended. All surfaces in the
        MultiSurface will be forced to have the same dimension. If any 3D surfaces
        exist, all 2D surfaces will be converted to 3D with a default Z value of 0.0.

        Args:
            surface (FMESurface): The surface to append.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def appendParts(self, multiSurface: FMEMultiSurface) -> None:
        """This appends the MultiSurface passed in to the MultiSurface.

        If None is passed in, nothing will be appended.

        Args:
            multiSurface (FMEMultiSurface): The MultiSurface to append.

        Raises:
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
    def getAppearanceReference(self, front: bool) -> int: ...
    def getArea(self) -> float: ...
    def getAsWireFrame(self) -> FMEMultiCurve | None:
        """This method returns a wireframe representation of the MultiSurface.

        Returns:
            (FMEMultiCurve): The wireframe of the contained surfaces or None if
                a multi curve count not be produced.

        Raises:
            FMEException: An exception is raised if there was a failure in
                creating the multi curve Python object.
        """
    def getMeasureNames(self) -> tuple[str]: ...
    def getName(self) -> text_type | None: ...
    def getPartAt(self, index: int) -> FMESurface | None:
        """This method returns the surface at the specified index.

        None is returned if the index is out of range.

        Args:
            index (int): The index of the surface to return.

        Returns:
            (FMESurface): The surface at the given index. Note: This method returns
            a terminal surface type of the FMESurface; i.e. one of the leaf
            classes in the FMESurface inheritance graph. For example, a FMELine
            is returned if the surface truly is a line.

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
    def isCollection(self) -> bool: ...
    def isInPlane(
        self,
        tolerance: float,
        normalVector: tuple[float, float, float],
        valD: float,
        recalculateD: bool,
    ) -> tuple[bool, tuple[float, float, float], float]:
        """Works similarly to isPlanar(), but checks planarity with respect to
        given normal or given plane.

        If given normal is the zero vector, the normal used to check the
        planarity is computed using Newell's method as in isPlanar(). valD is a
        reference to a value of D in the plane equation AX + BY + CZ = D. It can
        be used to make sure that multiple pieces lie in the same plane. If
        'recalculateD' is set to False, the passed in value of D will be used in
        the calculation. If 'recalcualted' is set to True, the passed in value
        is ignored and is instead automatically calculated (and returned in the
        second position of the returned tuple). A useful calling pattern for
        ensuring co-planarity is to get valD computed on the first call to the
        function setting 'recalculateD' to True, and then use this value for
        future calls with 'recalculateD' to False.

        Args:
            tolerance (float): The tolerance to check against.
            normalVector (tuple[float,float,float]): The normal used to check
                the planarity.
            valD (float): The value D from 'AX + BY + CZ = D'.
            recalculateD (bool): Whether to recalculate 'D' or not.

        Returns:
            (tuple[bool, tuple, float]): A tuple containing a boolean, tuple, and
            float representing:
            - 1) Whether or not the surface is in plane;
            - 2) The normal vector returned; and
            - 3) The value 'D'. Note: If recalculateD is False, the tuple returned
            will only contain the boolean and vector tuple (i.e. 'valD' is not returned).
        """
    def isPlanar(self, tolerence: float) -> bool:
        """Check if this geometry is planar.

        Returns True if this is planar within the given tolerance, and False
        otherwise.

        The planarity condition is computed by the following algorithm. The
        normal vector <A, B, C> is determined by the vertices of this surface
        using Newell's method. For the first point (x', y', z') of this surface,
        we compute D' = Ax' + By' + Cz'. Then, this surface is planar if and
        only if every subsequent point (x, y, z) of this surface gives a
        D = Ax + By + Cz, that is within the tolerance amount of D'. That is,
        | D - D' | <= tolerance.

        If the specified tolerance is negative, then this method always returns True.

        Args:
            tolerence (float): The tolerance to check against.

        Returns:
            (bool): Whether the surface is planar within the tolerance supplied.
        """
    def measureExists(self, measureName: str) -> bool: ...
    def numParts(self) -> int:
        """This method returns the number of parts in this MultiSurface.

        Returns:
            (int): The number of parts in this MultiSurface.
        """
    def offset(self, offsetPoint: FMEPoint) -> None: ...
    def removeAppeanceReference(self, front: bool) -> None:
        """When set at this FMEMultiSurface level, the appearance represents the
        default appearance to apply when the contained surfaces use the default
        appearance instead of a specific appearance.

        This call will remove the inherited appearance reference stored at this
        level, if any, on the side specified by the parameter front.

        Args:
            front (bool): Boolean indicting whether the appearance reference
                should be retrieved for the front or back of the multisurface.

        """
    def removeLastPart(self) -> FMESurface | None:
        """This method removes the last part from this MultiSurface.

        Returns:
            (FMESurface): The last surface of the MultiSurface. Note: This method
            returns a terminal surface type of the FMESurface; i.e. one of the leaf
            classes in the FMESurface inheritance graph. For example, a FMELine
            is returned if the surface truly is a line.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def removeMeasure(self, measureName: str) -> None: ...
    def removeTraits(self, regexp: str) -> None: ...
    def renameMeasure(self, oldMeasureName: str, newMeasureName: str) -> None: ...
    def resolvePartDefaults(self) -> None:
        """Recursively resolves surface parts with default appearances by replacing
        these defaults with the inherited appearance references stored by the parent
        surface, if such a value exists. The nearest non-default ancestor value
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

class FMECompositeSurface(FMESurface):
    """FME Composite Surface Class"""

    @overload
    def __init__(self) -> None:
        """This method creates a new composite surface.

        Returns:
          (FMECompositeSurface): A new composite surface.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    @overload
    def __init__(self, compositeSurface: FMECompositeSurface) -> None:
        """This method creates a new composite surface.

        Returns:
          (FMECompositeSurface): A new composite surface.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def appendPart(self, surface: FMESurface) -> None:
        """This method appends a part to this composite surface.

        f None is passed in, nothing will be appended. All areas in the composite
        surface will be forced to have the same dimension. If any 3D areas exist,
        all 2D areas will be converted to 3D with a default Z value of 0.0.

        Args:
            surface (FMESurface): The surface to append.

        Raises:
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
    def deleteSide(self, front: bool) -> bool:
        """This method deletes the side specified by 'front' and indicates whether
        or not it existed before being deleted.

        Args:
            front (bool): If True then the front side will be deleted, otherwise
                the back side will be deleted.

        Returns:
            (bool): Whether the side existed before being deleted.
        """
    def force2D(self) -> None: ...
    def force3D(self, newZ: float) -> None: ...
    def getAppearanceReference(self, front: bool) -> int: ...
    def getAsWireFrame(self) -> FMEMultiCurve | None: ...
    def getMeasureNames(self) -> tuple[str]: ...
    def getName(self) -> text_type | None: ...
    def getPartAt(self, index: int) -> FMESurface: ...
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
    ) -> tuple[bool, tuple[float, float, float], float]: ...
    def isOriented(self) -> bool: ...
    def isPlanar(self, tolerence: float) -> bool: ...
    def measureExists(self, measureName: str) -> bool: ...
    def numParts(self) -> int:
        """This returns the number of surfaces that make up this composite surface.

        Returns:
            (int): The number of surfaces that make up this composite surface.
        """
    def offset(self, offsetPoint: FMEPoint) -> None: ...
    def orient(self) -> None: ...
    def removeEndPart(self) -> FMESurface | None:
        """This method removes the last part from this composite surface.

        If there are no surfaces in the composite surface, it will return None.

        Returns:
            (FMESurface): The last surface of the composite surface. Note: This
                method returns a terminal surface type of the FMESurface;
                i.e. one of the leaf classes in the FMESurface inheritance graph.
                For example, a FMEMesh is returned if the area truly is a mesh.
        """
    def removeMeasure(self, measureName: str) -> None: ...
    def removeTraits(self, regexp: str) -> None: ...
    def renameMeasure(self, oldMeasureName: str, newMeasureName: str) -> None: ...
    def reorient(self) -> None: ...
    def resolvePartDefaults(self) -> None:
        """Recursively resolves surface parts with default appearances by replacing
        these defaults with the inherited appearance references stored by the parent
        surface, if such a value exists.

        The nearest non-default ancestor value will be used to set the default
        appearances on the part."""
    def reverse(self) -> None: ...
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
    def sideExists(self, front: bool) -> bool: ...
    def simpleSurfaceIter(self) -> FMESimpleSurfaceIterator:
        """This creates a simple surface iterator.

        Returns:
          (FMESimpleSurfaceIterator): A simple surface iterator.
        """

class FMESimpleSurface(FMESurface):
    """FME Simple Surface Class

    FMESimpleSurface is an abstract class. It cannot be created directly."""

    def __init__(self) -> None: ...
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
    def deleteSide(self, front: bool) -> bool: ...
    def force2D(self) -> None: ...
    def force3D(self, newZ: float) -> None: ...
    def getAppearanceReference(self, front: bool) -> int: ...
    def getArea(self) -> float: ...
    def getAsWireFrame(self) -> FMEMultiCurve | None: ...
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
    def isInPlane(
        self,
        tolerance: float,
        normalVector: tuple[float, float, float],
        valD: float,
        recalculateD: bool,
    ) -> tuple[bool, tuple[float, float, float], float]: ...
    def isOriented(self) -> bool: ...
    def isPlanar(self, tolerence: float) -> bool: ...
    def measureExists(self, measureName: str) -> bool: ...
    def numParts(self) -> int: ...
    def offset(self, offsetPoint: FMEPoint) -> None: ...
    def orient(self) -> None: ...
    def removeMeasure(self, measureName: str) -> None: ...
    def removeTraits(self, regexp: str) -> None: ...
    def renameMeasure(self, oldMeasureName: str, newMeasureName: str) -> None: ...
    def reorient(self) -> None: ...
    def reverse(self) -> None: ...
    def rotate2D(self, center: FMEPoint, angle: float) -> None: ...
    def scale(self, xScale: float, yScale: float, zScale: float) -> None: ...
    def setAppearanceReference(self, appearanceRef: int, front: bool) -> None: ...
    def setTrait(
        self,
        traitName: str,
        traitValue: bool | int | float | text_type | bytearray | bytes,
    ) -> None: ...
    def setTraitNullWithType(self, traitName: str, traitType: int) -> None: ...
    def sideExists(self, front: bool) -> bool: ...

class FMESimpleSurfaceIterator:
    """FME Simple Surface Iterator Class

    FMESimpleSurfaceIterator should not be constructed directly. Instead, use the
    iterator semantics of FMECompositeSurface to get an FMESimpleSurfaceIterator
    which can be used to iterate over its geometries."""

    def __init__(self) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class FMEFace(FMESimpleSurface):
    """FME Face Class"""

    @overload
    def __init__(self, boundary: FMEArea, mode: int) -> None:
        """This routine creates a new Face geometry object.

        The stroked boundary of the area is used. If there are any errors,
        None may be returned. If the area passed in is not in 3D, then the
        default value for the z coordinates is 0.0.

        Args:
            boundary (FMEArea): The boundary as an area.
            mode (int): The mode. Must be either FME_CLOSE_3D_AVERAGE_MODE,
                FME_CLOSE_3D_EXTEND_MODE, or FME_CLOSE_3D_EXTEND_OR_AVERAGE_Z_MODE.

        Returns:
            (FMEFace): An instance of a Face geometry object.
        """
    @overload
    def __init__(self, boundary: FMEArea, mode: int, matrix: list[list[float]]) -> None:
        """This routine creates a new Face geometry object with the specified transformation matrix .

        Args:
            boundary (FMEArea): The boundary as an area.
            mode (int): The mode. Must be either FME_CLOSE_3D_AVERAGE_MODE,
                FME_CLOSE_3D_EXTEND_MODE, or FME_CLOSE_3D_EXTEND_OR_AVERAGE_Z_MODE.
            matrix (list[list[float]]):  transformation matrix applied to the face,
                formatted [[dddd][dddd][dddd]].

        Returns:
            (FMEFace): An instance of a Face geometry object.
        """
    @overload
    def __init__(self, boundary: FMELine, mode: int) -> None:
        """This routine creates a new Face geometry object.

        The stroked boundary of the line is used. If there are any errors,
        None may be returned. If the line passed in is not in 3D, then the
        default value for the z coordinates is 0.0.

        Args:
            boundary (FMELine): The boundary as a line.
            mode (int): The mode. Must be either FME_CLOSE_3D_AVERAGE_MODE,
                FME_CLOSE_3D_EXTEND_MODE, or FME_CLOSE_3D_EXTEND_OR_AVERAGE_Z_MODE.

        Returns:
            (FMEFace): An instance of a Face geometry object.
        """
    @overload
    def __init__(self, boundary: FMELine, mode: int, matrix: list[list[float]]) -> None:
        """This routine creates a new Face geometry object with the specified transformation matrix .

        Args:
            boundary (FMELine): The boundary as a line.
            mode (int): The mode. Must be either FME_CLOSE_3D_AVERAGE_MODE,
                FME_CLOSE_3D_EXTEND_MODE, or FME_CLOSE_3D_EXTEND_OR_AVERAGE_Z_MODE.
            matrix (list[list[float]]):  transformation matrix applied to the face,
                formatted [[dddd][dddd][dddd]].

        Returns:
            (FMEFace): An instance of a Face geometry object.
        """
    @overload
    def __init__(self, points: list[tuple[float]], mode: int) -> None:
        """Creates a face from the list of points passed in.

        Args:
            points (list[tuple[float]]): The points of the face.
            mode (int): The mode. Must be either FME_CLOSE_3D_AVERAGE_MODE,
                FME_CLOSE_3D_EXTEND_MODE, or FME_CLOSE_3D_EXTEND_OR_AVERAGE_Z_MODE.

        Returns:
            (FMEFace): An instance of a Face geometry object.
        """
    @overload
    def __init__(self, points: list[tuple[float]], mode: int, matrix: list[list[float]]) -> None:
        """Creates a face from the list of points passed in with the specified transformation matrix .

        Args:
            points (list[tuple[float]]): The points of the face.
            mode (int): The mode. Must be either FME_CLOSE_3D_AVERAGE_MODE,
                FME_CLOSE_3D_EXTEND_MODE, or FME_CLOSE_3D_EXTEND_OR_AVERAGE_Z_MODE.
            matrix (list[list[float]]):  transformation matrix applied to the face,
                formatted [[dddd][dddd][dddd]].

        Returns:
            (FMEFace): An instance of a Face geometry object.
        """
    @overload
    def __init__(self, face: FMEFace) -> None:
        """Creates a face from the input face.

        Args:
            face (FMEFace): The face.

        Returns:
            (FMEFace): An instance of a Face geometry object.
        """
    @overload
    def __init__(self) -> None:
        """Initialize self. See help(type(self)) for accurate signature."""
    def addInnerBoundaryCurve(self, innerBoundary: FMECurve, closeMode: int) -> None:
        """Adds an inner-boundary area to this face, represented by the specified curve.

        Refer to setArea() for the usage of the parameter closeMode. If None is
        passed in, this face will not be modified.

        Args:
            innerBoundary (FMECurve): The face's inner boundary as a FMECurve.
            closeMode (int): The close mode. Must be either FME_CLOSE_3D_AVERAGE_MODE,
                FME_CLOSE_3D_EXTEND_MODE, or FME_CLOSE_3D_EXTEND_OR_AVERAGE_Z_MODE.
        """
    def addInnerBoundarySimpleArea(self, innerBoundary: FMEArea, closeMode: int) -> None:
        """Adds an inner-boundary area to this face, represented by the specified simple area.

        Args:
            innerBoundary (FMEArea): The face's inner boundary as a FMESimpleArea.
            closeMode (int): The close mode. Must be either FME_CLOSE_3D_AVERAGE_MODE,
                FME_CLOSE_3D_EXTEND_MODE, or FME_CLOSE_3D_EXTEND_OR_AVERAGE_Z_MODE.
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
    def deleteSide(self, front: bool) -> bool: ...
    def force2D(self) -> None: ...
    def force3D(self, newZ: float) -> None: ...
    def getAppearanceReference(self, front: bool) -> int: ...
    def getArea(self) -> float: ...
    def getAsArea(self) -> FMEArea:
        """Returns the Face as an area.

        Returns:
            (FMEArea): The face as a FMEArea object. Note: This method returns a
            terminal geometry type of the FMEArea; i.e. one of the leaf classes
            in the FMEArea inheritance graph. For example, a FMEPolygon is
            returned if the geometry truly is a polygon.
        """
    def getAsAreaInLocalCoordinates(self) -> FMEArea:
        """Returns the Face as an area in local coordinates.

        Returns:
            (FMEArea): The face as a FMEArea object. Note: This method returns a
            terminal geometry type of the FMEArea; i.e. one of the leaf classes
            in the FMEArea inheritance graph. For example, a FMEPolygon is
            returned if the geometry truly is a polygon.
        """
    def getAsWireFrame(self) -> FMEMultiCurve | None: ...
    def getMeasureNames(self) -> tuple[str]: ...
    def getName(self) -> text_type | None: ...
    def getNormal(self) -> tuple[float, float, float]:
        """Returns the normal vector of this face, normalized to the unit length.
        The returned vector is computed using Newell's method on the vertices
        contained on the outer boundary of this face. If the face is a single point,
        then a zero vector will be returned.

        Returns:
            (tuple[float,float,float]): The normal vector of this face.
        """
    def getTrait(
        self, traitName: str
    ) -> bool | int | float | string_types | bytearray | bytes | None: ...  # type: ignore
    def getTraitNames(self) -> tuple[str]: ...
    def getTraitNullMissingAndType(self, traitName: str) -> tuple[bool, bool, int]: ...
    def getTraitType(self, traitName: str) -> int: ...
    def getTransformationMatrix(self) -> list[list[float]]:
        """Gets this face's transformation matrix.

        If the face does not have such a matrix, an identity matrix is returned.
        Only the top three rows of the matrix will be returned, as the bottom
        row is always [ 0 0 0 1 ].

        Returns:
            (list[list[float]]): The face's tranformation matrix,
                formatted [[dddd][dddd][dddd]].
        """
    def hasMeasures(self) -> bool: ...
    def hasName(self) -> bool: ...
    def hasTransfromationMatrix(self) -> bool:
        """This method determines if the face has a transformation matrix or not.

        Returns:
            (bool): True if the face has a transformation matrix, False otherwise.
        """
    def is3D(self) -> bool: ...
    def isCollection(self) -> bool: ...
    def isConvex(self) -> bool:
        """Determines if face is convex.

        The polygon making up the area is convex if all internal angles are less
        than 180 degrees and it's not self-intersecting. Imperfectly planar 3D
        polygons are tolerated.

        Returns:
            (bool): True if the face is convex, False otherwise.
        """
    def isInPlane(
        self,
        tolerance: float,
        normalVector: tuple[float, float, float],
        valD: float,
        recalculateD: bool,
    ) -> tuple[bool, tuple[float, float, float], float]: ...
    def isOriented(self) -> bool: ...
    def isPlanar(self, tolerence: float) -> bool: ...
    def measureExists(self, measureName: str) -> bool: ...
    def numParts(self) -> int: ...
    def offset(self, offsetPoint: FMEPoint) -> None: ...
    def orient(self) -> None: ...
    def removeMeasure(self, measureName: str) -> None: ...
    def removeTraits(self, regexp: str) -> None: ...
    def removeTransformationMatrix(self) -> None:
        """Removes the transformation matrix from this face."""
    def renameMeasure(self, oldMeasureName: str, newMeasureName: str) -> None: ...
    def reorient(self) -> None: ...
    def reverse(self) -> None: ...
    def scale(self, xScale: float, yScale: float, zScale: float) -> None: ...
    def setAppearanceReference(self, appearanceRef: int, front: bool) -> None: ...
    def setArea(self, area: FMEArea, closeMode: int) -> None:
        """Sets the area of this face.

        The existing area will be replaced and the transformation matrix will be
        reset.The parameter 'closeMode' specifies how this face treates areas
        that are not closed in 3D.

        - If FME_CLOSE_3D_AVERAGE_MODE is specified, an additional point is added,
        connecting the start and end points of the area. This point is computed
        by the average of the start and end points, in 3D.
        - If FME_CLOSE_3D_EXTEND_MODE is specified, the start and end points are
        connected with no additional points.
        - If FME_CLOSE_3D_EXTEND_OR_AVERAGE_Z_MODE, we use the AVERAGE mode if
        and only if the start and end points lie on the same coordinate plane
        (i.e. they share the same x-, y-, or z-coordinates).
        - Otherwise, the EXTEND mode is used.
        - If the input area is None, then an error will be generated.

        Args:
            area (FMEArea): The area to set.
            closeMode (int): The face's close mode. Must be either
                FME_CLOSE_3D_AVERAGE_MODE, FME_CLOSE_3D_EXTEND_MODE, or
                FME_CLOSE_3D_EXTEND_OR_AVERAGE_Z_MODE.
        """
    def setAreaInLocalCoordinates(self, area: FMEArea, closeMode: int) -> None:
        """Sets the area of this face.

        The transformation matrix untouched. Refer to setArea() for the usage of
        the parameter 'closeMode'.

        Args:
            area (FMEArea): The area to set.
            closeMode (int): The face's close mode. Must be either
                FME_CLOSE_3D_AVERAGE_MODE, FME_CLOSE_3D_EXTEND_MODE, or
                FME_CLOSE_3D_EXTEND_OR_AVERAGE_Z_MODE.
        """
    def setName(self, name: text_type) -> None: ...
    def setTrait(
        self,
        traitName: str,
        traitValue: bool | int | float | text_type | bytearray | bytes,
    ) -> None: ...
    def setTraitNullWithType(self, traitName: str, traitType: int) -> None: ...
    def setTransformationMatrix(self, matrix: list[list[float]]) -> None:
        """Sets this face's transformation matrix, replacing the existing matrix
        if it exists. Only three rows are expected in the input array, as a
        bottom row of [ 0 0 0 1 ] is assumed.

        Args:
            matrix (list[list[float]]): The transformation matrix, formatted
                [[dddd][dddd][dddd]].
        """
    def sideExists(self, front: bool) -> bool: ...

class FMEFaceIterator(FMESimpleSurface):
    """FME Face Iterator Class

    FMEFaceIterator should not be constructed directly. Instead, use the iterator
    semantics of FMESurface to get an FMEFaceIterator which can be used to
    iterate over its geometries."""

    def __init__(self) -> None:
        """Initialize self. See help(type(self)) for accurate signature."""

class FMERectangleFace(FMESimpleSurface):
    """FME Rectangle Face Class"""

    @overload
    def __init__(self) -> None:
        """Create an instance of the FMERectangleFace class.

        Returns:
          (FMERectangleFace): The newly created FMERectangleFace object.
        """
    @overload
    def __init__(self, coordinates: tuple[float, float, float, float, float, float]) -> None:
        """The rectangle has to be parallel to a coordinate plane
        (i.e one of XY, XZ, or YZ plane).

        The first and second points are either the min and max or max and min
        points of the rectangle face. If the first point is the min point, then
        the normal of the rectangle is in the positive direction of the plane it
        is parallel to.

        Arguments:
            coordinates (tuple): tuple of coordinates in form (firstx, firsty,
                firstz, secondx, secondy, secondz).

        Returns:
          (FMERectangleFace): The newly created FMERectangleFace object.
        """
    @overload
    def __init__(
        self,
        coordinates: tuple[float, float, float, float, float, float],
        matrix: list[list[float]],
    ) -> None:
        """The rectangle has to be parallel to a coordinate plane
        (i.e one of XY, XZ, or YZ plane).

        The first and second points are either the min and max or max and min
        points of the rectangle face. If the first point is the min point, then
        the normal of the rectangle is in the positive direction of the plane it
        is parallel to.

        Arguments:
            coordinates (tuple): tuple of coordinates in form (firstx, firsty,
                firstz, secondx, secondy, secondz).
            matrix (list[list[float]]): The transformation matrix, formatted
                [[dddd][dddd][dddd]].

        Returns:
          (FMERectangleFace): The newly created FMERectangleFace object.
        """
    @overload
    def __init__(self, rectangleFace: FMERectangleFace) -> None:
        """Create a copy of the given rectangle face.

        Arguments:
          rectangleFace (FMERectangleFace): The rectangle face to copy.

        Returns:
          (FMERectangleFace): The newly created FMERectangleFace object.
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
    def deleteSide(self, front: bool) -> bool: ...
    def force2D(self) -> None: ...
    def force3D(self, newZ: float) -> None: ...
    def getAppearanceReference(self, front: bool) -> int: ...
    def getArea(self) -> float: ...
    def getAsFaceCopy(self) -> FMEFace:
        """Returns a copy of this face as a FMEFace object.

        Returns:
          (FMEFace): The newly created FMEFace object.
        """
    def getAsWireFrame(self) -> FMEMultiCurve | None: ...
    def getBoundaryAsLine(self) -> FMELine:
        """Return a copy of this rectangle's boundary as a line.

        Returns:
          (FMELine): The rectangle face's boundary as a line.
        """
    def getLocalFirstPointXYZ(self) -> tuple[float]:
        """Gets the coordinates of the first point of this rectangular face,
        prior to transformation.

        Returns:
          (tuple[float]): The coordinate value of the point.
        """
    def getLocalSecondPointXYZ(self) -> tuple[float]:
        """Gets the coordinates of the second point of this rectangular face,
        prior to transformation.

        Returns:
          (tuple[float]): The coordinate value of the point.
        """
    def getMeasureNames(self) -> tuple[str]: ...
    def getName(self) -> text_type | None: ...
    def getTrait(
        self, traitName: str
    ) -> bool | int | float | string_types | bytearray | bytes | None: ...  # type: ignore
    def getTraitNullMissingAndType(self, traitName: str) -> tuple[bool, bool, int]: ...
    def getTraitType(self, traitName: str) -> int: ...
    def getTransformationMatrix(self) -> list[list[float]]:
        """Gets this rectangle face's transformation matrix.

        If the rectangle face does not have such a matrix, an identity matrix is
        returned. Only the top three rows of the matrix will be returned, as the
        bottom row is always [ 0 0 0 1 ]."""
    def hasMeasures(self) -> bool: ...
    def hasName(self) -> bool: ...
    def hasTransformationMatrix(self) -> bool:
        """This method determines if the rectangle face has a transformation matrix or not.

        Returns:
          (bool): True if this face has a transformation matrix, False otherwise.
        """
    def is3D(self) -> bool: ...
    def isCollection(self) -> bool: ...
    def isInPlane(
        self,
        tolerance: float,
        normalVector: tuple[float, float, float],
        valD: float,
        recalculateD: bool,
    ) -> tuple[bool, tuple[float, float, float], float]: ...
    def isOriented(self) -> bool: ...
    def isPlanar(self, tolerence: float) -> bool: ...
    def measureExists(self, measureName: str) -> bool: ...
    def numParts(self) -> int: ...
    def offset(self, offsetPoint: FMEPoint) -> None: ...
    def orient(self) -> None: ...
    def removeMeasure(self, measureName: str) -> None: ...
    def removeTraits(self, regexp: str) -> None: ...
    def removeTransformationMatrix(self) -> None:
        """Removes this rectangle face's transformation matrix."""
    def renameMeasure(self, oldMeasureName: str, newMeasureName: str) -> None: ...
    def reorient(self) -> None: ...
    def reverse(self) -> None: ...
    def rotate2D(self, center: FMEPoint, angle: float) -> None: ...
    def scale(self, xScale: float, yScale: float, zScale: float) -> None: ...
    def setAppearanceReference(self, appearanceRef: str, front: bool) -> None: ...
    def setLocalFirstPointXYZ(self, x: float, y: float, z: float) -> None:
        """Sets the coordinates of the lower point of this rectangular face,
        prior to transformation.

        Arguments:
          x (float): The x coordinate.
          y (float): The y coordinate.
          z (float): The z coordinate.
        """
    def setLocalSecondPointXYZ(self, x: float, y: float, z: float) -> None:
        """Sets the coordinates of the upper point of this rectangular face,
        prior to transformation.

        Arguments:
          x (float): The x coordinate.
          y (float): The y coordinate.
          z (float): The z coordinate.
        """
    def setName(self, name: text_type) -> None: ...
    def setTrait(
        self,
        traitName: str,
        traitValue: bool | int | float | text_type | bytearray | bytes,
    ) -> None: ...
    def setTraitNullWithType(self, traitName: str, traitType: int) -> None: ...
    def setTransformationMatrix(self, matrix: list[list[float]]) -> None:
        """Sets this rectangle face's transformation matrix, replacing the
        existing matrix if it exists.

        Only three rows are expected in the input array, as a bottom row
        of [ 0 0 0 1 ] is assumed.

        Arguments:
          matrix (list[list[float]]): The transformation matrix, formatted
              [[dddd][dddd][dddd]].
        """
    def sideExists(self, front: bool) -> bool: ...

class FMEMesh(FMESimpleSurface):
    """FME Mesh Class"""

    @overload
    def __init__(self) -> None:
        """Default FMEMesh constructor.

        Returns:
            (FMEMesh): An instance of a Mesh geometry object.
        """
    @overload
    def __init__(self, mesh: FMEMesh) -> None:
        """Create a copy of the passed in Mesh geometry object.

        Args:
            mesh (FMEMesh): The Mesh geometry object to create a copy of.

        Returns:
            (FMEMesh): An instance of a Mesh geometry object.
        """
    def addMeshPart(
        self,
        appearanceReference: int,
        vertexIndices: list[int],
        vertexNormalIndices: list[int] | None,
        textureCoordinateIndices: list[int] | None,
    ) -> bool:
        """This routine adds a new mesh part to the mesh.

        The 'vertexNormalIndices' and 'textureCoordinateIndices' may be passed
        in as None if the user does not want to specify vertex normals or
        texture coordinates for the mesh part. The first indices of the mesh
        part should match the respective last indices, indicating a closed face.
        If this is not the case, the mesh part will be closed by the method.

        Args:
            appearanceReference (int): Should refer to a valid appearance in the
                shared object library, but no checking is done during this call.
                The appearance reference of 0 implies that this part will
                inherit the appearance reference of the mesh.
            vertexIndices (list[int]): Should refer to valid vertices in the
                vertex list of the mesh, but no validation is done by the method.
            vertexNormalIndices (list[int] or None): Should refer to valid
                vertex normals stored in the mesh.
            textureCoordinateIndices (list[int] or None): Should refer to valid
                texture coordinates of the mesh.

        Returns:
            (bool): Boolean indicating whether or not the addition was successful.
        """
    def addMeshPartExtended(
        self,
        hasAFront: bool,
        hasABack: bool,
        frontAppRef: int,
        backAppRef: int,
        vertexIndices: list[int],
        vertexNormalIndices: list[int] | None,
        frontTextCoordIndices: list[int] | None,
        backTextCoordIndices: list[int] | None,
    ) -> bool:
        """This routine extends the functionality of addMeshPart(), allowing
        double-sided mesh parts to be added.

        When both 'hasAFront' and 'hasABack' are True, a double sided part will
        be added. If one of these parameters is False, the corresponding
        appearance reference and texture coordinates will not be ignore.

        Args:
            hasAFront (bool): Boolean indicating whether or not the mesh has a front.
            hasABack (bool): Boolean indicating whether or not the mesh has a back.
            frontAppRef (int): Appearance reference for the front of the Mesh.
                Should refer to a valid appearance in the shared object library,
                but no checking is done during this call. The appearance reference
                of 0 implies that this part will inherit the appearance
                reference of the mesh. If 'hasAFront' is False the value of this
                parameter is not important, but it must be a valid int.
            backAppRef (int): Appearance reference for the back of the Mesh.
                Should refer to a valid appearance in the shared object library,
                but no checking is done during this call. The appearance reference
                of 0 implies that this part will inherit the appearance reference
                of the mesh. If 'hasAback' is False the value of this parameter
                is not important, but it must be a valid int.
            vertexIndices (list[int]): Should refer to valid vertices in the
                vertex list of the mesh, but no validation is done by the method.
            vertexNormalIndices (list[int] or None): Should refer to valid vertex
                normals stored in the mesh.
            frontTextCoordIndices (list[int] or None): Should refer to valid
                texture coordinates of the mesh.
            backTextCoordIndices (list[int] or None): Should refer to valid
                texture coordinates of the mesh.

        Returns:
            (bool): Boolean indicating whether or not the addition was successful.
        """
    def appendMesh(self, otherMesh: FMEMesh) -> None:
        """Appends a mesh passed in to the mesh.

        By appending the vertices, vertex normals and texture coordinates and
        then by appending mesh parts with updated indices.

        Args:
            otherMesh (FMEMesh): Another mesh to append to this mesh.
        """
    def appendTextureCoordinate(self, u: float, v: float, w: float, q: float) -> None:
        """Appends the texture coordinate to the end of the texture coordinate list.

        If there are already texture coordinates and a coordinate is supplied
        for a component that doesn't exist, it will be created and back filled
        with math.nan. Parameters set to math.nan will be ignored.

        Args:
            u (float): The U texture coordinate.
            v (float): The V texture coordinate.
            w (float): The W texture coordinate.
            q (float): The Q texture coordinate.
        """
    def appendVertex(self, x: float, y: float, z: float) -> None:
        """Appends the point to the end of the vertex list.

        This method will assume that passed vertices are in local coordinates
        (i.e. the transformation matrix will be applied to these vertices).

        Args:
            x (float): The X coordinate.
            y (float): The Y coordinate.
            z (float): The Z coordinate.
        """
    def appendVertexColored(self, x: float, y: float, z: float, r: float, g: float, b: float) -> None:
        """Appends the point to the end of the vertex list using color information
        provided.

        This method will assume that passed vertices are in local coordinates
        (i.e. the transformation matrix will be applied to these vertices).

        Args:
            x (float): The x coordinate of the vertex to be appended.
            y (float): The y coordinate of the vertex to be appended.
            z (float): The z coordinate of the vertex to be appended.
            r (float): The r value of the color.
            g (float): The g value of the color.
            b (float): The b value of the color.
        """
    def appendVertexNormal(self, x: float, y: float, z: float) -> None:
        """Appends the point to the end of the vertex normal list.

        Args:
            x (float): The x coordinate of the vertex to be appended.
            y (float): The y coordinate of the vertex to be appended.
            z (float): The z coordinate of the vertex to be appended.
        """
    def appendVertexNormals(self, points: list[tuple[float]]) -> None:
        """Appends the vertex normals to the end of the vertex normal list.

        Args:
            points (list[tuple[float]]): The list of vertices to be added.
                The vertices are represented as (x, y, z) tuples.
        """
    def appendVertices(self, points: list[tuple[float]]) -> None:
        """Appends the vertices to the end of the vertex list.

        This method will assume that passed vertices are in local coordinates
        (i.e. the transformation matrix will be applied to these vertices).

        Args:
            points (list[tuple[float]]): The list of vertices to be added.
                The vertices are represented as (x, y, z) tuples.
        """
    def appendVerticesColored(self, pointsColorsAndHasColor: list[tuple[float, bool]]) -> None:
        """Appends the vertices to the end of the vertex list using color
        information provided.

        This method will assume that passed vertices are in local coordinates
        (i.e. the transformation matrix will be applied to these vertices). The
        hasColor flag specifies whether a valid color exists at that vertex index.

        Args:
            pointsColorsAndHasColor (list[tuple[float, bool]]): The list of
                tuple of vertices, colors, and has color flag to be added. A
                tuple is in the form (x, y, z, r, g, b, hasColor), where
                vertices are the x, y, z as floats, color components are r, g, b
                as floats, and the hasColor is a bool.
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
        self,
        destFeature: FMEFeature,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None: ...
    def deleteName(self) -> bool: ...
    def deleteSide(self, front: bool) -> bool: ...
    def force2D(self) -> None: ...
    def force3D(self, newZ: float) -> None: ...
    def getAppearanceReference(self, front: bool) -> int: ...
    def getArea(self) -> float: ...
    def getAsCompositeSurface(self) -> FMECompositeSurface | None:
        """Returns a composite surface representation of this mesh.

        None is returned when an error is encountered.

        Returns:
            (FMECompositeSurface or None): Returns a composite surface
                representation of this mesh or none.
        """
    def getAsMultiSurface(self) -> FMEMultiSurface | None:
        """Returns a multi-surface representation of this mesh.

        None is returned when an error is encountered.

        Returns:
            (FMEMultiSurface or None): Returns a multi-surface representation
                of this mesh or none.
        """
    def getAsWireFrame(self) -> FMEMultiCurve | None: ...
    def getMeasureNames(self) -> tuple[str]: ...
    def getName(self) -> text_type | None: ...
    def getTextureCoordinateAt(self, index: int) -> tuple[float] | None:
        """Retrieve the texture coordinate at the specified index.

        Only components of the texture coordinate that return True from
        hasTextureCoordinates[U|V|W|Q] will be fetched. A value of None means
        that the texture coordinate value doesn't exist at that index. An error
        is returned if the index is out of range.

        Args:
            index (int): The index of the texture coordinate to retrieve.

        Returns:
            (tuple[float] or None): The texture coordinate at the specified
                index.

        Raises:
            FMEException: An error occurred.
        """
    def getTextureCoordinates(self) -> list[tuple[float]]:
        """Retrieves the texture coordinate list with texture coordinates in the
        same index position as referenced by the faces.

        Only components where hasTextureCoordinates[U|V|W|Q] is true will be
        fetched.

        Returns:
            (list[tuple[float]]): The list of coordinates represented as
                (u, v, w, q) tuples.
        """
    def getTrait(
        self,
        traitName: str,
    ) -> bool | int | float | string_types | bytearray | bytes | None: ...  # type: ignore
    def getTraitNames(self) -> tuple[str]: ...
    def getTraitNullMissingAndType(self, traitName: str) -> tuple[bool, bool, int]: ...
    def getTraitType(self, traitName: str) -> int: ...
    def getTransformationMatrix(self) -> list[list[float]]:
        """Gets this mesh's transformation matrix.

        If the mesh does not have such a matrix, an identity matrix is returned.
        Only the top three rows of the matrix will be returned, as the bottom
        row is always [ 0 0 0 1 ].

        Returns:
            (list[list[float]]): The mesh's tranformation matrix, formatted
                [[dddd][dddd][dddd]].
        """
    def getVertexAt(self, index: int) -> tuple[float] | None:
        """Retrieve the vertex, in global coordinates

        (i.e., the transformation matrix is applied, if it exists), at the
        specified index. An FMEException is raised if the index is out of range.

        Args:
            index (int): The index of the vertex to retrieve.

        Returns:
            (tuple[float] or None):The vertex at the index represented as a
                (x, y, z) tuple.

        Raises:
            FMEException: An error occurred.
        """
    def getVertexColorAt(self, index: int) -> tuple[float] | None:
        """Retrieves the vertex color at the specified index.

        Raises an FMEException when a valid color does not exist at the
        specified index, the index is out of range, or the mesh does not contain
        vertex colors.

        Args:
            index (int): The index of the vertex color to retrieve.

        Returns:
            (tuple[float] or None): The vertex at the index represented as a
                (x, y, z) tuple.

        Raises:
            FMEException: An error occurred.
        """
    def getVertexNormalAt(self, index: int) -> list[tuple[float]]:
        """Retrieve the vertex normal, in global coordinates

        (i.e., the transformation matrix is applied, if it exists), at the
        specified index. An FMEException is raised if the index is out of range.

        Args:
            index (int): The index of the vertex normal to retrieve.

        Returns:
            (list[tuple[float]]): The vertex normal at the index represented as
                a (x, y, z) tuple.

        Raises:
            FMEException: An error occurred.
        """
    def getVertexNormals(self) -> list[list[float]]:
        """Retrieves the vertex normal list with vertex normals, in global
        coordinates

        (i.e., the transformation matrix is applied, if it exists), in the same
        index position as referenced by the faces.

        Returns:
            (list[list[float]]): The list of vertex normals represented as
                (x, y, z) tuples.

        Raises:
            FMEException: An error occurred.
        """
    def getVertexNormalsInLocalCoordinates(self) -> list[list[float]]:
        """This is the same as getVertexNormals() with the exception that the
        transformation matrix is not applied.

        Returns:
            (list[list[float]]): The list of vertex normals represented as
                (x, y, z) tuples.

        Raises:
            FMEException: An error occurred.
        """
    def getVertices(self) -> list[tuple[float]]:
        """Retrieves the vertex list with vertices, in global coordinates

        (i.e., the transformation matrix is applied, if it exists), in the same
        index position as referenced by the faces.

        Returns:
            (list[tuple[float]]): The list of vertices represented as
                (x, y, z) tuples.

        Raises:
            FMEException: An error occurred.
        """
    def getVerticesInLocalCoordinates(self) -> list[tuple[float]]:
        """This is the same as getVertices() with the exception that the
        transformation matrix is not applied.

        Returns:
            (list[tuple[float]]): The list of vertices represented as
                (x, y, z) tuples.

        Raises:
            FMEException: An error occurred.
        """
    def hasColorAtVertex(self, index: int) -> bool:
        """This method determines if there is color at a vertex.

        Args:
            index (int): The index of the vertex color to check.

        Returns:
            (bool): Returns True if a valid color exists at the specified index,
                otherwise returns False if a valid color does not exist at the
                specified index, the index is out of range, or the mesh does not
                contain vertex colors.
        """
    def hasMeasures(self) -> bool: ...
    def hasName(self) -> bool: ...
    def hasTextureCoordinatesQ(self) -> bool:
        """Check if this geometry has texture coordinates.

        Returns True if the texture coordinates stored have the specified
        component. Returns False if no texture coordinates are stored or the
        specified component of the texture coordinates is not valid for this mesh.

        Returns:
            (bool): Returns True if the texture coordinates stored have the
                specified component, and False otherwise.
        """
    def hasTextureCoordinatesU(self) -> bool:
        """Check if this geometry has texture coordinates.

        Returns True if the texture coordinates stored have the specified
        component. Returns False if no texture coordinates are stored or the
        specified component of the texture coordinates is not valid for this mesh.

        Returns:
            (bool): Returns True if the texture coordinates stored have the
                specified component, and False otherwise.
        """
    def hasTextureCoordinatesV(self) -> bool:
        """Check if this geometry has texture coordinates.

        Returns True if the texture coordinates stored have the specified
        component. Returns False if no texture coordinates are stored or the
        specified component of the texture coordinates is not valid for this mesh.

        Returns:
            (bool): Returns True if the texture coordinates stored have the
                specified component, and False otherwise.
        """
    def hasTextureCoordinatesW(self) -> bool:
        """Check if this geometry has texture coordinates.

        Returns True if the texture coordinates stored have the specified
        component. Returns False if no texture coordinates are stored or the
        specified component of the texture coordinates is not valid for this mesh.

        Returns:
            (bool): Returns True if the texture coordinates stored have the
                specified component, and False otherwise.
        """
    def hasTransformationMatrix(self) -> bool:
        """This method determines if the mesh has a transformation matrix or not.

        Returns:
            (bool): True if this geometry has a transformation matrix, False
                otherwise.
        """
    def is3D(self) -> bool: ...
    def isCollection(self) -> bool: ...
    def isInPlane(
        self,
        tolerance: float,
        normalVector: tuple[float, float, float],
        valId: float,
        recalculateD: bool,
    ) -> tuple[bool, tuple[float, float, float], float]: ...
    def isOriented(self) -> bool: ...
    def isPlanar(self, tolerence: float) -> bool: ...
    def maxEdgeNumber(self) -> int:
        """Returns the maximum number of edges the mesh can contain.

        Returns:
            (int): The maximum number of edges in this geometry.
        """
    def measureExists(self, measureName: str) -> bool:
        """CReturns True if the specified measure exists and False otherwise.

        If the 'measureName' parameter is not specified then the default measure
        is checked.

        Returns:
            (bool): Boolean indicating whether or not the measure exists.
        """
    def numParts(self) -> int:
        """This returns the number of faces that are contained in this geometry.

        Returns:
            (int): The number of parts in this geometry.
        """
    def numTextureCoordinates(self) -> int:
        """Returns the number of texture coordinates that are contained in this mesh.

        Returns:
            (int): Returns the number of texture coordinates that are contained
                in this mesh.
        """
    def numVertexColors(self) -> int:
        """Returns the total number of vertex colors, including invalid ones.

        This will be either 0, if the mesh does not contain vertex colors, or
        the same as the number of vertices.

        Returns:
            (int): Returns the number of vertex colors.
        """
    def numVertexNormals(self) -> int:
        """Returns the number of vertex normals that are contained in this mesh.

        Returns:
            (int): Returns the number of vertex normals in this mesh.
        """
    def numVertexNormalsInLocalCoordinates(self) -> int:
        """This is the same as numVertexNormals() with the exception that the
        transformation matrix is not considered.

        If the transformation matrix is not invertible, this will return the
        number of unmodified normals, numVertexNormals() will return 0 because
        the normals will be removed if a non-invertible matrix is applied.

        Returns:
            (int): Returns the number of vertex normals in local coordinates for this mesh.
        """
    def numVertices(self) -> int:
        """Returns the number of vertices that are contained in this mesh.

        Returns:
            (int): Returns the number of vertices in this mesh.
        """
    def offset(self, offsetPoint: FMEPoint) -> None: ...
    def optimizeVertexPool(self) -> None:
        """Optimizes the mesh by removing all duplicate and unreferenced vertices,
        vertex normals, and texture coordinates.

        This will modify the underlying vertex pools and update the mesh part
        indices. This is a potentially expensive operation and should not be
        called unless necessary.
        """
    def orient(self) -> None: ...
    def removeDegenerateTriangleMeshParts(self) -> None:
        """Removes this mesh's degenerate triangle parts."""
    def removeMeasure(self, measureName: str) -> None: ...
    def removeTraits(self, regexp: str) -> None: ...
    def removeTransformationMatrix(self) -> None:
        """Removes this mesh's transformation matrix."""
    def renameMeasure(self, oldMeasureName: str, newMeasureName: str) -> None: ...
    def reorient(self) -> None: ...
    def resetGeometry(self) -> None:
        """Removes all vertices, texture coordinates, normals, and mesh parts."""
    def resolvePartDefaults(self) -> bool:
        """This call assumes that the mesh has been triangulated.

        It will remove any mesh parts that do not have three edges and will also
        remove triangles with repeated vertex indices. It will return true if
        any parts are removed by the call. This method assumes that duplicate
        indices have already been removed from the mesh.

        Returns:
            (bool): Returns True if any parts are removed by the call and False
                otherwise.
        """
    def reverse(self) -> None: ...
    def rotate2D(self, center: FMEPoint, angle: float) -> None: ...
    def scale(self, xScale: float, yScale: float, zScale: float) -> None: ...
    def setAppearanceReference(self, appearanceRef: int, front: bool) -> None: ...
    def setEdgeVisibilityFlagsToLastPart(
        self,
        edgeVisibilityFlags: list[bool],
    ) -> None:
        """This routine sets the edge visibility flags to the last mesh part
        that was added.

        It is intended to be called directly after addMeshPart(),
        typically. The size of the list of flags must be exactly one fewer than
        the number of vertices on the last part of the mesh.

        Passing in None will remove all edge visibility flags from the last mesh
        part.

        Args:
            edgeVisibilityFlags (list[bool]): The list of edge visibility flags.

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
    def setTransformationMatrix(self, matrix: list[list[float]]) -> None:
        """Sets this mesh's transformation matrix, replacing the existing matrix if it exists.

        Only three rows are expected in the input array, as a bottom row of
        [ 0 0 0 1 ] is assumed.

        Args:
            matrix (list[list[float]]): The transformation matrix, formatted
                [[dddd][dddd][dddd]].
        """
    def sideExists(self, front: bool) -> bool: ...

class FMEMeshPartIterator:
    """FME Mesh Part Iterator Class

    FMEMeshPartIterator should not be constructed directly. Instead, use the
    iterator semantics of FMEMesh to get an FMEMeshPartIterator which can be
    used to iterate over its geometries."""

    def __init__(self) -> None:
        """Initialize self. See help(type(self)) for accurate signature."""
    def getAppearanceReference(self, front: bool) -> int:
        """This method returns the appearance reference within the Library associated with this mesh part iterator. T

        The front parameter controls whether this query should return the front
        or the back appearance reference. Both can be fetched independently. If
        this mesh part iterator is a regular mesh part iterator with no geometry
        instance, a FMEException will be thrown.

        Args:
            front (bool): If True, the front appearance reference is returned.
                If False, the back appearance reference is returned.

        Returns:
            (int): The appearance reference for the geometry.

        Raises:
            FMEException: An exception is raised if this mesh part iterator is
            not associated with a geometry instance.
        """
    def getTextureCoordinateIndices(self, front: bool) -> list[int] | None:
        """This method returns the texture coordinate indices associated with this mesh part iterator.

        The front parameter controls whether this query should return the front
        or the back texture coordinate indices. Both can be fetched independently.

        Args:
            front (bool): Indicates whether the indices should be fetched for
                the front or back of the mesh part.

        Returns:
            (list[int]): The texture coordinate indices or None if a problem occurred.
        """
    def getVertexIndices(self) -> list[int] | None:
        """Returns the vertex indices in the current mesh part via a list of ints.

        Returns:
            (list[int]): The vertex indices or None if a problem occurred.
        """
    def getVertexNormalIndices(self) -> list[int] | None:
        """Returns the vertex normal indices in the current mesh part via a list of ints.

        Returns:
            (list[int]): The vertex normal indices or None if a problem occurred.
        """
    def hasTextureCoords(self, front: bool) -> bool:
        """Returns a boolean indicating whether or not the mesh part iterator has texture coordinates.

        The front parameter controls whether this query should be made on the
        front or back of the mesh part.

        Args:
            front (bool): Indicates whether the indices should be fetched for
                the front or back of the mesh part.

        Returns:
            (bool): True if the mesh part has texture coordinates, False otherwise.
        """
    def hasVertexNormals(self) -> bool:
        """Returns a boolean indicating whether or not the mesh part iterator has vertex normals.

        Returns:
            (bool): True if the mesh part has vertex normals, False otherwise.
        """
    def numVertices(self) -> int:
        """Returns the number of vertices.

        Returns:
            (int): The number of vertices.
        """
    def seek(self, index: int) -> bool:
        """This method advances the iterator to the mesh part specified by index,
        if it exists.

        Returns true if there is a valid part at the index and false if there is not.

        Args:
            index (int): The index to advance the iterator to.

        Returns:
            (bool): Indicates whether or not the mesh part at index is a valid part.
        """
    def sideExists(self, front: bool) -> bool:
        """Indicates whether of not the side of the mesh part exists.

        The front parameter controls whether this query should be made on the
        front or back of the mesh part.

        Args:
            front (bool):Indicates whether the query should be made on thhe
                front or back of the mesh part.

        Returns:
            (bool): Returns True if th side exists or False otherwise.
        """

class FMETriangleFan(FMESimpleSurface):
    """FME Triangle Fan Class"""

    @overload
    def __init__(self) -> None:
        """Create an instance of a Triangle Fan geometry object.

        Returns:
          (FMETriangleFan): An instance of a Triangle Fan geometry object.
        """
    @overload
    def __init__(self, points: list[tuple[float]]) -> None:
        """Creates a line consisting of the list of points.

        Args:
          points (list): The list of points to set to the triangle fan. The points are represented as (x, y, z) tuples.

        Returns:
          (FMETriangleFan): An instance of a Triangle Fan geometry object.
        """
    @overload
    def __init__(self, triangleFan: FMETriangleFan) -> None:
        """Creates a triangle fan from another triangle fan.

        Args:
          triangleFan (FMETriangleFan): The triangle fan to copy.

        Returns:
          (FMETriangleFan): An instance of a Triangle Fan geometry object.
        """
    def appendPointXYZ(self, x: float, y: float, z: float) -> None:
        """Appends coordinates to the end of the coordinate list that defines the
        triangle fan.

        This operation effectively appends new triangles to the triangle fan.
        After the append operation, coordinates at indices 0, i + 1, and i + 2
        define the ith triangle.

        Args:
          x (float): The x coordinate of the point.
          y (float): The y coordinate of the point.
          z (float): The z coordinate of the point.
        """
    def appendPoints(self, points: list[tuple[float]]) -> None:
        """Appends coordinates to the end of the coordinate list that defines the
        triangle fan.

        This operation effectively appends new triangles to the triangle fan.
        After the append operation, coordinates at indices 0, i + 1, and i + 2
        define the ith triangle.

        Args:
          points (list): The list of points to set to the triangle fan.
              The points are represented as (x, y, z) tuples.
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
    def deleteSide(self, front: bool) -> bool: ...
    def force2D(self) -> None: ...
    def force3D(self, newZ: float) -> None: ...
    def getAppearanceReference(self, front: bool) -> int: ...
    def getArea(self) -> float: ...
    def getAsFaceAt(self, index: int) -> FMEFace | None:
        """Returns a triangular face defined by this triangle fan.

        The index indicates the specific triangular face to return. In particular,
        given an index i, the triangular face returned is specified by the
        coordinate indices 0, i + 1, and i + 2. If the specified index is out of
        range, then None is returned.

        Args:
          index (int): The index of the face to return.

        Returns:
          (FMEFace): A copy of a triangular face defined by this triangle fan.
        """
    def getAsWireFrame(self) -> FMEMultiCurve | None: ...
    def getMeasureNames(self) -> tuple[str]: ...
    def getMeasureValueAt(self, index: int, measureName: str) -> float:
        """Get the value of the default measure at the 'index'.

        If 'measureName' is supplied, this method gets the value of the named
        measure at 'index'. Returns an error if the measure doesn't exist or
        'index' is out of range.

        Args:
          index (int): The index of the measure to return.
          measureName (str): (optional) The name of the measure to return.

        Returns:
          (float): The value of the default measure at the given index, or the
              measure named by 'measureName' at the given index.

        Raises:
          FMEException: An exception is raised if an error occurred
        """
    def getMeasureValues(self, measureName: str) -> list[float]:
        """Returns the value of the default measure, or the value of the measure
        named by 'measureName'.

        Args:
          measureName (str): (optional) The name of the measure to return.

        Returns:
          (list[float]): The values of the default measure, or the measures named
              by 'measureName'.

        Raises:
          FMEException: An exception is raised if an error occurred
        """
    def getName(self) -> text_type | None: ...
    def getPointAtXYZ(self, index: int) -> tuple[float]:
        """Gets a coordinate of this triangle fan at the specified index.

        If index is out of range, then an error is generated.

        Args:
          index (int): The index of the coordinate to return.

        Returns:
          (tuple[float]): The point is represented as a (x, y, z) tuple.

        Raise:
          FMEException: An exception is raised if an error occurred
        """
    def getPoints(self) -> list[FMEPoint]:
        """Gets the points of the triangle fan as a list of FMEPoint objects.
        The size of the given list must be exactly equal to the value returned
        by numPoints(). If the triangle fan is 2D the z values of the triangle
        fan will be populated with 0.0 values. Returns an error if an error occurred.

        Returns:
          (list[FMEPoint]): A list of points contained within the triangle fan.

        Raises:
          FMEException: An exception is raised if an error occurred
        """
    def getPointsAsLine(self) -> FMELine:
        """Returns a line that contains the points in this triangle fan.

        The line will have all the geometry traits and measures of the triangle fan.

        Returns:
          (FMELine): A copy of a line that contains the points in this triangle fan.
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
    ) -> tuple[bool, tuple[float, float, float], float]: ...
    def isOriented(self) -> bool: ...
    def isPlanar(self, tolerence: float) -> bool: ...
    def measureExists(self, measureName: str) -> bool: ...
    def numParts(self) -> int: ...
    def numPoints(self) -> int:
        """Returns the number of coordinates in the triangle fan.

        Returns:
          (int): The number of coordinates in the triangle fan.
        """
    def offset(self, offsetPoint: FMEPoint) -> None: ...
    def orient(self) -> None: ...
    def removeMeasure(self, measureName: str) -> None: ...
    def removeTraits(self, regexp: str) -> None: ...
    def renameMeasure(self, oldMeasureName: str, newMeasureName: str) -> None: ...
    def reorient(self) -> None: ...
    def reverse(self) -> None: ...
    def rotate2D(self, center: FMEPoint, angle: float) -> None: ...
    def scale(self, xScale: float, yScale: float, zScale: float) -> None: ...
    def setAppearanceReference(self, front: bool, appearanceReference: int) -> None: ...
    def setMeasure(self, measureValues: list[float], measureName: str) -> None:
        """Set the default measure to the given values.

        Create the measure if it doesn't already exist. If 'measureName' is
        supplied, this method sets the given measure to 'measureValues', or
        creates the measure if it doesn't already exist. The size of 'measureValues'
        must be exactly equal to the value returned by numPoints().

        Args:
          measureValues (list[float]): The values to set.
          measureName (str): Optional) The name of the measure whose value is to
          be set, or created.
        """
    def setMeasureAt(self, index: int, measureValues: list[float], measureName: str) -> None:
        """Set the default measure of the point at 'index' to the given 'measureValue'.

        If 'measureName' is supplied, this method sets the given measure of the
        point at 'index' to 'measureValue'. Creates the measure if it doesn't
        already exist and set the measures to all points other than the point at
        the given index to None. Return an error if the index is out of range.

        Args:
          index (int): The index of the measure to set.
          measureValues (list[float]): The values to set.
          measureName (str): Optional) The name of the measure whose value is to
          be set, or created.

        Raises:
          FMEException: An exception is raised if an error occurred
        """
    def setName(self, name: text_type) -> None: ...
    def setTrait(
        self,
        traitName: str,
        traitValue: bool | int | float | text_type | bytearray | bytes,
    ) -> None: ...
    def setTraitNullWithType(self, traitName: str, traitType: int) -> None: ...
    def sideExists(self, front: bool) -> bool: ...

class FMETriangleStrip(FMESimpleSurface):
    """FME Triangle Strip Class"""

    @overload
    def __init__(self) -> None:
        """Create and instance of the FMETriangleStrip class.

        Returns:
          (FMETriangleStrip): An instance of the FMETriangleStrip class.
        """
    @overload
    def __init__(self, points: list[tuple[float]]) -> None:
        """Creates a line consisting of the list of points passed in.

        Args:
          points (list[tuple[float]]): The list of points to set to the triangle
              strip. The points are represented as (x, y, z) tuples.

        Returns:
          (FMETriangleStrip): An instance of the FMETriangleStrip class.
        """
    @overload
    def __init__(self, triangleStrip: FMETriangleStrip) -> None:
        """Creates a copy of the given triangle strip.

        Args:
          triangleStrip (FMETriangleStrip): The triangle strip to copy.

        Returns:
          (FMETriangleStrip): An instance of the FMETriangleStrip class.
        """
    def appendPointXYZ(self, x: float, y: float, z: float) -> None:
        """Appends coordinates to the end of the coordinate list that defines the triangle strip.

        This operation effectively appends new triangles to the triangle strip.
        After the append operation, coordinates at indices 0, i + 1, and i + 2
        define the ith triangle.

        Args:
          x (float): The x value of the point to append.
          y (float): The y value of the point to append.
          z (float): The z value of the point to append.
        """
    def appendPoints(self, points: list[tuple[float]]) -> None:
        """Appends coordinates to the end of the coordinate list that defines the triangle strip.

        This operation effectively appends new triangles to the triangle strip.
        After the append operation, coordinates at indices 0, i + 1, and i + 2
        define the ith triangle.

        Args:
          points (list[tuple[float]]): The list of points to append. The points
              are represented as (x, y, z) tuples.
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
    def deleteSide(self, front: bool) -> bool: ...
    def force2D(self) -> None: ...
    def force3D(self, newZ: float) -> None: ...
    def getAppearanceReference(self, front: bool) -> int: ...
    def getArea(self) -> float: ...
    def getAsFaceAt(self, index: int) -> FMEFace | None:
        """Returns the face at the given index.

        Args:
          index (int): The index of the face to return.

        Returns:
          (FMEFace): A copy of a triangular face defined by this triangle strip.
        """
    def getAsWireFrame(self) -> FMEMultiCurve | None: ...
    def getMeasureNames(self) -> tuple[str]: ...
    def getMeasureValueAt(self, index: int, measureName: str) -> float:
        """Get the value of the default measure at the 'index'.

        If 'measureName' is supplied, this method gets the value of the named
        measure at 'index'. Returns an error if the measure doesn't exist or
        'index' is out of range.

        Args:
          index (int): The index of the measure to return.
          measureName (str): (Optional) The name of the measure whose value is
              to be returned.

        Returns:
          (float): The value of the default measure at the given index, or the
          measure named by 'measureName' at the given index.
        """
    def getMeasureValues(self, measureName: str) -> list[float]:
        """Get the values of the default measureor the value of the measure named by 'measureName'.

        Args:
          measureName (str): (Optional) The name of the measure whose value is
              to be returned.

        Returns:
          (list[float]): The values of the default measure, or the measures named by 'measureName'.

        Raises:
          FMEException: An exception is raised if an error occurred
        """
    def getName(self) -> text_type | None: ...
    def getPointAtXYZ(self, index: int) -> tuple[float]:
        """Gets a coordinate of this triangle strip at the specified index.

        If index is out of range, then an error is generated.

        Args:
          index (int): The index of the point to return.

        Returns:
          (tuple[float]): The point at the given index.
        """
    def getPoints(self) -> list[FMEPoint]:
        """Gets the points of the triangle strip as a list of FMEPoint objects.

        The size of the given list must be exactly equal to the value returned
        by numPoints(). If the triangle strip is 2D the z values of the triangle
        strip will be populated with 0.0 values. Throws an exception if an error
        occurred.

        Returns:
          (list[FMEPoint]): The points of this triangle strip.

        Raise:
          FMEException: An exception is raised if an error occurred
        """
    def getPointsAsLine(self) -> FMELine:
        """Returns a line that contains the points in this triangle strip.

        The line will have all the geometry traits and measures of the triangle strip.

        Returns:
          (FMELine): A copy of a line that contains the points in this triangle strip.
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
    def isFlipped(self) -> bool:
        """Determines whether the orientation of the triangle strip is the opposite
        of what the first triangle indicates (using a right-handed coordinate system).

        Returns:
          (bool): Returns True if the orientation of the triangle strip is the
              opposite of what the first triangle indictes and False otherwise.
        """
    def isInPlane(
        self,
        tolerance: float,
        normalVector: tuple[float, float, float],
        valD: float,
        recalculateD: bool,
    ) -> tuple[bool, tuple[float, float, float], float]: ...
    def isOriented(self) -> bool: ...
    def isPlanar(self, tolerence: float) -> bool: ...
    def measureExists(self, measureName: str) -> bool: ...
    def numParts(self) -> int: ...
    def numPoints(self) -> int:
        """Gets the number of points in this triangle strip.

        Returns:
          (int): The number of points in this triangle strip.
        """
    def offset(self, offsetPoint: FMEPoint) -> None: ...
    def orient(self) -> None: ...
    def removeMeasure(self, measureName: str) -> None: ...
    def removeTraits(self, regexp: str) -> None: ...
    def renameMeasure(self, oldMeasureName: str, newMeasureName: str) -> None: ...
    def reorient(self) -> None: ...
    def reverse(self) -> None: ...
    def rotate2D(self, center: FMEPoint, angle: float) -> None: ...
    def scale(self, xScale: float, yScale: float, zScale: float) -> None: ...
    def setAppearanceReference(self, appearanceRef: int, front: bool) -> None: ...
    def setMeasure(self, measureValues: list[float], measureName: str) -> None:
        """Sets the default measure of this triangle strip to the given values.

        Create the measure if it doesn't already exist. If 'measureName' is supplied,
        this method sets the given measure to 'measureValues', or creates the
        measure if it doesn't already exist. The size of 'measureValues' must be
        exactly equal to the value returned by numPoints().

        Args:
          measureValues (list[float]): The values of the default measure.
          measureName (str): (Optional) The name of the measure whose value is to
              be set, or created.
        """
    def setMeasureAt(self, index: int, measureValue: float, measureName: str) -> None:
        """Sets the value of the default measure at the 'index'.

        If 'measureName' is supplied, this method sets the given measure of the
        point at 'index' to 'measureValue'. Creates the measure if it doesn't
        already exist and set the measures to all points other than the point at
        the given index to None. Return an error if the index is out of range.

         Args:
           index (int): The index of the measure to set.
           measureValue (float): The value of the measure to set.
           measureName (str): (Optional) The name of the measure whose value is
              to be set, or created.

         Raises:
           FMEException: An exception is raised if an error occurred
        """
    def setName(self, name: text_type) -> None: ...
    def setTrait(
        self,
        traitName: str,
        traitValue: bool | int | float | text_type | bytearray | bytes,
    ) -> None: ...
    def setTraitNullWithType(self, traitName: str, traitType: int) -> None: ...
    def sideExists(self, front: bool) -> bool: ...
