import random
import copy
import numpy as np
from operator import attrgetter
from random import sample 
from GA.Crtr import *


class GeneticAlgorithm(object):
    def __init__(self, mnn, population_size=50, generations=100, crossover_probability=0.8, mutation_probability=0.2, elitism=True, maximise_fitness=True):
        self.seed_data = []
        for x in range(population_size):
            self.seed_data.append(Crtr(0, mnn))

        self.foodlocx = np.random.randint(1, 500)





        self.netsize = mnn
        self.population_size = population_size
        self.generations = generations
        self.crossover_probability = crossover_probability
        self.mutation_probability = mutation_probability
        self.elitism = elitism
        self.maximise_fitness = maximise_fitness
     
        self.foodlocy = 0
        self.current_generation = []
        self.fitness_function = None
       # self.tournament_selection = tournament_selection
        self.tournament_size = self.population_size // 10
       # self.random_selection = random_selection
    
        self.crossover_function = 9
        self.mutate_function = 8
        self.selection_function = self.tournament_selection


        #self.create_individual = create_individual
    def create_individual(seed_data):
        """Create a candidate solution representation.
        e.g. for a bit array representation:
        >>> return [random.randint(0, 1) for _ in range(len(data))]
        :param seed_data: input data to the Genetic Algorithm
        :type seed_data: list of objects
        :returns: candidate solution representation as a list
        """
        return [random.randint(0, 1) for _ in range(len(seed_data))]

    def crossover(parent_1, parent_2):
        """Crossover (mate) two parents to produce two children.
        :param parent_1: candidate solution representation (list)
        :param parent_2: candidate solution representation (list)
        :returns: tuple containing two children
        """
        #index = np.random.random_integers(1, len(parent_1))
        #child_1 = parent_1[:index] + parent_2[index:]
        childnewgenes = []
        for x in range(len(parent_1)):
            z = parent_1[x] + parent_2[x]
            z /= 2
            childnewgenes.append(z)

            
        return childnewgenes

    def mutate(individual):
        """Reverse the bit of a random index in an individual."""
        #mutate_index = np.random.random_integers(len(individual) - 1)
        #individual[mutate_index] += np.random.random()
        for x in range(len(individual)):
            individual[x] += np.random.random()

    def random_selection(population):
        """Select and return a random member of the population."""
        return random.choice(population)

    def tournament_selection(population):
        """Select a random number of individuals from the population and
        return the fittest member of them all.
        """
        if self.tournament_size == 0:
            self.tournament_size = 2
        members = sample(population, self.tournament_size)
        members.sort(
            key=attrgetter('fitness'), reverse=self.maximise_fitness)
        return members[0]

    









    def create_initial_population(self):
        """Create members of the first population randomly.
        """
        self.foodlocx = np.random.randint(1, 500)
        initial_population = []
        for _ in range(self.population_size):
            #genes = self.create_individual(self.seed_data)
            #individual = Chromosome(genes)
            initial_population.append(self.seed_data[_])#individual
        self.current_generation = initial_population










    def calculate_population_fitness(self):
        """Calculate the fitness of every member of the given population using
        the supplied fitness_function.
        """
        for individual in self.current_generation:
            individual.fitness = self.fitness_function(
                individual, self.foodlocx)







    def rank_population(self):
        """Sort the population by fitness according to the order defined by
        maximise_fitness.
        """
        self.current_generation.sort(
            key=attrgetter('fitness'), reverse=self.maximise_fitness)
        """
        for x in range(len(self.current_generation)):
            print(self.current_generation[x].fitness)
        """




    def create_new_population(self):
        """Create a new population using the genetic operators (selection,
        crossover, and mutation) supplied.
        """

        #self.foodlocx = np.random.randint(1, 500)
        new_population = []
        elite = copy.deepcopy(self.current_generation[0])
        selection = self.selection_function
        #self.foodlocx = np.random.randint(500)+

        

        while len(new_population) < self.population_size:
            parent_1 = copy.deepcopy(self.current_generation[0])
            parent_2 = copy.deepcopy(selection(self.current_generation))

            child = parent_1
            child.fitness = 0

            can_crossover = np.random.random() < self.crossover_probability
            can_mutate = np.random.random() < self.mutation_probability

            if can_crossover:
                
                child = self.crossover_function(parent_1, parent_2)
                #child.dna.genes = self.crossover_function(parent_1.dna.genes, parent_2.dna.genes)

            if can_mutate:
                

                bb , child.dna.genes = self.mutate_function(child, self.mutation_probability)
                if(len(child.dna.genes) == 0):
                    child.nuralnet.ARRToBias(bb)

  
                child.nuralnet.ARRToBias(bb)

           

            if len(new_population) < self.population_size:

                z = Crtr(child.dna, self.netsize)
                new_population.append(z)








        if self.elitism:
            new_population[0] = elite


     

        if len(self.current_generation) == self.population_size:
            self.current_generation += new_population
        else:
            self.current_generation.sort(key=attrgetter('fitness'), reverse=False)
            del self.current_generation[-self.population_size:]
            self.current_generation += new_population

        

        






    def create_first_generation(self):
        """Create the first population, calculate the population's fitness and
        rank the population by fitness according to the order specified.
        """
        self.create_initial_population()
        self.animate()
        self.calculate_population_fitness()
        self.rank_population()







    def create_next_generation(self):
        """Create subsequent populations, calculate the population fitness and
        rank the population by fitness in the order specified.
        """
        self.create_new_population()
        self.animate()
        self.calculate_population_fitness()
        self.rank_population()









    def run(self):
        """Run (solve) the Genetic Algorithm."""
        self.create_first_generation()

        for _ in range(1, self.generations):
            
            if(self.best_individual() == 1):
                break
            self.create_next_generation()
            print("generation : ", _, "   ", "foodloc  ",self.foodlocx )







    def best_individual(self):
        """Return the individual with the best fitness in the current
        generation.
        """
        best = self.current_generation[0]
        print(best.fitness)
        #print(best.fitness,best.bulletlocx)
        if(best.fitness < 0.0001):
            return 1
        #return (best.fitness, best.genes)

    def last_generation(self):
        """Return members of the last generation as a generator function."""
        return ((member.fitness, member.genes) for member
                in self.current_generation)
    


    def animate(self):
        for x in range(self.population_size):
            self.current_generation[x].update(self.foodlocx)







class Chromosome(object):
    """ Chromosome class that encapsulates an individual's fitness and solution
    representation.
    """
    def __init__(self, genes):
        """Initialise the Chromosome."""
        self.genes = genes
        self.fitness = 0

    def __repr__(self):
        """Return initialised Chromosome representation in human readable form.
        """
        return repr((self.fitness, self.genes))