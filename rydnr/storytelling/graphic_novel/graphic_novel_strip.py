# vim: set fileencoding=utf-8
"""
rydnr/storytelling/graphic_novel/graphic_novel_strip.py

This file defines StripStrip class.

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
from pythoneda.shared import attribute, EventListener, listen, Ports
from rydnr.storytelling import Painter
from rydnr.storytelling.graphic_novel.events import (
    StripRequested,
    StripCreated,
    StripNotCreated,
)
from .shrink_factor import ShrinkFactor
from typing import List, Union


class GraphicNovelStrip(EventListener):
    """
    Represents strips in graphic novels.

    Class name: GraphicNovelStrip

    Responsibilities:
        - Represent a strip in a graphic novel page.

    Collaborators:
        - None
    """

    def __init__(
        self,
        shrinkFactor: ShrinkFactor,
        stripFile: str,
        stripWidth: int,
        stripHeight: int,
        xPadding: int,
        yPadding: int,
        offset: int,
        rotationDegrees: int = 2,
    ):
        """
        Creates a new StripStrip instance.
        :param shrinkFactor: The shrink factor.
        :type shrinkFactor: rydnr.storytelling.graphic_novel.ShrinkFactor
        :param stripFile: The strip file.
        :type stripFile: str
        :param stripWidth: The width of the strip.
        :type stripWidth: int
        :param stripHeight: The height of the strip.
        :type stripHeight: int
        :param xPadding: The horizontal padding.
        :type xPadding: int
        :param yPadding: The vertical padding.
        :type yPadding: int
        :param offset: The offset.
        :type offset: int
        :param rotationDegrees: The rotation degrees to apply.
        :type rotationDegrees: int
        """
        super().__init__()
        self._shrink_factor = shrinkFactor
        self._strip_file = stripFile
        self._strip_width = stripWidth
        self._strip_height = stripHeight
        self._x_padding = xPadding
        self._y_padding = yPadding
        self._offset = offset
        self._rotation_degrees = rotationDegrees

    @property
    @attribute
    def shrink_factor(self) -> ShrinkFactor:
        """
        Retrieves the shrink factor.
        :return: Such value.
        :rtype: rydnr.storytelling.ShrinkFactor
        """
        return self._shrink_factor

    @property
    @attribute
    def strip_width(self) -> int:
        """
        Retrieves the strip width.
        :return: Such value.
        :rtype: int
        """
        return self._strip_width

    @property
    @attribute
    def strip_height(self) -> int:
        """
        Retrieves the strip height.
        :return: Such value.
        :rtype: int
        """
        return self._strip_height

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

    @property
    @attribute
    def offset(self) -> int:
        """
        Retrieves the offset.
        :return: Such value.
        :rtype: int
        """
        return self._offset

    @property
    @attribute
    def rotation_degrees(self) -> int:
        """
        Retrieves the rotation degrees.
        :return: Such value.
        :rtype: int
        """
        return self._rotation_degrees

    @classmethod
    def for_strip_file(
        cls, stripFile: str
    ) -> "rydnr.storytelling.graphic_novel.StripStrip":
        """
        Retrieves an instance using given file.
        :param stripFile: The strip file.
        :type stripFile: str
        :return: A new StripStrip instance.
        :rtype: rydnr.storytelling.graphic_novel.StripStrip
        """
        # TODO: create an instance
        return None

    @classmethod
    def strip_files_in_folder(cls, folder: str) -> List[str]:
        """
        Retrieves the names of the strip files in given folder.
        :param folder: The folder.
        :type folder: str
        :return: The list of names.
        :rtype: List[str]
        """
        return [
            "0001-evan-intro.png",
            "0002-monday-middleman.png",
            "0003-monday-sarcasm.png",
            "0004-monday-blossom.png",
        ]

    @classmethod
    @listen(StripRequested)
    async def on_strip_requested(
        cls, event: StripRequested
    ) -> Union[StripCreated, StripNotCreated]:
        """
        Receives a StripRequested event and generates a png file.
        :param event: The event.
        :type event: rydnr.storytelling.graphic_novel.events.StripRequested
        :return: The event representing the strip has been created or not.
        :rtype: Union[rydnr.storytelling.graphic_novel.events.StripCreated,rydnr.storytelling.graphic_novel.events.StripNotCreated]
        """
        print(f"Requested strip file: {event.script_file}")

        painter = Ports.instance().resolve_first(Painter)
        if painter is None:
            raise Exception("Painter not found")
        image_bytes = await painter.create(
            "a comic strip of a guy with a hat", 1024, 1024
        )
        with open(event.output_file, "wb") as f:
            f.write(image_bytes)
            print(f"Saved to {event.output_file}")

        result = StripNotCreated(
            f"Could not create a strip from the file {event.script_file}",
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
