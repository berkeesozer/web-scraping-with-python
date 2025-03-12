import bs4 as bs 
import urllib.request 
import operator 
# ALSO I USED lxml IF PROGRAM DOESNT EXECUTE IN YOUR CMD, TRY TO INSTALL lxml WITH PIP.

def dictionary_for_counting(finalwords): # function for counting words in the book
      wordcounter = {}
      for word in finalwords:
            if word in wordcounter:
                  wordcounter[word] += 1
            else:
                  wordcounter[word] = 1
      return wordcounter

book = input("Enter the book name: ")
answer = input("Do you want to compare word frequencies with another book?(Y/N)")

## only one book

if answer == 'N':
      book = book.replace(" ","_") 
      url = f"https://en.wikibooks.org/wiki/{book}/Print_version"
      req = urllib.request.urlopen(url).read() 
      soup = bs.BeautifulSoup(req,"lxml") 
      f = open("book.txt","w")  
      for i in soup.find_all(class_="mw-parser-output"): 
            f.write(i.text.encode('utf8').decode('ascii', 'ignore')) 
            f.close()
      stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you","name", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself","next","first", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to","line","value", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
      lastwords = []
      finalwords = []
      r = open("book.txt","r") 
      text = r.readlines()
      r.close()
      for line in text:
            for word in line.split():
                  word = word.lower()
                  if word not in stopwords:
                        lastwords.append(word) 

      symbols = "!,.;:(#?[]&)=\">\'<&@^*%'_-123456789/"
      for word in lastwords:
            for symbol in symbols:
                  if symbol in word:
                        index_of_symbol = word.index(symbol) 
                        word = word.replace(symbol,"")       
                        word = word[0:index_of_symbol]
            if len(word)!=1 and word != '' and word not in stopwords: 
                  finalwords.append(word) 
      wordcounter = dictionary_for_counting(finalwords) 
      book = book.replace("_"," ")
      a = 1
      b = int(input("How many word frequencies do you want to see? "))
      print(f"BOOK 1: {book}")
      print("NO WORD FREQ1")
      for word,quantity in sorted(wordcounter.items(),key = operator.itemgetter(1),reverse=True):
            print(a,word,quantity)
            a+=1                               
            if a > b:                          
                  break                        

#### comparison of two books

elif answer == "Y":
      book = book.replace(" ","_")
      url = f"https://en.wikibooks.org/wiki/{book}/Print_version" 
      req = urllib.request.urlopen(url).read()
      soup = bs.BeautifulSoup(req,"lxml")
      f = open("book.txt","w")
      for i in soup.find_all(class_="mw-parser-output"):
            f.write(i.text.encode('utf8').decode('ascii', 'ignore'))
            f.close()
      stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you","name", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself","next","first", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to","line","value", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
      lastwords= []
      finalwords = []
      r = open("book.txt","r")
      text = r.readlines()
      r.close()
      for line in text:
            for word in line.split():
                  word = word.lower()
                  if word not in stopwords:
                        lastwords.append(word) 

      symbols = "!,.;:(#?[]&)=\">\'<&@^*%'_-123456789/"
      for word in lastwords:
            for symbol in symbols:
                  if symbol in word:
                        index_of_symbol = word.index(symbol)
                        word = word.replace(symbol, "")
                        word = word[0:index_of_symbol]
            if len(word)!=1 and word != '' and word not in stopwords:
                  finalwords.append(word) 
      wordcounter = dictionary_for_counting(finalwords) 

      ######## asking for the second book


      book2 = input("Enter the second book name: ")
      book2 = book2.replace(" ", "_")                   
      url = f"https://en.wikibooks.org/wiki/{book2}/Print_version"
      req = urllib.request.urlopen(url).read()
      soup = bs.BeautifulSoup(req, "lxml")
      f = open("book2.txt", "w")
      for i in soup.find_all(class_="mw-parser-output"):
            f.write(i.text.encode('utf8').decode('ascii', 'ignore'))  # IGNORING ASCI CHARACTERS
            f.close()
      stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you","name", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself","next","first","it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to","line","value", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
      lastwords2 = []
      finalwords2 = []
      r = open("book2.txt", "r") 
      text = r.readlines()
      r.close()
      for line in text:
            for word in line.split():
                  word = word.lower()
                  if word not in stopwords:
                        lastwords2.append(word)

      symbols = "!,.;:(#?[]&)=\">\'<&@^*%'_-123456789/"
      for word in lastwords2:
            for symbol in symbols:
                  if symbol in word:
                        index_of_symbol = word.index(symbol)
                        word = word.replace(symbol, "")
                        word = word[0:index_of_symbol]
            if len(word)!=1 and word != '' and word not in stopwords:
                  word = word.lower()
                  finalwords2.append(word) 
      wordcounter2 = dictionary_for_counting(finalwords2)  
      book = book.replace("_", " ")
      book2 = book2.replace("_"," ")
      a = 1
      b = int(input("How many word frequencies do you want to see? "))
      print(f"BOOK 1: {book}")
      print(f"BOOK 2: {book2}")
      print("COMMON WORDS")
      print("NO WORD FREQ1 FREQ2 FREQ_SUM")
      commonfinalcount = {} 

      
      for word, quantity in sorted(wordcounter.items(), key=operator.itemgetter(1), reverse=True):
            if word in finalwords2:
                  commonfinalcount[word] = wordcounter2[word] + quantity

      
      for word, quantity in sorted(commonfinalcount.items(), key=operator.itemgetter(1), reverse=True):
                  print(a, word, wordcounter[word],wordcounter2[word],quantity) 
                  a += 1
                  if a > b: 
                        break


####### distinct word part
      a = 1
      print(" ")
      print(f"BOOK 1: {book}")
      print("DISTINCT WORDS")
      print("NO WORD FREQ1")

      for word, quantity in sorted(wordcounter.items(), key=operator.itemgetter(1), reverse=True):
            if word in finalwords:
                  if word not in finalwords2: # 
                        print(a,word,quantity)
                        a += 1
                        if a > b:
                              break

      a = 1
      print(" ")
      print(f"BOOK 2: {book2}")
      print("DISTINCT WORDS")
      print("NO WORD FREQ2")
      for word, quantity in sorted(wordcounter2.items(), key=operator.itemgetter(1), reverse=True):
            if word in finalwords2:
                  if word not in finalwords: 
                        print(a,word,quantity)
                        a += 1
                        if a > b:
                              break
else:
      print("Please enter Y or N") 



























