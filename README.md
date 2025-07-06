# 📊 Email Log Analyzer

A beginner-friendly Python project to analyze email logs from `.txt` files.  
Built after completing the **Python for Everybody** course by Dr. Charles Severance.

---

## 📌 Project Description

This script reads a plain-text email log file (like `mbox-short.txt`) and extracts:

- 📤 **Top email senders**
- 📨 **Frequency of email domains** (e.g., `umich.edu`)
- ⏰ **Number of emails sent by hour** (e.g., `15:00`)

All using just:
- File handling
- String parsing
- Python dictionaries
- Sorting

---

## 🧪 Sample Input

Example line from the input log:
From zqian@umich.edu Fri Jan 4 15:03:18 2008

yaml
Copy
Edit

---

## ▶️ How to Run

```bash
python3 email_analyzer.py
When prompted:

cpp
Copy
Edit
Enter filename: mbox-short.txt
📈 Example Output
makefile
Copy
Edit
📤 Top Email Sender:
zqian@umich.edu: 2 emails

📨 Email Domain Counts:
umich.edu: 2
media.berkeley.edu: 1
uct.ac.za: 1
iupui.edu: 1

⏰ Emails Sent by Hour:
09:00 - 1 emails
15:00 - 2 emails
16:00 - 1 emails
18:00 - 1 emails
📁 File Structure
csharp
Copy
Edit
email-log-analyzer/
├── email_analyzer.py      # Main script
├── mbox-short.txt         # Sample input file
├── README.md              # This file
💡 Concepts Used
open(), readline(), split()

Dictionary .get() method

max() with key=

sorted()

Basic string slicing

🚀 Future Additions (Ideas)
Export results to .csv

Plot histogram of hourly emails using matplotlib

Accept file path via CLI argument

Handle large files with memory optimization

🎓 Inspired By
Python for Everybody - University of Michigan (Coursera)

🧑‍💻 Author
Param Singh
🔗 github.com/param-bioinfo

yaml
Copy
Edit

---

### ✅ To Add to GitHub

1. Save this in your local `README.md`
2. Commit and push:
```bash
git add README.md
git commit -m "Added detailed README with usage and output"
git push