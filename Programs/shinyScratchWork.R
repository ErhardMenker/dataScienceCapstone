setwd("C:/Data/Analytics_Studies/R/Data_Science_Specialization/Capstone/Output")

library(stringr)

### Create a function that simulates how this text predictor will work for a given input

grams2 <- read.csv("grams2.csv", header = FALSE, stringsAsFactors = FALSE)
grams3 <- read.csv("grams3.csv", header = FALSE, stringsAsFactors = FALSE)
grams4 <- read.csv("grams4.csv", header = FALSE, stringsAsFactors = FALSE)
grams5 <- read.csv("grams5.csv", header = FALSE, stringsAsFactors = FALSE)

# function that takes a phrase and solves for the next best word iteratively from largest n thru 2 grams
predictNextWord <- function(phrase) {    
    
    # convert the phrase to lower case to be harmonious with stored data
    phrase <- tolower(trimws(phrase))
    
    ## Sequentially go thru the last n words (downwards 5) & see if they can be mapped to an ngram of that length
    
    # collapse the inputted phrase into a character vector; 1 entry for each space delimited word (amount of whitespace does not matter)
    phraseSplit <- stringr::str_split(phrase, "\\s+", simplify = TRUE)
    
    # 1) 5 Grams 
    if (ncol(phraseSplit) >= 4) {
        phraseSplitLast4 <- phraseSplit[1, (ncol(phraseSplit) - 3):ncol(phraseSplit)] # last 4 words from input
        if (!(NA %in% phraseSplitLast4) && !is.na(match(paste(phraseSplitLast4, collapse = " "), grams5[ , 1]))) {
            return(grams5[match(paste(phraseSplitLast4, collapse = " "), grams5[ , 1]), 2])
        }  
    }
    
    # 2) 4 Grams
    if (ncol(phraseSplit) >= 3) {
        phraseSplitLast3 <- phraseSplit[1, (ncol(phraseSplit) - 2):ncol(phraseSplit)] # last 3 words from input
        if (!(NA %in% phraseSplitLast3) && !is.na(match(paste(phraseSplitLast3, collapse = " "), grams4[ , 1]))) {
            return(grams4[match(paste(phraseSplitLast3, collapse = " "), grams4[ , 1]), 2])
        }
    }
    
    # 3) 3 Grams
    if (ncol(phraseSplit) >= 2) {
        phraseSplitLast2 <- phraseSplit[1, (ncol(phraseSplit) - 1):ncol(phraseSplit)] # last 2 words from input
        if (!(NA %in% phraseSplitLast2) && !is.na(match(paste(phraseSplitLast2, collapse = " "), grams3[ , 1]))) {
            return(grams3[match(paste(phraseSplitLast2, collapse = " "), grams3[ , 1]), 2])
        }
    }
    
    # 4) 2 Grams
    phraseSplitLast1 <- phraseSplit[1, ncol(phraseSplit)] # last 1 word from input
    if (!(NA %in% phraseSplitLast1) && !is.na(match(paste(phraseSplitLast1, collapse = " "), grams2[ , 1]))) {
        return(grams2[match(paste(phraseSplitLast1, collapse = " "), grams2[ , 1]), 2])
    }
    
    # 5) if nothing matches down through 2 grams, just predict "the"
    return("the")
}  

print(predictNextWord("The guy in front of me just bought a pound of bacon, a bouquet, and a case of"))