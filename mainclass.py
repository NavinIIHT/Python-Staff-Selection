from usecase import Applicant
from boundary import OutOfBoundaryMarksError
class MainClass:
    @staticmethod
    def calculate_result(app_data):
        candidate=app_data.split(",")
        app_result=[]
        name=candidate[0]
        app_result.append(name)

        if not (name.isalpha() and candidate[1].isdigit() and candidate[2].isdigit() and candidate[3].isdigit()):
            raise ValueError # raises for -ve value also

        total=0
        count_sub=0
        for mark in candidate[1:]:
            app_result.append(int(mark))
            total+=int(mark)
            count_sub+=1

        if count_sub!=3:
            raise IndexError

        s1=int(candidate[1])
        s2=int(candidate[2])
        s3=int(candidate[3])

        if s1>100 or s1<0 or s2>100 or s2<0  or s3>100 or s3<0:
            raise OutOfBoundaryMarksError("Marks should be in the range of 0 - 100")

        elif s1>=50 and s2>=50 and s3>=50:
            percentage=(total/300)*100
            if percentage>=70:
                app_result.append(total)
                app_result.append(percentage)
                return Applicant(app_result)
        else:
            pass

    @staticmethod
    def sort_result(all_app_result):
        sorted_result=sorted(all_app_result,key=lambda x:x.percentage,reverse=True)#sort in descending order based on percentage
        return sorted_result

if __name__=="__main__":
    all_app_result=[]
    n=int(input("Enter number of applicants"))
    for i in range(n):
        app_data=input("Enter name of the applicant,subject1 mark,subject2 mark& subject3 mark")
        app_result=MainClass.calculate_result(app_data)
        if app_result!=None:
            all_app_result.append(app_result)
    sorted_result=MainClass.sort_result(all_app_result)
    print("Name |Subject1 Marks| Subject2 Marks| Subject3 Marks |Total Marks |Percentage")
    for data in sorted_result:
        print(data.name,data.subject1,data.subject2,data.subject3,data.total,data.percentage)
    # print("* "*30)
    # for data in sorted_data:
    #     print("Name: {} Subject1 Marks: {} Subject2 Marks: {} Subject3 Marks: {} Total : {} Percentage {}".format(data.name,data.subject1,data.subject2,data.subject3,data.total,data.percentage))
