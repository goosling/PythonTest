__author__ = 'joe'
# -*- coding: utf-8 -*-

import xlwt
import json

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

wb = xlwt.Workbook(encoding='utf-8')
sheet = wb.add_sheet('student', cell_overwrite_ok=True)
txt = open('test.txt').read()
json_txt = json.loads(txt)
for x in range(len(json_txt)):
    sheet.write(x, 0, x+1)
    for y in range(len(json_txt[str(x + 1)])):
        sheet.write(x, y+1, json_txt[str(x+1)][y])
wb.save('students.xls')