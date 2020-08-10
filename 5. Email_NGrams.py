# Cell 1:
import os, sys, stat
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()

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
        
        destfile = open(dstpath,'w')
        print(" For File ", file)
        #         to be used to check whether the file contains nothing or not.
# it will be used for second if condition
        x = open(srcpath)
    
        emailfile = x.readlines()
        if(emailfile==None):
            destfile.close()
        
        elif(os.stat(srcpath).st_size==0):
            destfile.close()
            
        else:
            vectorizer = CountVectorizer(analyzer='char_wb', ngram_range=(5,5), stop_words ='english')
            vectorizer.fit_transform(open(srcpath))
            file_Data = ' '.join(vectorizer.get_feature_names())
            destfile.write(file_Data)
            destfile.close()d
        
#         vectorizer = CountVectorizer(analyzer='char_wb', ngram_range=(5,5), stop_words = None)
#         vectorizer.fit_transform(open(srcpath))
#         if (os.stat(srcpath).st_size==0):
#             destfile.close()
            
#         elif (emailfile==None):
#             destfile.close()
            
#         else:
#             file_Data = ' '.join(vectorizer.get_feature_names())
#             destfile.write(file_Data)
#             destfile.close()
#         vectorizer.fit_transform(open(srcpath))
#         for vectorizer.fit_transform(open(srcpath)) as emailfile:
#             first = emailfile.read(1)
#             if (os.stat(srcpath).st_size==0):
#                 destfile.close()
# #             first = emailfile.read(1)
#             elif (not first):
#                 print("File is empty "+dstpath)
#                 destfile.close()
#             else:
#                 vectorizer.fit_transform(open(srcpath))
#                 file_Data = '\n'.join(vectorizer.get_feature_names())
#                 destfile.write(file_Data)
#                 destfile.close()
    print("Operation is completed")

# Cell 3:
srcdir = "/Users/simrankaur/Documents/4. Spam_Emails/5. Spam_Digits_Spaces"
print("Input source directory: "+srcdir)
if not os.path.exists(srcdir):
    print("The source directory %s does not exist" % (srcdir))
    sys.exit()
# print("Input destination directory: ")
#dstdir = input()
dstdir = "/Users/simrankaur/Documents/4. Spam_Emails/6. Spam_NGrams"
print("The destination destination directory is: "+dstdir)
if not os.path.exists(dstdir):
    print("The destination directory is newly created.")
    os.makedirs(dstdir)
ExtractBodyFromDir ( srcdir, dstdir )
#print("Operation is completed")
