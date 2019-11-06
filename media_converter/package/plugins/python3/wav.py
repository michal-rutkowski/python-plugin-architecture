# -*- Coding: utf-8 -*-
#!/usr/bin/python
# iplugin.py
"""
    WAV Plugin
    ~~~~~~~~~~~~~~~~~~

    I/O Plugin for wav media file.

    Based on article "Fundamental concepts of plugin infrastructures"
    by Eli Bendersky (eliben@gmail.com)

    :Author: Michal Adam Rutkowski
    :Created: 2019/11/1
    :Python Version: 3.7
"""
import os
from package.app.iplugin import IPlugin


class Wav(IPlugin):
    def __init__(self, file):
        super().__init__(file)
        self.file_extension = ".wav"

    # hook getters
    def get_encode_hook(self, file):
        return self._encode_hook if self._get_extension(file) == self.file_extension else None

    def get_decode_hook(self, file):
        return self._decode_hook if self._get_extension(file) == self.file_extension else None

    # hooks
    def _encode_hook(self, file):
        print("Encoding data to", self.file_extension)
        return file

    def _decode_hook(self, file):
        print("Decoding data from", self.file_extension)
        return file

    # private methods
    def _decode(self, file):
        return file

    def _encode(self, file):
        return file
