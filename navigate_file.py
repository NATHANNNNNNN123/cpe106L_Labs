def display_file_lines(filename):
    try:
        # Open the file and read all lines into a list
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        # Loop for user interaction
        while True:
            # Display the number of lines in the file
            print(f"\nThe file contains {len(lines)} lines.")
            
            # Prompt the user for a line number
            try:
                line_number = int(input("Enter a line number (0 to exit): "))
                
                if line_number == 0:
                    print("Exiting program.")
                    break
                elif 1 <= line_number <= len(lines):
                    print(f"Line {line_number}: {lines[line_number - 1].strip()}")
                else:
                    print("Invalid line number. Please enter a valid number between 1 and", len(lines))
            
            except ValueError:
                print("Please enter a valid number.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main program
if __name__ == "__main__":
    # Prompt user for filename
    filename = input("Enter the filename: ")
    display_file_lines(filename)
