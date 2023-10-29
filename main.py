import random
print('Splinter dice que digites un numero, si aciertas vives, sino, mueres')
def adivinar():
    while True:
        num = random.randrange(2)
        user = int(input('Ingresa un numero del 1 al 10: '))
        if user == num:
            print('Bien, adivinaste el numero Splinteriano!, el numero era: ', num)
        else:
            print('Splinter te asesino, el numero era: ', num)
            break
adivinar()