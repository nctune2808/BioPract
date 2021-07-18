import copy
import random


class Individual:
    gene = []
    fitness = 0

    def __repr__(self):
        return "Gene string " + "".join(str(x) for x in self.gene) + " - fitness: " + str(self.fitness) + "\n"


P = 50
N = 10


def counting_ones(ind):
    fitness = 0
    for i in range(0, N):
        if ind.gene[i] == 1:  # if gene of an individual at index i equals to 1
            fitness = fitness + ind.gene[i]
    return fitness


def initialise_population():  # need fix
    population = []
    for x in range(0, P):
        tempgene = []
        for x in range(0, N):
            tempgene.append(random.randint(0, 1))  # a random gene between 0.0 and 1.0(inclusive)

        newindi = Individual()  # initialise new instance
        newindi.gene = tempgene.copy()  # copy the gene from tempgene and assign to gene of individual
        newindi.fitness = counting_ones(newindi)  # initialise instance's fitness

        print(tempgene, " -> ", newindi.fitness)
        population.append(newindi)

    return population


def touranment_selection(population):
    offspring = []
    # Select two parents and recombine pairs of parents
    for i in range(0, P):
        parent1 = random.randint(0, P - 1)
        off1 = population[parent1]
        parent2 = random.randint(0, P - 1)
        off2 = population[parent2]
        if off1.fitness > off2.fitness:  # if one's fitness higher then add to temp off_sptring
            offspring.append(off1)
        else:
            offspring.append(off2)

    return offspring


def crossover(offspring):
    cross_offsprings = []

    for i in range(0, P, 2):
        cross_point = random.randint(0, N - 1)

        off1 = Individual()
        off2 = Individual()

        head1 = []
        tail1 = []
        head2 = []
        tail2 = []

        for j in range(0, cross_point):
            head1.append(offspring[i].gene[j])
            head2.append(offspring[i + 1].gene[j])

        for j in range(cross_point, N):
            tail1.append(offspring[i].gene[j])
            tail2.append(offspring[i + 1].gene[j])

        off1.gene = head1 + tail2
        off1.fitness = counting_ones(off1)
        cross_offsprings.append(off1)

        off2.gene = head2 + tail1
        off2.fitness = counting_ones(off2)
        cross_offsprings.append(off2)

    return cross_offsprings


def mutation(cross_offsprings):
    mut_offsprings = []

    for i in range(0, P):
        new_ind = Individual();
        new_ind.gene = []
        for j in range(0, N):
            gene = cross_offsprings[i].gene[j]

            mut_prob = random.randint(0, 100)
            if mut_prob < (100 * 0.03):
                if gene == 1:
                    gene = 0
                else:
                    gene = 1
            new_ind.gene.append(gene)
        new_ind.fitness = counting_ones(new_ind)
        print(new_ind)


print(mutation(crossover(touranment_selection(initialise_population()))))
