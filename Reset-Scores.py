print("Changing values to 987654...")

for i in ["easy", "medium", "hard"]:
    with open(f"Scores/{i}","w") as s1:
	    s1.write("987654")

print("Done")

