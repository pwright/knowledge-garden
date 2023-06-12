from distutils.file_util import write_file
import os
import re
import sys
from pathlib import Path


logseqDir = os.getcwd()
dirName='/skupper-generate/podman/'


print(logseqDir)
for path in Path(logseqDir + dirName).iterdir():
    mdFile=str(path)
    if mdFile.endswith('.adoc'):

        file = open(mdFile, "r")
        replacement = ""
        # using the for loop
        for line in file:
            line = line.strip()
            changes=line
    
            changes = changes.replace("==","=")
            print(changes)
            changes = changes.replace('== Synopsis','.Synopsis')
            changes = changes.replace('----','```')
            changes = changes.replace('== Options', '.Options')
            
            # find end material
            #

            changes = changes.replace('=== Auto ','// Auto ')
            changes = changes.replace('=== Options ','// Options')
            changes = changes.replace('.*  -h, --help .*','// ')
            changes = changes.replace('  -c, --context string      The kubeconfig context to use','// ')
            changes = changes.replace('.*--kubeconfig.*','// ')
            changes = changes.replace('  -n, --namespace string    The Kubernetes namespace to use','// ')

         
         
             # find options

            if (result := re.match(r"skupper (.*)\[flags\]", line)) is not None:
                changes= ' skupper ' + result[1] + ' --[option]\n\n'
            if (result := re.match(r"      --(.*)\b(.*)?[ ]{2,}(.*)", line)) is not None:
                if (optionType := re.split(r"\s", result[1])) is not None:
                    if len(optionType)>1:
                        changes=  optionType[0] + ':: \n' + result[3] + '\n ('+ optionType[1] +')\n'
                    else:
                        changes=  optionType[0] + ':: \n' + result[3] + '\n (bool)\n'

            changes = changes.replace('== SEE ALSO','.See also')
            changes = changes.replace('[discrete\]','')
            changes = changes.replace('^====','// ')
            replacement = replacement + changes + "\n"
        file.close()
        # opening the file in write mode
        fout = open(mdFile, "w")
        fout.write(replacement)
        fout.close()
         

    
