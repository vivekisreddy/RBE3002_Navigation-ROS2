import string
import heapq


def file_to_wordlist(fname):
    """
    Reads a text file and returns a list of cleaned words.

    Processing steps:
    - Convert all text to lowercase
    - Remove punctuation (including apostrophes and hyphens)
    - Split text into individual words
    """

    wordlist = []

    # Open file and read entire contents as a string
    with open(fname, 'r') as f:
        text = f.read()

    # Convert all characters to lowercase to ensure uniformity
    text = text.lower()

    # Create translation table:
    # each punctuation character is replaced with a space
    # This ensures words like "rabbit-hole" → "rabbit hole"
    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))

    # Apply translation to remove punctuation
    text = text.translate(translator)

    # Split text into words based on whitespace
    wordlist = text.split()

    return wordlist


def wordlist_to_wordfreq(wordlist):
    """
    Takes a list of words and returns a dictionary
    mapping each word to its frequency.

    Demonstrates use of dictionaries as hash maps.
    """

    wordfreq = {}

    # Iterate through each word in the list
    for word in wordlist:
        # If word already exists in dictionary, increment count
        if word in wordfreq:
            wordfreq[word] += 1
        else:
            # Otherwise, initialize count to 1
            wordfreq[word] = 1

    return wordfreq


def wordfreq_to_wordpriority(wordfreq):
    """
    Converts a word-frequency dictionary into a priority queue (min-heap).

    Each element in the heap is a tuple (frequency, word),
    so the heap is ordered by frequency.

    Returns a list sorted in increasing order of frequency.
    """

    wordpriority = []

    # Push each (frequency, word) pair into the heap
    for word, freq in wordfreq.items():
        heapq.heappush(wordpriority, (freq, word))

    # Pop elements one by one to produce a sorted list
    # heapq.heappop always removes the smallest element
    return [heapq.heappop(wordpriority) for _ in range(len(wordpriority))]


if __name__ == "__main__":
    # Input file (make sure path is correct)
    fname = "ch1ch2.txt"

    # Step 1: Convert file → list of words
    words = file_to_wordlist(fname)
    print("Words:", len(words))

    # Step 2: Convert word list → frequency dictionary
    freq = wordlist_to_wordfreq(words)
    print("Unique words:", len(freq))

    # Step 3: Convert dictionary → sorted priority queue
    priority = wordfreq_to_wordpriority(freq)

    # Print first 10 entries (lowest frequency words)
    print("Sorted output sample:", priority[:10])