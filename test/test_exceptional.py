import colorama
from colorama import Fore
colorama.init(autoreset=True)
import unittest
import sys
sys.path.append("..")
from mainclass import MainClass
from boundary import OutOfBoundaryMarksError
class ExceptionalTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("output_exception_revised.txt","w") as f:
            pass
    def test_sufficient_details(self):
        try:
            MainClass.calculate_result("Venu,92,98")
            with open("output_exception_revised.txt","a") as f:
                f.write("TestSufficientDetails=False\n")
                print("{}TestSufficientDetails = {}Failed".format(Fore.YELLOW,Fore.RED))

        except IndexError:
            with open("output_exception_revised.txt","a") as f:
                f.write("TestSufficientDetails=True\n")
                print("{}TestSufficientDetails = {}Passed".format(Fore.YELLOW,Fore.GREEN))


    def test_data_format_at_name(self):
        try:
            MainClass.calculate_result("80,92xyz,98,90")
            with open("output_exception_revised.txt","a") as f:
                f.write("TestDataFormatAtName=False\n")
                print("{}TestDataFormatAtName = {}Failed".format(Fore.YELLOW,Fore.RED))
        except ValueError:
            with open("output_exception_revised.txt","a") as f:
                f.write("TestDataFormatAtName=True\n")
                print("{}TestDataFormatAtName = {}Passed".format(Fore.YELLOW,Fore.GREEN))

    def test_data_format_at_marks(self):
        try:
            MainClass.calculate_result("Venu,92xyz,98,90")
            with open("output_exception_revised.txt","a") as f:
                f.write("TestDataFormatAtMarks=False\n")
                print("{}TestDataFormatAtMarks = {}Failed".format(Fore.YELLOW,Fore.RED))
        except ValueError:
            with open("output_exception_revised.txt","a") as f:
                f.write("TestDataFormatAtMarks=True\n")
                print("{}TestDataFormatAtMarks = {}Passed".format(Fore.YELLOW,Fore.GREEN))


    def test_marks_boundary_exception(self):
        try:
            MainClass.calculate_result("Venu,192,98,90")
            with open("output_exception_revised.txt","a") as f:
                f.write("TestMarksBoundaryException=False\n")
                print("{}TestMarksBoundaryException = {}Failed".format(Fore.YELLOW,Fore.RED))
        except (ValueError,OutOfBoundaryMarksError):
            with open("output_exception_revised.txt","a") as f:
                f.write("TestMarksBoundaryException=True\n")
                print("{}TestMarksBoundaryException = {}Passed".format(Fore.YELLOW,Fore.GREEN))
    def test_negative_marks_exception(self):
        try:
            MainClass.calculate_result("Venu,-80,98,90")
            with open("output_exception_revised.txt","a") as f:
                f.write("TestNegativeMarksException=False\n")
                print("{}TestNegativeMarksException = {}Failed".format(Fore.YELLOW,Fore.RED))
        except (ValueError,OutOfBoundaryMarksError):
            with open("output_exception_revised.txt","a") as f:
                f.write("TestNegativeMarksException=True\n")
                print("{}TestNegativeMarksException = {}Passed".format(Fore.YELLOW,Fore.GREEN))
