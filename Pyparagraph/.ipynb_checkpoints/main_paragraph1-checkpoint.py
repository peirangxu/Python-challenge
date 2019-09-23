import csv
import re

with open("/Users/peirangxu/Desktop/Python-challenge/Pyparagraph/paragraph_1.txt","r") as txtfile:
    lines = txtfile.read()
    print(lines)
    
    #Count number of words in the paragraph
    words = lines.split(" ") 
    num_words = len(words)
    
    #Calculate the average letter count per word
    letter_count = []
    for i in range(len(words)):
        letter_count.append(len(words[i]))
    ave_letter_count = sum(letter_count)/len(letter_count)
    ave_letter_count = round(ave_letter_count,1)
    
    #Approximate sentence count
    sentence = re.split("(?<=[.!?]) +", lines)
    num_sen = len(sentence)
    
    word_count = []
    #Average sentence length
    for j in range(len(sentence)):
        word_in_sentence = sentence[j].split(" ")
        word_count.append(len(word_in_sentence))
    ave_sen_len = sum(word_count)/len(word_count)
        
with open("/Users/peirangxu/Desktop/Python-challenge/Pyparagraph/paragraph_1_Analysis.txt","w") as text:
    text.write("Paragraph 1 Analysis \n")
    text.write("--------------------------\n")
    text.write("Approximate Word Count: " + str(num_words) + "\n")
    text.write("Approximate Sentence Count: " + str(num_sen)+ "\n")
    text.write("Average Letter Count: " + str(ave_letter_count) + "\n")
    text.write("Average Sentence Length: " + str(ave_sen_len) + "\n")
    text.write("---------------------------\n")
          