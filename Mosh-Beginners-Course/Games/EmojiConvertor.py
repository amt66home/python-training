# We will create a dictionary to convert symbols to emojis
message = input(">")

# uses the split value as a separator to return multiple words  into a list
words = message.split(' ')
#create dictionery - windows key + . will give you emojis
emojis = {
    ":)": "😊",
    ":(": "😢",
    ":D": "😁"
}
output = " "
for word in words:
    output += emojis.get(word, word) + " "
print(output)

