from turtle import *

file = open("turtle", "r")
lines = file.readlines()

color('red', 'yellow')
begin_poly()
for line in lines:
	arr = line.split()
	amount = None
	op = None

	if not len(arr) or arr[0] == "Can":
		continue
	print(line)

	if arr[0] == "Avance":
		amount = int(arr[1])
		forward(amount)
	elif arr[0] == "Recule":
		amount = int(arr[1])
		backward(amount)
	if arr[0] == "Tourne":
		amount = int(arr[3])

		if arr[1] == "gauche":
			left(amount)
		elif arr[1] == "droite":
			right(amount)

end_poly()
done()