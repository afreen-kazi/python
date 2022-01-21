# create a program for count number of objects getting created out of class
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    def get_counter(self):
        return Counter.count


obj1 = Counter()
print(obj1.get_counter())
obj2 = Counter()
print(obj2.get_counter())
obj3 = Counter()
print(obj3.get_counter())
obj4 = Counter()
print(obj4.get_counter())
obj5 = Counter()
print(obj5.get_counter())
obj6 = Counter()
print(obj6.get_counter())
obj7 = Counter()
print(obj7.get_counter())
obj8 = Counter()
print(obj8.get_counter())





