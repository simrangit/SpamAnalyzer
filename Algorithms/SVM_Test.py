import os, sys, stat
from sklearn import svm
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()

df_email = pd.read_csv('/Users/simrankaur/Documents/Result_Emails', encoding='latin1', header = None)
# print(df_email)
df_label = pd.read_csv('/Users/simrankaur/Documents/Result_Labels', header = None)

X_label = df_label[0]
print(X_label)

vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(df_email[0]) 

clf = svm.SVC(C = 0.1, class_weight = 'balanced', gamma = 'scale')

clf.fit(X_train, X_label)

src_dir_email = '/Users/simrankaur/Documents/1. Ham_Emails/6. Email_NGrams'

if not os.path.exists(src_dir_email):
	print("The source directory %s does not exist" % (src_dir_email))
	sys.exit()

Ham = 0
Spam = 0

files = os.listdir(src_dir_email)
for file in files:
	Test_Email = os.path.join(src_dir_email,file)
	with open(Test_Email,'r') as f:
		print(" For file ",file)
		content = f.read()
		# print("content", content)
		Y_test = vectorizer.transform([content])
		predictions = clf.predict(Y_test)
		# print("predictions ",predictions)
		if(predictions == 'ham'):
			Ham = Ham + 1
		else: 
			Spam = Spam + 1
		# break

print("Ham Emails ", Ham)
print("Spam Emails ", Spam)
