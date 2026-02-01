# Error Handling and Debugging Using Logging in Python

## 📌 Aim
To demonstrate error handling in Python using try-except blocks, handle multiple exceptions, use else and finally, log errors using the logging module, save logs to a file, simulate runtime errors, and debug the program using logs.

---

## 📁 Files in the Project
- `error_handling.py` – Main Python program
- `error_log.log` – Log file generated during execution
- `README.md` – Project documentation

---

## 🛠 Tools Used
- Python 3.x
- VS Code
- logging module

---

## 📖 Description
This program demonstrates:
- Use of `try-except` for exception handling
- Handling multiple exceptions (`ZeroDivisionError`, `TypeError`)
- Use of `else` and `finally` blocks
- Custom error messages
- Logging errors and debug messages
- Saving logs to a file
- Simulating runtime errors
- Debugging the program using log files

---

## ⚙ Program Flow
1. Configure logging to save logs in `error_log.log`
2. Perform operations that may cause runtime errors
3. Handle exceptions using multiple `except` blocks
4. Display user-friendly custom error messages
5. Log detailed error information for debugging
6. Ensure execution completion using `finally`

---

## ▶ How to Run the Program
1. Open VS Code
2. Create a file named `error_handling.py`
3. Paste the program code
4. Run the program using:
   ```bash
   python error_handling.py
Check the terminal output

Open error_log.log to view debug and error logs

✅ Sample Output
Program Started... Check error_log.log for logs

Custom Error: Cannot divide by zero
Execution completed

Custom Error: Invalid data type used
Execution completed

🧪 Exceptions Handled

ZeroDivisionError

TypeError

Generic Exception

📄 Conclusion

This program successfully demonstrates Python error handling and debugging using logging. It improves program reliability and helps developers identify and fix runtime issues efficiently.
