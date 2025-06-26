fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

students_scores = [150, 180, 200, 170, 160]
max_score = students_scores[0]
max_score2 = max(students_scores)
sum_socores = 0
for score in students_scores:
    sum_socores += score
    if score > max_score:
        max_score = score

print (f"The highest score is: {max_score}, the second highest score is: {max_score2}, and the sum of all scores is: {sum_socores}")