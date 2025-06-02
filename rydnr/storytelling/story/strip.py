# vim: set fileencoding=utf-8
"""
rydnr/storytelling/story/strip.py

This file defines the Strip class.

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
from pythoneda.shared import ValueObject, primary_key_attribute
from .panel import Panel
from typing import List


class Strip(ValueObject):
    """
    Represents a strip.

    Class name: Strip

    Responsibilities:
        - Represents Strips.

    Collaborators:
        - None
    """

    def __init__(self, panels: List[Panel]):
        """
        Creates a new Strip instance.
        :param panels: The panels.
        :type panels: List[rydnr.storytelling.story.Panel]
        """
        self._panels = panels
        super().__init__()

    @property
    @primary_key_attribute
    def panels(self) -> List[Panel]:
        """
        Retrieves the panels.
        :return: The panel.
        :rtype: List[rydnr.storytelling.story.Panel]
        """
        return self._panels


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
