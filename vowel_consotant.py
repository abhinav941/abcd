n=input()
if n.isalpha():
    if n in set(['a','e','i','o','u','A','E'.'I','O','U']):
        print('Vowel')
    else:
        print('Consonant')
else:
    print('invalid')
