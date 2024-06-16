def is_palindrome(string):
    return string.casefold()[::-1] == string.casefold()
word = input("Please enter a word: ")

if is_palindrome(word):
    print("'{}' is a palindrome".format(word))

else:
    print("'{}' is not a palindrome".format(word))


