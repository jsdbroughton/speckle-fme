from fmeobjects.geometries.points import FMEPoint

class OrientMixin:
    def isOriented(self, orientation: int) -> bool:
        """Returns True if the geometry is oriented in the specified direction.

        Args:
            orientation: (int): The direction to check.

        Returns:
            bool: True if the geometry is oriented in the specified direction.
        """
    def orient(self, orientation: int) -> None:
        """Reorients the geometry such that either all the surface normals face out
        from the  geometry or all the surface normals face in to the geometry.

        Args:
            orientation: (int): The direction to orient the solid in.
        """
    def reorient(self) -> None:
        """Flips the underlying surfaces that make up the geometry, such that the
        front and back of each surface is switched. This has the effect of flipping
        the geometry inside-out. The front and back vertex normals are swapped."""

class TransformMixin:
    def offset(self, offsetPoint: FMEPoint) -> None:
        """Offset the geometry by the specified amount.

        Args:
            offsetPoint: (FMEPoint): The offset point.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def rotate2D(self, center: FMEPoint, angle: float) -> None:
        """Rotates this geometry about the z-axis by the specified angle, in degrees.

        The rotation is performed relative to the center specified. A positive
        angle corresponds to a counter-clockwise rotation, when looking down onto
        the XY-plane.

        Args:
            center: (FMEPoint): The center of rotation.
            angle: (float): The angle of rotation.
        """
    def reverse(self) -> None:
        """This reverses the order of the geometry's points."""
    def scale(self, xScale: float, yScale: float, zScale: float) -> None:
        """Scales this geometry by the specified factors.

        Args:
            xScale: (float): The x-axis scale factor.
            yScale: (float): The y-axis scale factor.
            zScale: (float): The z-axis scale factor.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """

class AppearanceMixin:
    def getAppearanceReference(self, front: bool) -> int:
        """Returns the appearance reference for this geometry.

        Args:
            front: (bool): True if the front appearance reference should be returned,
                False if the back appearance reference should be returned.

        Returns:
            int: The appearance reference.
        """
    def setAppearanceReference(self, appearanceRef: int, front: bool) -> None:
        """This method associates an appearance within the Library with this solid.
        This is done by passing in the unique appearance reference for this
        appearance. Subsequent calls to this method on the same side, will override
        the previous appearance used with the new appearance passed in.

        An appearance reference of '0' represents the default appearance.
        Interpretation of the default appearance is left to the consumer of this
        geometry. When set at this FMESolid level, the appearance represents the
        default appearance to apply when the contained surfaces use the default
        appearance instead of a specific appearance. Contained surfaces may be
        found within nested solids, geometry instances that reference geometries
        containing surfaces, or as surfaces or multi-surfaces.

        The second parameter controls whether this action should take place on
        the front of the contained surfaces or the back. Both can be set
        independently. The 'appearanceRef' should be a valid reference to a
        definition stored in the FMELibrary. If the reference was not found in
        the library, it will still attach the reference to the instance, but
        will throw a FMEException. This is an unhealthy situation as it represents
        a 'dangling reference'.

        Args:
            appearanceRef: (int): The appearance reference to set.
            front: (bool): True if the front appearance reference should be set,
                False if the back appearance reference should be set.

        Raises:
            FMEException: An exception is raised if an error occurred or the
                reference was not found in the library and a dangling reference
                was attached.
        """
