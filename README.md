# translation_PO_CSV_PO

To collect translations use \_() in python files and {% trans "" %}. It's better to avoid {% blocktrans %} and variables if possible, or use {% blocktrans with myvar = obj.my.var %} and {% blocktrans trimmed %}

Run poToCsv.py to get first translations.csv file
It'll contain strings to translate, indexes of the line where you will put translations later and column of encoded variables if any. Variable in text will be present as xxx12xxx to avoid GoogleTranslate interference.
(Make sure you keep the same order of the lines when you export the file with translations back.)

Load translations.csv to google spreadsheet. Add a new column for the new language. Formula:

=GoogleTranslate(c1, "en", "de")

Type =GoogleTranslate(c1, "en", "de")  into the first line of the column and populate the rest of the rows by simply dragging the corner of the blue box outlining the first row when you click on it down to the end of the table. You can change 'de' - German - to any language you like and populate as many columns as you want. Then correct awkward automatic translations. 

<img src="https://raw.githubusercontent.com/Dodotree/translation_PO_CSV_PO/master/translation_vars.JPG">

Save the file as CSV and run csvToPo.py to get .po files for each language column. Pay attention to what Google translation does to variables, make sure that any '%(my_var)s' and %(my_var')s has exact match in the translation including quotes and "s" at the end in the final .po files. You might need to fix some quote marks misplaced by GoogleTranslate if you run "sudo django-admin compilemessages"
