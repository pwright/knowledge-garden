from distutils.file_util import write_file
import os
import re
import sys
from pathlib import Path

logseqDir = os.getcwd()
dirName='/skupper-generate/podman/'

#print(get_current_dir())
for path in Path(logseqDir + dirName).iterdir():
    mdFile=str(path)
    if mdFile.endswith('.md'):
        print(mdFile)
        cmd = "kramdoc --format=GFM --wrap=ventilate " + mdFile 
    
        result = os.system(cmd)
        print(result)