# Python-Selenium-Basic


Installing Python and Selenium

Installing Python:

Windows : http://python.org/download/.

• Make sure you note Python Installation path in your machine.
It would be like below
logged in
• Set Python home in System Variables
• Check if Python is Successfully Installed
python --version

==========================================================================================================
Python Basic 
Class name
The class name should start with “Test”

File name
File name in the suite should start or end with “test”. So the wildcard for this name is “test_*.py” or “*_test.py”

Method or function name
Every function and method that is supposed to test something should have a name that starts with “test”

Example of the suite is:

test_for_login/
	test_signup.py
	login_test.py

test_for_checkout/
	test_cart.py
	test_form.py
	
===============================================================================================================================	
What is PIP?
pip is the standard package manager for Python. It allows you to install and
manage additional packages that are not part of the Python standard library.
Java -
Selenium installing instructions official link
https://pypi.org/project/selenium/
• pip install selenium

• How to Verify if Package is installed
pip show <packageName»

4.pip install -U selenium
The optional –U flag will upgrade the existing version of the installed package

=====================================================================================================
run the test case from the cmd
pytest -vs testCases\test_login.py -p no:logging

pytest -vs --alluredir=allure-report/  testCases\*.py -p no:logging 
for the run the test case with the log
pytest -p no:logging


run the test cases in the parellal
install the pakage name ----pytest-xdist:run test cases in the parell mode.

pytest -vs -n=2 testCases\test_login.py -p no:logging
here n=2 for the number of the test cases for the run

To run specific test case use -k flag
e.g py.test -k testCaseName 

To run specifig mark test cases use -m as mark and -s for logs
@pytest.mark.smoke
py.test -m smoke 

To Skip test case 
@pytest.mark.skip

To generate HTML report in CMD 
py.test test.py --html=report.html


# Any pytest file should start with test_ or end with _test
#pytest method names should start with test
#Any code should be wrapped in method only
#Method name should have sense
# -k stands for method names execution, -s logs in out put  -v stands for more info metadata
#you can run specific file with py.test <filename>
# you can mark (tag) tests @pytest.mark.smoke and then run with -m
#you can skip tests with @pytest.mark.skip
#@pytest.mark.xfail
#fixtures are used as setup and tear down methods for test cases- conftest file to generalize fixt
#fixture and make it available to all test cases (fixture name into parameters of method)
# datadriven and parameterization can be done with return statements in tuple format
#when you define fixture scope to class only, it will run once before class is initiated and at the end



@staticmethod is used to call method from  anytwhere using classname
class testExcel
  @staticmethod
    def getTestData(test_case_name):
        Dict = {}
        book = openpyxl.load_workbook("D:\\PythonSelFramework\\PythonExcel.xlsx")
        sheet = book.active
        for i in range(1, sheet.max_row + 1):  # to get rows
            if sheet.cell(row=i, column=1).value == "testcase1":
                for j in range(1, sheet.max_column + 1):
                    # print(sheet.cell(row=i, column=j).value)
                    # store excel data into dict variable in json format
                    Dict[sheet.cell(row=1, column=j).value] = sheet.cell(row=i, column=j).value
        return[Dict]
	
to call it in method :
   testExcel.getTestData("testcase1")	

====================================================================================================
            genration of the python report 
step 1- pip install allure-pytest
step 2=allure generate
step 3=pytest --alluredir=allure-report/     ---------------->this genrated the one folder as allure report in working dir.
step 4=allure serve allure-report/               ----------------->this is publish the report to local server.

























