# -*- coding: utf-8 -*-

# Cell 1:
import email.parser
import os, sys, stat
import shutil
import chilkat
import re
email = chilkat.CkEmail()

# Cell 2:
def ExtractSubPayload (filename):
    success = email.LoadEml(filename)
    str1 = ""
    for line in open(filename):
#         line = line.encode("utf8")
        line = line.rstrip().lower()
#         line = str(line)
        str1 = str1+line
#         print(line)
    return str1

# Cell 3:
def ExtractBodyFromDir ( srcdir, dstdir ):
    if not os.path.exists(dstdir): # dest path doesnot exist
        os.makedirs(dstdir) 
    files = os.listdir(srcdir)
    for file in files:
        srcpath = os.path.join(srcdir, file)
        dstpath = os.path.join(dstdir, file)
        dstfile = open(dstpath, 'w')
        # dstfile = open(dstpath, 'w', encoding="utf8")
        body = ExtractSubPayload (srcpath)
#         dstfile = open(dstpath, 'w')
#         body = body.encode('surrogateescape')
        body = str(body)
        dstfile.write(body)
        dstfile.close()

#Cell 4:
# This is where the program execution starts
srcdir = "/Users/simrankaur/Documents/4. Spam_Emails/2. Spam_Extract"
if not os.path.exists(srcdir):
    print("The source directory %s does not exist" % (srcdir))
    sys.exit()

dstdir = "/Users/simrankaur/Documents/4. Spam_Emails/3. Spam_Lower"  
print("Destination directory: ", dstdir)
if not os.path.exists(dstdir):
    print("The destination directory is newly created.")
    os.makedirs(dstdir)
ExtractBodyFromDir ( srcdir, dstdir )
print("Operation is Completed")
