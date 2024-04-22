import os

def generate_help():
    # Get the directory of the current module
    module_dir = os.path.dirname(__file__)
    # Construct the full path to the Markdown file
    file_path = os.path.join(module_dir, 'bot_help.md')
    
    with open(file_path, 'r') as file:
        help = file.read()
    return help

if __name__=="__main__":
    print(generate_help())