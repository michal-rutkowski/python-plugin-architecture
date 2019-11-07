# -*- Coding: utf-8 -*-
#!/usr/bin/python
# maya_exporter.py
"""
    Maya Exporter Demo
    ~~~~~~~~~~~~~~~~~~

    Demo project for plugin based architecture in Python 2.7

    Maya asset exporter tool.
    Uses plugins to determine export routines based on object name prefix.

    :Author: Michal Adam Rutkowski
    :Created: 2019/10/31
    :Python Version: 2.7/3.7
"""
import os
import sys

import package.app as Core


def run(maya_object):
    """
        Entry point for exporting routine.
        Loads plugins and passes maya_object to ExporterCore.
    """
    current_dir = path = os.path.join(os.path.dirname(os.path.abspath(__file__)))

    #  Plugin discovery #
    # Load plugins from package/plugins directory
    print("Loading plugins..")
    plugins_path = os.path.join(current_dir, "package", "plugins")
    plugins = Core.PluginRegistry.discover_plugins([plugins_path])

    #  Plugin usage #
    # Instance maya exporter providing a list of discovered plugins
    print("Loading exporter..")
    exporter = Core.ExporterCore.ExporterCore(plugins)

    # Run exporter
    exporter.run(maya_object)
    print("Finished exporting!")


if __name__ == '__main__':
    run(sys.argv[1])
