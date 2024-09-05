#John Wangwang Setting, Resetting, and Resetting

staff = 32
students = 100
allowed = 2
table_max = 12

students = students - 1
staff = staff - 3
guests = students * allowed
guests = guests - 15
school_board = 1
tables = (staff + guests + students + school_board) / table_max

print(int(tables))