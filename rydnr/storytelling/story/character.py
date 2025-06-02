# vim: set fileencoding=utf-8
"""
rydnr/storytelling/story/character.py

This file defines the Character class.

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
from pythoneda.shared import attribute, primary_key_attribute, ValueObject
from typing import List


class Character(ValueObject):
    """
    Represents a character.

    Class name: Character

    Responsibilities:
        - Represents Characters.

    Collaborators:
        - None
    """

    def __init__(
        self, id: str, name: str, description: str, referenceImages: List[str]
    ):
        """
        Creates a new Character instance.
        :param name: The name.
        :type name: str
        :param description: The character description.
        :type description: str
        :param referenceImages: The reference images.
        :type referenceImages: List[str]
        """
        self._name = name
        self._description = description
        self._reference_images = referenceImages
        super().__init__()

    @property
    @primary_key_attribute
    def name(self) -> str:
        """
        Retrieves the name.
        :return: Such name.
        :rtype: str
        """
        return self._name

    @property
    @attribute
    def description(self) -> str:
        """
        Retrieves the description.
        :return: The description.
        :rtype: str
        """
        return self._description

    @property
    @attribute
    def reference_images(self) -> List[str]:
        """
        Retrieves the reference images.
        :return: Such list.
        :rtype: List[str]
        """
        return self._reference_images


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
