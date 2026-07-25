from fmeobjects.geometries.general import FMEGeometry
from six import text_type

# Library Types
FME_LIB_APPEARANCE: int
FME_LIB_TEXTURE: int
FME_LIB_RASTER: int
FME_LIB_GEOMETRY_DEFINITION: int

# Mapper Types
FME_MAPPER_ALPHA_MAP: int
FME_MAPPER_ALPHA_MASK: int
FME_MAPPER_AMBIENT_MAP: int
FME_MAPPER_AMBIENT_MASK: int
FME_MAPPER_DIFFUSE_MAP: int
FME_MAPPER_DIFFUSE_MASK: int
FME_MAPPER_EMISSIVE_MAP: int
FME_MAPPER_EMISSIVE_MASK: int
FME_MAPPER_SHININESS_MAP: int
FME_MAPPER_SHININESS_MASK: int
FME_MAPPER_SPECULAR_MAP: int
FME_MAPPER_SPECULAR_MASK: int
FME_MAPPER_BUMP_MAP: int
FME_MAPPER_BUMP_MASK: int

# Texture Wrap Methods
FME_TEXTURE_REPEAT_BOTH: int
FME_TEXTURE_CLAMP_BOTH: int
FME_TEXTURE_CLAMP_U_REPEAT_V: int
FME_TEXTURE_REPEAT_U_CLAMP_V: int
FME_TEXTURE_MIRROR: int
FME_TEXTURE_BORDER_FILL: int
FME_TEXTURE_NONE: int

class FMETexture:
    """FME Texture Class"""

    def __init__(self) -> None:
        """Create an instance of a blank texture object."""
    def clone(self) -> "FMETexture":
        """Clone the texture object.

        Returns:
            FMETexture: A new texture object.
        """
    def getBorderColors(self) -> tuple[float, float, float]:
        """This routine retrieves the border color of this Texture.

        The color is a vector in r g b color space with values between 0.0 and 1.0.
        This will return None if it did not have a border color set.

        Returns:
            tuple[float,float,float]: The border color, formatted (ddd) (r, g, b).
        """
    def getCenter(self) -> tuple[float, float] | None:
        """This routine retrieves the center associated with the texture.

        This will return None if the center is the default center of (0,0).
        The center is only used for shearing and rotation.

        Returns:
            tuple[float,float]: The center, formatted (dd) (u, v).
        """
    def getOffset(self) -> tuple[float, float] | None:
        """This routine retrieves the offset associated with the texture.

        This will return None if the offset is the default offset of (0,0).
        The offset is only used for translation.

        Returns:
            tuple[float,float]: The offset, formatted (dd) (u, v).
        """
    def getRotation(self) -> int | None:
        """This routine retrieves the rotation angle associated with the texture.

        The angle is stored in degrees CCW from the x-axis, and is by default 0.
        Rotation is centered according to the Center variable. This return None
        if the scaling is the default angle of 0.

        Returns:
            int: The rotation, in degrees.
        """
    def getScaling(self) -> tuple[float, float] | None:
        """This routine retrieves the scaling factors associated with the texture.

        This will return None if the scaling is the default scaling of (1,1).

        Returns:
            tuple[float,float]: The scaling factors, formatted (dd) (u, v), or None.
        """
    def getShear(self) -> tuple[float, float] | None:
        """This routine retrieves the shear factors associated with the texture.

        Shearing is centered according to the Center variable. This will return
        None if the shearing is the default shearing of (0,0).

        Returns:
            tuple[float,float]: The shear factors, formatted (dd) (u, v), or None.
        """
    def getTextureWrap(self) -> int:
        """This routine retrieves the wrapping style associated with the texture.

        The style is stored as a Texture Wrap value, and is by default
        FME_TEXTURE_REPEAT_BOTH, which results in the texture being tiled in
        both the u and v direction.

        Returns:
            int: The texture wrap mode.
        """
    def getTransformationMatrix(self) -> list[list[float]]:
        """This routine retrieves the transformation matrix associated with the texture.

        It is a combination of the rotation, scaling, shear and translation factors,
        applied in that order.

        Returns:
            list[list[float]]: The texture's tranformation matrix, formatted [[ddd][ddd]].
        """
    def getTransformationMatricReverse(self) -> list[list[float]]:
        """This routine retrieves the texture transformation matrix associated with
        the texture in the reverse order and inverse of each operation, that
        consists of offset, negative shear, 1 / scale, and negative rotation in that order.

        This matrix can be used to transform the texture coordinates that are
        associated with this texture.

        Returns:
            list[list[float]]: The texture's tranformation matrix, formatted [[ddd][ddd]].
        """
    def hasNonIdentityTransform(self) -> bool:
        """This routine returns True if any non-default texture transform factors are set.

        The default texture transform matrix is identity and this returns False.

        Returns:
            bool: Returns True if any non-default texture transform factors are
                set, or False otherwise.
        """
    def setBorderColors(self, r: float, g: float, b: float) -> None:
        """This routine sets the border color of this Texture.

        The color values should be in r g b color space with values between 0.0
        and 1.0. The border color is used only if the Texture Wrap value is set
        to FME_TEXTURE_BORDER_FILL. Setting the border color will also set the
        Texture Wrap value to FME_TEXTURE_BORDER_FILL. Setting the any color
        value to a negative value will remove the color from this Texture and the
        Texture Wrap value will be reset to FME_TEXTURE_REPEAT_BOTH. If the
        underlying raster is single channel, the gray-scale equivalent border
        color will be calculated.

        Args:
            r (float): The red value.
            g (float): The green value.
            b (float): The blue value.
        """
    def setCentre(self, u: float, v: float) -> None:
        """This routine sets the center associated with the texture.

        he default center for a texture is (0,0). The center is only used for
        shearing and rotation.

        Args:
            u (float): The u value.
            v (float): The v value.
        """
    def setOffset(self, u: float, v: float) -> None:
        """This routine sets the offset associated with the texture.

        The default offset for a texture is (0,0).

        Args:
            u (float): The u value.
            v (float): The v value.
        """
    def setRotation(self, angle: float) -> None:
        """This routine sets the rotation angle associated with the texture.

        Rotation is centered according to the Center variable. The angle is
        stored in degrees CCW from the x-axis, and is by default 0.

        Args:
            angle (int): The angle, in degrees.
        """
    def setScaling(self, u: float, v: float) -> None:
        """This routine sets the scaling factors associated with the texture.

        The default scaling for a texture is (1,1).

        Args:
            u (float): The u value.
            v (float): The v value.
        """
    def setShear(self, u: float, v: float) -> None:
        """This routine sets the shear factors associated with the texture.

        The default shear for a texture is (0,0).

        Args:
            u (float): The u value.
            v (float): The v value.
        """
    def setTextureWrap(self, wrapStyle: int) -> None:
        """This routine sets the wrapping style associated with the texture.

        The style is stored as a Texture Wrap value. If the style is set to
        FME_TEXTURE_BORDER_FILL, the default border color of black (0,0,0), will
        be set. If the style is set to something other than FME_TEXTURE_BORDER_FILL,
        the border color will be removed from the texture.

        Args:
            wrapStyle (int): The wrapping style associated with the texture.
                One of : FME_TEXTURE_BORDER_FILL, FME_TEXTURE_REPEAT_BOTH,
                FME_TEXTURE_CLAMP_BOTH, FME_TEXTURE_CLAMP_U_REPEAT_V,
                FME_TEXTURE_REPEAT_U_CLAMP_V, FME_TEXTURE_MIRROR, FME_TEXTURE_NONE.
        """
    def setTransformationMatrix(self, matrix: list[list[float]]) -> None:
        """This routine sets the transformation matrix associated with the texture.

        The shear, offset, rotation and will be calculated from the matrix so
        that when rotation, shear, scale and translation are applied in order,
        it is the equivalent of the input matrix. If the non-translation component
        of the matrix has a zero determinant or m[0][0] = 0, the matrix will not
        be used and existing parameters will remain unchanged.

        Args:
            matrix (list[list[float]]): The transformation matrix,
                formatted [[ddd][ddd]].
        """

class FMELibraryIterator:
    """FME Library Iterator Class

    FMELibraryIterator should not be constructed directly. Instead, use the
    iterator semantics of FMELibrary to get an FMELibraryIterator which can be
    used to iterate over its librarys."""

    def __init__(self) -> None:
        """Constructor for FMELibraryIterator."""
    def getAppearance(self) -> FMEAppearance | None:
        """This method returns a copy of the current shared object as an appearance
        if getType() returns FME_LIB_APPEARANCE. Otherwise, it returns None.

        Returns:
            FMEAppearance: The current object's appearance.
        """
    def getAsTexture(self) -> FMETexture | None:
        """This method returns a copy of the current shared object as a texture
        if getType() returns FME_LIB_TEXTURE. Otherwise, it returns None.

        Returns:
            FMETexture: The current object's texture.
        """
    def getReference(self) -> int:
        """Returns the object's reference from the FMELibrary.

        Returns:
            int: The current object's reference.
        """
    def getType(self) -> int:
        """Returns the type of the current object.

        Returns:
            int: The object's type. Must be either: FME_LIB_APPEARANCE,
                FME_LIB_TEXTURE, FME_LIB_RASTER, or FME_LIB_GEOMETRY_DEFINITION.
        """

class FMELibrary:
    """FME Library Class

    Contains shared objects used by multiple features. Appearances and textures
    for all features are stored in this library."""

    def __init__(self) -> None:
        """Constructor for FMELibrary."""
    def addAppearance(self, appearance: FMEAppearance) -> int:
        """This routine adds the appearance object to the Library.

        If the appearance passed in is None, this appearance is will not be added
        to the Library. There is no checking for duplicates when adding an
        appearance. This call will always add the appearance to the Library,
        even if an identical appearance already exists therein. If the addition
        is successful, the method returns a unique appearance reference 'key' that
        is associated with the appearance. If there are any errors in operation,
        an exception is raised. If the appearance is successfully added to the
        library, the library consumes the appearance.

        Args:
            appearance (FMEAppearance): The appearance to add.

        Returns:
            int: The unique appearance reference 'key'.

        Raises:
            FMEException: If there is an error adding the appearance.
        """
    def addGeometryDefinition(self, geometryDef: FMEGeometry) -> int:
        """This routine adds the geometry definition object to the Library.

         If the Geometry Definition passed in is None, this Geometry Definition
         will not be added to the Library. There is no checking for duplicates
         when adding a Geometry Definition. This call will always add the Geometry
         Definition to the Library, even if an identical one already exists therein.
         If there are any errors in operation an exception is raised. If the
         addition is successful, a unique geometry definition reference 'key' that
         is associated with the Geometry Definition is returned.

        Args:
            geometryDef (FMEGeometry): The geometry definition to add.

        Returns:
            int: The unique geometry definition reference 'key'.

        Raises:
            FMEException: If there is an error adding the geometry definition.
        """
    def addTexture(self, texture: FMETexture) -> int:
        """This routine adds the texture object to the Library.

        If the texture passed in is None, this texture is will not be added to
        the Library. There is no checking for duplicates when adding a texture.
        This call will always add the texture to the Library, even if an identical
        texture already exists therein. If there are any errors in operation, an
        exception is raised. If the addition is successful, the method returns a
        unique texture reference 'key' that is associated with the texture.

        Args:
            texture (FMETexture): The texture to add.

        Returns:
            int: The unique texture reference 'key'.

        Raises:
            FMEException: If there is an error adding the texture.
        """
    def deleteAppearance(self, appearanceReference: int) -> None:
        """Deletes the appearance with the 'appearanceReference' index.

        Throws an exception if the current shared object is not of appearance type.

        Args:
            appearanceReference (int): The unique appearance reference 'key'.

        Raises:
            FMEException: If there is an error deleting the appearance.
        """
    def deleteGeometryDefinition(self, geometryDefinitionReference: int) -> None:
        """Deletes the geometry definition with the 'geometryDefinitionReference' index.

        Throws an exception if the current shared object is not of geometry definition type.

        Args:
            geometryDefinitionReference (int): The unique geometry definition reference 'key'.

        Raises:
            FMEException: If there is an error deleting the geometry definition.
        """
    def deleteTexture(self, textureReference: int) -> None:
        """Deletes the texture with the 'textureReference' index.

        Throws an exception if the current shared object is not of texture type.

        Args:
            textureReference (int): The unique texture reference 'key'.

        Raises:
            FMEException: If there is an error deleting the texture.
        """
    def getAppearanceCopy(self, appearanceReference: int) -> FMEAppearance | None:
        """This routine returns a copy of the referenced Appearance object from the Library.

        If there is no such Appearance in the Library, None is returned.

        Args:
            appearanceReference (int): The unique appearance reference.

        Returns:
            FMEAppearance: The copy of the appearance.
        """
    def getGeometryDefinitionCopy(self, geometryDefinitionReference: int) -> FMEGeometry or None:
        """This routine returns a copy of the referenced Geometry Definition object from the Library.

        If there is no such Geometry Definition in the Library, None is returned.

        Args:
            geometryDefinitionReference (int): The unique geometry definition reference.

        Returns:
            FMEGeometry: The copy of the geometry definition.
        """
    def getTextureCopy(self, textureReference: int) -> FMETexture | None:
        """This routine returns a copy of the referenced Texture object from the Library.

        If there is no such Texture in the Library, None is returned.

        Args:
            textureReference (int): The unique texture reference.

        Returns:
            FMETexture: The copy of the texture.
        """
    def hasEntry(self, reference: int) -> bool:
        """This routine returns True if the Library has an entry with the 'reference' index.

        Args:
            reference (int): The unique reference.

        Returns:
            bool: True if the library has an entry with the reference.
        """
    def hasType(self, reference: int) -> int:
        """Returns the Library Type if library has an object with the specified reference number.

        Throws an exception if the supplied reference refers to an object without
        a valid object type, or if there is no object within the Library with the
        supplied reference number. Use hasEntry() to determine if the library
        contains the specified reference.

        Args:
            reference (int): The reference to search the library for.

        Returns:
            int: If the library has an object with the specified reference number
                the Library Type (FME_LIB_APPEARANCE, FME_LIB_TEXTURE, FME_LIB_RASTER,
                or FME_LIB_GEOMETRY_DEFINITION) is returned, otherwise an exception
                is thrown.

        Raises:
            FMEException: If there is an error determining the Library Type.
        """
    def replaceAppearance(self, appearanceReference: int, newAppearance: FMEAppearance) -> None:
        """Replaces the Appearance with a new one at index = 'appearanceReference'.

        A FMEException is thrown if 'newAppearance' is None, 'appearanceReference'
        is not a valid index ,or the existing shared object is not an appearance type.
        If the 'newAppearance' successfully replaces the existing appearance, the
        library consumes the 'newAppearance'.

        Args:
            appearanceReference (int): The unique appearance reference 'key'.
            newAppearance (FMEAppearance): The new appearance.

        Raises:
            FMEException: If there is an error replacing the appearance.
        """
    def replaceGeometryDefinition(self, geometryDefinitionReference: int, newGeometryDefinition: FMEGeometry) -> None:
        """Replaces the Geometry Definition with a new one at index = 'geometryDefinitionReference'.

        A FMEException is thrown if 'newGeometryDefinition' is None, 'geometryDefinitionReference'
        is not a valid index ,or the existing shared object is not a geometry definition type.
        If the 'newGeometryDefinition' successfully replaces the existing geometry definition, the
        library consumes the 'newGeometryDefinition'.

        Args:
            geometryDefinitionReference (int): The unique geometry definition reference 'key'.
            newGeometryDefinition (FMEGeometry): The new geometry definition.

        Raises:
            FMEException: If there is an error replacing the geometry definition.
        """
    def replaceTexture(self, textureReference: int, newTexture: FMETexture) -> None:
        """Replaces the Texture with a new one at index = 'textureReference'.

        A FMEException is thrown if 'newTexture' is None, 'textureReference'
        is not a valid index ,or the existing shared object is not a texture type.
        If the 'newTexture' successfully replaces the existing texture, the
        library consumes the 'newTexture'.

        Args:
            textureReference (int): The unique texture reference 'key'.
            newTexture (FMETexture): The new texture.

        Raises:
            FMEException: If there is an error replacing the texture.
        """

class FMEAppearance:
    """FME Appearance Class"""

    def __init__(self) -> None:
        """Create an instance of a blank appearance object"""
    def getAlpha(self) -> float | None:
        """This routine retrieves the alpha (1-transparency) of this Appearance.

        This will return None if it did not have a alpha associated with it.

        Returns:
            float: The alpha value
        """
    def getColorAmbient(self) -> tuple[float, float, float] | None:
        """This routine retrieves the ambient color of this Appearance as r g b values between 0.0 and 1.0.

        This will return None if it did not have an ambient color associated with it.

        Returns:
            tuple[float,float,float]: A tuple of the r g b values of the ambient color.
        """
    def getColorDiffuse(self) -> tuple[float, float, float] | None:
        """This routine retrieves the diffuse color of this Appearance as r g b values between 0.0 and 1.0.

        This will return None if it did not have a diffuse color associated with it.

        Returns:
            tuple[float,float,float]: A tuple of the r g b values of the diffuse color.
        """
    def getColorEmissive(self) -> tuple[float, float, float] | None:
        """This routine retrieves the emissive color of this Appearance as r g b values between 0.0 and 1.0.

        This will return None if it did not have an emissive color associated with it.

        Returns:
            tuple[float,float,float]: A tuple of the r g b values of the emissive color.
        """
    def getColorSpecular(self) -> tuple[float, float, float] | None:
        """This routine retrieves the specular color of this Appearance as r g b values between 0.0 and 1.0.

        This will return None if it did not have a specular color associated with it.

        Returns:
            tuple[float,float,float]: A tuple of the r g b values of the specular color.
        """
    def getMapperReference(self, mapperType: int) -> int | None:
        """This routine retrieves the texture reference of 'mapperType' of this Appearance.

        This will return None if it did not have a mapper of mapper type associated
        with it.

        Args:
            mapperType: The mapper type to retrieve the reference for. One of:
                FME_MAPPER_ALPHA_MAP, FME_MAPPER_ALPHA_MASK, FME_MAPPER_AMBIENT_MAP,
                FME_MAPPER_AMBIENT_MASK, FME_MAPPER_DIFFUSE_MAP, FME_MAPPER_DIFFUSE_MASK,
                FME_MAPPER_EMISSIVE_MAP, FME_MAPPER_EMISSIVE_MASK,
                FME_MAPPER_SHININESS_MAP, FME_MAPPER_SHININESS_MASK,
                FME_MAPPER_SPECULAR_MAP, FME_MAPPER_SPECULAR_MASK, FME_MAPPER_BUMP_MAP,
                OR FME_MAPPER_BUMP_MASK.

        Returns:
            int: The texture reference of 'mapperType' of this Appearance.
        """
    def getName(self) -> text_type | None:
        """This routine retrieves the 'name' of this Appearance as a six.text_type. This will return None if it did not have a name associated with it.

        Returns:
            str: The name of this Appearance.
        """
    def getShininess(self) -> float | None:
        """This routine retrieves the shininess of this Appearance.

        This will return None if it did not have a shininess associated with it.

        Returns:
            float: The shininess of this Appearance.
        """
    def getTextureReference(self) -> int | None:
        """This routine retrieves the main texture reference of this Appearance.

        This will return None if it did not have a texture reference associated with it.

        Returns:
            int: The texture reference of this Appearance.
        """
    def removeMapperReference(self, mapperType: int) -> None:
        """Remove the specified mapper reference form this appearance

        Args:
          The mapper reference to remove.
        """
    def removeTextureReference(self) -> None:
        """Remove the texture reference form this appearance"""
    def setAlpha(self, alpha: float) -> None:
        """This routine sets the alpha of this Appearance.

        The alpha should be a floating point value in the range of 0.0 to 1.0,
        where 0.0 represents a fully transparent color, and 1.0 represents a
        fully opaque color. Setting the value to negative will remove this
        property from this appearance.

        Args:
            alpha (float): The alpha value to set.
        """
    def setColorAmbient(self, r: float, g: float, b: float) -> None:
        """This routine sets the ambient color of this Appearance.

        The color values should be in r g b color space with values between 0.0
        and 1.0. Setting any color value to a negative value will remove the
        color from this Appearance.

        Args:
            r (float): The red value to set.
            g (float): The green value to set.
            b (float): The blue value to set.
        """
    def setColorDiffuse(self, r: float, g: float, b: float) -> None:
        """This routine sets the diffuse color of this Appearance.

        The color values should be in r g b color space with values between 0.0
        and 1.0. Setting any color value to a negative value will remove the
        color from this Appearance.

        Args:
            r (float): The red value to set.
            g (float): The green value to set.
            b (float): The blue value to set.
        """
    def setColorEmissive(self, r: float, g: float, b: float) -> None:
        """This routine sets the emissive color of this Appearance.

        The color values should be in r g b color space with values between 0.0
        and 1.0. Setting any color value to a negative value will remove the
        color from this Appearance.

        Args:
            r (float): The red value to set.
            g (float): The green value to set.
            b (float): The blue value to set.
        """
    def setColorSpecular(self, r: float, g: float, b: float) -> None:
        """This routine sets the specular color of this Appearance.

        The color values should be in r g b color space with values between 0.0
        and 1.0. Setting any color value to a negative value will remove the
        color from this Appearance.

        Args:
            r (float): The red value to set.
            g (float): The green value to set.
            b (float): The blue value to set.
        """
    def setMapperReference(self, mapperType: int, textureReference: int) -> bool:
        """This routine sets a Mapper that modifies this Appearance.

        The Mapper is a texture object that modifies some property of the Appearance.
        One of: FME_MAPPER_ALPHA_MAP, FME_MAPPER_ALPHA_MASK, FME_MAPPER_AMBIENT_MAP,
        FME_MAPPER_AMBIENT_MASK, FME_MAPPER_DIFFUSE_MAP, FME_MAPPER_DIFFUSE_MASK,
        FME_MAPPER_EMISSIVE_MAP, FME_MAPPER_EMISSIVE_MASK, FME_MAPPER_SHININESS_MAP,
        FME_MAPPER_SHININESS_MASK, FME_MAPPER_SPECULAR_MAP, FME_MAPPER_SPECULAR_MASK,
        FME_MAPPER_BUMP_MAP, OR FME_MAPPER_BUMP_MASK. The 'textureReference' should
        refer to a Texture found in the common FMELibrary. True will be returned
        if the reference supplied refers to a valid Texture in the library, False
        indicates a hanging reference.

        Args:
            mapperType: The mapper type to set the reference for.
            textureReference: The texture reference to set.

        Returns:
            bool: Returns True if the reference supplied refers to a valid texture
                in the library and False otherwise.
        """
    def setName(self, name: text_type) -> None:
        """This routine sets the 'name' of this Appearance with a six.text_type .

        (It need not be a unique name among other, possibly different Appearances.)
        Setting the 'name' to be (blank) will remove the name from this Appearance.

        Args:
            name (text_type): The name to set.
        """
    def setShininess(self, shininess: float) -> None:
        """This routine sets the shininess of this Appearance.

        The shininess should be a floating point value in the range of 0.0 to 1.0,
        where 0.0 represents a fully dull material, and 1.0 represents a fully shiny
        material. Setting the value to negative will remove this property from this
        appearance.

        Args:
            shininess (float): The shininess to set.
        """
    def setTextureReference(self, textureReference: int) -> bool:
        """This routine sets the main texture reference of this Appearance.

        The texture reference should be valid reference to a Texture found in the
        common FMELibrary. True will be returned if the reference supplied refers
        to a valid Texture in the library, false indicates a hanging reference.

        Args:
            textureReference (int): The texture reference to set.

        Returns:
            bool: Returns True if the reference supplied refers to a valid texture
                in the library and False otherwise.
        """
