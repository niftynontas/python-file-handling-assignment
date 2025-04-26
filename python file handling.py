def read_and_write_file():
    try:
        # Ask the user for the filename to read
        input_filename = input("Enter the filename to read: ")
        
        # Try to open and read the file
        with open(input_filename, 'r') as file:
            content = file.read()
            print("File content successfully read.")
            
            # Modify the content (for this example, we'll convert it to uppercase)
            modified_content = content.upper()
            
            # Ask for the output filename to write the modified content
            output_filename = input("Enter the filename to write the modified content to: ")
            
            # Write the modified content to the new file
            with open(output_filename, 'w') as output_file:
                output_file.write(modified_content)
            
            print(f"Modified content written to {output_filename}")
    
    except FileNotFoundError:
        print("Error: The file does not exist.")
    
    except IOError:
        print("Error: An issue occurred while reading or writing the file.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
read_and_write_file()
