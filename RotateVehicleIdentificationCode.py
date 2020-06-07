# Infosys Programming Fundamental Practice Mock Question

'''
Scenario:

Consider a list (uniquecode_list) containing strings representing unique codes for vehicle identification.

    For Example:
    uniquecode_list: ['AZ01-1234','R137-8714','HR05-2941']

Write a function that takes the uniquecode_list as input and returns another list, say rotated_list containing encrypted strings of uniquecode_list. The logic for encryption is based on the two conditions as discussed below:

Unique codes in the uniquecode_list will be in 'XXXX-YYYY' format, where X is alphanumeric and Y is numeric. Alphabets in 'XXXX' will always appear at the beginning. There can be either only one or maximum two alphabets in 'XXXX'

Condition 1:	If 'XXXX' has two alphabets then rotate the numeric part 'YYYY' by bringing beginning digit to the end. Do this twice and append it to the alphabets in 'XXXX'.
Example:	
The first string of uniquecode_list mentioned above is 'AZ01-1234'. In this string 'AZ01' is 'XXXX' and '1234' is 'YYYY' part. The 'XXXX' part has 'AZ' two alphabets, so '1234' the numeric part (i.e. 'YYYY' part) needs to be rotated twice towards the right side. Consequently, you would get '3412'. It is appended with 'AZ' to form string 'AZ3412'. This is then added to the rotated_list. Similarly the third string in the uniquecode_list results in 'HR4129'.

Condition 2:	
If 'XXXX' has only one alphabet then rotate the numeric part 'YYYY' bringing beginning digit to the end. Do this only once and append it to the alphabets in 'XXXX'.
Example:	
The second string of uniquecode_list mentioned above is 'R137-8714'. In this string 'R137' is 'XXXX' and '8714' is 'YYYY' part. The 'XXXX' part has 'R' only one alphabet. So, '8714' the numeric part (i.e. 'YYYY" part) needs to be rotated once towards the right side. Consequently, you would get '7148'. It is appended with 'R' to form string 'R7148'. This is then added to the rotated_list.
Return the rotated_list.

For Example:
uniquecode_list: ['AZ01-1234','R137-8714','HR05-2941']
rotated_list: ['AZ3412', 'R7148', 'HR4129']
'''


def list_rotate(uniquecode_list):
    rotated_list = []

    for code in uniquecode_list:
        splitCode = code.split("-")

        xxxx = splitCode[0]
        yyyy = splitCode[1]

        alphaCount = 0
        for ch in xxxx:
            if ch.isalpha():
                alphaCount = alphaCount + 1
        if(alphaCount == 1):
            rotated_list.append(xxxx[0:1] + yyyy[1:4] + yyyy[0:1])
        else:
            rotated_list.append(xxxx[0:2] + yyyy[2:4] + yyyy[0:2])

    return rotated_list


#You may modify the below code for testing
uniquecode_list = ['AZ01-1234', 'R137-8714', 'HR05-2941']
rotated_list = list_rotate(uniquecode_list)
print(rotated_list)
