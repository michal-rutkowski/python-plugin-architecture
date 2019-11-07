# -*- Coding: utf-8 -*-
#!/usr/bin/python
# chr_exporter.py
"""
    Character Exporter Plugin
    ~~~~~~~~~~~~~~~~~~

    Exporter plugin for Maya characters.

    Based on article "Fundamental concepts of plugin infrastructures"
    by Eli Bendersky (eliben@gmail.com)

    :Author: Michal Adam Rutkowski
    :Created: 2019/11/6
    :Python Version: 2.7
"""
import os
import sys

from iplugin27 import IPlugin


class CharacterExporter(IPlugin):
    """
        Environment exporter plugin
    """
    def __init__(self, maya_object):
        IPlugin.__init__(self)
        self.plugin_name = "Character Exporter"
        self.maya_prefix = "CHR_"

    def get_prefix(self):
        """
            Returns Maya object prefix this plugin expects
        """
        return self.maya_prefix

    def get_export_hook(self, maya_object):
        """
            Getter method for export hook.
            Condition matching is handled here.
            This example uses a simple object name prefix.
        """
        return self._export_hook if maya_object.startswith(self.maya_prefix) else None

    def _export_hook(self, maya_object):
        """
            Export routine concrete implementation
        """
        return maya_object
