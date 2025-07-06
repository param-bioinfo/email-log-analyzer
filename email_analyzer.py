filename = input("Enter filename: ")

try:
    fhand = open(filename)
except:
    print("File not found.")
    quit()

email_counts = dict()
domain_counts = dict()
hour_counts = dict()

for line in fhand:
    if line.startswith("From "):
        parts = line.split()
        email = parts[1]
        time = parts[5]

        # Count sender emails
        email_counts[email] = email_counts.get(email, 0) + 1

        # Count email domains
        domain = email.split('@')[1]
        domain_counts[domain] = domain_counts.get(domain, 0) + 1

        # Count hours
        hour = time.split(':')[0]
        hour_counts[hour] = hour_counts.get(hour, 0) + 1

# Print top sender
print("\nTop Email Sender:")
max_email = max(email_counts, key=email_counts.get)
print(f"{max_email}: {email_counts[max_email]} emails")

# Print domain summary
print("\nEmail Domain Counts:")
for dom, count in sorted(domain_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"{dom}: {count}")

# Print hour summary
print("\nEmails Sent by Hour:")
for hr, count in sorted(hour_counts.items()):
    print(f"{hr}:00 - {count} emails")
