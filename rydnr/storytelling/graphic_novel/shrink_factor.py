# vim: set fileencoding=utf-8
"""
rydnr/storytelling/graphic_novel/shrink_factor.py

This file defines ShrinkFactor class.

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


class ShrinkFactor(BaseObject):
    """
    Creates ShrinkFactor artifacts.

    Class name: ShrinkFactor

    Responsibilities:
        - Generate storytelling artifacts.

    Collaborators:
        - None
    """

    def __init__(self, shrink: float = 0.5):
        """
        Creates a new ShrinkFactor instance.
        """
        super().__init__()
        self._shrink = shrink

    @property
    @attribute
    def shrink(self) -> float:
        """
        Retrieves the shrink.
        :return: Such value.
        :rtype: float
        """
        return self._shrink

    @classmethod
    def for_strip_file(cls, stripFile: str) -> "ShrinkFactor":
        """
        Figures out the shrink factor for given strip file.
        If no metadata file is present, it reverts to the default.
        :param stripFile: The strip file.
        :type stripFile: str
        :return: The shrink factor.
        :rtype: rydnr.storytelling.ShrinkFactor
        """
        meta_file = f"{stripFile}.metadata"
        if os.path.exists(meta_file):
            with open(meta_file, "r") as f:
                for line in f:
                    if line.strip().startswith("shrink="):
                        try:
                            return cls(float(line.strip().split("=", 1)[1]))
                        except ValueError:
                            pass
        return cls()


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
