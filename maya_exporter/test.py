# -*- Coding: utf-8 -*-
#!/usr/bin/python

import sys
import maya.cmds as cmds

# Read script from local path (or copy to maya2019/Scripts)
path = "C:/rumichal/Git/PythonPluginSetup/maya_exporter"
if path not in sys.path:
    sys.path.append(path)

# Import main module
import maya_exporter

# Get first selected object in Maya
sel = cmds.ls(sl=True)[0]

# Export selection
maya_exporter.run(sel)
