class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)

p1 = Person("pepa", 36)
p1.myfunc()

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)
