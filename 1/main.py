from stats import mean, get_median, get_mode

def main():
    # Sample data
    number_data = [1, 2, 3, 4, 4, 5, 5, 5, 6]
    word_data = ["apple", "banana", "apple", "orange", "banana", "banana"]

    print("Data:", number_data)
    print("Mean:", mean(number_data))
    print("Median:", get_median(number_data))
    print("Mode (from words):", get_mode(word_data))

if __name__ == "__main__":
    main()