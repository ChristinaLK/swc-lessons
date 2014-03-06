# middle.sh shows lines from the middle of a text file
# USAGE: middle.sh filename entry_line exit_line

head $2 $1 | tail $3 
