
output="b'"

for var in $@
do
	#echo $var
	output="$output\\\t$var"
done

	output="$output"\\\\n\'
#$output="${output}\\n"
echo "$output"
echo "$output" | pbcopy
