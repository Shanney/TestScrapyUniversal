from lxml import etree

class TestXPath():

    def __init__(self):
        pass

    def test(self):
        with open('/Users/xiangnan/test.html') as file_object:
            contents = file_object.read()
        # print(contents)

        parser = etree.HTMLParser(encoding="utf-8")
        html = etree.parse('/Users/xiangnan/test.html', parser=parser)
        # print(type(html))
        # a = etree.tostring(html, pretty_print=True)
        # print(a)
        result = html.xpath("//div[@id='_container_baseInfo']/table[2]/tbody/tr[10]/td[2]/text()")
        print(result)


if __name__ == '__main__':
    testObj = TestXPath()
    testObj.test()
