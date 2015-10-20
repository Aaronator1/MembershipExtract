__author__ = 'aaronmsmith'

from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement

# import untangle
#
doc=ElementTree.parse('/Users/aaronmsmith/projects/membershipextract/cdcatalog.xml')
#
catalog= doc.getroot()
# print catalog
for cd in catalog:
    for item in cd:
        print item.text
    # for item in cd:
    # print cd.text
#     for CD in CATALOG.CD:
#         print CD
#         print CATALOG
    # for item in CD:
    #     memberUniqueNumber= item.TITLE.cdata
    #     print 'Hello'
    #employeeID=item.EmployeeId.cdata
    #personNumber=item.PersonNumber.cdata
    #employeeSSN=item.EmployeeSsn.cdata
    #print "MemberUniqueNumber: %s  Employee ID: %s " %  (memberUniqueNumber , employeeID) # + ' ' + personNumber

