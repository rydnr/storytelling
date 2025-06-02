# vim: set fileencoding=utf-8
"""
rydnr/storytelling/infrastructure/google/imagen_painter.py

This file defines the ImagenPainter lass.

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
# from google import genai
# from google.genai import types

from rydnr.storytelling import Painter


class ImagenPainter(Painter):
    """
    Google Gemini's implementation of the Painter port.

    Class name: ImagenPainter

    Responsibilities:
        - Is able to create images using Google Gemini.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new ImagenPainter instance.
        """
        super().__init__()

    async def create(self, prompt: str, width: int, height: int) -> bytes:
        """
        Creates a new image.
        :param prompt: The prompt for the image.
        :type prompt: str
        :param width: The width of the image.
        :type width: int
        :param height: The height of the image.
        :type height: int
        :return: The image bytes.
        :rtype: bytes
        """
        client = genai.AsyncClient()
        response = await client.models.generate_content(
            model="imagen-2.0-flash-preview-image-generation",
            contents=(prompt),
            config=types.GenerateContentConfig(response_modalities=["TEXT", "IMAGE"]),
        )
        image_base64 = response.data[0].b64_json
        return base64.b64decode(image_base64)


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
