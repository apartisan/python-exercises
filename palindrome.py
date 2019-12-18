def palindrome(s):
  '''
  DOCSTRING: Check to see if a word, phrase or a sequence is a palindrome
  '''
    s = s.replace(" ", "")
    return s == s[::-1]
