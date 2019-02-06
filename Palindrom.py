# A word is a palindrome if it has fewer than two
# letters, or if the first and last letters are the
# same and the middle bit is a palidrome
def isPalindrome(text):
  # a word with one or no letters is a palindrome
  if len(text) < 2:
    return True
  # are the first and last letters the same?
  if text[0] != text[-1]:
    return False
  else:
    # is the middle bit of the word a palidrome?
    return isPalindrome(text[1:-1])

print("Palindrome:",isPalindrome(input("Enter a word:")))