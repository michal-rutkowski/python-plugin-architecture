# -*- Coding: utf-8 -*-
#!/usr/bin/python
# App.py
"""
    Plugin demo app
    ~~~~~~~~~~~~~~~~~~

    Demo project for plugin based architecture in Python 3
    A simple media converter example is provided.
    Plugins are used for both decoding and encoding files.

    Usage:
    py app.py [filename] [output extension]

    :Author: Michal Adam Rutkowski
    :Created: 2019/10/31
    :Python Version: 2.7/3.7
"""
import os
import sys

# python 2.7
if sys.version_info[0] < 3:
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "package", "app", "media_converter")
    sys.path.append(path)
    import converter as Converter
    import iplugin27 as PluginRegistry
# python 3.xx
else:
    import package.app.converter as Converter
    import package.app.iplugin as PluginRegistry


class MediaConverter():
    def __init__(self):
        #  Plugin discovery #
        # Load plugins from package/plugins directory
        print("Loading plugins..")
        current_dir = path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
        if sys.version_info[0] < 3:
            plugins = PluginRegistry.discover_plugins([os.path.join(current_dir, "package", "plugins", "media_converter", "python2")])
        else:
            plugins = PluginRegistry.discover_plugins([os.path.join(current_dir, "package", "plugins", "media_converter", "python3")])
        self.plugins = plugins

    def run(self, input_file, output_format):
        # Parse commandline arguments
        current_dir = path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
        if input_file is None or output_format is None:
            raise IOError("Please provide an input file and output format")

        # Input file
        if not os.path.isfile(input_file):
            raise IOError("Sorry this input file is invalid.")

        #  Plugin usage #
        # Instance our converter providing a list of discovered plugins
        print("Loading media converter..")
        converter = Converter.Converter(input_file, self.plugins)

        # Set output format from commandline argument
        converter.set_output_format(output_format)

        # Run encoding task
        converter.encode()
        print("Finished converting!")
