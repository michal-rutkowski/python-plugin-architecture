# -*- Coding: utf-8 -*-
#!/usr/bin/python
# App.py
"""
    Maya Exporter Demo
    ~~~~~~~~~~~~~~~~~~

    Demo project for plugin based architecture in Python 2.7
    This is a simple exporter for Maya assets based on object prefix.

    :Author: Michal Adam Rutkowski
    :Created: 2019/10/31
    :Python Version: 2.7/3.7
"""
import os
import sys

# Imports (Python 2.7)
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "package", "app", "maya_exporter"))
import exporter as Exporter
import iplugin27 as PluginRegistry


def run(maya_object):
    """
        Main method
    """
    current_dir = path = os.path.join(os.path.dirname(os.path.abspath(__file__)))

    #  Plugin discovery #
    # Load plugins from package/plugins directory
    print("Loading plugins..")
    plugins_path = os.path.join(current_dir, "package", "plugins", "maya_exporter")
    plugins = PluginRegistry.discover_plugins([plugins_path])
    #print("Plugins loaded:" + " ".join([p.plugin_name for p in plugins]))

    #  Plugin usage #
    # Instance maya exporter providing a list of discovered plugins
    print("Loading exporter..")
    exporter = Exporter.Exporter(maya_object, plugins)

    # Run exporter
    exporter.run()
    print("Finished exporting!")


if __name__ == '__main__':
    run(sys.argv[1])
