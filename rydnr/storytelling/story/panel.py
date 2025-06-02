# vim: set fileencoding=utf-8
"""
rydnr/storytelling/story/panel.py

This file defines the Panel class.

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
from pythoneda.shared import attribute, primary_key_attribute, value_object
from .character import Character
from .dialogues import Dialog
from .panel_size import PanelSize
from typing import List


class Panel(ValueObject):
    """
    Represents a strip.

    Class name: Panel

    Responsibilities:
        - Represents Panels.

    Collaborators:
        - None
    """

    def __init__(
        self,
        id: str,
        name: str,
        characters: List[Character],
        context: str,
        panelSize: PanelSize,
        dialogues: Dialog,
    ):
        """
        Creates a new Panel instance.
        :param id: The id.
        :type id: str
        :param name: The panel name.
        :type name: rydnr.storytelling.story.Panel
        :param characters: The characters.
        :type characters: List[rydnr.storytelling.story.Character]
        :param context: The context.
        :type context: str
        :param panelSize: The panel size.
        :type panelSize: rydnr.storytelling.story.PanelSize
        :param dialogues: The dialogues.
        :type dialogues: List[rydnr.storytelling.story.Dialog]
        """
        self._id = id
        self._name = name
        self._characters = characters
        self._context = context
        self._panel_size = panelSize
        self._dialogues = dialogues
        super().__init__()

    @property
    @primary_key_attribute
    def id(self) -> str:
        """
        Retrieves the id.
        :return: Such id.
        :rtype: str
        """
        return self._id

    @property
    @attribute
    def name(self) -> str:
        """
        Retrieves the name.
        :return: The name.
        :rtype: str
        """
        return self._name

    @property
    @attribute
    def characters(self) -> List[Character]:
        """
        Retrieves the characters.
        :return: Such list.
        :rtype: List[rydnr.storytelling.story.Character]
        """
        return self._characters

    @property
    @attribute
    def context(self) -> str:
        """
        Retrieves the context.
        :return: Such context.
        :rtype: str
        """
        return self._context

    @property
    @attribute
    def panel_size(self) -> PanelSize:
        """
        Retrieves the panel size.
        :return: The size.
        :rtype: rydnr.storytelling.story.PanelSize
        """
        return self._panel_size

    @property
    @attribute
    def dialogues(self) -> List[Dialog]:
        """
        Retrieves the dialogues.
        :return: Such dialogues.
        :rtype: List[rydnr.storytelling.story.Dialog]
        """
        return self._dialogues


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
