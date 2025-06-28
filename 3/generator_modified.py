import random

def getWords(filename):
    """Reads words from a file and returns them as a tuple."""
    words = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                words.extend(line.upper().split())
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    return tuple(words)

articles = getWords("C:/Lab2/3/articles.txt")
nouns = getWords("C:/Lab2/3/nouns.txt")
verbs = getWords("C:/Lab2/3/verbs.txt")
prepositions = getWords("C:/Lab2/3/prepositions.txt")

def sentence():
    """Builds and returns a sentence."""
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounPhrase() + " " + \
           prepositionalPhrase()

def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    """Allows the user to input the number of sentences to generate."""
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())

if __name__ == "__main__":
    main()
