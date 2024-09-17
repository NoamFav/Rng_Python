# Open the input file and read its contents
with open('cursus.txt', 'r') as f:
    text = f.read()

# Specify the words to search for and the replacement strings
search_words = ['<cursus>', '<ecole>']
replacement_strings = ['hi', 'planet']

# Loop through each search word and replace every occurrence with the corresponding replacement string
for i in range(len(search_words)):
    search_word = search_words[i]
    replacement_string = replacement_strings[i]
    text = text.replace(search_word, replacement_string)

# Write the modified text to a new file
with open('output.txt', 'w') as f:
    f.write(text)
