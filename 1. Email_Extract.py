# -*- coding: utf-8 -*-

# Cell 1
import email.parser 
import os, sys, stat
import shutil
import chilkat
#from bs4 import BeautifulSoup
import re

email = chilkat.CkEmail()

# Cell 2
def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
#     print(cleantext)
    return(cleantext)
# this code is for excluding the HTML tags from the content (body)

# Cell 3
def ExtractSubPayload (filename):
    success = email.LoadEml(filename)
    if (success != True):
        print(email.lastErrorText())
        sys.exit()
    bText = email.HasPlainTextBody()
#     print(bText)
    if (bText == True):
        raw_html = email.getPlainTextBody()
#         print(raw_html)
        return raw_html
    else:
        bHtml = email.HasHtmlBody()
        if (bHtml == True):
#             print(email.getHtmlBody())
            raw_html = cleanhtml(email.getHtmlBody())
            return 

# Cell 4
def ExtractBodyFromDir ( srcdir, dstdir ):
    if not os.path.exists(dstdir): # dest path doesnot exist
        os.makedirs(dstdir) 
    files = os.listdir(srcdir)
    for file in files:
        srcpath = os.path.join(srcdir, file)
        dstpath = os.path.join(dstdir, file)
        dstfile = open(dstpath, 'w')
        #dstfile = open(dstpath, 'w', encoding="utf-8")
        x = open(srcpath)
        emailfile = x.readlines()
        if (emailfile==None):
            dstfile.close()
            
        elif(os.stat(srcpath).st_size==0):
            dstfile.close()  
            
        else:  # copy the file
            print("For File", file)
            body = ExtractSubPayload (srcpath)
            #dstfile = open(dstpath, 'w')
            #dstfile = open(dstpath, 'w', encoding="utf-8")
            #body = body.encode('utf-8','surrogateescape')
            body = str(body)
            dstfile.write(body)
            dstfile.close()

# Cell 5
print("Input source directory: ")
srcdir = "/Users/simrankaur/Documents/4. Spam_Emails/1. Spam_Rename"
if not os.path.exists(srcdir):
    print("The source directory %s does not exist" % (srcdir))
    sys.exit()
print("Input destination directory: ",srcdir)
dstdir = "/Users/simrankaur/Documents/4. Spam_Emails/2. Spam_Extract"
if not os.path.exists(dstdir):
    print("The destination directory is newly created.")
    os.makedirs(dstdir)

print("Destination directory: ",dstdir)
ExtractBodyFromDir ( srcdir, dstdir )
print("Operation is Completed")
