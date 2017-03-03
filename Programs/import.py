#################################################################################
### Read in the Twitter, Blogs, & News text files into their own unique lists ###
#################################################################################

### Program assumes that there are text files containing Twitter, blogs, & news data in the sibling input folder 

from globals import *

t0 = time.time() # tic 

print "Beginning import script..."
print 

## change the current working directory
os.chdir("../Input")

## read the data into file handles
fTwitter = open("en_US.twitter.txt") # 1) Twitter
twitterData = fTwitter.readlines()

fBlogs = open("en_US.blogs.txt") # 2) Blogs
blogsData = fBlogs.readlines()

fNews = open("en_US.news.txt") # 3) News
newsData = fNews.readlines() 

## collapse these data lists into 1 list of data 
dataList = newsData + blogsData[:100000] + twitterData + blogsData[100000:]  # we want to sample some Twitter data too, so wedge it between blogs 
#dataList = twitterData + blogsData + newsData  

## restore the working directory to the project's program's folder
os.chdir("../Programs")

print 
print "import.py execution time:", round(time.time() - t0, 0), "seconds" # toc 
print 