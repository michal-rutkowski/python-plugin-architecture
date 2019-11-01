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

import package.app.converter as Converter
import package.app.iplugin as PluginRegistry

if __name__ == '__main__':
    current_dir = os.path.dirname(sys.argv[0])
    if len(sys.argv) < 3:
        raise IOError("Please provide an input file and output format")

    input_file = os.path.abspath(sys.argv[1])
    if not os.path.isfile(input_file):
        raise IOError("Sorry this input file is invalid.")

    # Load plugins from package/plugins directory
    print("Loading plugins..")
    plugins = PluginRegistry.discover_plugins([os.path.join(current_dir, "package", "plugins")])
    #print(plugins)

    # Instance our converter
    print("Loading media converter..")
    converter = Converter.Converter(input_file, plugins)
    converter.set_output_format(sys.argv[2])
    converter.encode()
