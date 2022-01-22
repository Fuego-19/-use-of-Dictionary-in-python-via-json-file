# Name - Mohit
# Roll No - 2020085


'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- DO NOT modify/delete the given functions. 

- DO NOT import any python libraries. You may only import a2.py.

- Make sure to return value as specified in the function description.

- Remove the pass statement from the function when you implement it.

- Do not create any global variables in this module.
'''
import a2
records1=a2.read_data_from_file(file_path="data.json")

print('Hello!')
print('Following are the Queries available:')
print('\n'+'-'*40,'\n'+'CODE | DESCRIPTION ','\n'+'-'*40,)
print('  1  | Read data from file')
print('  2  | Filter by first name')
print('  3  | Filter by last name','\n ','4  | Filter by full name')
print('  5  | Filter by age range','\n ','6  | Count by gender')
print('  7  | Filter by address','\n ','8  | Find alumni')
print('  9  | Find topper of each institute','\n ','10 | Find blood donors')
print('  11 | Get common Friends','\n ','12 | Check if two persons are related')
print('  13 | Delete by Id','\n ','14 | Add friend ')
print('  15 | Remove friend','\n ','16 | Add education ')
print('-'*40)


while True:
    nin = input('\n Which Query would you like to perform?(enter -1 to stop): ')
    if nin=="":
        print("Incorrect code, please enter correct code and try again")

    elif int(nin)==-1:
        print('Thank you')
        break
    else:
        if int(nin)==1:
            print(a2.read_data_from_file(file_path="data.json"))
        elif int(nin)==2:
            nm1=input('Enter first name: ')
            print(a2.filter_by_first_name(records1,nm1))
        elif int(nin)==3:
            nm2 = input('Enter last name: ')
            print(a2.filter_by_last_name(records1, nm2))
        elif int(nin)==4:
            nm3=input('Enter Full name(space seperated): ')
            print(a2.filter_by_full_name(records1, nm3))
        elif int(nin)==5:
            nm4=int(input('Enter minimum age: '))
            nm5=int(input('Enter maximum age: '))
            print(a2.filter_by_age_range(records1,nm4,nm5))
        elif int(nin)==6:
            print(a2.count_by_gender(records1))
        elif int(nin)==7:
            dic1={}
            d1=input("Enter house no.(leave blank if don't know): ")
            if d1!="":
                dic1['house_no']=int(d1)
            d2=input("Enter Block (leave blank if don't know): ")
            if d2!="":
                dic1['block']=d2
            d3=input("Enter town(leave blank if don't know): ")
            if d3!="":
                dic1['town']=d3
            d4=input("Enter city(leave blank if don't know): ")
            if d4!="":
                dic1['city']=d4
            d5=input("Enter state(leave blank if don't know): ")
            if d5!="":
                dic1['state']=d5
            d6=input("Enter Pincode(leave blank if don't know): ")
            if d6!="":
                dic1['pincode']=int(d6)
            print(a2.filter_by_address(records1,dic1))
        elif int(nin)==8:
            nm6=input("Enter the institute name: ")
            print(a2.find_alumni(records1,nm6))
        elif int(nin)==9:
            print(a2.find_topper_of_each_institute(records1))
        elif int(nin)==10:
            num7=input("Enter reciever person Id:")
            print(a2.find_blood_donors(records1,int(num7)))
        elif int(nin)==11:
            num88=input('Enter Ids(space seperated), for which you want to find common friends: ')
            num88=num88.split()
            m1=[]
            for s in num88:
                m1.append(int(s))
            print(a2.get_common_friends(records1,m1))
        elif int(nin)==12:
            num99=int(input("Enter person Id 1: "))
            num00=int(input("Enter person Id 2: "))
            print(a2.is_related(records1,num99,num00))
        elif int(nin)==13:
            hi1=int(input("Enter person Id: "))
            xyz=a2.delete_by_id(records1,hi1)
            records1=xyz
            print(xyz)
        elif int(nin)==14:
            nm8=int(input("Enter person Id: "))
            nm9=int(input("Enter friend Id: "))
            print(a2.add_friend(records1,nm8,nm9))
            records1=a2.add_friend(records1,nm8,nm9)
        elif int(nin)==15:
            nm10=int(input("Enter person Id: "))
            nm11=int(input("Enter friend Id: "))
            print(a2.remove_friend(records1,nm10,nm11))
            records1=a2.remove_friend(records1,nm10,nm11)
        elif int(nin)==16:
            nm12=int(input("Enter person Id: "))
            nm13=input("Enter Institute name: ")
            nm14=input("Enter ongoing: ")
            if nm14=='False' or nm14=="false" or nm14=="FALSE":
                nm15=float(input("Enter percentage: "))
                print(a2.add_education(records1,nm12,nm13,False,nm15))
                records1=a2.add_education(records1,nm12,nm13,False,nm15)
            elif nm14=='True' or nm14=="TRUE" or nm14=="true":
                print(a2.add_education(records1,nm12,nm13,True,"0"))
                records1=a2.add_education(records1,nm12,nm13,True,"0")

        else:
            print("Incorrect code, please enter correct code and try again")



