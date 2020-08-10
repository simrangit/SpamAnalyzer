# Cell 1:
import email.parser
import os, sys, stat
import chilkat

# to remove leading, trailing and duplicate/unncesssary spaces from a text in every .eml files
import re 

# for remove digits from a string
from string import digits
email = chilkat.CkEmail()

# Cell 2:
def ExtractBodyFromDir ( srcdir, dstdir ):
    #if not os.path.exists(dstdir): # dest path doesnot exist
       # os.makedirs(dstdir) 
    files = os.listdir(srcdir)
    for file in files:
        srcpath = os.path.join(srcdir, file)
        file_name = file.split(".")
        
         # this is giving the file a new name - filename_removePunctution.eml
        file_name = file_name[0]+".eml"
        dstpath = os.path.join(dstdir,file_name)
        print(" For File ", file)
        
        #remove digits, i.e; to remove all numbers
#         after removing punctuation and removing digits, we will write into a destination directory in a new file_name
        destfile = open(dstpath,'w')
        for line in open(srcpath):
            tr = str.maketrans("", "", digits)
            str1 = line.translate(tr)
            str1 = str1.lstrip()
            str1 = str1.rstrip()
            str1 = re.sub('\s+', ' ', str1)
            destfile.write(str1)
        destfile.close()


# Cell 3:
srcdir = "/Users/simrankaur/Documents/4. Spam_Emails/4. Spam_Punctuation"
if not os.path.exists(srcdir):
    print("The source directory %s does not exist" % (srcdir))
    sys.exit()
# print("Input destination directory: ")
#dstdir = input()
dstdir = "/Users/simrankaur/Documents/4. Spam_Emails/5. Spam_Digits_Spaces"
print("Input destination directory: "+dstdir)
if not os.path.exists(dstdir):
    print("The destination directory is newly created.")
    os.makedirs(dstdir)
ExtractBodyFromDir ( srcdir, dstdir )
print("Operation is Completed")
