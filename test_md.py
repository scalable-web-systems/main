# Get all markdown files in the directory 
def get_file_names():
    import os

    exceptions = ['README.md']
    files = os.listdir('.')
    file_names = []

    for file in files:
        if '.md' in file and file not in exceptions:
            print(file)
            file_names.append(file)
    return file_names


def test_check_comment():
    for file_name in get_file_names():
        with open(file_name, 'r') as f:
            text = f.read()
            first_line = text.split('\n')[0]
            if('<!--' in first_line and '-->' in first_line):
                assert True
            else: 
                assert False