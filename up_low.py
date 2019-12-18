# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
# 
# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected Output : 
# No. of Upper case characters : 4
# No. of Lower case Characters : 33

def up_low(s):
    ups = 0
    lows = 0
    for letter in s:
        if letter not in '., ?!':
            if letter.islower():
                lows +=1
            else:
                ups +=1
    print(f'Original String: {s}')
    print(f'No. of Upper case characters : {ups}')
    print(f'No. of Lower case characters : {lows}')
