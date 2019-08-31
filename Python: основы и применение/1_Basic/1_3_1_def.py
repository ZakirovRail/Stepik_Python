# def function_name(argument1, argument2):
#     return argument1+argument2
#
# x = function_name(2, 8)
# y = function_name(x, 21)
#
# print(y)
# print(type(function_name))
# print(id(function_name))

# ----------------------------------------------------------------------------------------------------------------------


# def list_sum(lst):
#     result = 0
#     for element in lst:
#         result+= element
#     return result
#
# def sum(a,b):
#     return a+b
#
# y = sum(14, 29)
# z = list_sum([1,2,3])
#
# print(z)
# print(y)

# ----------------------------------------------------------------------------------------------------------------------

# a = []
#
# def foo(arg1, arg2):
#     a.append("foo")
#
# foo(a.append("arg1"), a.append("arg2"))
# print(a)
# ----------------------------------------------------------------------------------------------------------------------

# x = [1,2,3]
#
# x.append(4)
# x.append(5)
#
# print(x)
#
# top = x.pop()
# print(top)
# print(x)
#
# top = x.pop()
# print(top)
# print(x)
# ----------------------------------------------------------------------------------------------------------------------

# def closest_mod_5(x):
#     return (x + 4) //5 * 5
#
# print(closest_mod_5(1))
# ----------------------------------------------------------------------------------------------------------------------
# def printab(a,b):
#     print(a)
#     print(b)
#
# print(printab(10, 20))
# print(printab(a=11, b=22))
#
# lst = [15, 25]
# print(printab(*lst))
# args = {'a':30, 'b': 60}
# print(printab(**args))

# ----------------------------------------------------------------------------------------------------------------------

# def printab(a=10, b):
#     print(a)
#     print(b)
#
# print(printab(2))

# ----------------------------------------------------------------------------------------------------------------------
# def printab(a,b, *args):
#     print("positional argument a", a)
#     print("positional argument b", b)
#     print("additional arguments:")
#     for arg in args:
#         print(arg)
#
# print(printab(10, 20, 30, 40, 50, 60))

# ----------------------------------------------------------------------------------------------------------------------
# def printab(a,b, **kwargs):
#     print("positional argument a", a)
#     print("positional argument b", b)
#     print("additional arguments:")
#     for key in kwargs:
#         print(key, kwargs[key])
#
# print(printab(10, 20, c=30, d=40, jimmi=50, willi=60))
# ----------------------------------------------------------------------------------------------------------------------
# def fib(x):
#     if x == 0 or x == 1:
#         return 1
#     else:
#         return fib(x - 1) + fib(x - 2)
#
# y = fib(5)
#
# print(y)
# ----------------------------------------------------------------------------------------------------------------------


# def C(n, k):
#     if k == 0:
#         return 1
#     elif k > n:
#         return 0
#     return C(n - 1, k) + C(n - 1, k - 1)
#
#
# n, k = map(int, input().split())
# print(C(10, 5))

# http://www.pythontutor.com/visualize.html#mode=display











