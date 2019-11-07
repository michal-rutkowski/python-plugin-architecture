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

import maya.cmds as cmds


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

    def _export_hook(self, maya_object):
        """
            Export routine concrete implementation
        """
        # group asset
        grp = cmds.group(maya_object, n='ENV_ASSET')

        # create lods for environment assets (example)
        object_renamed = cmds.rename(maya_object, maya_object + "_LOD0")
        for i in range(2):
            new_lod = cmds.duplicate(object_renamed)
            cmds.polyReduce(new_lod, p=50.0)
            cmds.delete(new_lod, ch=1)
            object_renamed = cmds.rename(new_lod, maya_object + "_LOD" + str(i+1))

        return maya_object
