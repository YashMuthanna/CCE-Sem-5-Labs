# (a) Create a text file with minimum eight lines.
with open("sample_text.txt", "w") as file:
    file.write("line 1.\n")
    file.write("line 2.\n")
    file.write("Line 3.\n")
    file.write("Line 4.\n")
    file.write("Line 5.\n")
    file.write("Line 6.\n")
    file.write("Line 7.\n")
    file.write("Line 8.\n")

# (b) Read the data from the file.
with open("sample_text.txt", "r") as file:
    lines = file.readlines()

# (c) Store the data in dictionary form with line numbers as keys and string and length as values.
line_dict = {}
for i, line in enumerate(lines, start=1):
    # loop iterates through each line in the lines list, generating an index i and the corresponding line
    # line using the enumerate() function. The start=1 parameter ensures that the indices start from 1, instead 0
    line = line.strip()
    # .strip() method on the line to remove leading and trailing whitespace characters
    line_length = len(line)
    line_dict[i] = [line, line_length]
    # adds an entry to the line_dict dictionary. The key is the line number (i), and the value is a list containing the
    # cleaned line (line) and its calculated length (line_length)
# enumerate(lines, start=1)-  returns an iterator that generates pairs of index-value pairs

print("Dictionary with line numbers as keys and [line, length] as values:")
for key, value in line_dict.items():
    print(key, ":", value)

# (d) Create a dictionary with letter frequencies.
letter_freq = {}
for line in lines:
    for char in line:
        if char.isalpha():
            # .isalpha() method of strings returns True if all characters in the string are letters.
            char = char.lower()
            #  count is case-insensitive
            if char in letter_freq:
                letter_freq[char] += 1
            else:
                letter_freq[char] = 1

print("\nDictionary with letters as keys and frequencies as values:")
for key, value in letter_freq.items():
    print(key, ":", value)
