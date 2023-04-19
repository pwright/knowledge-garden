dir=../skupper-docs/

for i in $(find $dir -name '*.adoc');
do
    filename=$(basename $i)
    echo $parent_dir_name
    parent=$(basename "$(dirname $i)")
    second_parent=$(basename "$(dirname "$(dirname $i)")")
    outfile=skupper-docs/$second_parent-$parent-$filename
    suffix=.md
    outfile=$(echo $outfile| sed "s/.adoc/.md/")
    downdoc -o $outfile $i
done;