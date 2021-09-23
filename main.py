# Doğrusal Arama Algoritması

def LinearSearch(array, search):
    for i in range(len(array)):
        if array[i] == search:
            return i

print(LinearSearch([4, 8, 18, 97], 18))