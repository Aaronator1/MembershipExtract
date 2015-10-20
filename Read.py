__author__ = 'aaronmsmith'
import untangle

doc=untangle.parse('/Users/aaronmsmith/projects/membershipextract/Simple.xml')

for item in doc.ArrayOfEligibility.Eligibility:
    memberUniqueNumber= item.MemberUniqueNumber.cdata
    employeeID=item.EmployeeId.cdata
    personNumber=item.PersonNumber.cdata
    employeeSSN=item.EmployeeSsn.cdata
    print "MemberUniqueNumber: %s  Employee ID: %s " %  (memberUniqueNumber , employeeID) # + ' ' + personNumber

