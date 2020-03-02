import unittest
TestCase_path = "D:/PythonWorkSpace/UIAutomation/TestCase"

def AutoRun(TestCaseName):
    discover = unittest.defaultTestLoader.discover(TestCase_path,pattern=TestCaseName)

    runner = unittest.TextTestRunner()
    runner.run(discover)


if __name__ == "__main__":
    AutoRun("TC_cashier.py")