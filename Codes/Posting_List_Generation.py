import os
import csv
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer 

#Creating a dictionary containing every text file
path= str(input("Enter the path to the folder\n"))
Texts= dict()
for filename in os.listdir(path):           
    f= path+"\\"+filename    
    m = open(f, "r")
    content=m.read()    
    Texts[filename]=content

#Cleaning the file
def remove_unwanted_characters(text):
    uwc= '!#$%&\'\"()*+-=,:;<>{}[]^@~`.?/1234567890\_|'
    for i in range(0, len(uwc)):
        text=text.replace(uwc[i], "")
    text=text.lower()
    return text

#Remaoval of stop words
def stop_words(text):
    stop_words = set(stopwords.words('english')) 
    text = " ".join([word for word in text.split() if word not in stop_words]) #Joins word list w/o stop words with a space " "
    return text

#Lemmatization of the data
def lemmatization(text):
    lemmatizer= WordNetLemmatizer() 
    text = " ".join([lemmatizer.lemmatize(word) for word in text.split()])#Joins lemmatized verbs list with a space " "
    return text

#creating a vocaubulary
def create_vocab(str):
    counts = dict()
    words = str.split()
    counts= Counter(words)
    return counts

#Pruning of vocabulary to create keywords
def key_words(dictionary):
    final_list= list()
    key_max = max(dictionary.keys(), key=(lambda k: dictionary[k]))
    max_freq= dictionary[key_max]
    
    #taking 90% as cutoff
    limit= int(99/100*max_freq)
    
    for word in dictionary:
        if dictionary[word]<=limit:
            final_list.append(word)
        
    return final_list

#creating posting lists per key word
def create_inverted_index():
    final_dict= {}
    for play in Texts:
        for K in key_word_list:
            final_dict.setdefault(K, [])
            if K in Texts[play]:
                final_dict[K].append(Value_play[play])

    return final_dict

#get value for plays
def get_value():
    Value= {}
    flag=0
    for play in Texts:
        Value[play]= flag+1
        flag=flag+1
    return Value

#Main code
key_word_list=[]
for play in Texts:
    Texts[play]= remove_unwanted_characters(Texts[play])
    Texts[play]= stop_words(Texts[play])
    Texts[play]= lemmatization(Texts[play])
    dictionary= create_vocab(Texts[play])
    key_word_list= key_words(dictionary)
    key_word_list.sort()
Value_play= get_value()
final_dictionary= create_inverted_index()
#print(final_dictionary)

#Saving the posting list in a CSV file for ease of access
with open('Posting Lists.csv', 'a',newline='') as csvfile:
    filewriter= csv.writer(csvfile)
    for key in final_dictionary:
        filewriter.writerow([key, final_dictionary[key]])
csvfile.close()
