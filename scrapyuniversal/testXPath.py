from lxml import etree
import re

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
        if len(result)>=1:
            tmpStr = result[0]
        year = tmpStr[:4]
        y = self.trans(year)
        mon = tmpStr[5:7]
        m = self.trans(mon)
        day = tmpStr[8:10]
        d = self.trans(day)
        register_time = y + '-' + m + '-' + d
        print(tmpStr)
        print(year, mon, day)
        print(register_time)

    def trans(self, A):
        num = []
        for i in range(0, len(A)):
            if A[i] == "0":
                zero = re.compile("0")
                z = re.sub(zero, "5", A[i])
                num.append(z)

            elif A[i] == "1":
                one = re.compile("1")
                o = re.sub(one, "9", A[i])
                # print(o,i)
                num.append(o)

            elif A[i] == "2":
                two = re.compile("2")
                t = re.sub(two, "8", A[i])
                # print(t,i)
                num.append(t)

            elif A[i] == "3":
                three = re.compile("3")
                t2 = re.sub(three, "0", A[i])
                # print(t2,i)
                num.append(t2)

            elif A[i] == "4":
                four = re.compile("4")
                f = re.sub(four, "5", A[i])
                # print(f,i)
                num.append(f)

            elif A[i] == "5":
                five = re.compile("5")
                f2 = re.sub(five, "3", A[i])
                # print(f2,i)
                num.append(f2)

            elif A[i] == "6":
                six = re.compile("6")
                s = re.sub(six, "7", A[i])
                # print(s,i)
                num.append(s)

            elif A[i] == "7":
                seven = re.compile("7")
                s2 = re.sub(seven, "1", A[i])
                # print(s2,i)
                num.append(s2)

            elif A[i] == "8":
                eight = re.compile("8")
                e = re.sub(eight, "1", A[i])
                # print(e,i)
                num.append(e)

            elif A[i] == "9":
                nine = re.compile("9")
                n = re.sub(nine, "2", A[i])
                # print(n,i)
                num.append(n)
        # print(num)

        number = ''.join(num)
        return number

if __name__ == '__main__':
    testObj = TestXPath()
    testObj.test()
