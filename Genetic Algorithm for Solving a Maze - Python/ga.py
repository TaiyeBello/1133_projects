import maze
import maze_samples
import random

class ga:
  
  def __init__(self,name,maze):
    self.name = name
    self.maze = maze #the maze(from import maze) is passed in so it can be used within this class
    self.current_pop = [] #creating an empty list that the original population can go into once it's made in the create_population method
  def create_population(self): #method that creates a population of indivduals which are strings
    Names = []
    for i in range(1,51): 
      Names.append('Mouse' + str(i)) #the names of the indivuduals are being created
    population_name = [] #a list for just the names
    population_string = [] #a list for the strings
    i = 0
    for el in Names:
      el = individual(Names[i]) #each individual is being made with the individual class below
      name = el.getName() #calling the getter method in the indivdual class for each individual
      string = el.make_Individual() #each indivdual is given a string
      i += 1
      population_name.append(name) #adding each name to a list
      population_string.append(string) #adding each string(indivdual) to a list
    self.current_pop = population_string #allows me to use the population in the rest of the class
  def SetWeightsForMonteCarloSelection(self,values): #this method increases the chances of an individual with a high fitnesss value of reproducing
    normalized_values = [int(v/sum(values)*100+.5) for v in values]
    accum = 0
    selection_weights = []
    for w in normalized_values:
      accum += w
      selection_weights.append(accum)
    return selection_weights
  def MonteCarloSelection(self,selection_weights): #this method returns the index of the individual so it can be used to create the next generation
    selection = random.randint(0,selection_weights[-1])
    for i,w in enumerate(selection_weights):
      if selection <= w:
        return i
  def ga_logic(self):
    self.create_population() #calling method so population is created
    for i in range(2): #the amount of generations that will be created
      fitness_list = [] #list of fitness values
      for el in self.current_pop: #for each individual in the population
        x = self.maze.RunMaze(el) #test the string
        fitness = x[2] #get their fitness value
        fitness_list.append(fitness) #put thier fitness value in a list
        self.maze.ResetMouse() #reset the mouse
      new_generation = [] #list where new generaiton will go 
      for p in range(len(self.current_pop)//2): 
        S = self.SetWeightsForMonteCarloSelection(fitness_list) 
        parent1 = self.MonteCarloSelection(S) #parents are picked based on fitness value
        parent2 = self.MonteCarloSelection(S) #parents equal an index value 
        new_individual1,new_individual2 = self.cross_breed(parent1,parent2) #two new individuals are created 
        mutation = 75
        r = random.randint(1,100)
        if r <= mutation: #indviduals are mutated 
          self.mutation(new_individual1,new_individual2)
        new_generation.append(new_individual1) #individuals are added to new generation
        new_generation.append(new_individual2)
      self.current_pop = new_generation #the current population will now be the newest generation
  def cross_breed(self,p1,p2):
    x = random.randint(1,61)
    Parent1 = self.current_pop[p1] #p1 = a integer that is used to index through the population
    Parent2 = self.current_pop[p2]
    baby1 = Parent1[0:x] + Parent2[x:] #new individuals are created
    baby2 = Parent2[0:x] + Parent1[x:]
    return [baby1,baby2]
  def mutation(self,baby1,baby2):
      idx1 = random.choice(baby1) #chooses a random letter in the string of the mouse
      idx2 = random.choice(baby2)
      x = random.choice('URLD') #chooses a random letter in this string
      y = random.choice('URLD')
      index1 = baby1.index(idx1) # gets the index of the choosen letter in the string of the mouse
      index2 = baby2.index(idx2)
      Baby1 = list(baby1) #changes the string to a list of letters
      Baby2 = list(baby2)
      Baby1[index1] = x #changes choosen letter in string of the mouse to a different letter
      Baby2[index2] = y
      return [Baby1,Baby2]


class individual:

  def __init__(self,name):
    self.name = name
  def getName(self):
    return self.name #getter method
  def make_Individual(self): #method to make each individual
    test_case = 0
    string_length = maze_samples.string_length[test_case] #60
    genes = 'URLD'
    id = '' #empty string
    for i in range(string_length): # create string of length 60
      id += random.choice(genes) #add letter to id until there are 60 letters
    return id
  
def main():

  test_case = 0
  M = maze.Maze(maze_samples.maze[test_case])
  M.Visualize()
  genetic_algorithm = ga("mega",M) #object of class ga
  genetic_algorithm.create_population() #create population
  genetic_algorithm.ga_logic() #runs genetic algortihm 
  
if __name__=='__main__' :

  main()


