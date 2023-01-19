import random
import sys

try:
    filename = sys.argv[1]
    #Open the input file
    f = open(filename, "r")
    
    #Open the output file
    f1 = open("nextfile.txt", "w")

    #creating an empty list
    list1 =[]

    for name in f:
        # Get first name, last name and initials
        parts = name.split(',')

        #Get the last name
        forenames_upper = parts[1]
        fornames_lower = forenames_upper.lower()
        list1.append(fornames_lower)
        
        for lastname in list1:
            new = lastname.strip().split(" ")
            #creating an empty string
            lname = ""
            for i in new:
                lname += i[0]+"."

        # Gets the id and first name
        surname_id = parts[0]
        b = surname_id.split(" ")
        #Gets id
        id = b[0]
        #Gets first name
        surname = b[1]
        surname = ''.join([x for x in surname if x.isalpha()]).lower()
        f1.write(f"{id} {lname}{surname}{random.randint(1111,9999)}@poppleton.ac.uk\n")

except IndexError:
    print("Error: Missing command-line argument.")

except:
    print(f'Error: Cannot open "{filename}". Sorry about that.')

