# class MyClass:
#     a = 10
#
#     def func(self):
#         print("Hello")
#
# print(MyClass.a)
# print(MyClass.func)
# print(type(MyClass.a))
# print(type(MyClass.func))
#-----------------------------------------------------------------------------------------------------------------------


# class MyClass:
#     a = 10
#
#     def func(self):
#         print("Hello")
#
# x = MyClass()
#
# print(type(x))
# print(type(MyClass))

#-----------------------------------------------------------------------------------------------------------------------

# class Counter:
#     pass

# x = Counter()
#
# x.count = 0
# x.count += 1
#
# # print(x.count)
# # print(type(x.count))
#
#
# print(Counter.count)
# print(Counter.x)
#-----------------------------------------------------------------------------------------------------------------------

# class Counter:
#     def __init__(self):
#         self.count = 0
#         self.mant = 1
#
#     a = 10
#
# x = Counter()
# print(x.count)
# print(x.mant)
# print(x.a)
# x.count +=1

#-----------------------------------------------------------------------------------------------------------------------

# class Counter:
#     def __init__(self):
#         self.count = 0
#
#     def inc(self):
#         self.count += 1
#
#     def reset(self):
#         self.count = 0
#
# x = Counter()
# x.inc()
# print(x.count)
# Counter.inc(x)
# print(x.count)
# x.reset()
# print(x.count)
#-----------------------------------------------------------------------------------------------------------------------

class Song:
    def __init__(self, artist, song):
        self.artist = artist
        self.song = song
        self.tags = []

    def add_tags(self, *args):
        self.tags.extend(args)

song1 = Song("Shakey", "Rolls")
song1.add_tags("Americana", "Country")


song2 = Song("Feofan", "Rolodno")
song2.add_tags("Russian", "Drum")

print(song2.tags)
print(song1.tags)


























