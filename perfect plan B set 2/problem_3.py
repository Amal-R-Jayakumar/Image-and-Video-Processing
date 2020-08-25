student={"name":"",
"assignments":[],
"test":[],
"labWorks":[],
"total":0}

list_Of_Students=[]
n=int(input("Number of Students: "))


for _ in range(n):
    student['name'] = input("name: ")
    student["assignments"]=list(map(int,input("Assignments: ").strip().split()))
    student["test"]=list(map(int,input("Tests: ").strip().split()))
    student["labWorks"]=list(map(int,input("Lab Works: ").strip().split()))
    list_Of_Students.append(student.copy())

for _ in list_Of_Students:
    _["total"]=(sum(_["assignments"])/len(_["assignments"]))*0.1+(sum(_["test"])/len(_["test"]))*0.7+(sum(_["labWorks"])/len(_["labWorks"]))*0.2
    print(f'{_["name"]} : {_["total"]}')
