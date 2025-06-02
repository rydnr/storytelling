# vim: set fileencoding=utf-8
"""
rydnr/storytelling/infrastructure/story/cli/file_story_http_server_start_requested_cli.py

This file declares the StartFileStoryHttpServerCli class.

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
from argparse import ArgumentParser
from pythoneda.shared import PrimaryPort
from pythoneda.shared.application import PythonEDA
from pythoneda.shared.infrastructure.cli import CliHandler
from rydnr.storytelling.infrastructure.story.http import FileStoryHttpServer
from typing import Union


class StartFileStoryHttpServerCli(CliHandler, PrimaryPort):
    """
    A PrimaryPort used to launch a FileStoryHttpServer.

    Class name: StartFileStoryHttpServerCli

    Responsibilities:
        - Parse the command-line to retrieve the information to run a FileStoryHttpServer instance.

    Collaborators:
        - pythoneda.shared.application.PythonEDA: It is notified back with the information retrieved from the command line.
    """

    def __init__(self):
        """
        Creates a new StartFileStoryHttpServerCli instance.
        """
        super().__init__(
            "Launches a FileStory HTTP Server", "StartFileStoryHttpServerCli"
        )

    @classmethod
    def priority(self) -> int:
        """
        Retrieves the priority of this port.
        :return: The priority.
        :rtype: int
        """
        return 90

    @classmethod
    @property
    def is_one_shot_compatible(cls) -> bool:
        """
        Retrieves whether this primary port should be instantiated when
        "one-shot" behavior is active.
        It should return False unless the port listens to future messages
        from outside.
        :return: True in such case.
        :rtype: bool
        """
        return False

    def add_arguments(self, parser: ArgumentParser):
        """
        Defines the specific CLI arguments.
        :param parser: The parser.
        :type parser: argparse.ArgumentParser
        """
        parser.add_argument(
            "-p",
            "--port",
            required=True,
            help="The port on which the prompt server will run",
        )
        parser.add_argument(
            "-f", "--story-folder", required=True, help="The story folder"
        )

    async def handle(self, app: PythonEDA, args):
        """
        Processes the command specified from the command line.
        :param app: The PythonEDA instance.
        :type app: pythoneda.shared.application.PythonEDA
        :param args: The CLI args.
        :type args: argparse.args
        """
        await FileStoryHttpServer(args.port, args.story_folder).start()
