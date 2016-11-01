def pig_it(text):
    # Constants
    TEXT_LIST = text.split()
    SUFFIX = "ay"
    PUNCTUATION = ["!", "?", ".", ","]

    # Variables
    newText = ""
    numWord = 0

    # Main loop
    for word in TEXT_LIST:
        numWord += 1
        if word in PUNCTUATION:
            newWord = word

        elif numWord == len(TEXT_LIST):
            newWord = word[1 :] + word[0] + SUFFIX

        else:
            newWord = word[1 :] + word[0] + SUFFIX + " "

        newText += newWord

    return newText
