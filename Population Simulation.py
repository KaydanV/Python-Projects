"""
Name: Kaydan Venter
Programming Assignment #: 2
Python Source File Name: K_Venter_Program2.py

Program Description:
This program asks the user to enter a sentence, splits the sentence into words,
and displays each word alongside its length. It demonstrates a while loop for
input validation and a for loop to process the words.

Variables:
- user_sentence (str): the sentence entered by the user.
- words (list[str]): the list of words from the sentence.
- word (str): the current word being processed.
- length (int): the length of the current word.
"""

def get_sentence() -> str:
    """Prompt the user until they enter a non-empty sentence."""
    while True:  # loop until valid input is given
        user_sentence = input("Enter a sentence: ").strip()
        if user_sentence:  # check if not empty
            return user_sentence
        print("Input cannot be empty. Please try again.")

def compute_word_lengths(sentence: str) -> list[tuple[str, int]]:
    """Split the sentence into words and return (word, length) pairs."""
    words = sentence.split()   # split on whitespace
    pairs = []                 # store results
    for word in words:         # loop through each word
        length = len(word)
        pairs.append((word, length))
    return pairs

def display_word_lengths(pairs: list[tuple[str, int]]) -> None:
    """Display each word and its length."""
    print("\nWord lengths:")
    for word, length in pairs:
        print(f"{word}: {length}")

def main():
    user_sentence = get_sentence()
    pairs = compute_word_lengths(user_sentence)
    display_word_lengths(pairs)

if __name__ == "__main__":
    main()
