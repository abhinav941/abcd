n=input()
if n.isalpha():
    if n in set(['a','e','i','o','u']):
        print('Vowel')
    else:
        print('Consonant')
else:
    print('invalid')
