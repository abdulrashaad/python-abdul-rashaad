fam = [{'name': 'Rashard', 'dob': 1999}, {'name': 'Yusiif', 'dob': 1995}, {'name': 'Kamal', 'dob': 1990}]



# Sort the fam list based on the 'dob' key using the re_dob function
fam.sort(key=lambda ele: ele['dob'],reverse=True)

# Print the sorted list
print(fam)
