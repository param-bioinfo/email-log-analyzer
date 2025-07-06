filename = input("Enter file name: ")
handle = open(filename)
counts = dict()

for line in handle:
    if line.startswith("From "):
        words = line.split()
        email = words[1]
        counts[email] = counts.get(email, 0) + 1

biggest = None
bigcount = None

for email, count in counts.items():
    if bigcount is None or count > bigcount:
        biggest = email
        bigcount = count

print(biggest, bigcount)
