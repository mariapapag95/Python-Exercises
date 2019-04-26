"""
with open("article.txt","r") as file_object:
    for line in file_object:
        words=line.split(" ")
        for word in words:
            word=word.lower()
            frequency=[words.count(i)]
            most_used=frequency[-1]
    print(most_used)


linecount=0
    wordcount=0
    bigwordlist = []
    for line in file_object:
        linecount=linecount+1
        words=line.split(" ")
        bigwordlist.extend(words)
        wordslen=len(words)
        wordcount=wordcount+wordslen


count=0
        occurences_of_words=[]
        for line in file_object:
            words=line.split()
            #creates a list of all the words in each line of the file
            for word in words: #each individual word
                word=word.casefold #sanitizes cases
                count += line.count(word)
                occurences_of_words.append(word)
        most_used=sorted(occurences_of_words, key=count)
        return most_used[0:n]
print(word_stats("article.txt",5))
        """

def word_stats(file,n):
    with open (file,"r") as file_object:
        bigwordlist = []
        count=0
        for line in file_object:
            words=line.split(" ")
            bigwordlist.extend(words)
            for word in words:
                count = file_object.count(word)
        return list(count)

print(word_stats("article.txt",5))

"""
def word_stats(file,n):
    with open (file, 'r') as file_object:
        word_dict={}
        for line in file_object:
            wordspilt=line.split()
            """
            