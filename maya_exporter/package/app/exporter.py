# -*- Coding: utf-8 -*-
#!/usr/bin/python
# maya_exporter.py
"""
    Maya Exporter
    ~~~~~~~~~~~~~~~~~~

    Simple file converter class.

    Based on article "Fundamental concepts of plugin infrastructures"
    by Eli Bendersky (eliben@gmail.com)

    :Author: Michal Adam Rutkowski
    :Created: 2019/11/6
    :Python Version: 2.7
"""
import os
import sys

# python 2.7
import iplugin27 as PluginRegistry


class Exporter():
    """
    Main media converter processor class.
    Initializer takes input filename and plugin list.
    """
    def __init__(self, input, plugins=[]):
        self.input = input
        self.plugins = plugins

    def run(self):
        """
        Run exporting (public method)
        """
        print("Exporting... " + self.input)
        self._export_input()

    def _export_input(self):
        """
        Run exporting (private method)
        """
        processing_method = self._get_processing_hook(self.input)
        processing_method(self.input)

    def _get_processing_hook(self, input):
        """
        Scans plugins to looks for appropriate encoding/decoding method.
        Takes input filename and processing mode enum.
        Returns hook if found.
        """
        #  Plugin usage #
        # Plugins are classes - we need to instantiate them to get objects.
        plugins = [P(input) for P in self.plugins]
        for p in plugins:
            hook = p.get_export_hook(input)
            if hook:
                return hook
        raise RuntimeError("Sorry could not find appropriate plugin")
