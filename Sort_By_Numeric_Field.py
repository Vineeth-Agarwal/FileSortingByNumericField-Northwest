##### Step0: Open input and output files and create empty lists.
input=open("InputFile.txt","r")
output=open("OutputFile.txt","w")
tupples_array = []
sorted_array = []

##### Step1: Read each line traditionally(as a String)
for line in input:
        
##### Step2: Break each field in the line separated by comma, into individual variables.
    data=line.strip().split(",")
    field_one,field_two,field_three=data
        
##### Step3: Create a tuple of all fields. While adding each field, convert string into numeric field 'int' or 'float' as necessary.
    tupple=(int(field_one),field_two,field_three)
        
##### Step4: Add or append the tuple to a list.
    tupples_array.append(tupple)
        
##### Step5: Repeat the process until all the lines are read and added to the list.

##### Step6: Write the new sorted function to sort by numeirc field, rather than traditional string sorting. 
sorted_array=(sorted(tupples_array, key=lambda array_elements: array_elements[0]))
    
##### Step7: Write the newly sorted list to output file in same format or any desired format.
output.write("\n".join('%s, %s, %s' % new_array_elements for new_array_elements in sorted_array))
    
##### Step8: Close the input and output files.
input.close()
output.close()
