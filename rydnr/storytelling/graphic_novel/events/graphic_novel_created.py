# vim: set fileencoding=utf-8
"""
rydnr/storytelling/graphic_novel/events/graphic_novel_created.py

This file defines GraphicNovelCreated class.

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


class GraphicNovelCreated(Event):
    """
    A graphic novel is created.

    Class name: GraphicNovelCreated

    Responsibilities:
        - Represent the moment in which a graphic novel has been created.

    Collaborators:
        - None
    """

    def __init__(
        self,
        graphicNovel: "rydnr.storytelling.graphic_novel.GraphicNovel",
        previousEventIds: List[str] = None,
        reconstructedId: str = None,
    ):
        """
        Creates a new GraphicNovelCreated instance.
        :param graphicNovel: The graphic novel.
        :type graphicNovel: rydnr.storytelling.graphic_novel.GraphicNovel
        :param previousEventIds: The id of the previous events, if any.
        :type previousEventIds: List[str]
        :param reconstructedId: The id of the event, if it's generated externally.
        :type reconstructedId: str
        """
        self._graphic_novel = graphicNovel
        super().__init__(previousEventIds, reconstructedId)

    @property
    @primary_key_attribute
    def graphic_novel(self) -> "rydnr.storytelling.graphic_novel.GraphicNovel":
        """
        Retrieves the graphic novel.
        :return: The graphic novel.
        :rtype: rydnr.storytelling.graphic_novel.GraphicNovel
        """
        return self._graphic_novel


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
