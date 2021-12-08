students_height = input("Input a list of students height: ").split()
sum_height = 0
count = 0
for i in students_height:
    sum_height += int(i)
    count += 1
average = round(sum_height / count)
print(f"Average height of students is: {average}")