# GROSS DURATION

gross_average = 5
gross_this_course = 3.5

# DURATION AVERAGE

min_course = 2.5
max_course = 7
average_course = 4
this_course = 1.5

# DURATION DIFFERENCES

print(
    "....................................................................................."
)
print("This course lasts:")
print(f" - {100 - this_course * 100 / min_course}% less than the minimum course")
print(f" - {100 - this_course * 1000 // max_course / 10}% less than the maximum course")
print(f" - {100 - this_course * 100 / average_course}% less than the average course")
print(
    "....................................................................................."
)


# GROSS DIFFERENCE

print(
    f"An average course eliminates {100 - average_course * 1000 // gross_average / 10}% of its gross duration"
)
print(
    f"This course eliminates {100 - this_course * 1000 // gross_this_course / 10}% of its gross duration"
)
print(
    "....................................................................................."
)


# DIFFERENCE IF THIS COURSE LASTS 10 HOURS

print(
    f"Ten hours of this course is equivalent to watching {average_course * 100 // this_course / 10} hours of other courses"
)

# DIFFERENCE IF OTHER COURSES LAST 10 HOURS

print(
    f"Ten hours of other courses are equivalent to watching {this_course * 100 // average_course / 10} hours of this course"
)
print(
    "....................................................................................."
)
