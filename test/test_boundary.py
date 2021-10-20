import colorama
from colorama import Fore
colorama.init(autoreset=True)
import unittest
import sys
sys.path.append("..")
from mainclass import MainClass
from boundary import OutOfBoundaryMarksError
class BoundaryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("output_boundary_revised.txt","w") as f:
            pass
    def test_negative_marks(self):
        try:
            MainClass.calculate_result("Venu,-80,98,90")
            with open("output_boundary_revised.txt","a") as f:
                f.write("TestNegativeMarks=False\n")
                print("{}TestNegativeMarks = {}Failed".format(Fore.YELLOW,Fore.RED))
        except (ValueError,OutOfBoundaryMarksError):
            with open("output_boundary_revised.txt","a") as f:
                f.write("TestNegativeMarks=True\n")
                print("{}TestNegativeMarks = {}Passed".format(Fore.YELLOW,Fore.GREEN))


    def test_marks_boundary(self):
        try:
            MainClass.calculate_result("Venu,192,98,90")
            with open("output_boundary_revised.txt","a") as f:
                f.write("TestMarksBoundary=False\n")
                print("{}TestMarksBoundary = {}Failed".format(Fore.YELLOW,Fore.RED))
        except (ValueError,OutOfBoundaryMarksError):
            with open("output_boundary_revised.txt","a") as f:
                f.write("TestMarksBoundary=True\n")
                print("{}TestMarksBoundary = {}Passed".format(Fore.YELLOW,Fore.GREEN))
