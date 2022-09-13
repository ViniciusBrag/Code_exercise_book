#! python3
# rename_dates.py rename the name of diretorie to format to date MM-DD-AAAA 

import shutil, os, re


date_pattern = re.compile(r"""
    ^(.*?) # all text before to date.
    ((0|1)?\d)- # one or two digits to month.
    ((0|1|2|3)?\d)- # one or two digits to day.
    ((19|20)\d\d) # four digits to year.
    (.*?)$ # all text after to date.
""", re.VERBOSE)

for amer_filename in os.listdir('files-format'):
    mo = date_pattern.search(amer_filename)
    if mo == None:
        continue
    before_part = mo.group(1)
    month_part = mo.group(2)
    day_part = mo.group(4)
    year_part = mo.group(6)
    after_part = mo.group(8)

    euro_filename = before_part + day_part + '-' + month_part + '-' + year_part + after_part


    abs_working_dir = os.path.abspath('files-format')
    amer_filename = os.path.join(abs_working_dir, amer_filename)
    euro_filename = os.path.join(abs_working_dir, euro_filename)

print('Renaming "%s" to "%s"..' %(amer_filename, euro_filename))
shutil.move(amer_filename, euro_filename)


