dir=../skupper-docs/

for i in $(find $dir -name '*.adoc');
do
    filename=$(basename $i)
    echo $parent_dir_name
    parent=$(basename "$(dirname $i)")
    second_parent=$(basename "$(dirname "$(dirname $i)")")
     # %2F represents a ns in logseq
    outfile=skupper-docs/$second_parent%2F$parent%2F$filename
    suffix=.md
    outfile=$(echo $outfile| sed "s/.adoc/.md/")
   
    downdoc -o $outfile $i
   
    sed -i -z 's/\n==/\n##/g' $outfile
    sed -i -z 's/\n=/\n#/g' $outfile
    sed -i 's/endif.*//g' $outfile
    sed -i 's/\[id="\(.*\)"]/sid:: \1/' $outfile
done;