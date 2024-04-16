# Create a function that takes a number as an argument and returns a grade based on that number.


# Score	Grade
# Anything greater than 1 or less than 0.6	"F"
# 0.9 or greater	"A"
# 0.8 or greater	"B"
# 0.7 or greater	"C"
# 0.6 or greater	"D"

# grader(0)   should be "F"
# grader(1.1) should be "F"
# grader(0.9) should be "A"
# grader(0.8) should be "B"
# grader(0.7) should be "C"
# grader(0.6) should be "D"

def grader(calificacion):
    if calificacion > 1 or calificacion < 0.6:
        return "F"
    elif calificacion >= 0.9:
        return "A"
    elif calificacion >= 0.8:
        return "B"
    elif calificacion >= 0.7:
        return "C"
    elif calificacion >= 0.6:
        return "D"
    

print(grader(0))
print(grader(1.1))
print(grader(0.9))
print(grader(0.8))
print(grader(0.7))
print(grader(0.6))