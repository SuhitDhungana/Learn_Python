def main():
    sentence = "I am Suhit Dhungana Apple Banana to pi a ballon hydrogenhalide four aaaaaaaluu."
    
    sentence_length = len(sentence.split())
    lengths = []
    for i in range(0, sentence_length - 1):
        length = len(sentence.split()[i])
        if length not in lengths:
            check = 0
            for j in range(i + 1, sentence_length):
                if length == len(sentence.split()[j]):
                    print(sentence.split()[j], end = " ")
                    check  = 1
        
            if check == 1:
                print(sentence.split()[i], end = " ")
                print()
        lengths.append(length)
    

    
if __name__ == "__main__":
    main()