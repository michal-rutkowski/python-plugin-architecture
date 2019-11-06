# -*- Coding: utf-8 -*-
#!/usr/bin/python
# chr.py
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


class Chr(IPlugin):
    """
    Environment exporter
    """
    def __init__(self, maya_object):
        super(Chr, self).__init__(maya_object)
        self.plugin_name = "Character Exporter"
        self.maya_prefix = "CHR_"

    # hook getters
    def get_export_hook(self, maya_object):
        return self._export_hook if maya_object.startswith(self.maya_prefix) else None

    # hooks
    def _export_hook(self, maya_object):
        print("Exporting " + maya_object + " using " + self.plugin_name)
        return maya_object
