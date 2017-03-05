#### Data Science Capstone Pipeline

### NOTE: contact Erhard Menker (ejmenker@gmail.com) for supplemental files that were too large to be tracked, like input CSVs

# Input/ 
    - contains the 3 text files (blogs, news, & Twitter) that are read into the program to be trained  

# Programs/
    - main.py controls the pipeline's execution
    - globals.py defines functions & parameters used throughout the text mining pipeline
    - import.py fetches the text files from the Input folder and stores them in lists
    - ngrams.py synthesizes the ngrams from the lists created in the import script 

# Output/ 
    - contains ngrams CSVs of size 2 - 5 that are read into the shiny app
    - /capstoneApp has the supplemental R codes, shiny App files, & ioslides app presentation