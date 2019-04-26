#make a function to sanitize words

with open ("mobydick.txt","r") as file_object:
    linecount=0
    wordcount=0
    bigwordlist = []
    for line in file_object:
        linecount=linecount+1
        words=line.split(" ")
        bigwordlist.extend(words)
        for words in bigwordlist:
            words = words.strip(string.punctuation + string.whitespace)
        wordslen=len(words)
        wordcount=wordcount+wordslen
    print("There are {:,} lines of text in the file.".format(linecount))
    print("There are {:,} words in the file.".format(wordcount))
    sorted_words=sorted(bigwordlist, key = len)
    longest=sorted_words[-1]
    print("'{}' is the longest word in the text.".format(longest))
    frequency={}
    for word in bigwordlist:
        word=word.lower()
        if word not in frequency:
            frequency[word]=1
        else:
            frequency[word]+=1
    print(sorted(frequency.items())[0])
#        frequency=[words.count(word)]
#        most_used=frequency[-1]
    
