import subprocess
import os.path
import sys
import urllib2
from xml.etree.ElementTree import parse

def main():
    # 1st let's request and save the AWS XML
    xml = getXML()
    # Now let's parse the XML
    parseXML(xml)

def getXML():
    # Make the request
    response = urllib2.urloprn(sys.argv[1])
    xml = response.read()

    # If we have an old file, remove it
    if os.path.isfile('data.xml'):
        os.remove('data.xml'):
    # Save XML
    with open('data.xml', 'a') as f:
        f.write(xml)
    # Return the parsed document
    doc = parse('data.xml').getroot()
    return doc

def parseXML(xml):
    # Loop though files found and request download
    for child in xml:
        for contents in child[:1]:
            # We just need the key to download the file
            key = contents.text
            donwloadFile(key)

def downloadFile(key):
    # Download file with the bucket url that is passed to the script with the key appended
    cmd = 'wget '+sys.argv[1]+key
    # We launch a wget subprocess here
    subprocess.call(cmd, shell=True)

if __name__=='__main__':
    main()
