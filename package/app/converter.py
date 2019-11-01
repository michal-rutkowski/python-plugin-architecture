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
    def __init__(self, input, plugins=[]):
        self.queue = RenderQueue.RenderQueue()
        self.input = input
        self.plugins = plugins
        self.input_raw = self._decode_input(input)

    def set_output_format(self, format):
        if "." not in format:
            format = "." + format
        self.output_format = format

    def encode(self):
        self._encode_input(self.output_format)

    def _decode_input(self, input):
        processing_method = self._get_processing_hook(input, ProcessingMode.DECODE)
        decode_task = RenderQueue.RenderTask(processing_method, self.input)
        self.queue.add_task(decode_task)
        results = self.queue.run()
        return results[0]

    def _encode_input(self, output_format):
        processing_method = self._get_processing_hook(output_format, ProcessingMode.ENCODE)

    def _get_processing_hook(self, input, processing_mode):
        # Plugins are classes - we need to instantiate them to get objects.
        plugins = [P(input) for P in self.plugins]
        for p in plugins:
            hook = p.get_decode_hook(input) if processing_mode == ProcessingMode.DECODE else p.get_encode_hook(input)
            if hook:
                print("Found appropriate plugin", hook)
                return hook
        raise RuntimeError("Sorry could not find appropriate plugin")
