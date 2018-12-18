# imports


# ask for the parent genotypes
father = input("Input full father genotype here: ")
print('\n')
mother = input("Input full mother genotype here: ")
print('\n')


# def generate_gametes(genotype):
# do something

def generate_offsprings(father_gametes, mother_gametes):
    offspring = []

    for father_gamete in father_gametes.copy():
        for mother_gamete in mother_gametes.copy():
            offspring.append(father_gamete + mother_gamete)

    return offspring


def prettify_offspring(offsprings):
    # not working
    # sort returns think like ABAB
    # but wanted result is AABB
    # sort takes more arguments, look up in documentation
    to_return = []
    for offspring in offsprings:
        sorted_offspring = sorted(list(offspring))
        sorted_string = ''.join(sorted_offspring)
        to_return.append(sorted_string)
    to_return.sort()
    return to_return


# declare strings for different cases in each allele
# for example:
# incoC = "CW"

offspring = generate_offsprings(['AB', 'Ab', 'aB', 'ab'], ['AB', 'Ab', 'aB', 'ab'])
genotypes = prettify_offspring(offspring)

print(genotypes)

