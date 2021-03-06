# 1. Update values in dictionaries and lists

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#Change the value 10 in x to 15
def changeXValue(x):
    x[1][0] = 15
    return x

print(changeXValue(x))

#Change the last_name of the first student from 'Jordan' to 'Bryant'
def changeLastName(students):
    students[0]['last_name'] = 'Bryant'
    return students

print(changeLastName(students))

#In the sports_directory, change 'Messi' to 'Andres'
def changeName (sports_directory):
    sports_directory['soccer'][0] = "Andres"
    return sports_directory

print(changeName(sports_directory))

#Change the value 20 in z to 30
def changeValue(z):
    z[0]['y'] = 30
    return z
print(changeValue(z))





# 2. Iterate Through a List of Dictionaries

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(list):
    for i in range(0, len(list)):
        output=""
        for key,val in list[i].items():
            output+=f"{key}-{val},"
        print(output)

iterateDictionary(students)





# 3. Get Values From a List of Dictionaries

def iterateDictionary2(key_name,some_list):
    for i in range(0,len(some_list)):
        for key,val in some_list[i].items():
            if key == key_name:
                print(val)

iterateDictionary2('first_name',students)
iterateDictionary2('last_name', students)





# 4. Iterate through a dictionary with list values

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(dictionary):
    for key,value in dictionary.items():
        print(f"{len(value)}{key.upper()}")
        for i in range(0, len(value)):
            print(value[i])


printInfo(dojo)

