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
    """
        Plugins are stored as a dictionary of {module_name : plugin_class}
        When hot reloading a plugin, the matching dictionary entry is
        simply updated with a new instance.
    """
    plugins = {}

    def __init__(cls, name, bases, attrs):
        """
            Called automatically when a plugin file is imported or reloaded.
        """
        if name != 'Plugin':
            module = str(attrs["__module__"])
            if module not in PluginRegistry.plugins.keys():
                print("Registering new plugin.. " + name)
            PluginRegistry.plugins[module] = cls


class Plugin(object):
    __metaclass__ = PluginRegistry

    def __init__(self):
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
            Checks for matching prefix of maya_object and if there is a match
            returns a concrete implementation of export routine.
            None if the plugin doesn't provide a hook for this role.
        """
        return None


def discover_plugins(dirs):
    """
        Discover the plugin classes contained in Python files, given a
        list of directory names to scan.
        Returns a dictionary of plugin classes.
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
                # Support plugin hot reloading
                imp.reload(module)
    return PluginRegistry.plugins
