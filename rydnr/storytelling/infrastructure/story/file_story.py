# vim: set fileencoding=utf-8
"""
rydnr/storytelling/infrastructure/prompt/file_story.py

This file defines the FileStory class.

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
from rydnr.storytelling.story.story import Story, Strip


class FileStory(Story):
    """
    Represents a story read from files.

    Class name: FileStory

    Responsibilities:
        - Represents a story whose strips are read from files.

    Collaborators:
        - None
    """

    def __init__(self, storyFolder: str):
        """
        Creates a new FileStory instance.
        :param storyFolder: The folder with the story strips.
        :type storyFolder: str
        """
        self._story_folder = storyFolder
        super().__init__(self.from_folder(storyFolder))

    @property
    @primary_key_attribute
    def story_folder(self) -> str:
        """
        :return: The story folder.
        :rtype: str
        """
        return self._story_folder

    @classmethod
    def from_folder(cls, folder: str) -> List[Strip]:
        """
        Reads story from the specified folder.
        :param folder: The folder containing strip files.
        :type folder: str
        :return: A list of story read from the folder.
        :rtype: List[rydnr.storytelling.story.Strip]
        """
        import json
        import os

        result = []
        filenames = sorted(f for f in os.listdir(folder_path) if f.endswith(".json"))
        for filename in filenames:
            full_path = os.path.join(folder_path, filename)
            with open(full_path, "r", encoding="utf-8") as file:
                json_objects.append(Strip.from_json(file.read()))
        return result


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
