__author__ = 'joe'
# -*- coding: utf-8 -*-
import simplejson as json
import xlwt

# 从文件中读取数据返回列表
def read_file(filename):
    with open(filename, 'r') as fp:
        content = fp.read()
        # content = str(content)
    l = json.JSONDecoder.decode(content)
    return l

# 生成对应的xls文件
def gen_xls(l, filename):
    fp = xlwt.Workbook()
    table = fp.add_sheet('number', cell_overwrite_ok=True)
    # 列表的遍历，用index
    for row in l:
        for col in row:
            table.write(l.index(row), row.index(col), col)
    fp.save(filename)
    print '写入完毕'

def main():
    filename = 'numbers.txt'
    xls_name = 'numbers.xls'
    l = read_file(filename)
    gen_xls(l, xls_name)

if __name__ == '__main__':
    main()