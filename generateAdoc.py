from distutils.file_util import write_file
import os
import re
import sys
from pathlib import Path

def modify_heading(file_path, addition):
    with open(file_path, 'r', encoding='utf-8') as file:
        contents = file.readlines()

    for i, line in enumerate(contents):
        # Match the first Markdown heading
        if re.match(r'^## .+', line):
            print(contents[i])
            #contents[i] = re.sub(r'^(# .+)', r'\1 (' + addition + ')', line)
            contents[i] = contents[i].strip() + ' (' + addition + ')'
            break

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(contents)

logseqDir = os.getcwd()
dirName='/skupper-generate/' + sys.argv[1]

#print(get_current_dir())
for path in Path(logseqDir + dirName).iterdir():
    mdFile=str(path)
    if mdFile.endswith('.md'):
        modify_heading(mdFile, sys.argv[1])
        cmd = "kramdoc --format=GFM --wrap=ventilate " + mdFile 
    
        result = os.system(cmd)
        print(result)


