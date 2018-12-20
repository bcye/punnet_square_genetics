# TODO: define implementation
def generate_gametes(genotype):
    pass

# TODO: recognize phenotypes using given offspring functions

# TODO: split genotypes into seperate traits
def split_genotype(genotype):
    pass

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

# tall = allele Aa
# returns true for dominant, false for recessive
def check_tall(trait):
    if 'A' in trait:
        return 1
    else:
        return 0

# BB is right handed (1)
# CC is left handed (2)
# BC is ambidextrous (0)
def check_handed(trait):
    if trait == 'BB':
        return 1
    if trait == 'CC':
        return 2
    if trait == 'BC' or trait == "CB":
        return 0

# is sorted alphabetically
# so traits that are together need to be alphabetically adjacent

# hair: Black > Brown > Blonde > Red > Purple
# Black: D (0)
# Brown: E (1)
# Blonde: F (2)
# Red: G (3)
# Purple: L (4)
def check_hair(trait):
    if 'D' in trait:
        return 0
    elif 'E' in trait:
        return 1
    elif 'F' in trait:
        return 2
    elif 'G' in trait:
        return 3
    elif 'L' in trait:
        return 4

# M: Pigment (0)
# m: No-Pigment (1)
def check_hair_pigment(trait):
    if 'M' in trait:
        return 0
    else:
        return 1

# red fur: NN (0)
# yellow fur: nn (1)
# orange fur: Nn (2)
def fur_color(trait):
    if trait == 'NN':
        return 0
    if trait == 'nn':
        return 1
    if trait == 'Nn':
        return 2

# Blood Type 0: O (0)
# Blood Type A: P (1)
# Blood Type B: Q (2)
# Blood Type AB: PQ (3)
def blood_type(trait):
    if 'P' in trait and 'Q' in trait:
        return 3
    elif 'P' in trait:
        return 1
    elif 'Q' in trait:
        return 2
    elif trait == 'OO':
        return 0

# hair pigment exists (returns color)
# hair no-pigment (returns NONE)
def check_hair_both(pigment_trait, color_trait):
    if check_hair_pigment(pigment_trait) == 0:
        return check_hair(color_trait)
    else:
        return None

def run():
    father_geno = input("Father Genotype:")
    mother_geno = input("Mother Genotype:")
    father_gametes = generate_gametes(father_geno)
    mother_gametes = generate_gametes(mother_geno)
    offspring = prettify_offspring(generate_offsprings(father_gametes, mother_gametes))
    