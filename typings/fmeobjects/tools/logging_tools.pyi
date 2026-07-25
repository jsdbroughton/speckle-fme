from types import TracebackType
from six import text_type, string_types

from fmeobjects.features import FMEFeature

class FMELogFile:
    """FME Log File Class"""

    def __init__(self) -> None:
        """Initialize self. See help(type(self)) for accurate signature."""
    def activityMessage(self, message: str) -> None:
        """[DEPRECATED] Log an activity message to the logfile.

        Args:
            message (str): This is the message string.
        """
    def allowDuplicateMessages(self, allowDuplicateMessages: bool) -> None:
        """This routine sets the allow duplicate messages status of the logfile.

        If in duplicate message mode subsequent messages with the same text are
        logged, otherwise only the first message is logged and the duplicates
        are counted and a count is logged as the next line instead once a
        different message is logged.

        Args:
            allowDuplicateMessages (bool): When True, duplicate messages are not
                hidden in the log. Otherwise if False, log hiding of duplicate
                messages is enabled. Default is False.
        """
    def getAllowDuplicateMessages(self) -> bool:
        """This routine gets the allow duplicate messages status of the logfile.

        If in duplicate message mode subsequent messages with the same text are
        logged, otherwise only the first message is logged and the duplicates
        are counted and a count is logged as the next line instead once a
        different message is logged.

        Returns:
            (bool): Default is False.
        """
    def getFileName(self) -> str:
        """Get the name of the file that is currently being used to log messages.

        Returns:
            (str): Filename
        """
    def getHeldMessages(self) -> bool:
        """Retrieve any held messages and clear the held messages buffer.

        Returns:
            (bool): True if there were held messages, otherwise False.
        """
    def getMessage(self, messageNumber: int, messageParameters: list[string_types]) -> text_type:  # type: ignore
        """This method returns the message mapped from 'messageNumber' in
        FME_HOME/messages/fmemessages.fms.

        The mapped message has all its %s replaced by the value in
        'messageParameters' indexed at s, where s is an integer >= 0.

        Args:
            messageNumber (int): The index of the message in FME's 'messages'.
            messageParameters (list[six.string_types]): The values used to
                replace the %s patterns in the returned message, where s is an
                integer >= 0.

        Returns:
            (six.text_type): The mapped message with %s patterns replaced.

        Raises:
            FMEException: An exception is raised if a message is not successfully
            retrieved.
        """
    def getSilent(self) -> bool:
        """Get the silent status of the logfile.

        Returns:
            (bool): Default is False.
        """
    def holdMessages(self, holdMessages: bool) -> None:
        """Inform FME whether or not log messages should be held.

        If set to True, then any log messages will be stored in an internal
        memory buffer for later retrieval, and no messages will be written to
        the log file, or sent to the callback.

        Held messages are retained until they are retrieved with
        getHeldMessages, even if holdMessages is set to False.

        Args:
            holdMessages (bool): If set to True, then any log messages will be
                stored in an internal memory buffer for later retrieval, and no
                messages will be written to the log file, or sent to the callback.
        """
    def logException(self, exception: Exception, severity: int) -> None:
        """Log an exception to the logfile.

        Args:
            exception (Exception): Exception to be logged.
            severity (int): (Optional) The message level. Default value is
                FME_INFORM. Must be one of FME_INFORM, FME_WARN, FME_ERROR,
                FME_FATAL, FME_STATISTIC, or FME_STATUSREPORT.
        """
    def logFeature(self, feature: FMEFeature, severity: int, maxCoords: int) -> None:
        """Log a feature to the logfile.

        Args:
            feature (FMEFeature): The feature is not modified.
            severity (int): (Optional) The message level. Default value is
                FME_INFORM. Must be one of FME_INFORM, FME_WARN, FME_ERROR,
                FME_FATAL, FME_STATISTIC, or FME_STATUSREPORT.
            maxCoords (int): (Optional) Default value: 20. Control how many
                coordinates to output. A value of -1 means all coordinates will
                be output.
        """
    def logMessage(self, messageNumber: int, parameters: list[string_types], severity: int) -> None:  # type: ignore
        """Log a message to the logfile.

        Args:
            messageNumber (int): This is the message index, which is stored in a
                file in FME's 'messages' directory.
            parameters (list[six.string_types]): Supply the values for the
                fill-in parameters (0, 1, 2, …) of the message.
            severity (int): (Optional) The message level. Default value is
                FME_INFORM. Must be one of FME_INFORM, FME_WARN, FME_ERROR,
                FME_FATAL, FME_STATISTIC, or FME_STATUSREPORT.
        """
    def logMessageString(self, message: str, severity: int) -> None:
        """Log a simple string to the log file.

        Args:
            message (str): This is the message string.
            severity (int): (Optional) The message level. Default value is
                FME_INFORM. Must be one of FME_INFORM, FME_WARN, FME_ERROR,
                FME_FATAL, FME_STATISTIC, or FME_STATUSREPORT.
        """
    def numFeaturesLogged(self) -> int:
        """Return the total number of features logged.

        Returns:
            (int): The number of features logged.
        """
    def setCallback(self, function: function) -> None:
        """Provide FME with a callback function that will be called whenever a
        message is logged.

        By default, messages will be logged to both the callback function and
        the Log file. If setFileName is called with None as the filename
        parameter, then messages will only be sent to the callback.

        The callback function must take two arguments: An int severity, and a
        string message.

        Args:
            function (Callable): The function to provide FME for use as a
                callback function.
        """
    def setFilename(self, fileName: str, append: bool) -> None:
        """If the filename is different from the current file, then the current
        file is closed, and the new one is opened.

        Args:
            fileName (str): The file name to set.
            append (bool): Append new messages to the file if True. Clear the
                file before any new log messages are added if False.

        Raises:
            FMEException: An exception is raised if there was a problem.
        """
    def silent(self, silent: bool) -> None:
        """Set the 'silent' status of the logfile.

        When in 'silent' mode, nothing is logged.

        Args:
            silent (bool): If set to True, then no messages will be logged.
        """

class FMEException:
    """FME Exception Class

    FME will raise an exception of this type if it encounters an error.

    Attributes:
        message (int or str): The message number defined in a message file, or a
            literal string to use as the error message.
        parms (list[str]):  (Optional) Parameters to the message string. Used
            only if msgNum is used for 'message'. Not to be used if 'message' is
            a string.
    """

    msgNum: int
    def __init__(self, message: int | str, parms: list[str]) -> None:
        """Initialize self. See help(type(self)) for accurate signature.

        Args:
            message (int or str): The message number or string to use.
            parms (list[str]): The parameters to use for the message.
        """
        """Initialize self. See help(type(self)) for accurate signature."""
    def with_traceback(self, tb: TracebackType) -> None:
        """set self.__traceback__ to tb and return self."""

# Severity levels
FME_INFORM: int
"""Default: White"""
FME_WARN: int
"""Warning: Blue"""
FME_ERROR: int
"""Error: Red"""
FME_FATAL: int
"""Fatal Error: Red"""
FME_STATISTIC: int
"""Stats: White"""
FME_STATUSREPORT: int
"""Status: Not Printed"""
