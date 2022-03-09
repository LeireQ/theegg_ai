#1. Asignaturas y notas
subjects = ["Matemáticas","Física","Química","Historia","Lengua"]
scores = []
for subject in subjects:
    score = input("¿Qué nota has sacado en " + subject + "? ")
    scores.append(score)
for i in range(len(subjects)):
    print("En " + subjects[i] + " has sacado " + scores[i])

#2. Lista inversa
numbers = [1,2,3,4,5,6,7,8,9,10]
for i in range(1,11):
    print(numbers[-i],end=", ")

#3. Palíndromo
word = input("\nIntroduce una palabra: ")
reversed_word = word
word = list(word)
reversed_word = list(reversed_word)
reversed_word.reverse()
if word == reversed_word:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")

#4. Orden de menor a mayor
prices = [50, 75, 46, 22, 80, 65, 8]
min = max = prices[0]
for price in prices:
    if price < min:
        min = price
    elif price > max:
        max = price
print("El mínimo es "+str(min))
print("El máximo es "+str(max))

#5. Contador de vocales
word = input("Introduce una palabra: ")
vocals = ['a','e','i','o','u']
for vocal in vocals:
    times = 0
    for letter in word:
        if letter == vocal:
            times += 1
    print("La vocal " + vocal + " aparece " + str(times) + " veces")

#6. Asignaturas aprobadas
subjects = ["Matemáticas","Física","Química","Historia","Lengua"]
passed = []
for subject in subjects:
    score = float(input("¿Qué nota has sacado en " + subject + "?"))
    if score >= 5:
        passed.append(subject)
for subject in passed:
    subjects.remove(subject)
print("Tienes que repetir " + str(subjects))