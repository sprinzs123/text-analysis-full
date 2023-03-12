#!/bin/bash



# get all templates for front end
# cat through all templates to see that include tags they have
cd ../
all_templates=`find  -type f -name "*.html" | grep news`

result=""

# iterate over all the html files absolute found
# get parent file name
# cat that file and see what include templates it has
for file in $all_templates;
do

	file_name=`echo $file | grep -o "[a-zA-Z_]\+.html"`
	all_includes=`cat $file | grep include | grep -o "[a-zA-Z_]\+.html"`
	result+=$file_name"="$all_includes
	result+=";"
done

echo $result



