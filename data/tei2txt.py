import re
import os
import glob
import pandas as pd
from os import listdir
from os.path import join
from nltk.tokenize import word_tokenize
import glob
import subprocess
from lxml import etree

#################################
# read TEI P5                   #
#################################


teiPath = 
txtFolder
xpath

def read_tei5(teiPath, txtFolder, xpath):
    """
    Extracts selected text from TEI P5 files and writes TXT files.
    xpath (string): "alltext", "bodytext, "seg" or "said".
    """
    if not os.path.exists(txtFolder):
        os.makedirs(txtFolder)
    ## Do the following for each file in the inpath.
    counter = 0
    for file in glob.glob(teiPath):
        with open(file, "r", encoding="utf8"):
            filename = os.path.basename(file)[:-4]
            idno = filename[:6] # assumes idno is at the start of filename.
            #print("Treating " + idno)
            counter +=1
            xml = etree.parse(file)
            namespaces = {'tei':'http://www.tei-c.org/ns/1.0'}

            ### Removes tags but conserves their text content.
            ### USER: Uncomment as needed.
            etree.strip_tags(xml, "{http://www.tei-c.org/ns/1.0}seg")
            #etree.strip_tags(xml, "{http://www.tei-c.org/ns/1.0}said")
            #etree.strip_tags(xml, "{http://www.tei-c.org/ns/1.0}hi")

            ### Removes elements and their text content.
            ### USER: Uncomment as needed.
            #etree.strip_elements(xml, "{http://www.tei-c.org/ns/1.0}reg", with_tail=False)
            #etree.strip_elements(xml, "{http://www.tei-c.org/ns/1.0}orig", with_tail=False)
            etree.strip_elements(xml, "{http://www.tei-c.org/ns/1.0}note", with_tail=False)
            etree.strip_elements(xml, "{http://www.tei-c.org/ns/1.0}quote", with_tail=False)
            #etree.strip_elements(xml, "{http://www.tei-c.org/ns/1.0}l", with_tail=False)
            #etree.strip_elements(xml, "{http://www.tei-c.org/ns/1.0}p", with_tail=False)
            etree.strip_elements(xml, "{http://www.tei-c.org/ns/1.0}head", with_tail=False)
            #etree.strip_elements(xml, "{http://www.tei-c.org/ns/1.0}stage", with_tail=False)
            etree.strip_elements(xml, "{http://www.tei-c.org/ns/1.0}speaker", with_tail=False)

            ### XPath defining which text to select
            xp_bodytext = "//tei:body//text()"
            xp_alltext = "//text()"
            xp_seg = "//tei:body//tei:seg//text()"
            xp_said = "//tei:body//tei:said//text()"
            
            ### Applying one of the above XPaths, based on parameter passed.
            ### USER: use on of the xpath values used here in the parameters.
            if xpath == "bodytext": 
                text = xml.xpath(xp_bodytext, namespaces=namespaces)
            if xpath == "alltext": 
                text = xml.xpath(xp_alltext, namespaces=namespaces)
            if xpath == "seg": 
                text = xml.xpath(xp_seg, namespaces=namespaces)
            if xpath == "said": 
                text = xml.xpath(xp_said, namespaces=namespaces)
            text = "\n".join(text)

            ### Some cleaning up
            text = re.sub("[ ]{2,8}", " ", text)
            text = re.sub("\n{2,8}", "\n", text)
            text = re.sub("[ \n]{2,8}", " \n", text)
            text = re.sub("\t{1,8}", "\t", text)

            outtext = str(text)
            outfile = os.path.join(txtFolder, filename +".txt")
        with open(outfile,"w") as output:
            output.write(outtext)
            
    print("Done. Files treated: " + str(counter))

read_tei5(teiPath, txtFolder, xpath)
