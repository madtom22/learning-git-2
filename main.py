lista = {
    'piekarni': ['chleb', 'bułki', 'pączka'],
    'warzywniaka': ['marchew', 'seler', 'rukolę']
}
things = 0

for shop, stuff in list(lista.items()):
    stuff_up = []

    for i in range(len(stuff)):
        x = stuff[i]
        y = x.capitalize()
        stuff_up.append(y)
        things = things + 1
print(' ')
print(things)
