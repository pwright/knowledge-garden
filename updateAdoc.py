from distutils.file_util import write_file
import os
import re
import sys
from pathlib import Path


logseqDir = os.getcwd()
dirName='/skupper-generate/cli/'


print(get_current_dir())
for path in Path(logseqDir + dirName).iterdir():
    mdFile=str(path)
    if mdFile.endswith('.adoc'):

        file = open(mdFile, "r")
        replacement = ""
        # using the for loop
        for line in file:
            line = line.strip()
    
            changes = line.replace(line,'^==','=')
            changes = line.replace(line,'== Synopsis','.Synopsis')
            changes = line.replace(line,'----','')
            changes = line.replace(line,'== Options', '.Options')
            
            # find end material
            #


            changes = line.replace(line,'.*  -h, --help .*','// ')
            changes = line.replace(line,'  -c, --context string      The kubeconfig context to use','// ')
            changes = line.replace(line,'.*--kubeconfig.*','// ')
            changes = line.replace(line,'  -n, --namespace string    The Kubernetes namespace to use','// ')

         
         
             # find options

            if (result := re.match(r"skupper (.*)\[flags\]", line)) is not None:
                line= ' skupper ' + result[1] + ' --[option]\n\n'
            if (result := re.match(r"      --(.*)\b(.*)?[ ]{2,}(.*)", line)) is not None:
                if (optionType := re.split(r"\s", result[1])) is not None:
                    if len(optionType)>1:
                        line=  optionType[0] + ':: \n' + result[3] + '\n ('+ optionType[1] +')\n'
                    else:
                        line=  optionType[0] + ':: \n' + result[3] + '\n (bool)\n'
            changes = line.replace(line,'== SEE ALSO','.See also')
            changes = line.replace(line,'\[discrete\]','')
            changes = line.replace(line,'^====','// ')
        file.close()
        # opening the file in write mode
        fout = open(mdFile, "w")
        fout.write(replacement)
        fout.close()
         

    
