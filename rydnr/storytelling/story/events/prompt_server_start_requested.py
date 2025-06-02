# vim: set fileencoding=utf-8
"""
rydnr/storytelling/prompt_server/events/prompt_server_start_requested.py

This file defines PromptServerStartRequested class.

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


class PromptServerStartRequested(Event):
    """
    A graphic novel is requested.

    Class name: PromptServerStartRequested

    Responsibilities:
        - Represent the moment in which the prompt server start has been requested.

    Collaborators:
        - None
    """

    def __init__(
        self,
        port: int = 9909,
        promptsFolder: str,
        previousEventIds: List[str] = None,
        reconstructedId: str = None,
    ):
        """
        Creates a new PromptServerStartRequested instance.
        :param port: The server port.
        :type port: str
        :param promptsFolder: The folder with the prompts.
        :type promptsFolder: str
        :param previousEventIds: The id of the previous events, if any.
        :type previousEventIds: List[str]
        :param reconstructedId: The id of the event, if it's generated externally.
        :type reconstructedId: str
        """
        self._port = port
        self._prompts_folder = promptsFolder
        super().__init__(previousEventIds, reconstructedId)

    @property
    @primary_key_attribute
    def port(self) -> str:
        """
        Retrieves the output file.
        :return: Such file.
        :rtype: str
        """
        return self._port

    @property
    @primary_key_attribute
    def prompts_folder(self) -> str:
        """
        Retrieves the prompts folder.
        :return: The folder with the prompts.
        :rtype: str
        """
        return self._prompts_folder

# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
