##Bash script for producing slides with ipynb
##Takes one ipynb as argument, posts slides to web browser

ipython nbconvert $1 --to slides --post serve