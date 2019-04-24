def china(start, end):
    for page in range(start, end + 1):
        yield 'http://tech.china.com/articles/index_' + str(page) + '.html'

def tianyancha(start, end):
    for page in range(start, end + 1):
        yield 'https://www.tianyancha.com/search/p' + str(page) + '?companyType=normal_company&base=jl'
