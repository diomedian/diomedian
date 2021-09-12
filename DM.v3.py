fname = input("Enter to start: ")
if len(fname) < 1 : fname = 'C:/Users/Huggies/Documents/Python/Python/LPA/docket.txt'

fh = open(fname)
Due = 0
Review = 0
count = 0
for line in fh:
	line = line.lstrip()
	line = line.rstrip()
	if line.startswith("[Closed]"):
		x = line.split(" ", 3)
	if line.startswith("[Due]"):
		x = line.split(" ", 3)
		#y = x[1]
		print(x[0], x[2], x[1], x[3:4])
		#print(x[0], x[2], x[1], x[3:4]) produces an IndexError. I have no clue why.
		Due = Due + 1
	if line.startswith("[due]"):
		x = line.split(" ", 3)
		y = x[1]
		print(x[0], x[2], x[1], x[3:4])
		#
		Due = Due + 1
	if line.startswith("[Deu]"):
		x = line.split(" ", 3)
		y = x[1]
		print(x[0], x[2], x[1], x[3:4])
		
		Due = Due + 1
	if line.startswith("[deu]"):
		x = line.split(" ", 3)
		y = x[1]
		print(x[0], x[2], x[1], x[3:4])
		
		Due = Due + 1
	if line.startswith("[Review]"):
		x = line.split(" ", 3)
		y = x[1]
		print(x[0], x[2], x[1], x[3:4])
		Review = Review + 1
	if line.startswith("[review]"):
		x = line.split(" ", 3)
		y = x[1]
		print(x[0], x[2], x[1], x[3:4])
		Review = Review + 1
	if line.startswith("[Reivew]"):
		x = line.split(" ", 3)
		y = x[1]
		print(x[0], x[2], x[1], x[3:4])
		Review = Review + 1
	if line.startswith("[reivew]"):
		x = line.split(" ", 3)
		y = x[1]
		print(x[0], x[2], x[1], x[3:4])
		Review = Review + 1
	if line.startswith("[Reveiw]"):
		x = line.split(" ", 3)
		y = x[1]
		print(x[0], x[2], x[1], x[3:4])
		Review = Review + 1
	if line.startswith("[reveiw]"):
		x = line.split(" ", 3)
		y = x[1]
		print(x[0], x[2], x[1], x[3:4])
		Review = Review + 1

#Upcoming = 40
#for line in fh
	#y = line.split('.')
	#z = y[0]

#Add sections for: Chronological order


print("You have", Due, "projects Due.")
print("You have", Review, "projects to Review.")
End = input("Enter to close: ")

