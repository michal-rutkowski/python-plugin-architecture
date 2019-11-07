# -*- Coding: utf-8 -*-
#!/usr/bin/python
# exporter_core.py
"""
    Exporter Core
    ~~~~~~~~~~~~~~~~~~

    Maya asset exporter tool core class.
    Uses plugins to determine export routines based on object name prefix.

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


class ExporterCore():
    """
        Maya Exporter core object.
        Call run() method with a Maya object to kick off exporting.
    """
    def __init__(self, plugins=[]):
        """
            Initialize with plugin list.
        """
        self.plugins = plugins

    def run(self, maya_object):
        """
            Kicks off exporting (public)
        """
        print("Exporting... " + maya_object)
        self._export_input(maya_object)

    def _export_input(self, maya_object):
        """
            Private export routine implementation.
            Tries to find matching export routine for maya_object
            based on name prefix, then calls that routine if found.
        """
        processing_method = self._get_processing_hook(maya_object)
        processing_method(maya_object)

    def _get_processing_hook(self, maya_object):
        """
            Scans plugins to looks for appropriate export method.
            Takes input filename and returns hook if found.
            Note that name matching is handled by plugins.
        """
        #  Plugin usage #
        # Plugins are classes - we need to instantiate them to get objects.
        plugins = [P(maya_object) for P in self.plugins]
        for p in plugins:
            hook = p.get_export_hook(maya_object)
            if hook:
                return hook
        raise RuntimeError("Sorry could not find appropriate plugin")
