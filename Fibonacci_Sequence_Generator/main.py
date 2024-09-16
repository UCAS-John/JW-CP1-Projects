#John Wangwang RAID: Fibonacci Sequence Generator

#Get user input for the length of Fibonacci Sequence
max = int(input("Enter the range of Fibonacci Sequence: "))

first_num = 0
second_num = 1

#print First two Fibonacci Sequence
print(f"{first_num}, {second_num}", end='')

#loop Fibonacci Sequence until reach the max length that user request
for i in range (0,max-2):

    #store the number of second_num in old_num beforce changing
    old_num = second_num

    #calculate the Fibonacci Sequence and set second_num to it
    second_num = first_num + second_num 

    #print Fibonacci Sequence
    print(f", {second_num}", end='')

    #set first_num to the value of old_num
    first_num = old_num