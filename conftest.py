import os
import pytest
from fixture.application import Application
from comtypes.client import CreateObject


@pytest.fixture(scope="session")
def app(request):
    fixture = Application("E:\\Projects\\FreeAddressBookPortable\\AddressBook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("xlsx_"):
            testdata = load_from_excel(fixture[5:])
            metafunc.parametrize(fixture, testdata)


def load_from_excel(file):
    excel_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), f"data/%s.xlsx" % file)
    xl = CreateObject("Excel.Application")
    wb = xl.Workbooks.Open(excel_file)
    sh = wb.Worksheets[1]
    group_data = []
    for cell in range(10):
        cell_value = sh.Cells.Item[cell+1, 1].Value[()]
        if cell_value is not None:
            group_data.append(cell_value)
    return group_data
