# vim: set fileencoding=utf-8
"""
rydnr/storytelling/infrastructure/story/cli/file_story_http_server.py

This file declares the FileStoryHttpServer class.

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
from pythoneda.shared import PrimaryPort
from pythoneda.shared.application import PythonEDA
from rydnr.storytelling.infrastructure.story import FileStory
from typing import Union


class FileStoryHttpServer:
    """
    A PrimaryPort used to launch a FileStoryHttpServer.

    Class name: FileStoryHttpServer

    Responsibilities:
        - Parse the command-line to retrieve the information to run a FileStoryHttpServer instance.

    Collaborators:
        - pythoneda.shared.application.PythonEDA: It is notified back with the information retrieved from the command line.
    """

    def __init__(self, port: int, folder: str):
        """
        Creates a new FileStoryHttpServer instance.
        """
        self._port = port
        self._folder = folder
        super().__init__("Launches a FileStory HTTP Server", "FileStoryHttpServer")

    @property
    def port(self) -> int:
        """
        :return: The port on which the HTTP server will run.
        :rtype: int
        """
        return self._port

    @property
    def folder(self) -> str:
        """
        :return: The folder containing the story strips.
        :rtype: str
        """
        return self._folder

    async def start(self):
        """
        Launches the HTTP server.
        """
        FileStoryHttpServer.logger().info(
            "Starting FileStory HTTP Server on port {self.port} for folder {self.folder} ..."
        )
        sleep(3000)
