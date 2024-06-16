def is_palindrome(string):
    return string.casefold()[::-1] == string.casefold()


def sentence_is_palindrome(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    return string.casefold()[::-1] == string.casefold()


word = input("Please enter a word: ")
if sentence_is_palindrome(word):
    print("'{}' is a palindrome".format(word))

else:
    print("'{}' is not a palindrome".format(word))