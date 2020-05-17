from string import punctuation #importing the necessary library to help process the file

def processTweet(tweet): #this function processes the tweets from the file
    tweetList = [] # Initializing a list
    tweet = tweet.lower() #converting to lowercase
    tweet = tweet.split() #splitting the list into words
    for word in tweet:
        word = word.strip(punctuation) #stripping the punctuation in the word (in the beginning and end of the word)
        tweetList.append(word) #appending the results to tweetList
    return tweetList

def happinessVal(tweetList, dict): #this function processes the tweets and outputs the happiness value, tweet keywords in the region, and the count
    avgScoreValues = [] #Initializing a list
    for tweet in tweetList:
        score = 0 #setting score to 0, so the variable can be reused to track the score of each tweet accurately
        keyWordCount = 0 #setting the keyWordCount to 0, so the variable can be reused to track the number of keywords found in a tweet
        for word in tweet:
            if word in dict:
                score += dict[word] #adding the score, corresponding to the values held in the dictionary
                keyWordCount += 1 #adding and keeping track of the keyWordCount per tweet

        if keyWordCount != 0: #only performs the operations below if the tweet has keywords
            happinessValueOfTweet = score/keyWordCount #average happiness value of the tweet
            avgScoreValues.append(happinessValueOfTweet) #adding the average value of each tweet to a list
    try:
        happinessValueOfRegion = sum(avgScoreValues)/len(avgScoreValues) #finding the average happiness value of a region using the average happiness values of each tweet
    except ZeroDivisionError:
        happinessValueOfRegion = 0 #setting the happiness value = 0 if a ZeroDivisionError occurs

    output = (happinessValueOfRegion, len(avgScoreValues), len(tweetList)) #outputting the results in the form, happiness value of the region, count of keyword tweets in the region, and the total number of tweets.
    return output

def compute_tweets(tweets, keywords): #this function outputs the values after called from the main program
    try:
        tweetFile = open(tweets, "r", encoding="utf‐8")
        keywordsFile = open(keywords, "r", encoding="utf-8")

        keywordsDict = {} #Initializing a dictionary

        for line in keywordsFile:
            line = line.rstrip("\n") #string processing
            line = line.split(",") #string processing
            keywordsDict[line[0]] = int(line[1]) #storing the keywords as the key and the sentiment values as the value for the key

        # Initializing a tweet list for each region
        easternList = []
        centralList = []
        mountainList = []
        pacificList = []

        for line in tweetFile:
            line = line.rstrip("\n") #string processing
            line = line.split(" ", 5)

            lat1 = line[0].rstrip(",")
            lat2 = lat1.lstrip("[")
            latitude = float(lat2) #converts the latitude into a float value to use to perform functions

            long = line[1].rstrip("]")
            longitude = float(long) #converts the longitude into a float value to perform functions

            #using if statements to process the file based on latitude and longitude values
            if (latitude <= 49.189787 and latitude >= 24.660845) and (longitude >= -87.518395 and  longitude <= -67.444574):
                tweet = processTweet(line[5]) #using the processTweet function to process the tweet
                easternList.append(tweet) #appending the result of the tweet into the easternList (tweet list in the region)

            if (latitude <= 49.189787 and latitude >= 24.660845) and (longitude >= -101.998892 and longitude <= -87.518395):
                tweet = processTweet(line[5])
                centralList.append(tweet)

            if (latitude <= 49.189787 and latitude >= 24.660845) and (longitude >= -115.236428 and longitude <= -101.998892):
                tweet = processTweet(line[5])
                mountainList.append(tweet)

            if (latitude <= 49.189787 and latitude >= 24.660845) and (longitude >= -125.242264 and longitude <= -115.236428):
                tweet = processTweet(line[5])
                pacificList.append(tweet)

        easternTuple = happinessVal(easternList, keywordsDict) #using the happinessVal function to compute the list
        centralTuple = happinessVal(centralList, keywordsDict)
        mountainTuple = happinessVal(mountainList, keywordsDict)
        pacificTuple = happinessVal(pacificList, keywordsDict)

        outputTuple = (easternTuple, centralTuple, mountainTuple, pacificTuple) #formatting the output as a tuple

        tweetFile.close() #closing the file
        keywordsFile.close() #closing the file

        return outputTuple

    except IOError: #excepting IOError in the case when the file doesn't exist
        print("Error", tweets, "or", keywords, "does not exist")
        output = [] #Initializing an empty list for when the file doesn't exist
        return output



