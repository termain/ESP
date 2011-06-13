#! /bin/bash

PDFS="01layoutalt 01layout example_controller_layout"

for FILE in $PDFS; do
    rm $FILE.pdf
done

rm *.eps
rm *.aux
rm *.log
