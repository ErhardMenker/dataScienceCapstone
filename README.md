#### Data Science Capstone Pipeline
# Input/ contains the 3 text files (blogs, news, & Twitter) that are read into the program to be trained  
# Programs/
    - week2.py & quiz1.py provide exploratory work to present the data in the provided text files
    - main.py controls the pipeline's execution
    - globals.py defines functions & parameters used throughout the text mining pipeline
    - import.py fetches the text files from the Input folder and stores them in lists
    - ngrams.py synthesizes the ngrams from the lists created in the import script 
# Output/ contains ngrams CSVs of size 2 - 5 that are read into the shiny app