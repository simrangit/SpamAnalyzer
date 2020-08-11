# -*- coding: utf-8 -*-

import os, sys, stat

from Spam_Dictionary import Spam_Dict
# print(Spam_Dict)

from NotSpam_Dictionary import NotSpam_Dict
# print(NotSpam_Dict)

prob_Spam = 0.3316 # we had 779 emails as Spam in training
prob_NotSpam = 0.6684 # we had 1721 emails as Ham in testing

def Naive_Bayes(source_dir):
	files = os.listdir(source_dir)
	Email_list = []
	Spam = 0
	NotSpam = 0
	for file in files:
		Email_file = os.path.join(source_dir, file)
		#print("For File ", Email_file)

		if(os.stat(Email_file).st_size == 0):
			print("Empty file - Contains no data")
			Spam = Spam + 1
			continue

		prob_Spam_NGram = 1
		prob_NotSpam_NGram = 1
		
		f = open(Email_file,'r')
		for line in f:
			for NGrams in line.split():
				# print("NGrams ", NGrams)
				prob_NGram_Spam = Spam_Dict.get(NGrams,1) # if the NGram does not exist, then ignore it or either take its probability as 1, because its presence does not tell us much information.
				# print("NGram  and its dict value in Spam ",NGrams, prob_NGram_Spam)
				prob_NGram_NotSpam = NotSpam_Dict.get(NGrams,1)
				# print("NGram  and its dict value in Not Spam ",NGrams, prob_NGram_NotSpam)

				prob_Spam_NGram = prob_Spam_NGram * prob_NGram_Spam
				prob_NotSpam_NGram = prob_NotSpam_NGram * prob_NGram_NotSpam

		A = prob_Spam_NGram * prob_Spam
		B = prob_NotSpam_NGram * prob_NotSpam

		print("Spam Probability ", A)
		print("Not Spam Probability ",B)
		

		if( (A < B and B < 1e-10) ):
			# print(B)
			NotSpam = NotSpam + 1
		else:
			Spam = Spam + 1
	print(" Spam emails ",Spam)
	print(" Ham emails ",NotSpam)

source_dir ="/Users/simrankaur/Documents/1. Ham_Emails/6. Email_NGrams"

if not os.path.exists(source_dir):
	print("The source directory %s does not exist" % (source_dir))
	sys.exit()

Naive_Bayes(source_dir)
