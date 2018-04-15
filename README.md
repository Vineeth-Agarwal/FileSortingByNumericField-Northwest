# FileSortingByNumericField-Northwest  
## Background:  
### Project:
This is a part of project requirement on YouTube Video Sentiment Analysis for Big Data Course at Northwest.
### Problem Description:
In python or any language, when we read all the lines in a file, and sort them using .sort(), it always sorts is alaphabetically. Even if there is a numeric field present in the beginning of each line, it considers it as a string and sorts it as a string.
#### Consider For example: 
##### Data in Input_File.tx
531,This is a string,There are three fields separated by a comma in this file  
322,This is the string 2,Again three fields  
1224,This is a thrid string,Again three fields  
233,This is a fourth string,Again three fields  

##### After reading it and applying standard list.sort(), results we expect are:
233,This is a fourth string,Again three fields  
322,This is the string 2,Again three fields  
531,This is a string,There are three fields separated by a comma in this file  
1224,This is a thrid string,Again three fields  

##### But the actual output we get is:
1224,This is a thrid string,Again three fields  
233,This is a fourth string,Again three fields  
322,This is the string 2,Again three fields  
531,This is a string,There are three fields separated by a comma in this file  

The reason for the line starting with 1224, resulting in the beginning of file, despite having the largest number is, while reading the lines in a list, they will be read as a String. Hence, 1224 is converted to "1224"(string) and compared with other lines. Since 1<2, 1<3, 1<5, the line starting with 1224 comes in beginning.

### Proposed Solution: Working and tested Python code is as below:

##### Step0: Open input and output files and create empty lists.
###### Sort_By_Numeric_Field.py
    input=open("inputFile.txt","r")
    output=open("outputFile.txt","w")
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
    
    
### And That's all required to smile :) . Please feel free to contact, vineeth.agarwal06@gmail.com for any queries.



