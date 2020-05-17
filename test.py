import string

def format(tweet):
    tweet = tweet.lower()
    #tweet = tweet.strip(string.punctuation)
    tweet = tweet.split()
    tweetList = []
    for word in tweet:
        word = word.strip(string.punctuation).rstrip(string.punctuation)
        tweetList.append(word)
    return tweetList


s = "I dont!!! understand this at all$UO@"
print(format(s))
print(s.strip(string.punctuation))


