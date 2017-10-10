
for file in $@
do
	result1=$(wc $file)
	output="b'"
	for var in $result1
	do
		output="$output\\\t$var"
	done
	output="$output"\\\\n\'
	echo ">>> test('"$file"')"
	echo $output

	result2=$(wc -w $file)
	output="b'"
	for var in $result2
	do
		output="$output\\\t$var"
	done
	output="$output"\\\\n\'
	echo ">>> test('-w "$file"')"
	echo $output

	result3=$(wc -l $file)
	output="b'"
	for var in $result3
	do
		output="$output\\\t$var"
	done
	output="$output"\\\\n\'
	echo ">>> test('-l "$file"')"
	echo $output


	result4=$(wc -c $file)
	output="b'"
	for var in $result4
	do
		output="$output\\\t$var"
	done
	output="$output"\\\\n\'
	echo ">>> test('-c "$file"')"
	echo $output

	result5=$(wc -cw $file)
	output="b'"
	for var in $result5
	do
		output="$output\\\t$var"
	done
	output="$output"\\\\n\'
	echo ">>> test('-cw "$file"')"
	echo $output

	result6=$(wc -cl $file)
	output="b'"
	for var in $result6
	do
		output="$output\\\t$var"
	done
	output="$output"\\\\n\'
	echo ">>> test('-cl "$file"')"
	echo $output

	result7=$(wc -wl $file)
	output="b'"
	for var in $result7
	do
		output="$output\\\t$var"
	done
	output="$output"\\\\n\'
	echo ">>> test('-wl "$file"')"
	echo $output

	result8=$(wc -wc $file)
	output="b'"
	for var in $result8
	do
		output="$output\\\t$var"
	done
	output="$output"\\\\n\'
	echo ">>> test('-wc "$file"')"
	echo $output

	result9=$(wc -lc $file)
	output="b'"
	for var in $result9
	do
		output="$output\\\t$var"
	done
	output="$output"\\\\n\'
	echo ">>> test('-lc "$file"')"
	echo $output

	result10=$(wc -lw $file)
	output="b'"
	for var in $result10
	do
		output="$output\\\t$var"
	done
	output="$output"\\\\n\'
	echo ">>> test('-lw "$file"')"
	echo $output

	result11=$(wc -clw $file)
	output="b'"
	for var in $result11
	do
		output="$output\\\t$var"
	done
	output="$output"\\\\n\'
	echo ">>> test('-clw "$file"')"
	echo $output

	result12=$(wc -wclwcllc $file)
	output="b'"
	for var in $result12
	do
		output="$output\\\t$var"
	done
	output="$output"\\\\n\'
	echo ">>> test('-wclwcllc "$file"')"
	echo $output

	result13=$(wc -w $file -c $file)
	output="b'"
	for var in $result13
	do
		output="$output\\\t$var"
	done
	output="$output"\\\\n\'
	echo ">>> test('-w "$file" -c "$file"')"
	echo $output

	result14=$(wc -l $file -wc $file -wl -c $file)
	output="b'"
	for var in $result14
	do
		output="$output\\\t$var"
	done
	output="$output"\\\\n\'
	echo ">>> test('-l "$file" -wc "$file" -wl -c "$file"')"
	echo $output

	result15=$(wc $file -w $file $file -ww -c $file)
	output="b'"
	for var in $result15
	do
		output="$output\\\t$var"
	done
	output="$output"\\\\n\'
	echo ">>> test('"$file" -w "$file" "$file" -ww -c "$file"')"
	echo $output
	echo ""
done


result=$(wc $@)
output="b'"
for var in $result
do
	output="$output\\\t$var"
done
output="$output"\\\\n\'
echo ">>> test('"$@"')"
echo $output
echo ""


args=$@
flags=('c','l','w')
command=''
for i in {1..10}
do
	command=$command${args[ $RANDOM % 12 ]}" "
done
#echo $command
result14=$(wc $command)
output="b'"
for var in $result14
do
	output="$output\\\t$var"
done
output="$output"\\\\n\'
#echo ">>> test('"$command"')"
#echo $output
