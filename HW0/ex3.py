import string
import heapq

fname = "ch1ch2.txt"
def file_to_wordlist(fname):
    wordlist = []

    # Step 1: Open and read the file
    with open(fname, 'r') as f:
        text = f.read()
        print("FILE READ SUCCESS")
    # Step 2: Convert all text to lowercase
    # This ensures "Alice" and "alice" are treated the same
    text = text.lower()
    # Step 3: Replace hyphens with spaces
    # So "rabbit-hole" becomes "rabbit hole"
    text = text.replace('-', ' ')
    # Step 4: Remove punctuation
    # string.punctuation includes: ! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)
    # Step 5: Split text into words
    # This creates a list of words separated by spaces
    wordlist = text.split()
    print("DEBUG: first 200 chars:", text[:200])
    print("DEBUG: number of words:", len(wordlist))

    return wordlist
def wordlist_to_wordfreq(wordlist):
    wordfreq = {}
    # Loop through every word in the list
    for word in wordlist:
        # If the word already exists in the dictionary,
        # increment its count by 1
        if word in wordfreq:
            wordfreq[word] += 1
        # If the word is not in the dictionary,
        # add it with a count of 1
        else:
            wordfreq[word] = 1

    return wordfreq

import heapq

def wordfreq_to_wordpriority(wordfreq):
    wordpriority = []
    # Step 1: Push (frequency, word) tuples into the heap
    # Heap will automatically sort based on the first element (frequency)
    for word, freq in wordfreq.items():
        heapq.heappush(wordpriority, (freq, word))
    # Step 2: Pop elements one by one to get sorted order (ascending frequency)
    sorted_list = []
    while wordpriority:
        sorted_list.append(heapq.heappop(wordpriority))
    return sorted_list

if __name__ == "__main__":
    words = file_to_wordlist(fname)
    print("Words:", len(words))
    freq = wordlist_to_wordfreq(words)
    print("Unique words:", len(freq))
    priority = wordfreq_to_wordpriority(freq)
    # Show lowest frequency words
    print("Lowest frequency words:", priority[:10])
    # Show highest frequency words
    print("Highest frequency words:", priority[-10:])