import random
def main():
    hangman_art = {
        1 : ("   ",
             "   ",
             "   "),
        2 : (" o ",
             "   ",
             "   "),
        3 : (" o ",
             " | ",
             "   "),
        4 : (" o ",
             " |\\ ",
             "   "),
        5 : (" o ",
             "/|\\ ",
             "   "),
        6 : (" o ",
             "/|\\ ",
             " /\\ ")
    }
    
    word_list = ("apple",
                 "banana",
                 "peach",
                 "mango",
                 "potato",
                 "tomato",
                 "lychee",
                 "raspberry",
                 "blueberry",
                 "strawberry",
                 "pineapple",
                 "carrot",
                 "lettuce",
                 "spinach",
                 "kimchi",
                 "momo",
                 "ginger",
                 "cranberry",
                 "grapes",
                 "kiwi",
                 "pomegranate",
                 "almond",
                 "raisin",
                 "pistachio",
                 "dates",
                 "cashew",
                 "jackfruit",
                 "orange",
                 "lemon",
                 "lime",
                 "watermelon",
                 "papaya"
    )
    
    underscores = []
    word = random.choices(word_list) # generate a random word from 'word_list'
    word = word[0] # converting list 'word' into string
        
    for i in range(0, len(word)): # making a string, containg 'len(word)' underscores
         underscores.append("_")
     
    hangman(word, underscores, hangman_art)

   
def hangman(word, underscores, hangman_art):
     wrong = 0
     correct = 0
     changed_word = []
     counter = 0
     # letter = "" (I don't think this line of code is needed)
     for i in range(0, len(word)):
          changed_word.append(word[i])
     print(word) # remove this line after the program is complete
     
     while wrong < 5 and correct < len(word): 
          letter = input("Enter the letter: ")
          
          if letter in word:
               temp_1 = replace_underscore(letter, underscores, changed_word, counter)
               underscores = temp_1[0]
               changed_word = temp_1[1]    
               counter = temp_1[2]          
               correct += 1
          else:
               wrong += 1
          
          underscores_copy = underscores
          presentation(underscores_copy, hangman_art, wrong, correct, word)
          

def replace_underscore(letter, underscores, changed_word, counter):
     position = changed_word.index(letter)
     if changed_word.count(letter) > 1: # Repetition of letter
          underscores[position + counter] = letter
          counter += 1
          changed_word.remove(letter)
     else:
          underscores[position] = letter
     
     return (underscores, changed_word, counter)
        
            
def presentation(underscores, hangman_art, wrong, correct, word):
     for i in range(0, len(underscores)):
          print(underscores[i], end= " ")
               
     print()
          
     for i in range(0, 3):
          print(hangman_art[wrong + 1][i])
     
     if wrong == 5:
          print("************ ALAS! YOU LOST THE HANGMAN!! ************")
     elif correct == len(word):
          print("************ BRAVO! YOU WON THE HANGMAN!! ************")
          
          
if __name__ == "__main__":
    main()
  

''' 
I guess I need to make separate cases if the repetiton of letter is before or after
(something like this; i'm not sure, however)
'''