# vim: set fileencoding=utf-8
"""
rydnr/storytelling/prompt/story.py

This file defines the Story class.

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
from pythoneda.shared import Port, primary_key_attribute


class Story(Port):
    """
    Represents a story.

    Class name: Story

    Responsibilities:
        - Represents a story consisting of a list of strips.

    Collaborators:
        - None
    """

    def __init__(self, strips: List[Strip]):
        """
        Creates a new Story instance.
        :param strips: The strips.
        :type strips: List[rydnr.storytelling.prompt.Strip]
        """
        self._strips = strips
        super().__init__()

    @property
    @primary_key_attribute
    def strips(self) -> List[Strip]:
        """
        :return: The strips.
        :rtype: List[rydnr.storytelling.prompt.Strip]
        """
        return self._strips


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
