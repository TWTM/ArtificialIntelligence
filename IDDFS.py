# My first search algorithm
# All possible paths, ex: from 'minha casa' i can go to 'rua principal' and 'mcdonalds'
caminhos = {
    'minha casa': ('rua principal', 'mcdonalds'),
    'mcdonalds': 'minha casa',
    'rua principal': ('minha casa', 'sao sebastiao', 'escola', 'casa do douglas'),
    'sao sebastiao': ('rua principal', 'casa do douglas', 'parque'),
    'parque': 'sao sebastiao',
    'escola': ('rua principal', 'barbearia'),
    'casa do douglas': ('barbearia', 'rua principal', 'sao sebastiao'),
    'barbearia': ('casa do douglas', 'escola')
}
starting_point = 'barbearia'
goal = 'mcdonalds'
new = []
checked_paths = []
counter = 1

def filhos(oo):
    new = []
    for z in oo:
        # checked paths is created so that we can append to the variable
        checked_paths.append(z)
        if caminhos.get(z) is not None:
            print('Nos estamos olhando os caminhos de', z, 'que são', caminhos.get(z))
            for i in caminhos.get(z):
                if i == goal:
                    print('Achamos', goal)
                    exit()
                if i not in new:
                    new.append(i)
            for i in checked_paths:
                if i in new:
                    new.remove(i)
        else:
            continue
    if new == []:
        print(goal, "não esta presente")
        exit()
    print("profundidade")
    filhos(new)


# Main
filhos(caminhos.get(starting_point))