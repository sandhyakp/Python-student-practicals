# Step 1: 5 subjects ke marks input karen
marks1 = int(input("Pehle subject ke marks daaliye: "))
marks2 = int(input("Dusre subject ke marks daaliye: "))
marks3 = int(input("Teesre subject ke marks daaliye: "))
marks4 = int(input("Chauthe subject ke marks daaliye: "))
marks5 = int(input("Paanchve subject ke marks daaliye: "))

# Step 2: Aggregate marks calculate karen (total marks)
aggregate = marks1 + marks2 + marks3 + marks4 + marks5

# Step 3: Average marks calculate karen
average = aggregate / 5

# Step 4: Aggregate aur average marks ko print karen
print("Aggregate marks hain:", aggregate)
print("Average marks hain:", average)
