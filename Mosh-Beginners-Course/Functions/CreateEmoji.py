def emoji_convertor(message):
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
    return output