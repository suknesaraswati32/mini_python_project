# with open('text.txt','r') as f:
#   text=f.read()
# list=text.split()
# count=0
# freq={}
# for word in list:
#   if word not in freq:
#     freq[word]=1
#   else:
#     freq[word]+=1
      
#   count=count+1
# print(freq)  
# print(count)
# for key,val in freq.items():
#   if(val>=1):
#     print(key,":",val)
  
# queryt=0 
# with open ('sara.txt','a+') as f:
#    f.write('Highlight (or mark) all occurrences of the query in the text by surrounding them with ** or another marker of your choice.')
#    query=input("enter your query")
#    f.seek(0)
#    text=f.read()
# if query in text:
#    queryt=queryt+1
#    query="**"
# print(queryt)  
# print(text) 



# import re


# input_file = input("Enter input file name: ")
# target = input("Enter word or phrase to find: ")
# replacement = input("Enter replacement word or phrase: ")

# choice = input("Case-insensitive replacement? (yes/no): ")

# try:
#     with open(input_file, "r", encoding="utf-8") as file:
#         text = file.read()

#     if choice.lower() == "yes":
#         modified_text = re.sub(
#             re.escape(target),
#             lambda match: replacement,
#             text,
#             flags=re.IGNORECASE
#         )
#     else:
#         modified_text = text.replace(target, replacement)

#     output_file = "modified_" + input_file
#     with open(output_file, "w", encoding="utf-8") as file:
#         file.write(modified_text)

#     print("Replacement completed successfully.")
#     print("New file:", output_file)

# except FileNotFoundError:
#     print("File not found.")

# except Exception as e:
#     print("An error occurred:", e)
    
    
    
    
# import re


# text = input("Enter a paragraph:\n")


# abbreviations = [
#     "Mr.", "Mrs.", "Ms.", "Dr.", "Prof.",
#     "Sr.", "Jr.", "St.", "vs.", "etc."
# ]

# for abbreviation in abbreviations:
#     text = text.replace(
#         abbreviation,
#         abbreviation.replace(".", "<DOT>")
#     )


# sentences = re.split(r'(?<=[.!?])\s+', text.strip())

# for i in range(len(sentences)):
#     sentences[i] = sentences[i].replace("<DOT>", ".")

# print("\nIndividual Sentences:")

# for i, sentence in enumerate(sentences, 1):
#     print(i, ":", sentence)
    
    
# import re
# from collections import Counter


# text = input("Enter the text:\n")


# sentences = re.split(r'(?<=[.!?])\s+', text.strip())


# words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

# stop_words = {
#     "the", "is", "am", "are", "was", "were",
#     "a", "an", "and", "or", "but", "in", "on",
#     "at", "to", "of", "for", "with", "from",
#     "this", "that", "it", "as", "by", "be",
#     "has", "have", "had", "he", "she", "they",
#     "we", "you", "i"
# }


# important_words = [
#     word for word in words
#     if word not in stop_words
# ]

# word_frequency = Counter(important_words)

# sentence_scores = {}

# for sentence in sentences:
#     sentence_words = re.findall(r'\b[a-zA-Z]+\b', sentence.lower())

#     score = 0

#     for word in sentence_words:
#         if word in word_frequency:
#             score += word_frequency[word]

#     sentence_scores[sentence] = score

# summary_length = max(1, len(sentences) // 3)


# top_sentences = sorted(
#     sentence_scores,
#     key=sentence_scores.get,
#     reverse=True
# )[:summary_length]

# summary = [
#     sentence for sentence in sentences
#     if sentence in top_sentences
# ]
# print("\n----- SUMMARY -----")

# for sentence in summary:
#     print(sentence)
    
    
    
import re

text = input("Enter text:\n")
contractions = {
    "don't": "do not",
    "doesn't": "does not",
    "didn't": "did not",
    "can't": "cannot",
    "couldn't": "could not",
    "won't": "will not",
    "wouldn't": "would not",
    "isn't": "is not",
    "aren't": "are not",
    "wasn't": "was not",
    "weren't": "were not",
    "hasn't": "has not",
    "haven't": "have not",
    "hadn't": "had not",
    "shouldn't": "should not",
    "mustn't": "must not",
    "i'm": "i am",
    "i'll": "i will",
    "i've": "i have",
    "you're": "you are",
    "you'll": "you will",
    "you've": "you have",
    "he's": "he is",
    "she's": "she is",
    "it's": "it is",
    "we're": "we are",
    "they're": "they are"
}

text = text.lower()


for contraction, expansion in contractions.items():
    text = text.replace(contraction, expansion)

text = re.sub(r'\d+', '', text)

text = re.sub(r'[^a-zA-Z\s]', '', text)

text = re.sub(r'\s+', ' ', text).strip()

print("\n----- CLEANED TEXT -----")
print(text)    