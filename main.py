from sentiment_analysis import compute_tweets #importing the necessary function from the sentiment_analysis module

userFile = input("Enter the name of the file with the tweets: ") #taking user input
userKey = input("Enter the name of the file with keywords: ")

output = compute_tweets(userFile, userKey) #using the compute_tweets function to output the results after file processing

def formatOutput(output): #this function outputs the values for the user
    print("Happiness Value: ", round(output[0],3)) #rounding the happiness value in a region to 3 digits
    print("Tweet with Keywords: ", output[1])
    print("Total Number of Tweets: ", output[2])

if len(output) > 0: #prints the output if the list contains anything (so that if an exception is generated the empty list doesn't get formatted)
    print("\nEASTERN: ")
    formatOutput(output[0])

    print("\nCENTRAL: ")
    formatOutput(output[1])

    print("\nMOUNTAIN: ")
    formatOutput(output[2])

    print("\nPACIFIC: ")
    formatOutput(output[3])
else:
    print(output)

