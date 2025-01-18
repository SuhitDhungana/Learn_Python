sentence = "I am Suhit Dhungana Apple Banana to pi a ballon hydrogenhalide ."
    
sentence_length = len(sentence.split())
for i in range(0, sentence_length):
    length = len(sentence.split()[i])
    print(length)