# vim: set fileencoding=utf-8
"""
rydnr/storytelling/painter.py

This file defines the Painter lass.

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
from pythoneda.shared import Port


class Painter(Port):
    """
    Represents a painter.

    Class name: Painter

    Responsibilities:
        - Is able to create images.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new Painter instance.
        """
        super().__init__()

    async def create(self, width: int, height: int) -> bytes:
        """
        Creates a new image.
        :param width: The width of the image.
        :type width: int
        :param height: The height of the image.
        :type height: int
        :return: The image bytes.
        :rtype: bytes
        """
        raise NotImplementedError("create(int, int) method not implemented")


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
