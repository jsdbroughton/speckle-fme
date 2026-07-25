# FMEReader.setConstraints() keywords
from fmeobjects.features import FMEFeature

from six import text_type

kFMERead_AllFeatures: int
kFMERead_EnvelopeHeightInPixels: int
kFMERead_EnvelopeIntersects: int
kFMERead_EnvelopeWidthInPixels: int
kFMERead_FMEType: int
kFMERead_FeatureType: int
kFMERead_Geometry: int
kFMERead_SearchType: int
kFMERead_Where: int

# FMESpatialIndex directives
kFME_SIPassphrase: int
kFME_SISerializeRasterData: int

# Has Support For Constants (support_type)
FME_SUPPORT_FEATURE_TABLE: int
FME_SUPPORT_FEATURE_TABLE_SHIM: int
FME_SUPPORT_FEATURE_TABLES_ONLY: int
FME_SUPPORT_WRITER_GET_SCHEMA: int

class FMEDialog:
    """FME Dialog Class

    Provides access to the standard FME dialog boxes."""

    def about(self, applicationName: str) -> None:
        """This method displays a dialog box that shows the kind of FME license
        and FME build number that the FMEObjects application is using.

        Args:
            applicationName (str): The name of the application.
        """
    def coordSysPrompt(self, coordSysName: str) -> str | None:
        """This method displays a standard FME coordinate system dialog to prompt
        the user to choose a coordinate system.

        Args:
            coordSysName (str): (Optional) the default coordinate system to be
                highlighted when the dialog is opened.

        Returns:
            (str): The coordinate system name chosen by the user.
        """
    def destPrompt(
        self,
        defaultDestFormat: str,
        defaultDestDataset: str,
        userDirectives: dict[str, str] | list[str],
    ) -> tuple[str, str, list[str]] | None:
        """This method displays a dialog to prompt the user to choose a destination
        format and dataset.

        Args:
            defaultDestFormat (str): The default format that will be selected when
                the dialog is opened. If none is desired, then this should be a
                0 length string.
            defaultDestDataset (str): The default dataset that will appear when
                the dialog is opened. If none is desired, then this should be a
                0 length string.
            userDirectives (dict[str,str] or list[str]): (Optional) Specify one
                or more additional directives to be used by the dialog. All elements
                in this collection must be strings. A list should be used if one
                key is to be set to multiple values. If a list is passed in,
                key-value pairs such as those in a dict must be placed side by
                side. For example, the key should be placed in the first list
                element, followed by the value for the key.
                These user directives are honoured:
                TITLE: The title to be used in the dialog box.
                - LIMIT_FORMATS: The short names of the only formats that will
                be allowed, separated by | characters.
                - EXCLUDE_FORMATS: The short names of the formats that will NOT
                be allowed, separated by | characters. Exclude takes precedence
                over LIMIT_FORMATS.
                - SETTINGS_ONLY: If value is “yes”, then the settings box is shown
                for the passed in default destination format/dataset The default
                is “no”.
                - SPATIAL_SETTINGS If value is “yes”, then any settings box that
                allows for specifying spatial constraints will have that aspect
                remain enabled. The default is”yes”. If the value is “no”, then
                the spatial area specification aspect of the settings boxes is
                disabled. This directive is useful for disabling spatial settings
                when a source dialog is done only for the purpose of gathering
                schema information.

        Returns:
            (str, str, list[str]): The destination format and dataset along with
                the user directives, these can be used directly with the
                FMEUniversalWriter. This tuple is formatted (destFormat,
                destDataset, [directives]). None is returned if the user pressed
                Cancel. The directives returned are as follows:

                - RUNTIME_MACROS: The runtime macros are in the next position.
                - META_MACROS: The metafile macros are in the next position.
                - METAFILE: The metafile name is in the next position.
                - COORDSYS: The coordinate system is in the next position.
        """
    def featTypeProperties(self, format: str, source: bool, schemaFeat: FMEFeature) -> FMEFeature | None:
        """Bring up the feature type properties dialog on the given schema feature.

        Args:
            format (str): The format name for the format this schema feature is a part of.
            source (bool):  True if this feature type is a source, False otherwise.
            schemaFeat (FMEFeature): The schema feature to edit. The schema feature is represented through the following values on the feature:

            - Feature Type: The feature type of the schema feature.
            - Geometry Type: The geometry type(s) of the schema feature, set as
            the 'fme_geometry{n}' attribute on the schema feature, where n is an
            index starting at 0. The geometry type values are the format specific
            geometry types that are defined in the metafile of the target format.
            - User Attributes: The user attribute(s) of the schema feature, set
            as regular attribute name/type pairs on the schema feature.
            - Format Attributes: The format attribute(s) of the schema feature,
            set as 'fme_format_attr_name{n}' and 'fme_format_attr_type{n}'
            attributes on the schema feature, where n is an index starting at 0.

        Returns:
            (FMEFeature): The schema feature that has been edited, None otherwise.
        """
    def generate(self, defaultSourceDataset: str) -> tuple[str, str]:
        """This method displays the Generate Workspace dialog box.

        Args:
            defaultSourceDataset (str): The default source dataset displayed in
                the Generate Workspace dialog.

        Returns:
            tuple[str, str]: The parameter filename and workspace filename. This
                tuple is formatted: (parameterFileName, workspaceFileName).
                Returns None if the user hit cancel.The parameterFileName that is
                returned can be used to generate a workspace with this fme
                invocation:fme PARAMETER_FILE < parameterFile > Then the parameterFile
                should be deleted from the disk. The workspace itself will not
                exist until after the FME returns.
        """
    def guessFormat(self, filename: str) -> str | None:
        """This method attempts to guess the format based on the extension of the filename passed in.

        Args:
            filename (str): The filename to be used to guess the format.

        Returns:
            (str): The format guessed or None if we were unable to make a guess.
        """
    def parameterPrompt(self, filename: str) -> bool:
        """This method parses the file with the passed in name and does a standard
        FME dialog for the parameters listed in the GUI lines in the file.

        If any DEFAULT_MACRO lines were found, these supply default values. If
        the user exits the form with OK, then the file will be overwritten with
        a new file that alternates MACRO NAME and VALUE, line by line.

        Args:
            filename (str): The name of the file to be parsed.

        Returns:
            bool: True if the user pressed OK, False otherwise.
        """
    def sourcePrompt(
        self,
        defaultSourceFormat: str,
        defaultSourceDataset: str,
        userDirectives: dict[str, str] | list[str],
    ) -> tuple[str, str, list[str]] | None:
        """This method displays a dialog to prompt the user to choose a source format and dataset.

        Args:
            defaultSourceFormat (str): The default format that will be selected when
                the dialog is opened. If none is desired, then this should be a
                0 length string.
            defaultSourceDataset (str): The default dataset that will appear when
                the dialog is opened. If none is desired, then this should be a
                0 length string.
            userDirectives (dict[str,str] or list[str]): (Optional) Specify one
                or more additional directives to be used by the dialog. All elements
                in this collection must be strings. A list should be used if one
                key is to be set to multiple values. If a list is passed in,
                key-value pairs such as those in a dict must be placed side by
                side. For example, the key should be placed in the first list
                element, followed by the value for the key.
                These user directives are honoured:
                TITLE: The title to be used in the dialog box.
                - LIMIT_FORMATS: The short names of the only formats that will
                be allowed, separated by | characters.
                - EXCLUDE_FORMATS: The short names of the formats that will NOT
                be allowed, separated by | characters. Exclude takes precedence
                over LIMIT_FORMATS.
                - SETTINGS_ONLY: If value is “yes”, then the settings box is shown
                for the passed in default source format/dataset The default
                is “no”.
                - SPATIAL_SETTINGS If value is “yes”, then any settings box that
                allows for specifying spatial constraints will have that aspect
                remain enabled. The default is”yes”. If the value is “no”, then
                the spatial area specification aspect of the settings boxes is
                disabled. This directive is useful for disabling spatial settings
                when a source dialog is done only for the purpose of gathering
                schema information.

        Returns:
            (str, str, list[str]): The source format and dataset along with the
                user directives, these can be used directly with the FMEUniversalReader.
                This tuple is formated (sourceFormat, sourceDataset, [directives]).
                None is returned if the user pressed Cancel. The directives returned
                are as follows:

                - RUNTIME_MACROS: The runtime macros are in the next position.
                - META_MACROS: The metafile macros are in the next position.
                - METAFILE: The metafile name is in the next position.
                - COORDSYS: The coordinate system is in the next position.
                - IDLIST: The id list is in the next position.
        """
    def xlatePrompt(
        self,
        defaultSourceFormat: str,
        defaultSourceDataset: str,
        defaultDestFormat: str,
        defaultDestDataset: str,
        userDirectives: dict[str, str] | list[str],
    ) -> tuple[str, str, str, str, list[str]] | None:
        """This method displays a dialog to prompt the user to choose a source format, dataset, destination format and dataset.

        Args:
            defaultSourceFormat (str): The default format that will be selected when
                the dialog is opened. If none is desired, then this should be a
                0 length string.
            defaultSourceDataset (str): The default dataset that will appear when
                the dialog is opened. If none is desired, then this should be a
                0 length string.
            defaultDestFormat (str): The default destination format that will be selected when
                the dialog is opened. If none is desired, then this should be a
                0 length string.
            defaultDestDataset (str): The default destination dataset that will appear when
                the dialog is opened. If none is desired, then this should be a
                0 length string.
            userDirectives (dict[str,str] or list[str]): (Optional) Specify one
                or more additional directives to be used by the dialog. All elements
                in this collection must be strings. A list should be used if one
                key is to be set to multiple values. If a list is passed in,
                key-value pairs such as those in a dict must be placed side by
                side. For example, the key should be placed in the first list
                element, followed by the value for the key.
                These user directives are honoured:
                TITLE: The title to be used in the dialog box.
                - LIMIT_FORMATS: The short names of the only formats that will
                be allowed, separated by | characters.
                - EXCLUDE_FORMATS: The short names of the formats that will NOT
                be allowed, separated by | characters. Exclude takes precedence
                over LIMIT_FORMATS.
                - SETTINGS_ONLY: If value is “yes”, then the settings box is shown
                for the passed in default source format/dataset The default
                is “no”.
                - SPATIAL_SETTINGS If value is “yes”, then any settings box that
                allows for specifying spatial constraints will have that aspect
                remain enabled. The default is”yes”If the value is “no”, then the
                spatial area specification aspect of the settings boxes is disabled.
                This directive is useful for disabling spatial settings when a
                source dialog is done only for the purpose of gathering schema
                information.

          Returns:
              (str, str, str, str, list[str]): The source format, source dataset,
              destination format, and destination dataset along with the source
              user directives and destination user directives, these can be used
              directly with the FMEUniversalReader and FMEUniversalWriter respectively.
              This tuple is formated (sourceFormat, sourceDataset, destFormat,
              destDataset, [sourceUserDirectives], [destUserDirectives]). None is
              returned if the user pressed Cancel. The source user directives
              returned are as follows:

              - RUNTIME_MACROS: The runtime macros are in the next position.
              - META_MACROS: The metafile macros are in the next position.
              - METAFILE: The metafile name is in the next position.
              - COORDSYS: The coordinate system is in the next position.
              - IDLIST: The id list is in the next position.

              The destination user directives returned are as follows:`
              - RUNTIME_MACROS: The runtime macros are in the next position.
              - META_MACROS: The metafile macros are in the next position.
              - METAFILE: The metafile name is in the next position.
              - COORDSYS: The coordinate system is in the next position.
        """

class FMEFactoryPipeline:
    """FME Factory Pipeline Class"""

class FMERegex:
    """FME Regex Class"""

    def __init__(self, regexPattern: text_type) -> None:
        """This class provides FME regular expression functionality that is
        differs from Python's built-in re module.

        Returns: (FMERegex): The FMERegex object.
        """
    def findall(self, inputString: text_type) -> list[text_type]:
        """Return all non-overlapping matches in string, as a list of strings.

        The string is scanned left-to-right, and matches are returned in the
        order found.

        Args:
            inputString (text_type): The string to search.

        Returns: (list[text_type]): The list of matches.
        """
    def findlist(self, inputString: text_type) -> list[text_type]:
        """Return a list yielding match objects over all non-overlapping matches in string.

        The string is scanned left-to-right, and matches are returned in the order
        found.

        Args:
            inputString (text_type): The string to search.

        Returns: (list[text_type]): A list of match tuples of the form (match,
            start, end), where match is the string segment matching the regular
            expression pattern, start is the start index of the string segment,
            and end is the end index of the string segment.
        """
    def match(self, inputString: text_type) -> tuple[str, int, int]:
        """If zero or more characters at the beginning of string match this regular
        expression, return a corresponding match tuple.

        Args:
            inputString (text_type): The string to search.

        Returns: (tuple[str, int, int]): A match tuple of the form
            (match, start, end), where match is the string segment matching the
            regular expression pattern, start is the start index of the string
            segment, and end is the end index of the string segment. None is
            returned if a match is not found.
        """
    def search(self, inputString: str) -> tuple[str, int, int]:
        """Scan through string looking for the first location where this regular
        expression produces a match, and return a corresponding match object.

        Args:
            inputString (str): The string to search.

        Returns: (tuple[str, int, int]): A match tuple of the form
            (match, start, end), where match is the string segment matching the
            regular expression pattern, start is the start index of the string
            segment, and end is the end index of the string segment. None is
            returned if a match is not found.
        """

class FMESession:
    """FME Session Class"""

class FMESpatialIndex:
    """FME Spatial Index Class"""

class FMETemporaryFileManager:
    """FME Temporary File Manager Class"""

class FMEUniversalReader:
    """FME Universal Reader Class"""

class FMEUniversalWriter:
    """FME Universal Writer Class"""

class FMEWorkspaceRunner:
    """FME Workspace Runner Class"""
