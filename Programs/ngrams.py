##########################################################################################
### Use the frequent word histogram & available text data to create most common ngrams ###
##########################################################################################

t0 = time.time() # tic 

print "Beginning ngram creation..."
print 

### Program assumes existence of wordHisto (frequently enough appeared words) & lineGroups (nested data structures with lines of text)

## Synthesize ngrams & export so we can verify results as the pipeline continues for big data; clear out variable after export to save memory 

print "Synthesizing 2 GRAMS:"
grams2 = CREATE_NGRAMS(lineGroups, wordHisto, 2)

csvFile = "../Output/grams2.csv"
with open(csvFile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(grams2)
print "2 Grams Exported"
print 
grams2 = None 

print "Synthesizing 3 GRAMS:"
grams3 = CREATE_NGRAMS(lineGroups, wordHisto, 3)
csvFile = "../Output/grams3.csv"
with open(csvFile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(grams3)
print "3 Grams Exported"
print
grams3 = None

print "Synthesizing 4 GRAMS:"
grams4 = CREATE_NGRAMS(lineGroups, wordHisto, 4)
csvFile = "../Output/grams4.csv"
with open(csvFile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(grams4)
print "4 Grams Exported"
print
grams4 = None 

print "Synthesizing 5 GRAMS:"
grams5 = CREATE_NGRAMS(lineGroups, wordHisto, 5)
csvFile = "../Output/grams5.csv"
with open(csvFile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(grams5)
print "5 Grams Exported"
print 
grams5 = None 
    
print 
print "ngrams.py execution time:", round(time.time() - t0, 0), "seconds" # toc 
print 