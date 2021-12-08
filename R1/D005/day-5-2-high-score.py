student_scores = input("Input a list of a student scores: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

high_score = student_scores[0]
for score in student_scores:
    if score > high_score:
        high_score = score
print(f"High score is: {high_score}")