#! /bin/bash

PDFS="01layoutalt 01layout example_controller_layout"

cd ../documents

for FILE in $PDFS; do
    rm $FILE.pdf
done

rm *.eps
rm *.aux
rm *.log
rm *.gz
rm esp.pdf
