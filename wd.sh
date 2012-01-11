#!/bin/sh
# Uses the python wrd program to print out multiple scriptures
# Options for $1 are 2 to 7

case "$1" in
	2) wrd;echo;wrd
	;;
	3) wrd;echo;wrd;echo;wrd
	;;
	4) wrd;echo;wrd;echo;wrd;echo;wrd
	;;
	5) wrd;echo;wrd;echo;wrd;echo;wrd;echo;wrd
	;;
	6) wrd;echo;wrd;echo;wrd;echo;wrd;echo;wrd;echo;wrd
	;;
	7) wrd;echo;wrd;echo;wrd;echo;wrd;echo;wrd;echo;wrd;echo;wrd
	;;
	*) echo "Enter 2 through 7 as arguments."
	   echo "Arguments = number of scriptures."
	;;
esac
