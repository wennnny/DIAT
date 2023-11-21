#!/usr/bin/python3
import os
from ctypes import *

os.environ["path"] += ";/"
lib = CDLL("libRobotFactoryPythonBridge.dll", winmode = 0)

print(lib)