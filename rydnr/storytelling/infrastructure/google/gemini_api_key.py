# vim: set fileencoding=utf-8
"""
rydnr/storytelling/infrastructure/cli/google/gemini_api_key.py

This file declares the GeminiApiKey class and exits if the key is not provided
via the GEMINI_API_KEY environment variable.

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
from pythoneda.shared import BaseObject, primary_key_attribute


class GeminiApiKey(BaseObject):
    """
    Represents the OpenAI API key.

    Class name: GeminiApiKey

    Responsibilities:
        - Provides the GEMINI_API_KEY value.

    Collaborators:
        - None
    """

    def __init__(self, key: str):
        """
        Creates a new GeminiApiKey instance.
        :param key: The API key.
        :type key: str
        """
        self._gemini_api_key = key
        super().__init__()

    @property
    @primary_key_attribute
    def key(self) -> str:
        """
        Retrieves the API key.
        :return: Such value.
        :rtype: str
        """
        return self._gemini_api_key

    @classmethod
    def initialize(cls, key: str):
        """
        Initializes the singleton instance with given key.
        :param key: The API key.
        :type key: str
        """
        GeminiApiKey._singleton = GeminiApiKey(key)
        import gemini

        gemini.api_key = key
        GeminiApiKey.logger().debug("OpenAI API key initialized")

    @classmethod
    def instance(cls) -> "GeminiApiKey":
        """
        Retrieves the singleton instance.
        :return: Such instance.
        :rtype: rydnr.storytelling.infrastructure.GeminiApiKey
        """
        return GeminiApiKey._singleton


import os

if os.getenv("GEMINI_API_KEY"):
    GeminiApiKey.initialize(os.getenv("GEMINI_API_KEY"))
else:
    #    print("GEMINI_API_KEY is mandatory")
    import sys

#    sys.exit(1)
