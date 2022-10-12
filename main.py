# TODO promenne

oddelovac = '=' * 40

potraviny = {
    'mleko':    [30,  5],    # index 0 -> cena; index 1 -> mnozstvi
    'maso':     [100, 1],
    'banan':    [30, 10],
    'jogurt':   [10,  5],
    'chleb':    [20,  5],
    'jablko':   [10, 10],
    'pomeranc': [15, 10],
    'rohlik':   [ 2, 50] 
}

kosik = {}
# kosik = dict()

budget = 150
budget_updated = budget * 1

# TODO Pozdrav a vypsani nabidky
print(
    'Vitejte v nasem online nakupnim centru'.center(len(oddelovac)), 
    oddelovac, 
    sep='\n')

for goods in potraviny:
    print(
        f'| POTRAVINA: {goods:<9} | CENA: {potraviny[goods][0]:>3},-Kc |'.center(len(oddelovac))
        )

print(
    oddelovac,
    'pro ukonceni napis \'konec\''.center(len(oddelovac)), 
    oddelovac, 
    sep='\n')

# TODO cely cyklus
while budget_updated > 0 and (zbozi := input('Zadej nazev zbozi: ')) != 'konec':
    # TODO pokud zbozi nebude v nabidce
    if zbozi not in potraviny:
        print(f'Produkt |{zbozi}| bohuzel neni v nabidce :-(')

    # TODO Pokud vybrane neni v nakupnim kosiku
    elif zbozi not in kosik and potraviny[zbozi][1] > 0:
        kosik[zbozi] = [potraviny[zbozi][0], 1]
        potraviny[zbozi][1] -= 1
        budget_updated -= kosik[zbozi][0]
        # print(kosik) # kontrolni print
        print(budget_updated)

    # TODO pokud zbozi je v kosiku
    elif zbozi in kosik and potraviny[zbozi][1] > 0:
        kosik[zbozi][1] += 1
        potraviny[zbozi][1] -= 1
        budget_updated -= kosik[zbozi][0]
        # print(kosik) # kontrolni print
        print(budget_updated)

    # TODO pokud zbozi jiz neni skladem
    elif potraviny[zbozi][1] == 0:
        print(f'{zbozi} jiz neni na sklade')

# TODO vypis uctenky
else:
    suma = []
    for cena in kosik:
        suma.append(kosik[cena][1]*kosik[cena][0])
    # print(suma)
    celkem = sum(suma)

    print(oddelovac, 'Vase uctenka'.center(len(oddelovac)), oddelovac, sep='\n')

    for item in kosik:
        print(f'| {kosik[item][1]: >3}x {item: <10}    ={kosik[item][0]*kosik[item][1]: >4},-Kc |'.center(len(oddelovac)))

    print(oddelovac)
    print(f'Celkova cena za nakup: {celkem},-Kc'.rjust(len(oddelovac)))
    if celkem > budget:
        sekera = celkem - budget
        print(f'Mate u nas sekeru {sekera},-Kc'.rjust(len(oddelovac)))
