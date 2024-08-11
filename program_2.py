# Creating the employee dictionary
emp = {
    'id': 1,
    'name': 'John Doe',
    'designation': 'Software Engineer',
    'salary': 50000
}

print("Original dictionary:")
print(emp)

# Deleting the 'designation' key
if 'designation' in emp:
    del emp['designation']

print("\nDictionary after deleting 'designation':")
print(emp)

# Updating the 'name' key
emp['name'] = 'Jane Doe'

print("\nDictionary after updating 'name':")
print(emp)
