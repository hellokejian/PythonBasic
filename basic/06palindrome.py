def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]
def test(str):
    if len(str) == 0:
        # print('you should enter something')
        return True
    elif len(str) == 1:
        return True
    else:
        if first(str) != last(str):
            return False
        else:
            return test(middle(str))
print(test('kejian'))
print(test(''))
print(test('noon'))
print(test('aba'))