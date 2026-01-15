'''5. Use the re module to write a script that searches through a paragraph and extracts all
words that start with an uppercase letter (e.g., "London", "Python") to identify proper
nouns or sentence starters.'''

import re

paragraph = "London is the capiTal of England. Python is a powerful Language. I Study Computer Science."

# Find words that start with an uppercase letter
capital_words = re.findall(r'\b[A-Z][a-zA-Z]*\b', paragraph)

print("Words starting with uppercase letter:")
print(capital_words)
