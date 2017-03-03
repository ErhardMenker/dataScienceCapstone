#############################################################
### Perform systematic cleaning on each of the text lists ###
#############################################################

### Program assumes existence of comprehensive dataList from import.py (lists where each element is a line represented as a string) 

from globals import *

t0 = time.time() # tic

print "Beginning clean.py script..."
print 

## 1) Tokenize each line into sentences and each sentence into words; store these elements in a nested tuple 
## (each main element of the tuple is a line, each element of the line a sentence, each element of the sentence a word) 
print "Tokenize each line using NLTK"
# process each line of the text file  
lineGroups = list() 
for line in dataList[:LINE_COUNT]:
    line = line.translate(None).lower()
    try:
        # group all sentences in a line together in a list & append to list of all data 
        tempList = list() 
        for sentence in sent_tokenize(line):
            tempList.append(nltk.pos_tag(word_tokenize(sentence)))
        lineGroups.append(tempList)
    except:
        pass
lineGroups = tuple(lineGroups) # save memory 

## 2) Clean the lineGroups data tuple with custom functions defined & explained in the ./globals.py 
# a. remove punctuation & cardinal numbers from the text file (these are tokens as communicated by the nltk library)...
#    ...place these data into a list of sentences stripped of nltk tokens, this is the tokens' only purpose  
print "Remove Non-Sensical Characters"
lineGroups = REMOVE_TAGS(lineGroups, [".", ":", ",", "(", ")", "CD"])

# b. collapse contractions
print "synthesizing contractions"
lineGroups = SYNTHESIZE_CONTRACTIONS(lineGroups) 

# c. create a histogram of words that appear a minimum amount of time (will throw out words in n-grams that appear less)
print "create frequent word histogram"
wordHisto = CREATE_HISTO(lineGroups) 

print
print "clean.py execution time:", round(time.time() - t0, 0), "seconds" # toc  
print 
