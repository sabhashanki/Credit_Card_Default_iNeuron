education_dict = {
       'uneducated' : 0,
       'middle_school' : 1,
       'high_school' : 2,
       'ug' : 3,
       'pg' : 4,
       'phd' : 5,
       'others' : 6,
    }

education = 'others'
for name, value in education_dict.items():
    if education == name:
        education = value
        break

print(education)