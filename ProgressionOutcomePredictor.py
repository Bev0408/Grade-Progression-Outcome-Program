from graphics import GraphWin, Rectangle, Point, Text

def show_progression(pass_credits, defer_credits, fail_credits):
    conditions = [
        (120, 0, 0, "progress"),
        (100, 20, 0, "progress(module trailer)"),
        (100, 0, 20, "progress(module trailer)"),
        (80, 40, 0, "do not progress - module retriever"),
        (80, 20, 20, "do not progress - module retriever"),
        (80, 0, 40, "do not progress - module retriever"),
        (60, 60, 0, "do not progress - module retriever"),
        (60, 40, 20, "do not progress - module retriever"),
        (60, 20, 40, "do not progress - module retriever"),
        (60, 0, 60, "do not progress - module retriever"),
        (40, 80, 0, "do not progress - module retriever"),
        (40, 60, 20, "do not progress - module retriever"),
        (40, 40, 40, "do not progress - module retriever"),
        (40, 20, 60, "do not progress - module retriever"),
        (40, 0, 80, "exclude"),
        (20, 100, 0, "do not progress - module retriever"),
        (20, 80, 20, "do not progress - module retriever"),
        (20, 60, 40, "do not progress - module retriever"),
        (20, 40, 60, "do not progress - module retriever"),
        (20, 20, 80, "exclude"),
        (20, 0, 100, "exclude"),
        (0, 120, 0, "do not progress - module retriever"),
        (0, 100, 20, "do not progress - module retriever"),
        (0, 80, 40, "do not progress - module retrievre"),
        (0, 60, 60, "do not progress - module retriever"),
        (0, 40, 80, "exclude"),
        (0, 20, 100, "exclude"),
        (0, 0, 120, "exclude"),
     ]
    for condition in conditions:
         if (pass_credits, defer_credits, fail_credits) == condition[:3]:
             return condition[3]
    return "outcome not defined"

# get valid input
def get_input(message, valid_range):
    while True:
        try:
            value = int(input(message))
            if value in valid_range: 
                return value
            else:
                print("Out of range. Try again.")
        except ValueError:
            print("Integer required. Try again.")


# these are the valid credit ranges
valid_credit_range = [0, 20, 40, 60, 80, 100, 120]

#dictionary that will store the number of outcome counts
outcome_counts = {
    "progress": 0,
    "progress(module trailer)": 0,
    "do not progress - module retriever": 0,
    "exclude": 0,
}

#stores all progression data inputs in list
student_data = [] 

# get users input of results
while True:
    pass_credits = get_input("Enter credit for Pass: ", valid_credit_range)
    defer_credits = get_input("Enter credit for Defer: ", valid_credit_range)
    fail_credits = get_input("Enter credit for Fail: ", valid_credit_range)

    #check if values add up to 120
    total_credits = pass_credits + defer_credits + fail_credits

    if total_credits !=120:
        print("the total is incorrect")
    else:
        # determine and print the progression outcome
        outcome = show_progression(pass_credits, defer_credits, fail_credits)
        print("Progression Outcome: ", outcome)

        # Increment the count for the obtained outcome
        outcome_counts[outcome] += 1

        # adds the input progression data in the list
        student_data.append((outcome, pass_credits, defer_credits, fail_credits))


    #ask user if they want to predict and another students outcome
    predict_additional_outcome = input("do you want to predict another students outcome? \n(yes/no): ").lower()
    if predict_additional_outcome != "yes":
        print("Have a nice day!")
        break #this will end the loop

# Creates a histogram

win = GraphWin("Overall Results", 700, 500)
win.setBackground("MintCream")

bar_width = 55
bar_padding = 105
x_position = 50

total_students = sum(outcome_counts.values())

title = Text(Point(win.getWidth() // 2, 30), "Overall Results")
title.setSize(35)
title.draw(win)

color_mapping = {"progress": "green", "Trailer": "yellow", 
                 "Retriever": "orange", "exclude": "red"}

for outcome, count in outcome_counts.items():
    bar_height = count * 8
    bar_color = color_mapping.get(outcome, "gray")
    bar = Rectangle(Point(x_position, 300), Point(x_position + bar_width, 300 - bar_height))
    bar.setFill(bar_color)
    bar.draw(win)

    label = Text(Point(x_position + bar_width // 2, 310), f"{outcome}\n({count} students)")
    label.setSize(8)
    label.draw(win)

    x_position += bar_width + bar_padding

total_label = Text(Point(win.getWidth() // 2, 380), f"Total Students: {total_students}")
total_label.setSize(12)
total_label.draw(win)

win.getMouse()
win.close()


# Print stored progression data for the user
print("\nPart 2:")
for data in student_data:
    outcome, pass_credits, defer_credits, fail_credits = data
    print(f"{outcome} - {pass_credits}, {defer_credits}, {fail_credits}")


























