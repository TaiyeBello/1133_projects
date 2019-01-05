## CSCI 1133, Fall 2017 - Programming Examination 3

> **Due: 10:00 pm: WEDNESDAY, DEC 6**

A friendly reminder: PLEASE back up your work as you go along. You can push to github after every coding session -- we will see only the latest version that you submitted. If github is too intimidating, use your google drive. Also, your cselabs account is backed up every night. And if nothing else, email a copy to yourself every once in awhile.

PLEASE NOTE: This is a graded assessment of individual programming understanding and ability, and is not a collaborative assignment; you must design, implement and test the solution(s) completely on your own without outside assistance from anyone except teaching staff. You may not consult or discuss the solution with anyone. In addition, you may not include solutions or portions of solutions obtained from any source other than those provided in class. Note that providing a solution or assisting another student in any way on this examination is also considered academic misconduct. Failure to heed these directives will result in a failing grade for the course and an incident report filed with the Office for Student Conduct and Academic Integrity for further sanction.</font>

>Read the requirements carefully, as it is your responsibility to have a clear understanding of what is being asked. If you do not understand, please ask teaching staff. Requirements for software are particularly difficult to express in English, thus it is likely that there will be subtleties that need clarification.

<hr>

### A. Simulated Swarming Behavior

Swarming behavior seen in animals such as birds, fish, and bees can be simulated in artificial life with relatively simple rules. If each animal is attracted to a source (e.g. food or light) but has a rule to maintain space between it and other things, then swarming behavior emerges. In this exam, you will create a collection of artificial life forms with light sources that attract some of the creatures but repel others. The simulation will be displayed in turtle graphics.

The total point value will be awarded for solutions that are well designed, correct, complete, and well constructed. A "well constructed" program entails good design, appropriate comments and general readability (descriptive names for variables and procedures, appropriate use of blank space, etc.). _Good_ design takes advantage of variables and classes to create generic code that can be easily extended in functionality. As part of your design, you must use classes and **__inheritance__** in your design.

<hr>

### Environment and Entities  

In this environment there will be lights and creatures, some of which are attracted to the light and some of which are repelled by the light. As you think about the classes that you need for this exam, consider what is the same and what is different. For those elements that are the same, they should be in a base/parent class. If you are copying and pasting code from one class to another, think carefully -- can that be written once in a base class instead? The answer is not always "yes," but it often is.

#### Creatures

Each creature should be placed in the environment with its heading set randomly. It moves in the direction of its heading by _speed_ pixels at each update of the simulation. The heading of the creature is impacted by its proximity to other creatures and to a light source, as well as the wall. If the creature bumps into the wall, it should reflect off of it. _collision.py_ has been provided which will bounce a ball off of a wall or another ball at the angle of reflection, based on the code provided at http://flatredball.com/documentation/tutorials/math/circle-collision/. For each creature, calculate the distance from itself to each light and each creature (e.g. dist = ((pos2.x-pos1.x)^2 + (pos2.y-pos1.y)^2)^0.5). Adjust the heading, scaled by the distance to the light, so that it turns towards the closest light if it is attracted and away from all the lights in its vicinity if it is repelled by light. You can use math.atan2(y,x) to determine the heading from the creature to another object. Also, adjust the heading to move away from creatures that are within a certain distance. During class, we will talk more about the strategy for modifying the heading to get the swarming behavior correct. Start by setting the heading to move the creature directly toward the closest light or in a direction away fom close-by lights, based on whether it is attracted or repelled, respectively. Then add in the functionality to modify the heading to avoid running into other creatures.

It is your choice on how to display the creature, but you should have some indication of heading (e.g. a line or a head shape or maybe a fish tail). You can choose the creature shape, color, and size, although keep them relatively small so that you can put lots of them in the environment. Creatures are conceptualized as circles, but you can make them any shape you like (even a plain circle).

#### Lights

Each light should be placed in the environment with its heading set randomly. It moves in the direction of its heading by _speed_ pixels at each update of the simulation. The heading of the light is impacted by running into the wall -- if it bumps into a wall then it should reflect off the wall. If it is indicated that it should randomize its movement, then it should occasionally change its heading by some random angle. It is your choice on how to display a light. You do not have to indicate the heading of a light. Lights should be visually distinct from creatures.

#### Arena

Create an Arena class that contains all the creatures and lights. Update these entities through the Arena using a method, for example Arena.Update() would update the heading and position of each entity then draw it at its new location. You can initialize the graphics through the Arena class or through _main()_. Call your update function from within a loop in _main()_.


### Configuration File

A configuration file has been included that has 2 examples of an environment. A class structure is used to configure the types of creatures and lights, as such:

```Python
class CreatureConfiguration:
  def __init__(self, count, attract=True, space=20, speed=3 ) :
    self.count = count
    self.attract = attract
    self.speed = speed
    self.space = space

class LightConfiguration:
  def __init__(self, count, speed=5, random=True):
    self.count = count
    self.speed = speed
    self.random = random
```

- Creature.count: the number of creatures to place in the environment with the given characteristics
- Creature.attract: True if creatures are attracted to lights, False if repelled
- Creature.speed: the number of pixels to move the creature at each update
- Creature.space: other creatures within this distance influence the heading of the creature. For example, if creature1 has space set to 20, then if it is within 20 pixels of another creature, then creature1 should adjust its heading to move away from the other creature.
- Light.count: the number of lights to place in the environment
- Light.speed: the number of pixels to move the light at each update
- Light.random: True if the light should occasionally randomly change direction  

### File Structure

**__entities.py__**: Place your classes for the creature and the light in the file _entities.py_ (and any class or functions that these entity classes depend upon). Include ONLY classes and functions in this file. Import this file into _swarm.py_.

**__swarm.py__**: Place your Arena class in the file _swarm.py_, as well as the _main()_ function. _main()_ might look like this ...

```Python
def main() :
  turtle.tracer(0,0)
  arena = Arena(TestConfiguration.example[test_case])
  arena.InitializeGraphics()
  try:
    while True:
      Arena.Update()
      turtle.update()
  except KeyboardInterrupt:
    print('Done swarming.')
```

Your main function may be different, but keep in mind that the creatures and lights must be stored in the Arena class and must be updated through a call to a method in Arena. Although if you have a compelling reason for doing otherwise, please consult with Dr. Larson. There are many ways to design a program and you might have a better way than what is presented here, and she would be happy to discuss other options.

The try-except is a way to gracefully exit out of the program. It "tries" the code inside the _try_ block and if there are any errors or exceptions like a keyboard interrupt signal, which is a ctrl-c, it then executes the code in the _except_ block. Once the script is running, if you hit ctrl-c, it will break out of the while loop and end the program gracefully. Otherwise, close the graphics window to kill it ungracefully (i.e. with error messages). You do not have to use the try-except.

### Assessment

This assignment will be assessed on the basis of its design, functionality, and code quality, with an emphasis on design. Code that is poorly designed, even if it functions correctly, will not earn an A. Code that is very well designed, but does not function perfectly, might earn an A.

Correct Design:
- Classes for arena entities are in the file _entities.py_.
- Class Inheritance was used.
- **Class structure reflects the similarities through the base class and the differences in the derived classes. In other words, code is not unnecessarily replicated in multiple classes.**
- There exists an Arena class.
- The Arena class stores all entities.
- The Arena class updates all entities.
- **Appropriate data types and structures (e.g. lists, dictionaries, classes) are used.**
- The _main_ function is in _swarm.py_.
- The _main_ function has relatively few lines of code.

Correct Functionality:
- Creatures are configured according to the configuration file.
- Lights are configured according to the configuration file.
- Creatures and lights are displayed in turtle graphics and are visually distinguishable.
- Creatures and lights move at each update.
- Creatures and lights bounce off of walls.
- Creatures are attracted to or repelled from lights.
- Creatures avoid each other.
- Lights randomly change direction when configured to do so.

Quality Code:
- Functions and variables have descriptive names.
- **The problem is decomposed into small functions and small class methods.**
- In-line comments are used to better understand the code.
- Variables are used where appropriate rather than "hard-coding" values.

<hr>

### Getting Started

Think about the design of your classes. What are the methods that you will need to get the required functionality? One approach might be to get a creature moving in the environment to better understand what is needed. Then work on your design of the creature, light, and arena. Once those entities are moving around independently, develop the interaction between them. The exercise _robot.py_ might be helpful to you.

### Seeking Assistance

You may ask any questions of teaching staff regarding general Python concepts, such as class inheritance.

You may ask questions of teaching staff in a limited capacity regarding the specifics of this exam. You may ask questions about:

- Trigonometry related to calculating distance and heading.
- Turtle graphics related to setting the coordinates (for example, you might want to change the origin to the lower left instead of the middle of the window), increasing or decreasing the display area, or improving the rendering speed.
- Strategies for modifying the heading to improve swarming behavior.

You may ask for debugging advice regarding specific code, if you have the problem isolated. This means that you have spent time debugging the code, and you know which lines or which function is not working. Staff will not debug code for you, but they can offer strategies to better isolate and identify the problem.

> The emphasis for this exam is program design using Object-Oriented Programming concepts. For this reason, teaching staff cannot discuss specifics about the design of your classes.  

<hr>

#### Submission Instructions

Submit your files to your exam repo on github.

Your work will be graded using the current version of Python 3 on CSE Labs UNIX machines, thus it must function correctly on that platform. If you complete this programming exam using a different system, it is your responsibility to ensure it works on CSELabs machines prior to submitting it. You can confirm this by cloning your repo into a new directory when logged in to a CSELabs machine and running the code from that directory.

*PLEASE NOTE:* missing submissions will result in a grade of zero.

*NO LATE WORK ACCEPTED*

<u>It is HIGHLY recommended</u> that you regularly put your working version of your code in github, particularly if you are working on your personal machine. Laptops and PCs die all the time - and sometimes the night your assignment is due!! **PLEASE back-up your work regularly** - github is great for that.
