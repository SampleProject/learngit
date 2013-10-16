class Person(object):
    def __init__(self, name):
        self.name = name
    
if __name__ == '__main__':
    p = Person('John')
    print p.name
