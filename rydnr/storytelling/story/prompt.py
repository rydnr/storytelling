# vim: set fileencoding=utf-8
"""
rydnr/storytelling/story/prompt.py

This file defines the Prompt class.

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
from .dialog import Dialog


class Prompt(Port):
    """
    Represents a prompt.

    Class name: Prompt

    Responsibilities:
        - Represents Prompts.

    Collaborators:
        - None
    """

    def __init__(self, dialogs: List[Dialog]):
        """
        Creates a new Prompt instance.
        :param dialogs: The dialogs.
        :type dialogs: List[rydnr.storytelling.story.Dialog]
        """
        self._dialogs = dialogs
        super().__init__()

    @property
    @primary_key_attribute
    def dialogs(self) -> List[Dialog]:
        """
        Retrieves the dialogs.
        :return: The prompt.
        :type text: str
        """
        return self._text


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
