from lxml import etree

class TestXPath():

    def __init__(self):
        pass

    def test(self):
        with open('test.html', encoding='UTF-8') as file_object:
            contents = file_object.read()
        # print(contents)

        parser = etree.HTMLParser(encoding="utf-8")
        html = etree.parse('test.html', parser=parser)
        # print(type(html))
        # a = etree.tostring(html, pretty_print=True)
        # print(a)
        # //div[@id='_container_baseInfo']/table[2]/tbody/tr[10]/td[2]/text()
        # https://www.cnblogs.com/MrFiona/p/5954084.html
        result = html.xpath("//div[ @ id = '_container_baseInfo'] / table[2] / tbody / tr[1] / td[4] / div/text/text()")
        print(result)


if __name__ == '__main__':
    testObj = TestXPath()
    testObj.test()
