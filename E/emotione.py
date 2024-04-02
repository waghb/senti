
import string
from collections import Counter
import matplotlib.pyplot as plt

text = open(r"/home/rutika/Documents/PBL/E/output_file", encoding='utf-8').read()
#print(text)

# lower case conversion
lower_case=text.lower()
#print(lower_case)

#removing punctuation
cleaned_text=lower_case.translate(str.maketrans('','',string.punctuation))
#print(cleaned_text)


#tokenizing
token_text=cleaned_text.split()
#print(token_text)

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

# Removing stop words from the tokenized words list
final_words = []
for word in token_text:
    if word not in stop_words:
        final_words.append(word)

#print(final_words)

emotion_list=[]

with open('emotions.txt','r') as file:
    for line in file:
        clear_line=line.replace("\n",'').replace(",",'').replace("'",'').strip()
        word,emotion=clear_line.split(':')
      #  print("word:"+word+""+"emotions:"+emotion)

        if word in final_words:
            emotion_list.append(emotion)

print(emotion_list)
w=Counter(emotion_list)
#print(w)


fig, axl=plt.subplots()
axl.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()
