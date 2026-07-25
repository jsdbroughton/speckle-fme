from typing import overload
from six import string_types, text_type
from fmeobjects.features import FMEFeature
from fmeobjects.geometries.points import FMEPoint

# removeTraits() Constants¶
kFME_RecurseAll: int
kFME_RecurseSome: int

class FMEGeometryIterator:
    """FMEGeometryIterator Class

    FMEGeometryIterator should not be constructed directly. Instead, use the
    iterator semantics of FMEAggregate to get an FMEGeometryIterator which can
    be used to iterate over its geometries.
    """

    def __init__(self) -> None:
        """Initialize self. See help(type(self)) for accurate signature."""

class FMEGeometry:
    """FME Geometry Class"""

    def __init__(self) -> None:
        """Default FMEMesh constructor.

        Returns:
            (FMEMesh): An instance of a Mesh geometry object.
        """
    def boundingBox(self) -> tuple[tuple[float]]:
        """Returns the bounding box of the mesh.

        Returns:
            (tuple[tuple[float]]): The bounding box of the Geometry, in the
                form ((minx, miny), (maxx, maxy)).
        """
    def boundingCube(self) -> tuple[tuple[float]]:
        """Returns the bounding cube of the mesh.

        Returns:
            (tuple[tuple[float]]): The bounding cube of the Geometry, in the
                form ((minx, miny, minz), (maxx, maxy, maxz)).
        """
    def bounds(self) -> tuple[FMEPoint, FMEPoint]:
        """Returns the bounds of the mesh.

        Returns:
            (tuple[FMEPoint]): The min point and max point of the bounds.
                None is returned if the geometry contains no points.
        """
    def clearMeasures(self) -> None:
        """Clears all measures from the mesh."""
    def copyAttributesFromFeature(
        self,
        sourceFeature: FMEFeature,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None:
        """Copies all the attributes from the given feature to traits on this
        geometry, if they match the (optional) regular expression.

        Args:
            sourceFeature (FMEFeature): The source feature to copy attributes from.
            overwriteExisting (bool): Existing traits will be overwritten only
                if overwriteExisting is True.
            regexp (str):  (Optional) The regular expression to match the
                attributes against. If regexp is not specified, then all
                attributes will be copied.
            prefix (str): (Optional) The prefix is put on all the trait names as
                they are copied. If it is not specified, a prefix will not be
                added to the trait names.
        """
    def copyNameFromGeometry(self, sourceGeometry: FMEGeometry) -> None:
        """Copies the name from the given geometry to this geometry.

        If 'sourceGeometry's name is blank or None, this geometry's name will
        become None.

        Args:
            sourceGeometry (FMEGeometry): The source geometry to copy the name from.
        """
    def copyTraitsFromGeometry(
        self,
        sourceGeometry: FMEGeometry,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None:
        """Copies all the traits from the given geometry that match the (optional)
        regular expression.

        Args:
            sourceGeometry (FMEGeometry): The source geometry to copy traits from.
            overwriteExisting (bool): Existing traits will be overwritten only
                if overwriteExisting is True.
            regexp (str):  (Optional) The regular expression to match the traits
                against. If regexp is not specified, then all traits will be copied.
            prefix (str): (Optional) The prefix is put on all the trait names as
                they are copied. If it is not specified, a prefix will not be
                added to the trait names.
        """
    def copyTraitsToFeature(
        self,
        destFeature: FMEFeature,
        overwriteExisting: bool,
        regexp: str,
        prefix: str,
    ) -> None:
        """Copies all the traits from this geometry to attributes on the given
        feature, if they match the (optional) regular expression

        Args:
            destFeature (FMEFeature): The destination feature to copy traits to.
            overwriteExisting (bool): Existing traits will be overwritten only
                if overwriteExisting is True.
            regexp (str):  (Optional) The regular expression to match the traits
                against. If regexp is not specified, then all traits will be copied.
            prefix (str): (Optional) The prefix is put on all the trait names as
                they are copied. If it is not specified, a prefix will not be
                added to the trait names.
        """
    def deleteName(self) -> bool:
        """Deletes the name of the geometry.

        If a name existed prior to this call then True is returned; otherwise
        False is returned.

        Returns:
            (bool): Returns a boolean indicating whether or not the name existed
                before deletion.
        """
    def force2D(self) -> None:
        """Reduces the geometry to be 2D."""
    def force3D(self, newZ: float) -> None:
        """This sets the geometry's dimension to 3D.

        All Z values are set to the value passed in, even if the geometry is
        already 3D.

        Args:
            newZ (float): The z coordinate to use for the new geometry.
        """
    def getArea(self) -> float:
        """Area calculation.

        Returns:
            (float): The calculated area.
        """
    def getMeasureNames(self) -> tuple[str]:
        """Retrieve the names of the measures on this geometry.

        Returns:
            (tuple[string]): Return a tuple storing the names of the measures on
                this geometry. This will return an empty tuple if there are no
                measures. For FMEAggregate, FMEMultiSurface, and
                FMECompositeSurface, this will return the union of all measure
                names of all of its parts.
        """
    def getName(self) -> text_type | None:
        """This routine retrieves the 'name' of this geometry as a six.text_type.

        This will return None if it did not have a name associated with it.

        Returns:
            (six.text_type or None): The geometry's name.
        """
    def getTrait(
        self,
        traitName: str,
    ) -> bool | int | float | string_types | bytearray | bytes | None:  # type: ignore
        """Retrieves the geometry trait value of the specified trait name.

        Null trait values will be returned as an empty string.
        Binary blob traits are returned as a bytearray.

        Args:
            traitName (str): The name of the geometry trait.

        Returns:
            (bool or int or float or six.string_types or bytearray or bytes or None):
                The trait value.

        Raises:
            FMEException: An exception is raised if there was a problem in
                retrieving the trait value.
        """
    def getTraitNames(self) -> tuple[str]:
        """Retrieves the names of the traits on this geometry.

        Returns:
            (tuple[str]): Return a tuple storing the names of the traits on this
                geometry. This will return an empty tuple if there are no traits.
                For all collections and containers, this will only return the
                names of traits on the outermost object only.
        """
    def getTraitNullMissingAndType(self, traitName: str) -> tuple[bool, bool, int]:
        """This method returns a tuple of a boolean, indicating if the trait is
        null, a boolean, indicating if the trait is missing, and an integer
        representing the type of the trait.

        The first boolean is True if 'traitName' maps to a null trait value on
        the geometry. Otherwise it is False. The second boolean is True if
        'traitName' maps to a no value on the geometry. Otherwise it is False.
        If the trait is absent, FME_ATTR_UNDEFINED is returned for the type.

        The possible trait types are FME_ATTR_UNDEFINED, FME_ATTR_BOOLEAN,
        FME_ATTR_INT8, FME_ATTR_UINT8, FME_ATTR_INT16, FME_ATTR_UINT16,
        FME_ATTR_INT32, FME_ATTR_UINT32, FME_ATTR_REAL32, FME_ATTR_REAL64,
        FME_ATTR_REAL80, FME_ATTR_STRING, FME_ATTR_ENCODED_STRING, FME_ATTR_INT64,
        FME_ATTR_UINT64.

        Args:
            traitName (str): The trait's name.

        Returns: tuple[bool, bool, int]: A tuple of 2 boolean values the first
            indicating whether or not the value of the trait is null, the second
            indicating whether or not the trait is missing, and an integer
            representing the trait type.
        """
    def getTraitType(self, traitName: str) -> int:
        """This method returns the type of the trait.

        If the trait cannot be found, FME_ATTR_UNDEFINED will be returned.

        Returns one of  FME_ATTR_UNDEFINED, FME_ATTR_BOOLEAN, FME_ATTR_INT8,
        FME_ATTR_UINT8, FME_ATTR_INT16, FME_ATTR_UINT16, FME_ATTR_INT32,
        FME_ATTR_UINT32, FME_ATTR_REAL32, FME_ATTR_REAL64, FME_ATTR_REAL80,
        FME_ATTR_STRING, FME_ATTR_ENCODED_STRING, FME_ATTR_INT64, FME_ATTR_UINT64.

        Args:
            traitName (str): The trait's name.

        Returns:
            (int): The type of the trait.
        """
    def hasMeasures(self) -> bool:
        """Check if this geometry or any sub part of this geometry has measures.

        Returns:
            (bool): True if this geometry or any sub part of this geometry has
                measures, False otherwise.
        """
    def hasName(self) -> bool:
        """Check if this geometry has a name.

        Returns:
            (bool): True if this geometry has a name, False otherwise.
        """
    def is3D(self) -> bool:
        """Check if this geometry is 3D.

        Returns:
            (bool): Returns True if the geometry is 3D and False otherwise. For
                FMENull, this method will always return True. For FMEAggregate,
                FMEMultiPoint, FMEMultiArea, FMEMultiText and FMEMultiCurve,
                this method will return True if any one of the sub-parts is 3D.
                If the collection is empty or all of its members are 2D, this
                method will return False.
        """
    def isCollection(self) -> bool:
        """Check if the geometry is an aggregate or multi-part collection.

        Returns:
            (bool): True if the geometry is an aggregate or multi-part collection,
                False otherwise.
        """
    def measureExists(self, measureName: str) -> bool:
        """CReturns True if the specified measure exists and False otherwise.

        If the 'measureName' parameter is not specified then the default measure
        is checked.

        Returns:
            (bool): Boolean indicating whether or not the measure exists.
        """
    def removeMeasure(self, measureName: str) -> None:
        """Removes the measure with name 'measureName' if supplied, or the
        default measure, if there is one.

        Args:
            measureName (str): (Optional) The name of the measure to remove.
        """
    def removeTraits(self, regexp: str) -> None:
        """Removes all traits that match the given regular expression.

        This method has 4 modes:
            Remove all traits at the top level: regex == NULL
            Remove some traits at the top level: regex == <string>
            Remove all traits at all levels: regex == kFME_RecurseAll
            Remove some traits at all levels: regex == kFME_RecurseSome <string>

        For example, specifying regex == NULL for a multi-surface will remove
        all traits at the root level of the multi-surface, whereas specifying
        regex == kFME_RecurseSome <string> will remove all traits from all
        levels of the multi surface that match <string>. If <string> is an
        illegal regular expression, no traits will be removed.
        """
    def renameMeasure(self, oldMeasureName: str, newMeasureName: str) -> None:
        """Renames the measure with name 'oldMeasureName' to 'newMeasureName'.

        Args:
            oldMeasureName (str): The name of the measure to rename.
            newMeasureName (str): The new name of the measure.
        """
    def setName(self, name: text_type) -> None:
        """Sets the geometry's name with a six.text_type.

        By supplying a blank name as input, this method will act as deleteName().

        Args:
            name (six.text_type): The name to set.
        """
    def setTrait(
        self,
        traitName: str,
        traitValue: bool | int | float | text_type | bytearray | bytes,
    ) -> None:
        """Sets a geometry trait with the specified value.

        If the geometry trait already exists, its value and type will be changed.
        The following type numeric mappings are used:
            PyInt ==> FME_Int32
            PyFloat ==> FME_Real64
            PyLong ==> FME_Int64

        For Python 2.7, strings can be input as one of two possible types:
        system encoded strings or unicode strings. Binary values are to be
        specified as bytearray values or bytes values for Python 3 and as
        bytearray values for Python 2.7.

        Args:
            traitName (str): The name of the trait to set.
            traitValue (bool or int or float or six.text_type or bytearray or bytes): The value of the trait.
        """
    def setTraitNullWithType(self, traitName: str, traitType: int) -> None:
        """This method supplies a null trait value with a type to the geometry.

        If a trait with the same name already exists, it is overwritten.

        Trait type must be one of FME_ATTR_UNDEFINED, FME_ATTR_BOOLEAN,
        FME_ATTR_INT8, FME_ATTR_UINT8, FME_ATTR_INT16, FME_ATTR_UINT16,
        FME_ATTR_INT32, FME_ATTR_UINT32, FME_ATTR_REAL32, FME_ATTR_REAL64,
        FME_ATTR_REAL80, FME_ATTR_STRING, FME_ATTR_ENCODED_STRING, FME_ATTR_INT64,
        FME_ATTR_UINT64.

        Args:
            traitName (str): The name of the trait to set.
            traitType (int): The type of the trait.
        """

class FMENull(FMEGeometry):
    """FME Null Class"""

    def __init__(self, null: FMENull) -> None:
        """Create a copy of the passed in Null geometry object.

        Args:
            mesh (FMENull): The Null geometry object to create a copy of.

        Returns:
            (FMENull): An instance of a Null Geometry object.
        """

class FMEAggregate(FMEGeometry):
    """FME Aggregate Class"""

    @overload
    def __init__(self) -> None:
        """Create an instance of an Aggregate geometry object.

        Returns:
            (FMEAggregate): An instance of a Aggregate Geometry object.
        """
    @overload
    def __init__(self, aggregate: FMEAggregate) -> None:
        """Create a copy of the passed in Aggregate geometry object.

        Args:
            mesh (FMEAggregate): The Aggregate geometry object to create a copy of.

        Returns:
            (FMEAggregate): An instance of a Aggregate Geometry object.
        """
    def appendPart(self, geometry: FMEGeometry) -> None:
        """This appends the geometry to the aggregate.

        If None is passed in, nothing will be appended. Note that the geometries
        stored in an aggregate may have different dimensions. Calling this method
        will implicitly apply and clear any matrix associated with this aggregate.

        Args:
            geometry (FMEGeometry): The geometry to be appended.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def appendPartInLocalCoordinates(self, geometry: FMEGeometry) -> None:
        """This appends the geometry to the aggregate in local coordinates.

        If None is passed in, nothing will be appended. Note that the geometries
        stored in an aggregate may have different dimensions. Calling this method
        will leave any matrix associated with the aggregate intact, meaning the
        new part will have any matrix applied.

        Args:
            geometry (FMEGeometry): The geometry to be appended.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def appendParts(self, aggregate: FMEAggregate) -> None:
        """This appends the aggregate of geometries passed in to the aggregate.

        If None is passed in, nothing will be appended. Calling this method will
        implicitly apply and clear any matrix associated with this aggregate.

        Args:
            aggregate (FMEAggregate): The aggregate of geometries to be appended.


        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getAppearanceReference(self, front: bool) -> int:
        """This method returns the appearance reference within the Library associated with this aggregate.

        The 'front' parameter controls whether this query should return the
        front or the back appearance reference. Both can be fetched independently.
        If this aggregate is a regular aggregate with no geometry instance, a
        FMEException will be thrown.

        Args:
            front (bool): Boolean indicating whether the appearance reference
                should be retrieved for the front or back of the aggregate.

        Returns:
            (int): The unique appearance reference for this appearance.
        """
    def getGeometryDefinitionReference(self) -> int | None:
        """This method will get the geometry definition reference associated with
        this aggregate, if this aggregate is a geometry instance.

        If this aggregate is a regular aggregate with no geometry instance, None
        will be returned.

        Returns:
            (int): The geometry definition reference, or None.
        """
    def getGeometryInstanceLocalOrigin(self) -> list[list[float]] | None:
        """This method retrieves the local origin associated with the geometry
        instance, if this aggregate is a geometry instance.

        This method will return None if the aggregate is a regular aggregate.

        Returns:
            (list[list[float]]): The local origin, formatted (ddd), or None.
        """
    def getGeometryInstanceMatrix(self) -> list[list[float]] | None:
        """This method retrieves the geometry instance transformation matrix
        associated with the geometry instance, if this aggregate is a geometry
        instance.

        This method will return None if the aggregate either contains
        no such matrix or is a regular aggregate.

        Returns:
            (list[list[float]]): The geometry instance transformation matrix,
                formatted [[dddd][dddd][dddd]], or None.
        """
    def getMultipleGeometryFlag(self) -> bool:
        """This method determines if the aggregate contains a MultipleGeometry,
        that is, whether the aggregate is structured in a way such that each part
        is its own geometry separate from the other parts in the aggregate.

        As a result, it is possible for an aggregate of 1 part to return true
        since it is about the structure of the aggregate, and not the content.

        Returns:
            (bool): Returns True if the aggregate contains a multiple geometry
            and False otherwise.
        """
    def getPartAt(self, index: int) -> FMEGeometry | None:
        """This method returns the geometry at the given index.

        None is returned if the index is out of range. For an aggregate with a
        transformation matrix, the transformed geometry is returned.

        Args:
            index (int): The index of the geometry to be returned.

        Returns:
            (FMEGeometry): The geometry at the given index. Note: This method
                returns a terminal geometry type of the FMEGeometry; i.e. one of the
                leaf classes in the FMEGeometry inheritance graph. For example, a
                FMEPoint is returned if the geometry truly is a point.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getPartAtInLocalCoordinates(self, index: int) -> FMEGeometry | None:
        """This method returns the geometry at the given index.

        None is returned if the index is out of range. For an aggregate with a
        transformation matrix, it will NOT be applied to the part.

        Args:
            index (int): The index of the geometry to be returned.

        Returns:
            (FMEGeometry): The geometry at the given index. Note: This method
                returns a terminal geometry type of the FMEGeometry; i.e. one
                of the leaf classes in the FMEGeometry inheritance graph. For
                example, a FMEPoint is returned if the geometry truly is a point.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def getTransformationMatrix(self) -> list[list[float]]:
        """Gets this aggregate's transformation matrix.

        If the aggregate does not have such a matrix, an identity matrix is
        returned. Only the top three rows of the matrix will be returned, as the
        bottom row is always [ 0 0 0 1 ].

        Returns:
            (list[list[float]]): The aggregate's tranformation matrix,
                formatted [[dddd][dddd][dddd]].
        """
    def hasGeometryInstance(self, recursive: bool) -> bool:
        """This method returns True if this aggregate contains an instance of a
        geometry definition.

        If the parameter recursive is set to False, it will only test this
        aggregate itself. If 'recursive' is equal to True, then this method will
        return True if any part contained in this aggregate at any level is a
        geometry instance.

        Args:
            recursive (bool): To recurse or not.

        Returns:
            (bool): Whether there is geometry instance.
        """
    def hasTransformationMatrix(self) -> bool:
        """This method returns True if this aggregate has a transformation
        matrix.

        Returns:
            (bool): Whether there is a transformation matrix.
        """
    def isAMulti(self) -> bool:
        """This method determines if the aggregate's parts conform to a
        FMEMultiCurve, FMEMultiArea, or FMEMultiText, representation.

        Returns:
            (bool): This means that it will only return True if the aggregate contains:
                Arcs, Lines, Paths, and nothing else.

                Polygons, Ellipses, Donuts, and nothing else.

                Text objects and nothing else.

                Points and nothing else. This returns false for empty aggregates.
        """
    def isSimpleAggregate(self) -> bool:
        """This method determines if the aggregate is a simple aggregate.

        i.e. that none of its geometries are an Aggregate or Multi.

        Returns:
            (bool): Whether this aggregate is a simple aggregate.
        """
    def numParts(self) -> int:
        """This method returns the number of parts in the aggregate.

        Returns:
            (int): The number of parts in the aggregate.
        """
    def offset(self, point: FMEPoint) -> None:
        """Offsets the geometry by the coords specified by 'point'.

        The offset will be applied to the transformation matrix associated with
        this aggregate. If the aggregate has no matrix, a new matrix will be created.

        Args:
            point (FMEPoint): The point to offset the coordinates of the geometry by.
        """
    def removeLastPart(self) -> FMEGeometry | None:
        """This removes and returns the last geometry of the aggregate.

        If there are no geometries in the aggregate, it will return None. Calling
        this method will implicitly apply and clear any matrix associated with
        this aggregate.

        Returns:
            (FMEGeometry): The last geometry of the aggregate. Note: This method
                returns a terminal geometry type of the FMEGeometry; i.e. one of
                the leaf classes in the FMEGeometry inheritance graph. For
                example, a FMEPoint is returned if the geometry truly is a point.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def removeTransformationMatrix(self) -> None:
        """Removes this aggregate's transformation matrix."""
    def rotate2D(self, center: FMEPoint, angle: float) -> None:
        """The angle is CCW up from the horizontal and is measured in degrees.

        The rotation will be applied to the transformation matrix associated
        with this aggregate. If the aggregate has no matrix, a new matrix will
        be created.

        Args:
            center (FMEPoint): The center of the rotation.
            angle (float): The angle of the rotation in degrees

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def scale(self, xscale: float, yscale: float, zscale: float) -> None:
        """Applies a scale factor to the aggregate.

        The scale factor will be applied to the transformation matrix associated
        with this aggregate. The 'zscale' is ignored if geometry is 2D. If the
        aggregate has no matrix, a new matrix will be created.

        Args:
            xscale (float): The x-scale factor.
            yscale (float): The y-scale factor.
            zscale (float): The z-scale factor.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setAppearanceReference(self, appearanceRef: int, front: bool) -> None:
        """This method associates an appearance within the Library with this aggregate.

        This is done by passing in the unique appearance reference for this
        appearance. Subsequent calls to this method on the same side, will
        override the previous appearance used with the new appearance passed in.

        An appearance reference of '0' represents the default appearance.
        Interpretation of the default appearance is left to the consumer of this
        geometry. When set at this FMEAggregate level, the appearance represents
        the default appearance to apply when the contained surfaces use the
        default appearance instead of a specific appearance. Contained surfaces
        may be found within nested aggregates, geometry instances that reference
        geometries containing surfaces, or as surfaces or multi-surfaces.

        The second parameter controls whether this action should take place on
        the front of the contained surfaces or the back. Both can be set
        independently. The 'appearanceRef' should be a valid reference to a
        definition stored in the FMELibrary. If the reference was not found in
        the library, it will still attach the reference to the instance, but
        will throw a FMEException. This is an unhealthy situation as it
        represents a 'dangling reference'.

        Args:
            appearanceRef (int): The unique appearance reference for this appearance.
            front (bool): Whether the appearance is for the front or back of the
                geometry.

        Raises:
            FMEException: An exception is raised if an error occurred or the
            reference was not found in the library and a dangling reference was
            attached.
        """
    def setGeometryDefinitionReference(self, gdReference: int) -> None:
        """This method sets the geometry definition reference of this aggregate.

        If this aggregate is not currently a geometry instance, this call will
        cause the aggregate to destroy all owned parts and turn the aggregate
        into a geometry instance.

        If 'gdReference' reference was not found in the library, it will still
        attach the reference to the instance, but will this is an unhealthy
        situation as it represents a 'dangling reference' and the user should
        decide to remedy this by either adding a Geometry Definition with that
        exact reference to the library, or else remove the reference from this
        geometry instance.

        Args:
            gdReference (int): A valid geometry definition reference to a
            geometry definition stored in the FMELibrary.

        Raises:
            FMEException: An exception is raised if an error occurred or the
              reference was not found in the library and a dangling reference
              was attached.
        """
    def setGeometryInstanceLocalOrigin(self, x: float, y: float, z: float) -> None:
        """Sets the local origin of the geometry instance.

        If this aggregate is not currently a geometry instance, this call will
        cause the aggregate to destroy all owned parts and turn the aggregate
        into a geometry instance. The local origin is the origin from which the
        geometry instance transformation matrix is applied. The default local
        origin is (0,0,0).

        Args:
            x (float): The x-coordinate of the local origin.
            y (float): The y-coordinate of the local origin.
            z (float): The z-coordinate of the local origin.
        """
    def setGeometryInstanceMatrix(self, matrix: list[list[float]]) -> None:
        """Sets the transformation matrix of the geometry instance.

        If this aggregate is not currently a geometry instance, this call will
        cause the aggregate to destroy all owned parts and turn the aggregate
        into a geometry instance. The transformation matrix is applied to the
        geometry definition from the local origin to obtain the instantiated geometry.

        Args:
            matrix (list[list[float]]): The geometry instance transformation
                matrix, formatted [[dddd][dddd][dddd]].
        """
    def setMultipleGeometryFlag(self, isMultiple: bool) -> None:
        """This method sets whether the aggregate contains a MultipleGeometry.

        That is, whether the aggregate is structured in a way such that each
        part is its own geometry separate from the other parts in the aggregate.

        Args:
            isMultiple (bool): True if the aggregate contains a MutlipleGeometry
        """
    def setTransformationMatrix(self, matrix: list[list[float]]) -> None:
        """Sets or replaces the transformation matrix of the aggregate.

        If this aggregate has no matrix, a new matrix will be created.
        Only three rows are expected in the input array, as a bottom row of
        [ 0 0 0 1 ] is assumed.

        Args:
            matrix (list[list[float]]): The transformation matrix, formatted
                [[dddd][dddd][dddd]].
        """
