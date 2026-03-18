import string

def file_to_wordlist(fname):
    wordlist = []

    with open(fname, 'r') as f:
        text = f.read()

    print("DEBUG: raw length =", len(text))  # keep for now

    # Step 1: lowercase
    text = text.lower()

    # Step 2: remove punctuation
    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    text = text.translate(translator)

    # Step 3: split into words
    wordlist = text.split()

    return wordlist

