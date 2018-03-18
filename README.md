# translation_PO_CSV_PO

Run poToCsv.py to get first translations.csv file
It'll contain strings to translate and indexes of the line where you will put translations later
(Make sure you keep the same order of the lines when you export the file with translations back.)

Load translations.csv to google spreadsheet. Add a new column for the new language. Formula:

=GoogleTranslate(b1, "en", "de")

Type =GoogleTranslate(b1, "en", "de")  into the first line of the column and populate the rest of the rows by simply dragging the corner of the blue box outlining the first row when you click on it down to the end of the table. You can change 'de' - German - to any language you like and populate as many coluns as you want. Then correct awkward automatic translations, then save the file as CSV and run csvToPo.py to get .po files for each language column.
