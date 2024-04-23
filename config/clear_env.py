'''
This script is used to generate the dotenv file, based on my actual .env file, which isnt synchronized to git.
'''
import os

def clear_and_refill_env(file_path, refill_value="'***Your_Data***'", output_file='dotenv'):
    # Read the contents of the .env file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Clear values associated with existing keys
    modified_lines = []
    for line in lines:
        key_value = line.strip().split('=', 1)
        if len(key_value) == 2:
            modified_lines.append(f"{key_value[0]}={refill_value}\n")  # Refill the value with refill_value
        else:
            modified_lines.append(line)  # Keep comments or empty lines

    # Write the modified content to a new file
    with open(output_file, 'w') as file:
        file.writelines(modified_lines)

# Example usage
env_file_path = '.env'

clear_and_refill_env(env_file_path)
