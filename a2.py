# Assignment - 2
# Name - Mohit
# Roll No - 2020085

import json




def read_data_from_file(file_path="data.json"):
	'''
	**** DO NOT modify this function ****
	Description: Reads the data.json file, and converts it into a dictionary.

	Parameters: 
	- file_path (STRING): The path to the file (with .json extension) which contains the initial database. You can pass the file_path parameter as "data.json".

	Returns:
	- A dictionary containing the data read from the file
	'''
	
	with open(file_path, 'r') as data:
		records = json.load(data)

	return records


def filter_by_first_name(records, first_name):
	'''
	Description: Searches the records to find all persons with the given first name (case-insensitive)

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- first_name (STRING): The first name

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given first name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''
	a1=records
	b1=[]
	for i in range(len(a1)):
		if a1[i]["first_name"].lower() == first_name.lower():
			b1.append(a1[i]['id'])
	return b1
def filter_by_last_name(records, last_name):
	'''
	Description: Searches the records to find all persons with the given last name (case-insensitive)

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- last_name (STRING): The last name

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given last name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''
	a2=records
	b2=[]
	for i in range(len(a2)):
		if a2[i]["last_name"].lower() == last_name.lower():
			b2.append(a2[i]['id'])
	return b2



def filter_by_full_name(records, full_name):
	'''
	Description: Searches the records to find all persons with the given full name (case-insensitive)

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- full_name (STRING): The full name (a single string with 2 space-separated words, the first name and the last name respectively)

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given full name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''
	a3=records
	b3=[]
	f1=full_name.split()
	for i in range(len(a3)):
		if a3[i]["first_name"].lower() == f1[0].lower() and a3[i]["last_name"].lower() == f1[1].lower():
			b3.append(a3[i]['id'])
	return b3





def filter_by_age_range(records, min_age, max_age):
	'''
	Description: Searches the records to find all persons whose age lies in the given age range [min_age, max_age]

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- min_age (INTEGER): The minimum age (inclusive)
	- max_age (INTEGER): The maximum age (inclusive)

	Note: 0 < min_age <= max_age

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given full name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''
	a4 = records
	b4=[]
	for i in range(len(a4)):
		if a4[i]['age']>=min_age and a4[i]['age']<=max_age:
			b4.append(a4[i]['id'])
	return b4



def count_by_gender(records):
	'''
	Description: Counts the number of males and females

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)

	Returns:
	- A dictionary with the following two key-value pairs:
		KEY        VALUE
		"male"     No of males (INTEGER)
		"female"   No of females (INTEGER)
	'''
	a5 = records
	b5={'male':0,'female':0}
	for i in range(len(a5)):
		if a5[i]['gender']=='male':
			b5['male']+=1
		else:
			b5['female']+=1
	return b5


def filter_by_address(records, address):
	'''
	Description: Filters the person records whose address matches the given address.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- address (DICTIONARY): The keys are a subset of { "house_no", "block", "town", "city", "state", "pincode" } (case-insensitive)
		Some examples are:
			Case 1: {}
				=> All records match this case

			Case 2: { "block": "AD", "city": "Delhi" }
				=> All records where the block is "AD" and the city is "Delhi" (the remaining address fields can be anything)

			Case 3: { "house_no": 24, "block": "ABC", "town": "Vaishali", "city": "Ghaziabad", "state": "Uttar Pradesh", "pincode": 110020 }

	Returns:
	- A LIST of DICTIONARIES with the following two key-value pairs:
		KEY            VALUE
		"first_name"   first name (STRING)
		"last_name"    last name (STRING)
	'''



	a6 = records
	ls1 = ["house_no", "block", "town", "city", "state", "pincode"]
	b6 = []
	for i in ls1:
		if i not in address:
			address[i] = '*'
	for j in range(len(a6)):
		if a6[j]['address']['house_no'] == address['house_no'] or address['house_no'] == '*':
			if a6[j]['address']['block'].lower() == address['block'].lower() or address['block'] == '*':
				if a6[j]['address']['town'].lower() == address['town'].lower() or address['town'] == '*':
					if a6[j]['address']['city'].lower() == address['city'].lower() or address['city'] == '*':
						if a6[j]['address']['state'].lower() == address['state'].lower() or address['state'] == '*':
							if a6[j]['address']['pincode'] == address['pincode'] or address['pincode'] == '*':
								s1 = {}
								s1['first_name'] = a6[j]['first_name']
								s1['last_name'] = a6[j]['last_name']
								b6.append(s1)
	return b6


def find_alumni(records, institute_name):
	'''
	Description: Find all the alumni of the given institute name (case-insensitive). 
	
	Note: A person is an alumnus of an institute only if the value of the "ongoing" field for that particular institute is False.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- institute_name (STRING): Name of the institute (case-insensitive)

	Returns:
	- A LIST of DICTIONARIES with the following three key-value pairs:
		KEY            VALUE
		"first_name"   first name (STRING)
		"last_name"    last name (STRING)
		"percentage"   percentage (FLOAT)
	'''
	a7=records
	b7=[]

	for i in range(len(a7)):
		for j in range(len(a7[i]['education'])):
			if len(a7[i]['education'])!=0:
				if a7[i]['education'][j]['institute']==institute_name.upper() and a7[i]['education'][j]['ongoing']==False:  #since in the directory institute name is in uppercase
					s1={}
					s1['first_name'] = a7[i]['first_name']
					s1['last_name'] = a7[i]['last_name']
					s1['percentage'] = a7[i]['education'][j]['percentage']
					b7.append(s1)
	return b7




def find_topper_of_each_institute(records):
	'''
	Description: Find topper of each institute

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)

	Returns:
	- A DICTIONARY with the institute name (STRING) as the keys and the ID (INTEGER) of the topper of that institute.

	Note: If there are `N` distinct institutes in records, the dictionary will contain `N` key-value pairs. The ongoing status does NOT matter. It is guaranteed that each institute will have exactly one topper.
	'''
	d1 = {}
	d2 = {}
	a8 = records
	for i in range(len(a8)):
		for j in range(len(a8[i]['education'])):
			if a8[i]['education'][j]['institute'] not in d1:
				if a8[i]['education'][j]['ongoing'] == False:
					d1[a8[i]['education'][j]['institute']] = a8[i]['education'][j]['percentage']
					d2[a8[i]['education'][j]['institute']] = a8[i]['id']

			else:
				if 'percentage' in a8[i]['education'][j].keys():
					if a8[i]['education'][j]['percentage'] > d1[a8[i]['education'][j]['institute']]:
						d1[a8[i]['education'][j]['institute']] = a8[i]['education'][j]['percentage']
						d2[a8[i]['education'][j]['institute']] = a8[i]['id']
	return d2


def find_blood_donors(records, receiver_person_id):
	'''
	Description: Find all donors who can donate blood to the person with the given receiver ID.

		Note: 
		- Possible blood groups are "A", "B", "AB" and "O".

		Rules:
		BLOOD GROUP      CAN DONATE TO
		A                A, AB
		B                B, AB
		AB               AB
		O                A, B, AB, O

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- receiver_person_id (INTEGER): The ID of the donee
		Note: It is guaranteed that exactly one person in records will have the ID as receiver_person_id

	Returns:
	- A DICTIONARY with keys as the IDs of potential donors and values as a list of strings, denoting the contact numbers of the donor
	'''
	a9=records
	b9={}
	for i in range(len(a9)):
		if a9[receiver_person_id]['blood_group']=="AB":
			b9[i]=a9[i]['contacts']
		elif a9[receiver_person_id]['blood_group']=="A" :
			if a9[i]['blood_group']=='A' or a9[i]['blood_group']=="O":
				b9[i]=a9[i]['contacts']
		elif a9[receiver_person_id]['blood_group']=="B":
			if a9[i]['blood_group']=='B' or a9[i]['blood_group']=="O":
				b9[i]=a9[i]['contacts']
		else:
			if a9[i]['blood_group']=="O":
				b9[i]=a9[i]['contacts']
	b9.pop(receiver_person_id)
	return b9




def get_common_friends(records, list_of_ids):
	'''
	Description: Find the common friends of all the people with the given IDs

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- list_of_ids (LIST): A list of IDs (INTEGER) of all the people whose common friends are to be found

	Returns:
	- A LIST of INTEGERS containing the IDs of all the common friends of the specified list of people
	'''
	a10=records
	b10=[]
	x = 0
	q1=[]
	for i in range(len(a10)):
		for j in list_of_ids:
			if j==a10[i]['id']:
				q1.append(a10[i]['friend_ids'])

	for k in q1[0]:
		x = 0
		for j in q1:
			if k in j:
				x += 1
		if x == len(q1):
			b10.append(k)

	return b10



def is_related(records, person_id_1, person_id_2):
	'''
	**** BONUS QUESTION ****
	Description: Check if 2 persons are friends

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id_1 (INTEGER): first person ID
	- person_id_2 (INTEGER): second person ID

	Returns:
	- A BOOLEAN denoting if the persons are friends of each other, directly or indirectly (if A knows B, B knows C and C knows D, then A knows B, C and D).
	'''
	a11 = records
	x1=False
	x2=False
	for l in a11:
		if l['id']==person_id_2:
			x1=True
		if l['id']==person_id_1:
			x2=True
	if x1==False or x2==False:
		print('Enter a correct person id')
		return 0
	else:
		l1 = []

		for i in range(len(a11)):
			if person_id_1 == a11[i]['id']:
				l1 = a11[i]['friend_ids']

		for m in range(len(a11)):
			for n in l1:
				if n == a11[m]['id']:
					l1.extend(a11[m]['friend_ids'])
		if person_id_2 in l1:
			flag = True
		else:
			flag = False

		return flag

def delete_by_id(records, person_id):
	'''
	Description: Given a person ID, this function deletes them from the records. Note that the given person can also be a friend of any other person(s), so also delete the given person ID from other persons friend list. If the person ID is not available in the records, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	
	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	'''
	a12=records.copy()

	for k in range(len(records)):
		if records[k]['id']==person_id:
			a12.pop(k)
	records=a12
	for j in range(len(records)):
		if person_id in a12[j]['friend_ids']:
			a12[j]['friend_ids'].remove(person_id)
	return a12

def add_friend(records, person_id, friend_id):
	'''
	Description: Given a person ID and a friend ID, this function makes them friends of each other. If any of the IDs are not available, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	- friend_id (INTEGER): The friend id
	
	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	'''
	a13=records
	for i in range(len(a13)):
		if person_id==a13[i]['id']:
			if friend_id not in a13[i]['friend_ids']:
				a13[i]['friend_ids'].append(friend_id)
		if friend_id==a13[i]['id']:
			if person_id not in a13[i]['friend_ids']:
				a13[i]['friend_ids'].append(person_id)

	return records

def remove_friend(records, person_id, friend_id):
	'''
	Description: Given a person ID and a friend ID, this function removes them as friends of each other. If any of the IDs are not available, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	- friend_id (INTEGER): The friend id
	
	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	'''
	a14=records
	for i in range(len(a14)):
		if person_id==a14[i]['id']:
			if friend_id in a14[i]['friend_ids']:
				a14[i]['friend_ids'].remove(friend_id)
		if friend_id==a14[i]['id']:
			if person_id in a14[i]['friend_ids']:
				a14[i]['friend_ids'].remove(person_id)

	return records


def add_education(records, person_id, institute_name, ongoing, percentage):
	'''
	Description: Adds an education record for the person with the given person ID. The education record constitutes of insitute name, the person's percentage and if that education is currently ongoing or not. Please look at the format of an education field from the PDF. If the person ID is not available in the records, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	- institute_name (STRING): The institute name (case-insensitive)
	- ongoing (BOOLEAN): The ongoing value representing if the education is currently ongoing or not
	- percentage (FLOAT): The person's score in percentage

	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	'''
	a15=records

	for i in range(len(a15)):
		if a15[i]['id']==person_id:
			if ongoing==False:
				x2={"institute":institute_name,"ongoing":ongoing,'percentage':percentage}
				a15[i]['education'].append(x2)
			elif ongoing==True:
				x2={"institute":institute_name,"ongoing":ongoing}
				a15[i]['education'].append(x2)

	return a15


