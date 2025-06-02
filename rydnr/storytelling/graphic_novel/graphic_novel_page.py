# vim: set fileencoding=utf-8
"""
rydnr/storytelling/graphic_novel/graphic_novel_page.py

This file defines GraphicNovelPage class.

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
from pythoneda.shared import BaseObject, attribute
from .shrink_factor import ShrinkFactor
from .graphic_novel_strip import GraphicNovelStrip
from typing import List


class GraphicNovelPage(BaseObject):
    """
    Creates GraphicNovelPage artifacts.

    Class name: GraphicNovelPage

    Responsibilities:
        - Represent a page in a graphic novel.

    Collaborators:
        - None
    """

    def __init__(
        self,
        strips: List[GraphicNovelStrip],
        indexOfLastStrip: int = 0,
        pageWidth: int = 1240,
        pageHeight: int = 1754,
        columns: int = 2,
        xPadding: int = 20,
        yPadding: int = 20,
    ):
        """
        Creates a new GraphicNovelPage instance.
        :param strips: The list of strips.
        :type strips: List[rydnr.storytelling.graphic_novel.GraphicNovelStrip]
        :param indexOfLastStrip: The index of the last strip.
        :type indexOfLastStrip: int
        :param pageWidth: The page width.
        :type pageWidth: int
        :param pageHeight: The page height.
        :type pageHeight: int
        :param columns: The number of columns.
        :type columns: int
        :param xPadding: The X padding.
        :type xPadding: int
        :param yPadding: The Y padding.
        :type yPadding: int
        """
        super().__init__()
        self._strips = strips
        self._index_of_last_strip = indexOfLastStrip
        self._page_width = pageWidth
        self._page_height = pageHeight
        self._columns = columns
        self._x_padding = xPadding
        self._y_padding = yPadding

    @property
    @attribute
    def strips(self) -> List[GraphicNovelStrip]:
        """
        Retrieves the strips.
        :return: Such value.
        :rtype: List[rydnr.storytelling.graphic_novel.GraphicNovelStrip]
        """
        return self._strips

    @property
    @attribute
    def index_of_last_strip(self) -> int:
        """
        Retrieves the index of the last strip.
        :return: Such value.
        :rtype: int
        """
        return self._index_of_last_strip

    @property
    @attribute
    def page_width(self) -> int:
        """
        Retrieves the page width.
        :return: Such value.
        :rtype: int
        """
        return self._page_width

    @property
    @attribute
    def page_height(self) -> int:
        """
        Retrieves the page height.
        :return: Such value.
        :rtype: int
        """
        return self._page_height

    @property
    @attribute
    def columns(self) -> int:
        """
        Retrieves the number of columns.
        :return: Such value.
        :rtype: int
        """
        return self._columns

    @property
    @attribute
    def x_padding(self) -> int:
        """
        Retrieves the X padding.
        :return: Such value.
        :rtype: int
        """
        return self._x_padding

    @property
    @attribute
    def y_padding(self) -> int:
        """
        Retrieves the Y padding.
        :return: Such value.
        :rtype: int
        """
        return self._y_padding

    @classmethod
    def next_batch(cls, stripFiles: List[str], offset: int) -> List[str]:
        """
        Retrieves the next batch of strips.
        :param stripFiles: The list of strip files.
        :type stripFiles: List[str]
        :param offset: The offset.
        :type offset: int
        :return: The next batch of strips.
        :rtype: List[str]
        """
        # TODO: retrieve strips until the next one doesn't fit
        result = []
        for i in range(offset, len(stripFiles)):
            strip = GraphicNovelStrip.for_strip_file(stripFiles[i])
            shrink = ShrinkFactor.for_strip_file(stripFiles[i])
            if strip.width * shrink.shrink > cls.page_width:
                break
            else:
                result.append(stripFiles[i])
        return result

    @classmethod
    def layout(cls, stripFiles: List[str]) -> List[GraphicNovelStrip]:
        """
        Lays out the strips.
        :param stripFiles: The list of strip files.
        :type stripFiles: List[str]
        :return: The laid out strips.
        :rtype: List[rydnr.storytelling.graphic_novel.GraphicNovelStrip]
        """
        # TODO: layout the strips
        return stripFiles

    @classmethod
    def next(cls, stripsFolder: str, offset: int = 0) -> "GraphicNovelPage":
        """
        Creates the next page from strips from given folder.
        :param stripsFolder: The strip folder.
        :type stripsFolder: str
        :param offset: The offset.
        :type offset: int
        :return: A new page.
        :rtype: rydnr.storytelling.GraphicNovelPage
        """
        strip_files = cls.next_batch(
            GraphicNovelStrip.strip_files_in_folder(stripsFolder), offset
        )
        last_strip = offset + len(strip_files)
        # TODO: layout them
        strips = cls.layout(strip_files[offset:last_strip])
        # TODO: create the page
        return cls(strips)


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
