## CSCI 1133, Fall 2017 - Programming Examination 1


> Part 1 Due: 10:00 pm: Fri, Oct 6

> Part 2 Due: 10:00 pm: Mon, Oct 16

PLEASE NOTE: This is a graded assessment of individual programming understanding and ability, and is not a collaborative assignment; you must design, implement and test the solution(s) completely on your own without outside assistance from anyone. You may not consult or discuss the solution with anyone. In addition, you may not include solutions or portions of solutions obtained from any source other than those provided in class. Note that providing a solution or assisting another student in any way on this examination is also considered academic misconduct. Failure to heed these directives will result in a failing grade for the course and an incident report filed with the Office for Student Conduct and Academic Integrity for further sanction.</font>

>Read the requirements carefully, as it is your responsibility to have a clear understanding of what is being asked. If you do not understand, please ask teaching staff. Requirements for software are particularly difficult to express in English, thus it is likely that there will be subtleties that need clarification.


Clarifications to this document are marked with **[EDIT]**

<hr>

### A. (100 points) Sudoku

This examination consists of two parts. The first part involves creating a short text file that must be committed and pushed to your GitHub examination repository (discussed below) prior to the Part 1 deadline on Friday, October 6. The second part requires designing and writing a single Python program (module) that must be committed and pushed to your GitHub examination repository prior to the Part 2 deadline on Monday, October 16. Late submissions will not be accepted and will result in a zero score for the exam.

The total point value will be awarded for solutions that are complete, correct, and well constructed. A "well constructed" program entails good design, appropriate comments and general readability (descriptive names for variables and procedures, appropriate use of blank space, etc.).

Note that your work will be graded using the current version of Python 3 on CSE Labs UNIX machines, thus it must function correctly on that platform. If you complete this programming exam using a different system, it is your responsibility to ensure it works on CSELabs machines prior to submitting it. You can confirm this by cloning your repo into a new directory when logged in to a CSELabs machine and running the code from that directory.

#### Examination Repository
Examination files must be submitted to the GitHub using a special "exam repository". Exam repositories will be created for each registered student and are named using the string exam- followed by your X500 userID (e.g., exam-smit1234). You must first clone your exam repository in your local home directory before submitting the materials for this exam. If you are having difficulty, consult the github from earlier in the semester. If your exam repository is missing or something is amiss, please contact the graduate TA.

_DO NOT SUBMIT YOUR EXAM FILES TO YOUR LAB/EXERCISE REPOSITORY!_

<hr>

#### Part 1 (10 points)

HAND WRITE LEGIBLY the following academic integrity pledge (exactly as it appears), replacing the last line with your full name and X500 ID. Add your signature. Take a picture or scan the writing and paste into a text file or create a pdf with the name academic pledge and commit/push it to your GitHub examination
repository:


<p align="center">
<img src="pledge.png" alt="Drawing" style="width: 500px;"/>
</p>

<p align="center">
_YOUR SIGNATURE HERE_
</p>

If you do not commit and push the `academicpledge.*` file prior to the October 16 deadline for Part 2, your entire examination solution will not be accepted for grading, resulting in a score of zero. In order to receive the 10 points for Part 1, you must submit the pledge file to your exam repository prior to 10:00pm,
October 6.

\* Can be  .docx, .pptx, .txt, .pdf, .jpg, .png, .gif, ...

<hr>

#### Part 2 (90 points)

Using Turtle graphics, write a Python program that will play the game of Sudoku. Sudoku is a puzzle game in which you must fill in each box of a grid with a number following some constraints. The constraints are that each row and each column must not have any duplicates; and that within a subgrid there are no duplicates. Here is an example of a starting puzzle and the completed puzzle:

<p align="center">
<img src="puzzle.png" alt="Drawing" style="width: 400px;"/>
</p>


Notice that there are darker lines around the four boxes that make each corner. Within those inner grids, there are no duplicate elements.

#### Submission Instructions

Put all of your source code into a single module and name it `sudoku.py` Commit/push your source file to your exam repository prior to the deadline for Part 2 on October 16.

*PLEASE NOTE:* missing or misnamed submissions will not be graded and will result in a grade of zero.

#### Requirements:

Your program must do the following:

- Define a Python list of 5 4x4 puzzles in its initial <s>and completed</s> configuration. Use a data structure you
think is appropriate and easy to use. For example, the above puzzle in its unsolved form might be
[[3,4,1,3],[0,0,0,0],[0,0,0,0],[4,2,3,1]], and the completed puzzle as
[[3,4,1,3],[2,1,4,3],[1,3,2,4],[4,2,3,1]].

- You might instead use tuples or classes. Lots of 4x4 puzzles can
be found here: https://www.allkidsnetwork.com/puzzles/kids-sudoku.asp and here: http://www.mathinenglish.com/puzzlessudoku.php?pstid=601

- Randomly select one of the puzzles at the start of the game.

- Use turtle graphics to implement a graphical display of the game.

- Give the user the option of playing with real-time correction or not. With real-time correction, the value given by the user is checked for correctness <s>against the answer</s>. If it is wrong, the user should get an appropriate message and the number is not added to the puzzle. If it is correct, you do not need to display a message and the value is added to the puzzle. **[EDIT]** Since you are not storing the answer, you can only check against what has already been input along the relevant row, column, and inner box.

- **[EDIT]** Indicate to the user how to enter in numbers for the game. You can (optionally) create a pop-up window that describes the rules in general and how to play your game specifically.

- Repeatedly ask the user for a location and value to place into the puzzle. If the user indicates a location where a number already appears, overwrite the number that is there. Display the number or a message as appropriate given the player’s choice as described above.

- You decide how the user should specify a location. You might want to label the rows and columns to make it easier for the user. For example, if rows top to bottom were labeled “A”,”B”,”C”,”D” and columns with “1”,”2”,”3”,”4”, then a user could put in a request as B1=2 or B1,2 or [B,1]=2. This is just an example – use whatever makes sense to you and is easy to explain to the user.

- Allow the user to erase the value in a square as well. They do not need to erase before replacing the current value. You decide how the user should indicate that.

- Once all boxes are filled in, give the player the option of submitting their solution. If they don’t want to submit, ask for another value before again asking if they want to submit.

- **[EDIT]** Check the solution by checking the constraints that numbers are unique across each row, column, and inner box. Indicate to the user that s/he has won if all are good. You decide what to do if the solution provided is not correct.

- You will find the `.textinput()`, `.numinput()`  <s>turtle</s> screen methods and the `.write()` turtle method to be useful for input and output. You can find descriptions of these functions/methods (along with all the Turtle graphics module functions) here:
https://docs.python.org/3/library/turtle.html. To write text, you can use this method: `turtle.write("1", move=False, align="left", font=("Arial", 28, "normal"))`, which writes “1” in font size 28. _See Helpful Hints section for hint about input methods._

- All of the drawing can be done using basic turtle drawing methods as used in Lab exercises.

- You will not need the "turtle" image, you can disable it using the `.hideturtle()` method.

- Be sure to speed up the drawing using the `.speed(0)` method call.

- As an optional feature, you may add code to allow the user to play another game when finished.

- The set-up for the game should be done in the code without user intervention such that when the script is run the game is immediately ready to play.

**Programming Constraints:**
- You may use any built-in Python object methods (string, list, etc.)

- You may use imported methods from the random and turtle modules only

- You may use any built-in Python functions/operations as appropriate, with the exception of `input()`
and `print()` which will not work with a graphical display environment.

**Helpful Hints:**

- You will find this much easier if you employ the principles of "top-down, functional decomposition" and implement your program as a collection of short, simple functions. For example, you might consider a separate function for drawing the grid, and another for filling in the boxes, and another for checking correctness, etc.

- Consider using multiple turtles for different tasks in your program. For example,
the snippet below clears everything drawn only by the turtle `erasable`.
```
import turtle
erasable = turtle.Turtle()
erasable.clear()
```

- To check if two lists have exactly the same elements you can use the notion of sets. In mathematics, a set is an unordered collection of distinct elements. You can use curly brackets or `set()` to create a set in Python.

```
    >>> a = {1,2,3}
    >>> type(a)
    <class 'set'>
    >>> b = set([3,1,2])
    >>> a == b
    True
    >>> c = {1,1,2,2,2,3}
    >>> a == c
    True
```

- **[ADDITION]** Here is an example of a pop-up window in turtle graphics when calling textinput. Note that textinput is a method for screen, not for turtle. You have to get the screen from turtle to call this function. See Sections 23.1.3.7 and 23.1.4.4 of https://docs.python.org/3.1/library/turtle.html

<p align="center">
<img src="textinput.png" alt="textinputwindow" width="50%"/>
</p>

<hr>

**[EDIT]: Assessment:**

- **[EDIT]** __Functionality__: Each program will be played by a person to assess the meeting of the requirements.

- **[EDIT]** __Code Quality__: The code will be evaluated for 1) good organization, which means you have deconstructed the problem into smaller problems and written helper functions to solve the smaller problems; 2) good naming conventions, which means a reader can infer meaning from the function or variable name (limit your use of abbreviations) and the approach to naming is consistent; 3) good documentation, which means comments that highlight the logic (note that if you use good naming conventions, the code is self-documenting and requires fewer comments).

- **[EDIT]** __Interview:__  During the lab in the week you turned in your code, you will meet with the TA and answer a few questions about what you wrote. These questions will be related to the many choices you made as you completed the assignment, including data structures, code layout, and logic.
