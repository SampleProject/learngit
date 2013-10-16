class Person(object):
    def __init__(self, name, id, zipcode):
        self.name = name
        self.id = id
        self.zipcode = zipcode
    
if __name__ == '__main__':
    p = Person('John')
    print p.name
