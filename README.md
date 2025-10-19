# 🧩Duplicate-File-Remover-Using-Hashing

## Before
<img width="652" height="446" alt="Screenshot 2025-10-19 125613" src="https://github.com/user-attachments/assets/d7262d62-3c51-4719-a713-4a6c4a0a45b7" />

## After 
<img width="631" height="268" alt="Screenshot 2025-10-19 125647" src="https://github.com/user-attachments/assets/62a8a5da-7733-4dab-8256-5abfd132af5b" />

This Python project automatically detects and optionally deletes duplicate files in a folder using hashing techniques.
Instead of comparing filenames, it compares the file contents using MD5 hash, ensuring accurate detection even if the names differ.

## It demonstrates:

* Practical use of hash functions in file management

* Implementation of set data structure for O(1) duplicate detection

* Exception handling and file I/O operations

* Use of the walrus operator (:=) in Python

## 🧠 Learning Outcomes

* What is hashing, and how to use it with Python’s hashlib module

* How to work with binary files (rb)

* How to use the walrus operator (:=)

* How to handle file path issues on Windows (double backslashes \\)

* Importance of closing files to avoid access errors

## ⚠️ Common Challenges Faced

###  File access error:
* The process cannot access the file because it is being used by another process.
*  Solved by ensuring file.close() after reading.

### Path issues:
* Use double backslashes \\ in folder paths.

### Binary mode:
* Always use "rb" for reading files like PDF/DOCX stored in bytes.

## Clone This Project 
``` bash
# 1️⃣ Clone the repository
git clone https://github.com/jayanthss/Duplicate-file-remover.git

# 2️⃣ Move into the project folder
cd Duplicate-file-remover

# 3️⃣ Run the Python script
python Remove_duplicate_files.py
```
