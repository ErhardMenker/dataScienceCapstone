###############################################################################################################
### Program to define functions & global constants that are to be used throughout this text mining pipeline ###
###############################################################################################################

import re 

### Global Constants
MIN_WORD = 5 # the number of times a word must appear in order to be included in ngrams 
MIN_NGRAM = 2 # the number of times an ngram must appear to be included in the exported ngram list 
LINE_COUNT = 200000 # the number of lines to parse from the beginning of the capstone provided text file 

### Global Functions

def REMOVE_TAGS(lst, tags):
    ''' 
    eliminate words from nested tuple list "lst" that have tag in list "tags" 
    '''
    # must iterate through every word of every sentence of every line and reconstruct (excluding words in tags argument) 
    lst_output = list() 
    for line in lst:
        sentence_list = list() 
        for sentence in line:
            word_list = list() 
            for word in sentence:
                # append this word to the word list if not in banned tags argument 
                if word[1] not in tags:
                    word_list.append(word[0])
            sentence_list.append(word_list)
        lst_output.append(sentence_list)
    return tuple(lst_output)
    
def SYNTHESIZE_CONTRACTIONS(lst):
    '''
    nltk splits contractions at the apostrophe (e.g. they've -> they' ve); collapse these contractions into 1 in list & coerce proper grammar tag
    note the "gon" + "na" -> "gonna" special case 
    '''
   # must iterate through every word of every sentence of every line and reconstruct 
    lst_output = list() 
    for line in lst:
        sentence_list = list() 
        for sentence in line:
            (word_list, word_idx, word_prev) = (list(), 0, None) 
            for word in sentence:
                # synthesize the contraction if it starts with an apostrophe 
                if (re.search("'", word) and word_idx != 0):
                    word_prev = word_list.pop() # we appended the 1st part of the contraction on as a standalone word, remove it 
                    word = word_prev + word
                # special case: synthesize "gon" & "na" into "gonna"
                elif (word_prev == "gon") and (word == "na"):
                    word_list.pop() # we appended "gon", remove it 
                    word = word_prev + word 
                word_list.append(word) 
                word_prev = word
                word_idx += 1 
            sentence_list.append(word_list)
        lst_output.append(sentence_list)
    return tuple(lst_output) 
    
def CREATE_HISTO(lst):
    '''
    create a histogram with word frequencies; we're going to toss sentences with words that appear infrequently to save memory and kick out arbitrary misspellings
    '''
    word_histo = dict()
    # create raw histogram 
    for line in lst:
        for sentence in line:
            for word in sentence:
                word_histo[word] = word_histo.get(word, 0) + 1
    # eliminate entries with just 1 instance or have undesirable characters 
    for entry, count in word_histo.items():
        # give metacharacters their own unique literal regex search to not mess up the regex, otherwise bundle literals only 
        if count < MIN_WORD or re.search("\.", entry) or re.search("\+", entry) or re.search("\@", entry) or re.search("\%", entry) or re.search("\/", entry) or re.search("\#", entry) or re.search("\`", entry) or re.search("\=", entry) or re.search("\<", entry) or re.search("\>", entry) or re.search("@", entry) or re.search("\$", entry) or re.search("''", entry): 
            del word_histo[entry]   
    # just care about the word at this point (not count)
    word_histo = [x for x in word_histo] 
    return tuple(word_histo) 
    
def CREATE_NGRAMS(lst, word_histo, n):
    '''
    Create ngrams of size n using nested sentences lst; assumes all n consecutive words of the phrase exist in word_histo  
    '''
    # strip off the nltk tag on each word 
    sentence_list = list()
    for line in lst:
        for sentence in line:
            sentence_iter = list()
            for word in sentence:
                sentence_iter.append(word)
            sentence_list.append(sentence_iter)
    # create raw ngrams (contains ALL, not just most popular beginning (n - 1) words)
    ngrams = dict() 
    for sentence in sentence_list:
        for word_idx in range(len(sentence) - 1): 
            # tack on to the ngrams iff all words in the ngram are in the word_histo & the sentence is within proper length (greater than n)
            if (len(sentence) >= n + word_idx) and (False not in [True if word in word_histo else False for word in sentence[word_idx:(word_idx + n)]]):
                if ' '.join(sentence[word_idx:(word_idx + n - 1)]) not in ngrams:
                    ngrams[' '.join(sentence[word_idx:(word_idx + n - 1)])] = {sentence[word_idx + n - 1]: 1}
                else:
                    ngrams[' '.join(sentence[word_idx:(word_idx + n - 1)])][sentence[word_idx + n - 1]] = ngrams[' '.join(sentence[word_idx:(word_idx + n - 1)])].get(sentence[word_idx + n - 1], 0) + 1              
    # iterate through each (n - 1) gram and place the most popular n gram in list ngrams_clean
    ngrams_clean = list()
    for ngram in ngrams:
        # ngram has to appear a certain amount of times; we want to eliminate gibberish 
        if ngrams[ngram][max(ngrams[ngram], key = ngrams[ngram].get)] >= MIN_NGRAM:
            ngrams_clean.append([ngram, max(ngrams[ngram], key = ngrams[ngram].get)])
    return ngrams_clean 
    
    
    