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

# Imports (Python 2.7)
if sys.version_info[0] < 3:
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "package", "app")
    sys.path.append(path)
    sys.path.append(os.path.join(path, "media_converter"))
    import converter as Converter
    import iplugin27 as PluginRegistry

# Imports (Python 3.xx)
else:
    import package.app.media_converter.converter as Converter
    import package.app.iplugin as PluginRegistry


def run(input_file, output_format):
    """
        Main method
    """

    # Input validation
    if input_file is None or output_format is None:
        raise IOError("Please provide an input file and output format")

    # Input file
    if not os.path.isfile(input_file):
        raise IOError("Sorry this input file is invalid.")

    current_dir = path = os.path.join(os.path.dirname(os.path.abspath(__file__)))

    #  Plugin discovery #
    # Load plugins from package/plugins directory
    print("Loading plugins..")
    if sys.version_info[0] < 3:
        plugins = PluginRegistry.discover_plugins([os.path.join(current_dir, "package", "plugins", "media_converter", "python2")])
    else:
        plugins = PluginRegistry.discover_plugins([os.path.join(current_dir, "package", "plugins", "media_converter", "python3")])
    #  Plugin usage #
    # Instance our converter providing a list of discovered plugins
    print("Loading media converter..")
    converter = Converter.Converter(input_file, plugins)

    # Set output format from commandline argument
    converter.set_output_format(output_format)

    # Run encoding task
    converter.encode()
    print("Finished converting!")


if __name__ == '__main__':
    run(sys.argv[1], sys.argv[2])
