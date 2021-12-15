# import markdown
import re
with open('TEST1.md', 'r') as f:
    text = f.read()
    print(int(re.search(r'\d+', text).group()))