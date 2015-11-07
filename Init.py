__author__ = 'aaronmsmith'

import fileinput
import time


fileToSearch = '21037-Eligibility-4-1-2015 - Copy.xml'


# header='<?xml version="1.0" encoding="utf-8"?><ArrayOfEligibility>'
# footer='</ArrayOfEligibility>'
# r=open(fileToSearch,'r+')
# contents=r.read()
# newcontents=str(header + contents + footer)
# print(newcontents)
# r.seek(0)
#
# r.write(newcontents)
# r.close()
#
# time.sleep(1) #pause for 1 second

textToSearch='xsi:nil="true" '
textToReplace=""
f= fileinput.FileInput(fileToSearch, inplace=True, backup='.bak')

for line in f:
    print(line.replace(textToSearch, textToReplace))

f.close()
