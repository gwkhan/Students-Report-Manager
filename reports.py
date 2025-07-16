import csv
try:
	with open("reports.csv","r")as file:
		read = csv.reader(file)
		reads = list(read)
		print(f"last added details: {reads[0]}\n{reads[-1]}")
except FileNotFoundError:
	with open("reports.csv","w",newline="")as file:
		write = csv.writer(file)
		write.writerow(["Name", "Class", "Roll", "Subject", "Marks"])
while True:
	ask = input("1. Add New Student Record\n2. View All Records\n3. Search by Student Name\n4. Show Average & Grade of Student\n5. Exit\n enter: ")
	if ask=="1":
		a = input("enter details in format(Name, Class, Roll, Subject, Marks)\n").capitalize()
		with open ("reports.csv","a",newline='')as file:
			write = csv.writer(file)
			write.writerow(a.split(","))
	elif ask =="2":
		with open("reports.csv","r")as file:
			read = csv.reader(file)
			for row in read:
				print(row)
	elif ask=="3":
		a = input("enter student name: ").capitalize()
		found = False
		with open('reports.csv',"r")as file:
			read = csv.reader(file)
			for r in read:
				if a in r:
					print(r)
					found = True
		if not found:
			print("does not exist ")
	elif ask =="4":
		a = input("enter name of student: ").capitalize()
		count = 0
		score = 0
		with open("reports.csv")as file:
			read = csv.reader(file)
			next(read)
			for row in read:
				if a in row:
					count += 1
					score += float(row[-1])
		if count > 0:
			average = score/count
			if average >= 90:
				print("grade A")
			elif average >= 75:
				print("grade B")
			elif average >= 60:
				print("grade C")
			else:
			  print("grade D")
			  print("average")
		else:
			print("student not dou")
	elif ask =="5":
		print("thnx")
		break
	else:
		print("wrong input")