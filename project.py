tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I' II do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)


# using of input
print("How are you:?", end=' ')
age = input()
print("How tall are you:?", end=' ')
height = input()
print("How much do you weight:?", end=' ')
weight = input()

print(f"So, you 're {age} old, {height} tall, and {weight} heavy ")


age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")

print(f"So, you're {age} old, {height} tall, {weight} heavy")


print("Mary had a little lamb")
print("its fleece was white as{}.". format( ' snow'))
print("And everywhere that Mary went.")
print("." * 10) # what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = ' ' at the end. try removing it to see what happends
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)


formatter = "{}  {}  {}  {}"

print(formatter .format(1, 2, 3, 4))
print(formatter .format("one", "two", "three", "four"))
print(formatter .format(True, False, False, True))
print(formatter .format(formatter, formatter, formatter, formatter))
print(formatter.format ( 
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
 ))


# There's Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days: ", days)
print("Here are the months: ", months)

print("""
There's something going on here.
With the three double-quates.
we'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""
)