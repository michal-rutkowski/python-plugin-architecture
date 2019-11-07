# -*- Coding: utf-8 -*-
#!/usr/bin/python
# env_exporter.py
"""
    Environment Exporter Plugin
    ~~~~~~~~~~~~~~~~~~

    Exporter plugin for Maya environments.

    Based on article "Fundamental concepts of plugin infrastructures"
    by Eli Bendersky (eliben@gmail.com)

    :Author: Michal Adam Rutkowski
    :Created: 2019/11/6
    :Python Version: 2.7
"""
import os
import sys

from iplugin27 import IPlugin


class EnvironmentExporter(IPlugin):
    """
        Environment exporter plugin
    """
    def __init__(self, maya_object):
        IPlugin.__init__(self)
        self.plugin_name = "Environment Exporter"
        self.maya_prefix = "ENV_"

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

    # hooks
    def _export_hook(self, maya_object):
        print("Exporting " + maya_object + " using " + self.plugin_name)
        return maya_object
