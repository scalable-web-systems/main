# Get all markdown files in the directory 
exceptions = ['README.md']

# Herlp Functions
def get_file_names():
    import os
    
    files = os.listdir('.')
    file_names = []

    for file in files:
        if '.md' in file and file not in exceptions:
            print(file)
            file_names.append(file)
    return file_names

# Check the PR has only Markdown files
def test_check_only_md():
    import os

    files = os.listdir('.')

    for file in files:
        if '.md' not in file:
            assert False
    
    assert True


# Check the Markdown file has a comment
def test_check_comment():
    for file_name in get_file_names():
        with open(file_name, 'r') as f:
            text = f.read()
            first_line = text.split('\n')[0]
            if('<!--' in first_line and '-->' in first_line):
                assert True
            else: 
                assert False



