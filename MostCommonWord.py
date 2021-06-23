# Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned.
# It is guaranteed there is at least one word that is not banned, and that the answer is unique.
# The words in paragraph are case-insensitive and the answer should be returned in lowercase.
import collections, operator
def mostCommonWord(paragraph, banned):
    processed_text = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
    word_list = processed_text.split()
    word_count = collections.defaultdict(int)
    for word in word_list:
        if word not in banned:
            word_count[word]+=1
    return max(word_count.items(), key=operator.itemgetter(1))[0]

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(mostCommonWord(paragraph, banned))