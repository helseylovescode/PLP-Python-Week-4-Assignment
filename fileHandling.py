def modify_file_content(input_filename, output_filename):
    
    """
    Reads a file, modifies its content, and writes to a new file.
    
    Parameters:
    - input_filename (str): The name of the file to read.
    - output_filename (str): The name of the file to write modified content.
    """
    
    try:
        # Open the input file for reading
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
        
        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()
        
        # Open the output file for writing
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
        
        print(f"Modified content written to '{output_filename}' successfully.")
    
    except FileNotFoundError:
                
        # Handle the case where the input file doesn't exist
        print(f"Error: The file '{input_filename}' does not exist.")
        create_file = input(f"Would you like to create '{input_filename}'? (yes/no): ").strip().lower()
        if create_file == 'yes':
            with open(input_filename, 'w') as new_file:
                print(f"File '{input_filename}' has been created. Add content to it and try again.")
        else:
            print("Operation canceled.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Main program
if __name__ == "__main__":
    # Ask the user for the input filename
    input_filename = input("Enter the name of the file to read: ")
    
    # Define the output filename
    output_filename = "modified_" + input_filename
    
    # Call the function to process the file
    modify_file_content(input_filename, output_filename)
