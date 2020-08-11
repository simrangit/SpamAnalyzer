import time
start_time = time.time()
import os, sys, stat
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model.logistic import LogisticRegression
from sklearn.metrics import accuracy_score

vectorizer = TfidfVectorizer()
classifier = LogisticRegression()

df_email = pd.read_csv('/Users/simrankaur/Documents/Result_Emails', encoding='latin1', header = None)
# print(df_email)
df_label = pd.read_csv('/Users/simrankaur/Documents/Result_Labels', header = None)

X_label = df_label[0]

vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(df_email[0])

# classifier = LogisticRegression(class_weight='balanced', solver = 'lbfgs')
# the above classifier is working successfully

classifier = LogisticRegression(C = 0.001, class_weight = 'balanced', solver = 'lbfgs') # default C = 1

print("Printing classifier ",classifier.fit(X_train,X_label))

src_dir_email = '/Users/simrankaur/Documents/2. Spam_Emails/6. Spam_NGrams'

if not os.path.exists(src_dir_email):
	print("The source directory %s does not exist" % (src_dir_email))
	sys.exit()

Ham = 0
Spam = 0

files = os.listdir(src_dir_email)
for file in files:
	Test_Email = os.path.join(src_dir_email,file)
	with open(Test_Email,'r') as f:
		content = f.read()
		# print("content", content)
		Y_test = vectorizer.transform([content])
		predictions = classifier.predict(Y_test)
		# print("predictions ",predictions)
		if(predictions == 'ham'):
			Ham = Ham + 1
		else: 
			Spam = Spam + 1
		# break

print("Ham Emails ", Ham)
print("Spam Emails ", Spam)
end_time = time.time()
print(" Time ",(end_time - start_time))


# content = 'strip sucks sydne tacey tarts teen  this uckst uncut usrnp'

# Y_test = vectorizer.transform(['Your Mobile No was awarded a Prize', 'Hey honey whats up','strip sucks sydne tacey tarts teen  this uckst uncut usrnp','my name is simra and is studying in uvic under the guid ance of docto octor issa'])
# # print("Y_test ",Y_test)
# predictions = classifier.predict(Y_test)
# print(predictions)

