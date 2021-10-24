count = int(input("give me how many numbers you want to give.:  "))
total = 0
for i in range(count):
	bib = int(input(f"numbers {i+1}:   "))
	total = total + bib
average = total / count
print(average)
