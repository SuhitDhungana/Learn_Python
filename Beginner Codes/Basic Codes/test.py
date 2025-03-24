def main():
    sentence = input("Enter the sentence: ").strip()
    letter_count, space_count, sentence_count, counter = 0, 0, 0, 0

    # Count letters, spaces, and sentences
    for character in sentence:
        if character.isalpha():
            letter_count += 1
        elif character == " ":
            space_count += 1
        elif character == "?" or character == "." or character == "!":
            sentence_count += 1
        counter += 1

    word_count = space_count + 1

    # Calculation of Coleman-Liau Index
    L = letter_count / word_count * 100
    S = sentence_count / word_count * 100.0
    index = 0.0588 * L - 0.296 * S - 15.8
    grade = round(index)

    # Check Grade
    if grade < 1:
        print("Before Grade 1")
    elif grade > 16:
        print("Grade 16+")
    else:
        print(f"Grade {grade}")


if __name__ == "__main__":
    main()
