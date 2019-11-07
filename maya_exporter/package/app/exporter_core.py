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

from plugin import PluginRegistry

import maya.cmds as cmds


class ExporterCore():
    """
        Maya Exporter core object.
        Call run() method with a Maya object to kick off exporting.
    """
    def __init__(self, plugins={}):
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
        plugin_name, processing_method = self._get_processing_hook(maya_object)

        # handle error when object name is not supported
        if processing_method is None:
            prefixes_dict = self._get_all_prefixes()
            error_msg = "Please rename your object to use one of supported plugin prefixes:\n"
            error_msg += str(prefixes_dict).replace("{", "").replace("}", "").replace("'", "").replace(", ", "\n")
            cmds.confirmDialog(
                title="Maya Exporter",
                message=error_msg,
                button=["Cancel"],
                defaultButton="Cancel")
            return

        # show confirm dialog before exporting
        dialog_msg = "Would you like to export " + maya_object + " using " + plugin_name + "?"
        confirm_button = "OK"
        result = cmds.confirmDialog(
            title="Maya Exporter",
            message=dialog_msg,
            button=[confirm_button, "Cancel"],
            defaultButton=confirm_button,
            cancelButton="Cancel",
            dismissString="Cancel")

        # if everything is ok run export routine
        if(result == confirm_button):
            processing_method(maya_object)

    def _get_processing_hook(self, maya_object):
        """
            Scans plugins to looks for appropriate export method.
            Takes input filename and returns hook if found.
            Note that name matching is handled by plugins.
        """
        # Plugins are classes - we need to instantiate them to get objects.
        plugins = [P(maya_object) for P in self.plugins.values()]
        for p in plugins:
            hook = p.get_export_hook(maya_object)
            if hook:
                return p.plugin_name, hook
        return None, None

    def _get_all_prefixes(self):
        """
            Scans plugins and returns all supported object prefices.
        """
        # Plugins are classes - we need to instantiate them to get objects.
        plugins = [P("default") for P in self.plugins.values()]
        prefix_dict = {}
        for p in plugins:
            prefix_dict[p.plugin_name] = p.get_prefix()
        return prefix_dict
