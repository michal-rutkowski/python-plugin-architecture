# -*- Coding: utf-8 -*-
#!/usr/bin/python
# App.py
"""
    Plugin demo app
    ~~~~~~~~~~~~~~~~~~

    Demo project for plugin based architecture in Python 3

    :Author: Michal Adam Rutkowski
    :Created: 2019/10/31
    :Python Version: 3.7
"""
import os
import sys

import package.app.iplugin as PluginRegistry

if __name__ == '__main__':
    # Load plugins from package/plugins directory
    mydir = os.path.dirname(sys.argv[0])
    plugins = PluginRegistry.discover_plugins([os.path.join(mydir, "package", "plugins")])
    print(plugins)
