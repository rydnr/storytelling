# vim: set fileencoding=utf-8
"""
rydnr/storytelling/graphic_novel/events/strip_requested.py

This file defines StripRequested class.

Copyright (C) 2025-today rydnr's storytelling

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from pythoneda.shared import Event, primary_key_attribute
from typing import List


class StripRequested(Event):
    """
    A strip is requested.

    Class name: StripRequested

    Responsibilities:
        - Represent the moment in which a strip has been requested.

    Collaborators:
        - None
    """

    def __init__(
        self,
        scriptFile: str,
        outputFile: str,
        previousEventIds: List[str] = None,
        reconstructedId: str = None,
    ):
        """
        Creates a new StripRequested instance.
        :param scriptFile: The file with the strip description.
        :type scriptFile: str
        :param outputFile: The output file.
        :type outputFile: str
        :param previousEventIds: The id of the previous events, if any.
        :type previousEventIds: List[str]
        :param reconstructedId: The id of the event, if it's generated externally.
        :type reconstructedId: str
        """
        self._script_file = scriptFile
        self._output_file = outputFile
        super().__init__(previousEventIds, reconstructedId)

    @property
    @primary_key_attribute
    def script_file(self) -> str:
        """
        Retrieves the strip file.
        :return: The file with the strip description.
        :rtype: str
        """
        return self._script_file

    @property
    @primary_key_attribute
    def output_file(self) -> str:
        """
        Retrieves the output file.
        :return: Such file.
        :rtype: str
        """
        return self._output_file


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
