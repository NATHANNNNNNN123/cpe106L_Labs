def mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def get_median(numbers):
    if not numbers:
        return 0
    numbers.sort()
    midpoint = len(numbers) // 2
    if len(numbers) % 2 == 1:
        return numbers[midpoint]
    else:
        return (numbers[midpoint] + numbers[midpoint - 1]) / 2

def get_mode(words):
    if not words:
        return None
    theDictionary = {}
    for word in words:
        word = word.upper()
        theDictionary[word] = theDictionary.get(word, 0) + 1

    theMaximum = max(theDictionary.values())
    for key in theDictionary:
        if theDictionary[key] == theMaximum:
            return key
        

def main():
    # Sample data
    number_data = [1, 12, 3, 4, 4, 5, 5, 5, 6]
    word_data = ["apple", "banana", "apple", "orange", "banana", "banana"]

    print("Data:", number_data)
    print("Mean:", mean(number_data))
    print("Median:", get_median(number_data))
    print("Mode (from words):", get_mode(word_data))

if __name__ == "__main__":
    main()