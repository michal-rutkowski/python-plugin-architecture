# -*- Coding: utf-8 -*-
#!/usr/bin/python
# plugin.py
"""
    Plugin Interface
    ~~~~~~~~~~~~~~~~~~

    Plugin and PluginRegistry interface classes.
    Plugins inheriting from Plugin placed in
    the plugins directory are automatically discovered.

    Based on article "Fundamental concepts of plugin infrastructures"
    by Eli Bendersky (eliben@gmail.com)

    :Author: Michal Adam Rutkowski
    :Created: 2019/11/6
    :Python Version: 2.7
"""
import importlib
import imp

import os
import sys


class PluginRegistry(type):
    plugins = []
    def __init__(cls, name, bases, attrs):
        # Added check for existing entries to ensure dynamic reload support
        if name != 'Plugin' and name not in PluginRegistry.plugins:
            PluginRegistry.plugins.append(cls)


class Plugin(object):
    __metaclass__ = PluginRegistry
    def __init__(self, plugin_name=None):
        """
            Initialize the plugin.
        """
        return

    """
        Plugin classes inherit from Plugin. The methods below can be
        implemented to provide services.
    """

    def get_export_hook(self, maya_object):
        """
            Return a function accepting full document contents.
            The functin will be called with a single argument - the document
            contents (after paragraph splitting and role processing), and
            should return the transformed contents.
            None if the plugin doesn't provide a hook for this role.
        """
        return None


def discover_plugins(dirs):
    """
        Discover the plugin classes contained in Python files, given a
        list of directory names to scan. Return a list of plugin classes.
    """
    for dir in dirs:
        for filename in os.listdir(dir):
            modname, ext = os.path.splitext(filename)
            if ext == '.py':
                # importlib throws error when passing absolute path
                if dir not in sys.path:
                    sys.path.append(os.path.abspath(dir))
                # Loading the module registers the plugin in PluginRegistry
                module = importlib.import_module(modname)
                # This is for development only
                imp.reload(module)
    return PluginRegistry.plugins
