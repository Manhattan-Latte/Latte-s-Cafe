import threading
from math import floor

import General
import Functions
import Tutorials
import time

Text = Functions.Text
Space = Functions.Space
Clamp = Functions.Clamp
Numerical = Functions.Numerical

print("Welcome to a quick and simple Python Fundamentals tutorial!")
##time.sleep(2)
print("Here, you're able to learn the basics for the programming language known as python!")
##time.sleep(2)
print("Have fun!")
##time.sleep(2)
print("\n" * 100)

Lessons = General.Lessons
LessonsKey = list(Lessons.keys())
def Choices():
    Input = Clamp(
        Numerical(input(f"Select which lesson you'd like to proceed with from the following.\n")),
        1,
        len(LessonsKey)
    )

    print("\n" * 100)
    Lesson : str = LessonsKey[Input - 1]
    LessonList = list(Lesson)
    LessonListKeys = list(Lessons[Lesson].keys())

    print(Text("=", "Green") * (100))
    print(Space(Lesson, 50 + floor((len(Lesson) / 2)), False, False) + Text(Lesson.upper(), "Blue", True))
    print(Text("=", "Green") * (100))

    for Index, Option in enumerate(Lessons[Lesson]):
        print(f"{Index + 1})", Text(Option, "Green"))

    print(f"{len(Lessons[Lesson]) + 1})", Text("Return", "Green"))

    Input = Clamp(
        Numerical(input(f"Which would you like to learn about?\n")),
        1,
        len(Lessons[Lesson]) + 1
    )

    print("\n" * 2)

    SelectedLesson = LessonListKeys[Input - 1]
    print(f"{Text("! " + SelectedLesson, "Blue")}")
    time.sleep(.5)
    if Input >= len(Lessons[Lesson]) + 1:
        Start()
    else:
        Description = Lessons[Lesson][SelectedLesson]
        if isinstance(Description, dict):
            print(f"{Text(Description["Description"], "Green")}")
            time.sleep(1)

            Proceed = Clamp(Numerical(
                input(f"Press {Text("1", "Yellow")} to proceed to a tutorial, {Text("2", "Red")} to skip!\n")), 1,
                2)

            if Proceed == 1:
                while True:
                    print("\n" * 100)
                    Tutorials.Tutorials[Description["Tutorial"]]()
                    End = Clamp(Numerical(
                        input(f"Press {Text("1", "Yellow")} to continue testing out the code, {Text("2", "Red")} to go back to the menu!\n")),
                        1,
                        2)
                    if End == 2:
                        break

            Start()

        else:
            print(f"{Text(Lessons[Lesson][SelectedLesson], "Green")}")
            time.sleep(1)
            Proceed = input(f"Press {Text("Any Input", "Yellow")} to proceed.")
            Start()

def Start():
    print("\n" * 100)
    print(Text("=", "Green") * 100)
    print(Space("Python Fundamentals!", 50 + 10, False, False) + Text("PY", "Blue", True) + Text("THON", "Yellow", True) + Text(" FUNDAMENTALS!", "Blue", True))
    print(Text("=", "Green") * 100)

    time.sleep(.5)
    for Lesson, Options in Lessons.items():
        print(f"{LessonsKey.index(Lesson) + 1})", Text(Lesson, "Green"))

    Choices()

Start()
