import colorama
from colorama import Fore
colorama.init(autoreset=True)
import unittest
import sys
sys.path.append("..")
from mainclass import MainClass
class FuctionalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("output_revised.txt","w") as f:
            pass
    def test_is_candidate_qualified(self):
        obj=MainClass.calculate_result("Venu,92,98,96")
        if type(obj)!=type(None):
            with open("output_revised.txt","a") as f:
                f.write("TestIsCandidateQualified=True\n")
                print("{}TestCaseTestIsCandidateQualified = {}Passed".format(Fore.YELLOW,Fore.GREEN))
        else:
            with open("output_revised.txt","a") as f:
                f.write("TestIsCandidateQualified=False\n")
                print("{}TestIsCandidateQualified = {}Failed".format(Fore.YELLOW,Fore.RED))

    def test_is_candidate_fail(self):
        obj=MainClass.calculate_result("Ravan,42,38,96")
        #print(type(obj),type(None))
        if type(obj)==type(None):
            with open("output_revised.txt","a") as f:
                f.write("TestIsCandidateFail=True\n")
                print("{}TestIsCandidateFail = {}Passed".format(Fore.YELLOW,Fore.GREEN))
        else:
            with open("output_revised.txt","a") as f:
                f.write("TestIsCandidateFail=False\n")
                print("{}TestIsCandidateFail = {}Failed".format(Fore.YELLOW,Fore.RED))
    def test_is_candidate_pass(self):
        obj=MainClass.calculate_result("Ravan,52,55,58")
        #print(type(obj),type(None))
        if type(obj)==type(None):
            with open("output_revised.txt","a") as f:
                f.write("TestIsCandidatePass=True\n")
                print("{}TestIsCandidatePass = {}Passed".format(Fore.YELLOW,Fore.GREEN))
        else:
            with open("output_revised.txt","a") as f:
                f.write("TestIsCandidatePass=False\n")
                print("{}TestIsCandidatePass = {}Failed".format(Fore.YELLOW,Fore.RED))
