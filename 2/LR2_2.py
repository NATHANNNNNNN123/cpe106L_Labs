def main():
    # Prompt for the filename
    filename = input("Enter the filename: ").strip().strip('"').strip("'")

    try:
        with open(filename, 'r') as file:
            lines = [line.rstrip('\n') for line in file]

        if not lines:
            print("The file is empty.")
            return

        print(f"\nThe file has {len(lines)} lines.\n")

        while True:
            try:
                choice = int(input(f"Enter a line number (1 to {len(lines)}), or 0 to quit: "))
                if choice == 0:
                    print("Exiting program.")
                    break
                elif 1 <= choice <= len(lines):
                    print(f"Line {choice}: {lines[choice - 1]}\n")
                else:
                    print(f"Invalid input. Please enter a number between 1 and {len(lines)}.\n")
            except ValueError:
                print("Please enter a valid number.\n")

    except FileNotFoundError:
        print("The file does not exist. Please check the filename and try again.")

if __name__ == "__main__":
    main()
