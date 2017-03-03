########################################################################################################
##### The purpose of this program is to source in other programs that read in & process the data #######
########################################################################################################

### Module Import Calls ###
import os
import re 
import string
import time 
import csv 
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

t_0 = time.time()

########################################################################################################
### Call the individual scripts ###

execfile("import.py") # 1) read in the data 
execfile("clean.py") # 2) clean each text file's list structure
execfile("ngrams.py") # 3) convert the clean data to ngrams & export to Output folder as each completes

########################################################################################################

print 
print "TOTAL PIPELINE EXECUTION TIME:", round(time.time() - t_0, 0) / 60, "minutes" # toc