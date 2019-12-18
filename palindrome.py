def palindrome(s):
  '''
  DOCSTRING: Check to see if a word, phrase or a sequence is a palindrome
  '''
    s = s.replace(" ", "")
    middle = int(len(s)/2)
    if len(s)%2 == 0:
        first_half = s[:middle]
        second_half = s[middle:]
    else:
        first_half = s[:middle]
        second_half = s[middle+1:]
    return first_half == second_half[::-1]
