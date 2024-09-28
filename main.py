#list Comprehensions
numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

name = "Angela"
letters_list = [letter for letter in name]
print(letters_list)

range_list = [num * 2 for num in range(1, 5)]
print(range_list)

#Conditional List Comprehension
#Used for tests
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)#List Comprehensions
numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

name = "Angela"
letters_list = [letter for letter in name]
print(letters_list)

range_list = [num * 2 for num in range(1, 5)]
print(range_list)

#Conditional List Comprehension
#Used for tests
import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)

#No teachers do NOT assign random test scores to students
#This is a practice set
student_scores = {student:random.randint(50, 100) for student in names}
print(student_scores)

passed_student = {student:score for (student, score) in student_scores.items() if score >= 60}
print(passed_student)

#Iterating over a pandas dataframe
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries
for (key, value) in student_dict.items():
    print(value)

#But there's a better way!
import pandas
#Loop through a Data Frame
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
for (key, value) in student_data_frame.items():
    print(value)

#Loop through rows of a data frame
#So we can use data within that row, not column
for (index, row) in student_data_frame.iterrows():
    print(row.student)
    print(row.score)

#for the NATO project in the NATO folder:
#{new_key:new_value for (index, row) in df.itterrows()}
#TODO: Create a dictionary in this format
#TODO: Create a dictionary in this format of {"Letter": "Code"}