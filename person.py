class Person(object):
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
if __name__ == '__main__':
    p = Person('John')
    print p.name
