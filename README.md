# Email Log Analyzer

A beginner-friendly Python project to analyze email logs from `.txt` files.  
Built after completing the **Python for Everybody** course by Dr. Charles Severance.

---

## Project Description

This script reads a plain-text email log file (like `mbox-short.txt`) and extracts:

- **Top email senders**
- **Frequency of email domains** (e.g., `umich.edu`)
- **Number of emails sent by hour** (e.g., `15:00`)

All using just:
- File handling
- String parsing
- Python dictionaries
- Sorting

---

## Sample Input

Example line from the input log: From zqian@umich.edu Fri Jan 4 15:03:18 2008

---

## How to Run

```bash
python3 email_analyzer.py
When prompted:


Enter filename: mbox-short.txt
```
---
## Example Output
```bash
Top Email Sender:
cwen@iupui.edu: 5 emails

Email Domain Counts:
iupui.edu: 8
umich.edu: 7
uct.ac.za: 6
media.berkeley.edu: 4
caret.cam.ac.uk: 1
gmail.com: 1

Emails Sent by Hour:
04:00 - 3 emails
06:00 - 1 emails
07:00 - 1 emails
09:00 - 2 emails
10:00 - 3 emails
11:00 - 6 emails
14:00 - 1 emails
15:00 - 2 emails
16:00 - 4 emails
17:00 - 2 emails
18:00 - 1 emails
19:00 - 1 emails
```
---

## File Structure
```bash
email-log-analyzer/
├── email_analyzer.py   
├── mbox-short.txt         
├── README.md
```
---        
## Concepts Used
open(), readline(), split()

Dictionary .get() method

max() with key=

sorted()

Basic string slicing

---
## Inspired By
Python for Everybody - University of Michigan (Coursera)
---
## Author
Param Singh
🔗 github.com/param-bioinfo

