# t_c = 18
# tmp = "ok"
#
# def fahrenheit(t_c):
#     tmp = t_c*9/5
#     return tmp + 32
#
# print(fahrenheit(t_c))
# print(tmp)
#-----------------------------------------------------------------------------------------------------------------------

# x  = int(input())
#
# if x % 2 == 1:
#     print("Your digit is NOT ODD")
# else:
#     print("Your digit is ODD")

#-----------------------------------------------------------------------------------------------------------------------

# for i in range(5):
#     x = i * i
#     print("now we have the following value of x:", x)
# print(x)

#-----------------------------------------------------------------------------------------------------------------------
# ok_status = True
# vowels = ['a','u','i','e','o']
#
# def check(word):
#     global ok_status
#     for vowel in vowels:
#         if vowel in word:
#             return True
#     ok_status = False
#     return False
#
# print(check("abracadabra"))

#-----------------------------------------------------------------------------------------------------------------------
def f():
    ok_status = True
    vowels = ['a','u','i','e','o']

    def check(word):
        nonlocal ok_status
        for vowel in vowels:
            if vowel in word:
                return True
        ok_status = False
        return False

    print(check("abracadabra"))
    print(ok_status)
    print(check("www"))
    print(ok_status)


print(f())
print(ok_status)






