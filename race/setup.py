#! usr/bin/python
# -*- coding:utf-8 -*-
# hqwfq21@gmail.com
from distutils.core import setup
import py2exe
includes = ["encodings", "encodings.*"]
options = {"py2exe":
            {   "compressed": 1,
                "optimize": 2,
                "includes": includes,
                "bundle_files": 1
            }
          }
setup(   
    options = options,
    zipfile=None,
    windows=[{"script": "race.py", "icon_resources": [(1, "boa.ico")] }],  
    
    )
