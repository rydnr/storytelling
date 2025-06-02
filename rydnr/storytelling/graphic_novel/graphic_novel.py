# vim: set fileencoding=utf-8
"""
rydnr/storytelling/graphic_novel/graphic_novel.py

This file defines GraphicNovel class.

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
import os
from pythoneda.shared import attribute, EventListener, listen, primary_key_attribute
from rydnr.storytelling.graphic_novel.events import (
    GraphicNovelCreated,
    GraphicNovelNotCreated,
    GraphicNovelRequested,
)
from .graphic_novel_page import GraphicNovelPage
from typing import List, Union


class GraphicNovel(EventListener):
    """
    Creates GraphicNovel artifacts.

    Class name: GraphicNovel

    Responsibilities:
        - Generate storytelling artifacts.

    Collaborators:
        - None
    """

    def __init__(self, pages: List[GraphicNovelPage] = [], outputFile: str = None):
        """
        Creates a new GraphicNovel instance.
        :param pages: The pages of the graphic novel.
        :type pages: List[rydnr.storytelling.graphic_novel.GraphicNovelPage]
        :param outputFile: The output file.
        :type outputFile: str
        """
        super().__init__()
        self._pages = pages
        self._output_file = outputFile

    @property
    @primary_key_attribute
    def pages(self) -> List[GraphicNovelPage]:
        """
        Retrieves the pages.
        :return: The pages.
        :rtype: List[rydnr.storytelling.graphic_novel.GraphicNovelPage]
        """
        return self._pages

    @property
    @attribute
    def output_file(self) -> str:
        """
        Retrieves the output file.
        :return: The output file.
        :rtype: str
        """
        return self._output_file

    def generate_output(self):
        """
        Generates the output file.
        """
        # TODO: concatenate pages
        content = None
        if content is not None:
            with open(outputFile, "w") as file:
                file.write(content)
            Dot.logger().info(
                f"{outputFile} file created successfully by {self.__class__}"
            )

    @classmethod
    @listen(GraphicNovelRequested)
    async def on_graphic_novel_requested(
        cls, event: GraphicNovelRequested
    ) -> Union[GraphicNovelCreated, GraphicNovelNotCreated]:
        """
        Receives a GraphicNovelRequested event and generates a dot file.
        :param event: The event.
        :type event: rydnr.storytelling.graphic_novel.events.GraphicNovelRequested
        :return: The event representing the graphic novel has been created.
        :rtype: Union[rydnr.storytelling.graphic_novel.events.GraphicNovelCreated,rydnr.storytelling.graphic_novel.events.GraphicNovelNotCreated]
        """
        offset = 0
        page = GraphicNovelPage.next(event.strips_folder, offset)
        while page is not None:
            pages.append(page)
            offset = page.last_strip + 1
            page = GraphicNovelPage.next(event.strips_folder, offset)
        if pages:
            novel = cls(pages, event.output_file)
            novel.generate_output()
            result = GraphicNovelCreated(novel, event.previous_event_ids + [event.id])
        else:
            result = GraphicNovelNotCreated(
                f"Could not create any page from the strips in {event.strips_folder}",
                event.previous_event_ids + [event.id],
            )
        return result


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
