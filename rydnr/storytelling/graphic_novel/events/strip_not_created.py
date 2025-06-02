# vim: set fileencoding=utf-8
"""
rydnr/storytelling/graphic_novel/events/strip_not_created.py

This file defines StripNotCreated class.

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


class StripNotCreated(Event):
    """
    A strip couldn't be created.

    Class name: StripNotCreated

    Responsibilities:
        - Represent the moment in which we report that a requested strip could not been created.

    Collaborators:
        - None
    """

    def __init__(
        self,
        message: str,
        previousEventIds: List[str] = None,
        reconstructedId: str = None,
    ):
        """
        Creates a new StripNotCreated instance.
        :param message: The error message.
        :type message: str
        :param previousEventIds: The id of the previous events, if any.
        :type previousEventIds: List[str]
        :param reconstructedId: The id of the event, if it's generated externally.
        :type reconstructedId: str
        """
        self._message = message
        super().__init__(previousEventIds, reconstructedId)

    @property
    @primary_key_attribute
    def message(self) -> str:
        """
        Retrieves the message.
        :return: The message.
        :rtype: str
        """
        return self._message


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
