#! /bin/bash

PDFS="01layoutalt 01layout example_controller_layout"

cd ../documents

for FILE in $PDFS; do
    dia -t eps $FILE.dia
    epstopdf $FILE.eps
done

pdflatex esp.tex

for FILE in $PDFS; do
    rm $FILE.pdf
done

rm *.eps
rm *.aux
rm *.log
