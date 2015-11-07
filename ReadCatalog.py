__author__ = 'aaronmsmith'

from xml.etree import ElementTree

doc=ElementTree.parse('cdcatalog.xml')
root=doc.getroot()
#

for cd in root.findall('CD'):
    title= cd[0].text
    artist=cd[1].text
    print "Title: %s,  Artist: %s" % (title, artist)

