# -*- coding: utf-8 -*-

# Cell 1:
import email.parser
import os, sys, stat
import shutil
import chilkat
import re
import string
   # for tokenization, to remove punctuation marks
email = chilkat.CkEmail()

# Cell 2:
def ExtractBodyFromDir ( srcdir, dstdir ):
    #if not os.path.exists(dstdir): # dest path doesnot exist
       # os.makedirs(dstdir) 
    files = os.listdir(srcdir)
    for file in files:
        tr = str.maketrans("", "", string.punctuation)
        srcpath = os.path.join(srcdir, file)
        file_name = file.split(".")
        
         # this is giving the file a new name - filename_removePunctution.eml
        file_name = file_name[0]+".eml"
        dstpath = os.path.join(dstdir,file_name)
        
        #tokenize the file, i.e; to remove all punctuation marks
#         after removing punctuation, we will write into a destination directory in a new file_name
        print("For File ", file)
        destfile = open(dstpath, 'w')
        for line in open(srcpath):
            # print("For file ",file)
            #tr = str.maketrans("", "", string.punctuation)
            str1 = line.translate(tr)
            destfile.write(str1)
        destfile.close()
        
        
#         #Make N-Grams of the file
#         vectorizer = CountVectorizer(analyzer='char', ngram_range=(5, 5))
#         vectorizer.fit_transform(open(srcpath))
#         file_Data = '\n'.join(vectorizer.get_feature_names())
#         print(file_Data)
        
#         # Create the file and store it in the new directory
#         file_name = file.split(".")
#         file_name = file_name[0]+"_ngram"+".eml"
#         print(file_name)

# Cell 3:
srcdir = "/Users/simrankaur/Documents/4. Spam_Emails/3. Spam_Lower"
print("Input source directory: "+srcdir)
if not os.path.exists(srcdir):
    print("The source directory %s does not exist" % (srcdir))
    sys.exit()
# print("Input destination directory: ")
#dstdir = input()
dstdir = "/Users/simrankaur/Documents/4. Spam_Emails/4. Spam_Punctuation" 
print("Input destination directory: "+dstdir)
if not os.path.exists(dstdir):
    print("The destination directory is newly created.")
    os.makedirs(dstdir)
ExtractBodyFromDir ( srcdir, dstdir )
print("Operation is completed")

# files = os.listdir(srcdir)
# print("Files are ",files)
