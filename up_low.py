def up_low(s):
    '''
    Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
     
    Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
    # Expected Output : 
    # No. of Upper case characters : 4
    # No. of Lower case Characters : 33
    '''
    ups = 0
    lows = 0
    for letter in s:
        if letter.islower():
            lows +=1
        elif letter.isupper():
            ups +=1
        else:
            continue
    print(f'Original String: {s}')
    print(f'No. of Upper case characters : {ups}')
    print(f'No. of Lower case characters : {lows}')
