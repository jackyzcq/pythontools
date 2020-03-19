#/bin/sh
python3 rec2mlf.py test.txt > test.mlf
./HResults -t -I $1 /dev/null test.mlf
rm test.mlf