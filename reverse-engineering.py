def hash_string(to_encode):
    hash_value = 26
    letters = "abcdefghijklmnopqrstuvwxyz"
    
    for char in to_encode:
        hash_value = hash_value * 37 + letters.index(char)
    
    return hash_value

test = hash_string("hello")
print(test)

def inverse_hash_string(hash_value):
    letters = "abcdefghijklmnopqrstuvwxyz"
    inverse_string = ""

    while hash_value > 0:
        index = hash_value % 37
        if index < len(letters):
            inverse_string = letters[index] + inverse_string
        else:
            inverse_string = inverse_string
        hash_value = (hash_value - index) // 37

    return inverse_string

inverse_test = inverse_hash_string(test)
print(inverse_test)
