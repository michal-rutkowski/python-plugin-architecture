# -*- Coding: utf-8 -*-
#!/usr/bin/python
# converter.py
"""
    Converter
    ~~~~~~~~~~~~~~~~~~

    Simple file converter class.

    Based on article "Fundamental concepts of plugin infrastructures"
    by Eli Bendersky (eliben@gmail.com)

    :Author: Michal Adam Rutkowski
    :Created: 2019/10/31
    :Python Version: 3.7
"""
import os
from enum import Enum

import package.app.render_queue as RenderQueue
import package.app.iplugin as IPluginRegistry


class ProcessingMode(Enum):
    DECODE = 1
    ENCODE = 2


class Converter():
    """
    Main media converter processor class.
    Initializer takes input filename and plugin list.
    """
    def __init__(self, input, plugins=[]):
        self.queue = RenderQueue.RenderQueue()
        self.input = input
        self.plugins = plugins
        self.input_raw = self._decode_input(input)

    def set_output_format(self, format):
        """
        Setter for output format
        """
        if "." not in format:
            format = "xxx." + format
        self.output_format = format

    def encode(self):
        """
        Run encoding (public method)
        """
        assert self.output_format, "Output format unspecified"
        self._encode_input()

    def _decode_input(self, input):
        """
        Decodes input and returns raw data. Called by initializer.
        """
        processing_method = self._get_processing_hook(input, ProcessingMode.DECODE)
        decode_task = RenderQueue.RenderTask(processing_method, self.input)
        self.queue.add_task(decode_task)
        return self.queue.run()[0]

    def _encode_input(self):
        """
        Run encoding (private method)
        """
        processing_method = self._get_processing_hook(self.output_format, ProcessingMode.ENCODE)
        encode_task = RenderQueue.RenderTask(processing_method, ProcessingMode.ENCODE)
        self.queue.add_task(encode_task)
        return self.queue.run()[0]

    def _get_processing_hook(self, input, processing_mode):
        """
        Scans plugins to looks for appropriate encoding/decoding method.
        Takes input filename and processing mode enum.
        Returns hook if found.
        """
        #  Plugin usage #
        # Plugins are classes - we need to instantiate them to get objects.
        plugins = [P(input) for P in self.plugins]
        for p in plugins:
            hook = p.get_decode_hook(input) if processing_mode == ProcessingMode.DECODE else p.get_encode_hook(input)
            if hook:
                return hook
        raise RuntimeError("Sorry could not find appropriate plugin")
