import sys
import maya.cmds as cmds

path = "C:/rumichal/Git/PythonPluginSetup/maya_exporter"
if path not in sys.path:
    sys.path.append("C:/rumichal/Git/PythonPluginSetup/maya_exporter")
from maya_exporter import maya_exporter

sel = cmds.ls(sl=True)
maya_exporter.run(sel[0])
