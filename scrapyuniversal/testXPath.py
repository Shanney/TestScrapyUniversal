

class TestXPath():

    def __init__(self):
        pass

    def test(self):
        with open('/Users/xiangnan/test.html') as file_object:
            contents = file_object.read()
        print(contents)


if __name__ == '__main__':
    testObj = TestXPath()
    testObj.test()
