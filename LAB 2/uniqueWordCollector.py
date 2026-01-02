# 2. Unique Words Collector
# Take a paragraph input from the user. Split it into words, remove duplicates, sort them
# alphabetically, and count the total number of unique words.

import string
def Unique_Word_Collector():

    while True:
        user_input = input("Enter a paragraph\n ")
        
        if user_input == "":
            print("No more input. Exiting...")
            break

        words_entries = user_input.split(" ")
        print("Words are : \n", words_entries)
        
        user_input = user_input.lower()

        for ch in string.punctuation:
            user_input = user_input.replace(ch, "")

        words = user_input.lower().split() # Lower ma lagcha 

        unique_words = set(words) # set removes dublicate

        sorted_words = sorted(unique_words) # Sorted function sortes the words aplhabetically.

        print("\nSorted Words are words:", sorted_words)

        print("\nUnique words are:", (unique_words))

        print("\nTotal unique words:", len(unique_words))

Unique_Word_Collector()