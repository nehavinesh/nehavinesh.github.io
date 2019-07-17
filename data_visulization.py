import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

polarity = []
subjectivity = []


def word_cloud_generate(tweetData):
    combinedTweets = " "
    for tweet in tweetData:
        combinedTweets += tweet["text"]

    tweetCloud= TextBlob(combinedTweets)

    filteredWords = ["and", "about", "the", "automation", "https", "to", "as","for"]
    filteredDictionary = dict()


    for word in tweetCloud.words:
        if len(word) <= 2:
            continue

        if not word.isalpha():
            continue

        if word.lower() in filteredWords:
            continue
        filteredDictionary[word.lower()] = tweetCloud.word_counts[word.lower()]

    wordCloud = WordCloud().generate_from_frequencies(filteredDictionary)
    return wordCloud


word_cloud = word_cloud_generate(tweetData)
plt.imshow(word_cloud, interpolation= "bilinear")
plt.axis("off")
plt.show()




for tweet in tweetData:
    tb = TextBlob(tweet["text"])
    polarity.append(tb.sentiment.polarity)
    subjectivity.append(tb.sentiment.subjectivity)

paverage = sum(polarity)/len(polarity)
saverage = sum(subjectivity)/len(subjectivity)

print("the average polarity of this list is: ", "{:<15.2f}".format(paverage))
print("the average subjectivity of this list is: ", "{:<15.2f}".format(saverage))

# histogram = plt.hist(polarity)
# plt.xlabel("Polarity")
# plt.ylabel("Number of Tweets")
# plt.title("Polarity of Tweets")
# plt.xlim(-0.6,0.6)
# plt.ylim(0,60)
# plt.grid(True)
# plt.show()
#
# histogram = plt.hist(subjectivity)
# plt.xlabel("subjectivity")
# plt.ylabel("Number of Tweet")
# plt.title("Histogram of subjectivity")
# plt.xlim(-0.1,1.1)
# plt.ylim(0,40)
# plt.grid(True)
# plt.show()
