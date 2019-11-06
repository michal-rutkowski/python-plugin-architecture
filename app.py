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
    :Python Version: 3.7
"""
import os
import sys

# python 2.7
if sys.version_info[0] < 3:
    sys.path.append("./package/app")
    import converter as Converter
    import iplugin27 as PluginRegistry
# python 3.xx
else:
    import package.app.converter as Converter
    import package.app.iplugin as PluginRegistry

if __name__ == '__main__':
    # Parse commandline arguments
    current_dir = os.path.dirname(sys.argv[0])
    if len(sys.argv) < 3:
        raise IOError("Please provide an input file and output format")

    # Input file
    input_file = os.path.abspath(sys.argv[1])
    if not os.path.isfile(input_file):
        raise IOError("Sorry this input file is invalid.")

    #  Plugin discovery #
    # Load plugins from package/plugins directory
    print("Loading plugins..")
    if sys.version_info[0] < 3:
        plugins = PluginRegistry.discover_plugins([os.path.join(current_dir, "package", "plugins", "python2")])
    else:
        plugins = PluginRegistry.discover_plugins([os.path.join(current_dir, "package", "plugins", "python3")])
    #  Plugin usage #
    # Instance our converter providing a list of discovered plugins
    print("Loading media converter..")
    converter = Converter.Converter(input_file, plugins)

    # Set output format from commandline argument
    converter.set_output_format(sys.argv[2])

    # Run encoding task
    converter.encode()
    print("Finished converting!")
