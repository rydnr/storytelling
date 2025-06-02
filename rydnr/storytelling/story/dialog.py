# vim: set fileencoding=utf-8
"""
rydnr/storytelling/story/dialog.py

This file defines the Dialog class.

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
from pythoneda.shared import primary_key_attribute, value_object
from .character import Character
from typing import Map


class Dialog(ValueObject):
    """
    Represents a dialog.

    Class name: Dialog

    Responsibilities:
        - Represents dialogs.

    Collaborators:
        - None
    """

    def __init__(self, character: Character, text: Map[str, str]):
        """
        Creates a new Dialog instance.
        :param character: The character.
        :type character: int
        :param text: The dialog texts.
        :type text: Map[str,str]
        """
        self._character = character
        self._text = text
        super().__init__()

    @property
    @primary_key_attribute
    def character(self) -> str:
        """
        Retrieves the character.
        :return: Such character.
        :rtype: rydnr.storytelling.story.Character
        """
        return self._character

    @property
    @primary_key_attribute
    def text(self) -> Map[str, str]:
        """
        Retrieves the text, internationalized.
        :return: The text.
        :rtype: Map[str,str]
        """
        return self._text


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-character: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
