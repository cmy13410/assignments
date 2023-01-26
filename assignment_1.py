def remove_val(i, val):  # This function removes multiple of the same value from age list
    count = 0
    while count < i:
        ages.remove(val)
        count += 1


def add_val(i, val):  # This function adds back multiple of the same value from age list
    count = 0
    while count < i:
        ages.append(val)
        count += 1


print("Question 1: ")
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print("Initial List", ages)

# Sort the code, then save values of min and max functions
ages.sort()
min_val = min(ages)
max_val = max(ages)
print("Sorted list:", ages)

# find if there are duplicate min and max functions
min_count = ages.count(min_val)
max_count = ages.count(max_val)

# remove all min and max values
remove_val(min_count, min_val)
remove_val(max_count, max_val)
print("With removed values:", ages)

# add min and max values back
add_val(min_count, min_val)
add_val(max_count, max_val)
print("Removed values added back:", ages)
ages.sort()  # Sorts list back to normal

# find median
length = len(ages)
tmp = int(length/2)
if length % 2 == 0:  # Sees if list length is even or odd to find median values
    median1 = ages[tmp]
    median2 = ages[tmp]
    print("Median values: {} and {}".format(median1, median2))
else:  # If list is odd
    median = ages[tmp]
    print("Median value:", median)

# Find average
print("Average:", sum(ages) / length)

# Find range
print("Range:", max_val - min_val)

# Question 2
print("\nQuestion 2: ")
dog = {}  # Creates empty dictionary
print("Initial dog:", dog)
dog = {'Name': 'Kopi', 'Color': 'Beige', 'Breed': 'Husky', 'Legs': 4}  # Assigns values to dictionary
print("Dog updated:", dog)
# Create student dictionary
student = {'first_name': 'Steven', 'last_name': 'Roy', 'gender': 'Male', 'age': 22, 'marital_status': 'Single',
           'skills': ['Has great communication'], 'country': 'USA', 'city': 'NY',
           'address': '4509 East Street'}
print("Student dictionary:", student)
print("Length of student dictionary:", len(student))  # Prints length of student dictionary
print("Skills:", student.get('skills'))  # Gets skills value
print("Data Type:", type(student['skills']))  # Shows type of skills

student.update({'skills': ['Has great communication', 'and great leadership skills']})  # Updates dict value
print("Updated Skills:", student.get('skills'))  # Gets skills value
# Prints out student's values and keys
print("Values:", student.values())
print("Keys:", student.keys())

# Question 3
print("\nQuestion 3: ")
# Create tuples
brothers = ('Jason', 'Jacob')
sisters = ('Lucy', 'Candace')
print("Brothers:", brothers)
print("Sisters:", sisters)

siblings = brothers + sisters  # Joins brothers & sisters tuples into siblings
print("Siblings:", siblings)

print("Amount of siblings:", len(siblings))  # Shows how many siblings
family_members = ('Richard', 'Mary') + siblings  # Joins tuples
print("Family", family_members)

# Question 4
print("\nQuestion 4: ")

# Declares Sets and List
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print("Length of it_companies:", len(it_companies))  # Shows it_companies current length
it_companies.add('Twitter')  # Adds 'Twitter' to it companies
print("Updated set: ", it_companies)  # Prints to show change
it_companies.update(['YouTube', 'Instagram', 'Tumblr'])  # Adds multiple companies
print("Updated set: ", it_companies)  # Prints to show change
it_companies.remove('Twitter')  # Removes a company
print("Removed a company:", it_companies)

# set operations on sets A and B
print("Joined sets:", A.union(B))  # joins A and B

print("Intersect A and B", A & B)  # intersects A and B

print("Join A to B:", A.union(B))  # joins A and B
print("Join B to A:", B.union(A))  # joins B and A

print("Symmetric Difference:", A ^ B)  # Finds symmetric difference

del A  # Deletes set A
del B  # Deletes set B

age_set = set(age)
print("Age set length:", len(age_set))  # Prints length of set
print("Age list length:", len(age))  # Prints length of list

# Question 5
print("\nQuestion 5: ")
radius = 30
pi = 3.14159265359
_area_of_circle_ = pi * radius ** 2  # Saves areas of the circle
print("Area of 30cm circle:", _area_of_circle_)
_circum_of_circle_ = 2 * pi * radius  # Saves circumference of the circle
print("Circumference of 30cm circle", _circum_of_circle_)

user_radius = input("Please enter radius: ")  # Gets user input
_area_of_circle_ = pi * float(user_radius) ** 2  # Calculates user input
print("Area of circle:", _area_of_circle_)


# Question 6
print("\nQuestion 6: ")
txt = 'I am a teacher and I love to inspire and teach people'
words = txt.split(' ')
unique_words = set()  # set that will hold unique words
for i in words:  # Iterates through words list
    if i not in unique_words:  # Sees if the word is in the set
        unique_words.add(i)  # Adds if word is not in the set already
print(unique_words)

# Question 7
print("\nQuestion 7:")
print("\tName\tAge\tCountry\tCity")
print("\tAsabeneh\t250\tFinland\tHelsinki")

# Question 8
print("\nQuestion 8: ")
radius = 10
area = 3.14 * radius ** 2

print("The area of a circle with radius {} is {} meters square".format(radius, int(area)))

# Question 9
print("\nQuestion 9:")
user_input = input("Please enter a list, separating values by commas: ")  # Get user input
l1 = user_input.split(", ")  # splits user input
output = []  # output will be stored in this list

for i in l1:  # loops to add to output list
    tmp = int(i) / 2.2046
    output.append("{:.2f}".format(tmp))
print(output)
