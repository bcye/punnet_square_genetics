# imports


# ask for the parent genotypes
father = input("Input full father genotype here: ")
print('\n')
mother = input("Input full mother genotype here: ")
print('\n')

# TODO: define implementation
def generate_gametes(genotype):
    pass

# TODO: recognize phenotypes using given offspring functions

# TODO: split genotypes into seperate traits

# implementation done
def generate_offsprings(father_gametes, mother_gametes):
    offspring = []

    for father_gamete in father_gametes.copy():
        for mother_gamete in mother_gametes.copy():
            offspring.append(father_gamete + mother_gamete)

    return offspring

# implementation done
def prettify_offspring(offsprings):
    to_return = []
    for offspring in offsprings:
        sorted_offspring = sorted(list(offspring), key= lambda x:(x.lower(),x)) # sorts so it appears like a genotype
        sorted_string = ''.join(sorted_offspring)
        to_return.append(sorted_string)
    to_return.sort()
    return to_return

# tall = allele Tt
# returns true for dominant, false for recessive
def check_tall(trait):
    if trait.contains('T'):
        return 1
    else:
        return 0

# RR is right handed (1)
# LL is left handed (2)
# RL is ambidextrous (0)
def check_handed(trait):
    if trait == 'RR':
        return 1
    if trait == 'LL':
        return 2
    if trait == 'RL':
        return 0

# hair: Black > Brown > Blonde > Red > Purple
 

offspring = generate_offsprings(['AB', 'Ab', 'aB', 'ab'], ['AB', 'Ab', 'aB', 'ab'])
genotypes = prettify_offspring(offspring)

print(genotypes)

