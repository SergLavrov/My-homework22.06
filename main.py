#
# # Задача 1
# # Написать функцию для определения - является ли введенное
# # вами число полиндромом?
#
def isPolindrom(number):
    str1 = str(number)

    for index in range(len(str1)):
        if str1[index] == str1[len(str1) - (index+1)]:

        return True
    return False

num = int(input('Enter number: '))
result = isPolindrom(num)
print(result)


# Зад.2
# Написать функцию, которая находит самый большой префикс среди массива строк.

def findLongPrefiks(someList):

