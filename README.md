# SpamAnalyzer

The pre-processing is done on email (.eml) files. Each file takes input from the previous output, that means the emails are pre-processed in sequential order. This is done as follows:

1. Email_Extract.py - Files are extracted (script tags, header information) are removed, and the plain text (body) is extracted from the email message.

2. Email_Lower.py - Output from (Email_Extract.py) is fetched to the input of Email_Lower.py. The extracted message is converted to lowercase, as I do not want the classifiers to take 2 same words with different cases separately in the training phase.

3. Email_Digits_Spaces.py - The lower case messages are now passed and this stage removes the duplicate/front/rear spaces in the text and removes numbers.

4. Email_Punctation.py - The previous stage output is passed and this removes all the punctuation marks from the text message.

5. Emai_NGrams.py - The n-grams (5,5) are generated for training and testing by the classifiers.

Note: The pre-processing is done on all emails (training and testing).
