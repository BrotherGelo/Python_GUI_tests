from comtypes.client import CreateObject
import os

n = 4
file_name = "groups.xlsx"
#project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
file_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "data")

xl = CreateObject("Excel.Application")
xl.Visible = 1
wb = xl.Workbooks.Add()
for i in range(n):
    xl.Range["A%s" % (i+1)].Value[()] = "group %s" % i
wb.SaveAs(os.path.join(file_dir, file_name))
xl.Quit()