grep "Question" $1 | cut  -d , -f 1,5 | cut  -d / -f 4-6 | sort -t , -k 2 -r | head