from fontTools.ttLib import TTFont

class TestFonts():

    def __init__(self):
        pass

    def doTest(self):
        font = TTFont('tyc-num.woff')
        gly_list = font.getGlyphOrder()
        for gly in gly_list:
            print(gly)
        # font.saveXML(r'd:\tycFont.xml')


if __name__ == "__main__":
    test = TestFonts()
    test.doTest()