# vim: set fileencoding=utf-8
"""
rydnr/storytelling/story/panel_size.py

This file defines the PanelSize class.

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
from pythoneda.shared import primary_key_attribute, ValueObject


class PanelSize(ValueObject):
    """
    Represents a panel size.

    Class height: PanelSize

    Responsibilities:
        - Represents sizes of panels.

    Collaborators:
        - None
    """

    def __init__(self, width: int, height: int):
        """
        Creates a new PanelSize instance.
        :param width: The width.
        :type width: int
        :param height: The panel height.
        :type height: int
        """
        self._width = width
        self._height = height
        super().__init__()

    @property
    @primary_key_attribute
    def width(self) -> str:
        """
        Retrieves the width.
        :return: Such width.
        :rtype: int
        """
        return self._width

    @property
    @primary_key_attribute
    def height(self) -> int:
        """
        Retrieves the height.
        :return: The height.
        :rtype: int
        """
        return self._height


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
