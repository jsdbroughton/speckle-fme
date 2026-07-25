from typing import overload
from six import text_type
from fmeobjects.geometries.general import FMEGeometry
from fmeobjects.geometries.points import FMEPoint

class FMETextIterator:
    """FME Text Iterator Class

    FMETextIterator should not be constructed directly. Instead, use the
    iterator semantics of FMEMultiText to get an FMETextIterator which can be
    used to iterate over its geometries."""

    def __init__(self) -> None:
        """Initialize self. See help(type(self)) for accurate signature."""

class FMEText(FMEGeometry):
    """FME Text Class"""

    @overload
    def __init__(
        self,
        location: FMEGeometry,
        textString: text_type,
        textSize: float,
        textRotation: float,
    ) -> None:
        """Creates a new Text geometry object.

        'textRotation' is CCW up from the horizontal and is measured in degrees.
        'textSize' is the height of the text's box before rotation. It includes
        all lines and interline spacing for multi-line text. The 'textString' is
        specified as a six.text_type , which is set as an encoded text string on
        the text object.

        Args:
            location (FMEGeometry): The location of the text.
            textString (text_type): The text string to display.
            textSize (float): The text size.
            textRotation (float): The rotation value to set.

        Returns:
            (FMEText): An instance of a Text Geometry object.
        """
    @overload
    def __init__(self, text: FMEText) -> None:
        """Creates a text from an existing text.

        Args:
            text (FMEText): The Text geometry object to create a copy of.

        Returns:
            (FMEText): An instance of a Text Geometry object.
        """
    def getLocation(self, asPoint: bool) -> FMEGeometry | FMEPoint:
        """Returns the location of the text.

        Args:
            asPoint (bool): Whether to return the location as a FMEPoint

        Returns:
            (FMEGeometry): The location of the text.
        """
    def getTextRotation(self) -> float:
        """Returns the rotation of the text object.

        The returned rotation is counter-clockwise up from the horizontal and is
        measured in degrees.

        Returns:
            (float): The text rotation.
        """
    def getTextSize(self) -> float:
        """Returns the text size of the text object.

        Text size is actually the height of hte text's box before rotation. It
        includes all lines and interline spacing for multiline text.

        Returns:
            (float): The text size.
        """
    def getTextString(self) -> text_type:
        """Returns the text string of the text object.

        It includes all lines and interline spacing for multi-line text.

        Returns:
            (text_type): The text string.

        Raises:
            FMEException: An exception is raised if an error occurs.
        """
    def offset(self, offsetPoint: FMEPoint) -> None:
        """Offsets the geometry by the coordinate values specified by 'offsetPoint'.

        An error is returned if the operation is unsuccessful.

        Args:
            offsetPoint (FMEPoint): The point whose coordinate values will be
                used to offset the text object.

        Raises:
            FMEException: An exception is raised if an error occurs.
        """
    def reset(self, text: FMEText) -> None:
        """Resets the existing text object, and sets its values to the data stored
        in 'text'.

        Args:
            text (FMEText): The FMEText object whose data will be set to the
                existing text object.
        """
    def rotate2D(self, center: FMEPoint, angle: float) -> None:
        """Rotates the text counterclockwise around the 'center' point by the
        specified 'angle' (in degrees). An error is returned if the operation is
        unsucessful.

        Args:
            center (FMEPoint): The center point around which the text will be rotated.
            angle (float): The angle of rotation in degrees.

        Raises:
            FMEException: An exception is raised if an error occurs.
        """
    def scale(self, xScale: float, yScale: float, zScale: float, scaleText: bool) -> None:
        """Scale the feature by the given amounts.

        'zScale' is ignored if the text object is 2D. An error is returned if
        the operation is unsucessful.

        Args:
            xScale (float): The x-scale factor.
            yScale (float): The y-scale factor.
            zScale (float): The z-scale factor.
            scaleText (bool): (Optional) Whether to scale the text.

        Raises:
            FMEException: An exception is raised if an error occurs.
        """
    def setLocation(self, location: FMEGeometry) -> None:
        """Sets the existing text object's location to the value in 'location.
        An error is returned if the new location is invalid or NULL.

        Args:
            location (FMEGeometry): The new location of the text.

        Raises:
            FMEException: An exception is raised if an error occurs.
        """
    def setTextRotation(self, textRotation: float) -> None:
        """Sets the rotation of the text object.

        The rotation is counter-clockwise up from the horizontal and is
        measured in degrees.

        Args:
            textRotation (float): The text rotation.
        """
    def setTextSize(self, textSize: float) -> None:
        """Sets the text size of the text object.

        An error is returned if the new size is invalid or NULL.

        Args:
            textSize (float): The text size.

        Raises:
            FMEException: An exception is raised if an error occurred.
        """
    def setTextString(self, textString: text_type) -> None:
        """Sets the existing text object's text string to 'textString'.

        The 'textString' is specified as a six.text_type, which is set as an
        encoded text string on the text object.

        Args:
            textString (text_type): The text string.
        """

class FMEMultiText(FMEGeometry):
    """FME Multi-Text Class"""

    def __init__(self, multiText: FMEMultiText) -> None:
        """Creates a new Multi-Text object from an existing Multi-Text object.

        Args:
            multiText (FMEMultiText): The Multi-Text object to create a copy of.

        Returns:
            (FMEMultiText): An instance of a Multi-Text Geometry object.
        """
    def appendPart(self, text: FMEText) -> None:
        """This appends the text to the existing MultiText.

        If None is passed in, nothing will be appended. All texts in the
        MultiText will be forced to have the same dimension. If any 3D texts
        exist, all 2D texts will be converted to 3D with a default Z value of 0.0.

        Args:
            text (FMEText): The text to append.

        Raises:
            FMEException: An exception is raised if an error occurs.
        """
    def appendParts(self, multiText: FMEMultiText) -> None:
        """This appends the texts to the existing MultiText.

        If None is passed in, nothing will be appended.

        Args:
            multiText (FMEMultiText): The MultiText to append.

        Raises:
            FMEException: An exception is raised if an error occurs.
        """
    def getPartAt(self, index: int) -> FMEText | None:
        """Returns the text at the specified index.

        Args:
            index (int): The index of the text to return.

        Returns:
            (FMEText): The text at the given index. Note: This method returns a
                terminal text type of the FMEText ; i.e. one of the leaf classes
                in the FMEText inheritance graph. For example, a FMELine is
                returned if the text truly is a line.
        """
    def numParts(self) -> int:
        """Returns the number of parts in the MultiText.

        Returns:
            (int): The number of parts.
        """
    def offset(self, offsetPoint: FMEPoint) -> None:
        """Offsets the geometry by the coordinate values specified by 'offsetPoint'.

        An error is returned if the operation is unsuccessful.

        Args:
            offsetPoint (FMEPoint): The point whose coordinate values will be
                used to offset the text object.

        Raises:
            FMEException: An exception is raised if an error occurs.
        """
    def removeLastPart(self) -> FMEText | None:
        """This removes and returns the last text of the MultiText.

        If there are no texts in the MultiText, it will return None.

        Returns:
            (FMEText): The last text of the MultiText. Note: This method returns
                a terminal text type of the FMEText; i.e. one of the leaf classes
                in the FMEText inheritance graph. For example, a FMELine is
                returned if the text truly is a line.

        Raises:
            FMEException: An exception is raised if an error occurs.
        """
    def rotate2D(self, centre: FMEPoint, angle: float) -> None:
        """The angle is CCW up from the horizontal and is measured in degrees.

        Args:
            centre (FMEPoint): The center point around which the text will be rotated.
            angle (float): The angle of rotation in degrees.

        Raises:
            FMEException: An exception is raised if an error occurs.
        """
    def scaleXYZ(self, xScale: float, yScale: float, zScale: float) -> None:
        """Scale the feature by the given amounts.

        'zScale' is ignored if the text object is 2D. An error is returned if
        the operation is unsucessful.

        Args:
            xScale (float): The x-scale factor.
            yScale (float): The y-scale factor.
            zScale (float): The z-scale factor.

        Raises:
            FMEException: An exception is raised if an error occurs.
        """
    def scaleXYZT(self, xScale: float, yScale: float, zScale: float, scaleText: bool) -> None:
        """Scale the feature by the given amounts.

        'zScale' is ignored if the text object is 2D. An error is returned if
        the operation is unsucessful.

        Args:
            xScale (float): The x-scale factor.
            yScale (float): The y-scale factor.
            zScale (float): The z-scale factor.
            scaleText (bool): (Optional) Whether to scale the text.

        Raises:
            FMEException: An exception is raised if an error occurs.
        """
