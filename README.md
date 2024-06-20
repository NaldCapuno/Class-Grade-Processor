# Class Records Processor
This Python program processes a CSV file containing class records and provides statistical insights, including the average, highest, and lowest grades of the class. It also identifies the students with the highest and lowest grades.

## Features
- Calculate the average grade of the class.
- Determine the highest and lowest grades in the class.
- Identify the students who achieved the highest and lowest grades.

## How to use
**Prerequisites**

Make sure you have Python installed on your system. You can download it from [python.org](www.python.org).

1. Create a new folder on your computer.
2. Download the Python file **grade_processor.py** and put it into the folder.
3. Place your CSV file containing class records into the folder and rename it to classRecord.csv.

The classRecord.csv should have the following format (name, grade):
```csv
John Doe,85
Jane Smith,92.5
...
```

4. Open a terminal or command prompt, navigate to the folder where your script and CSV file are located, and run:
```bash
python grade_processor.py
```

## Sample Output
```text
Average grade of the class: 88.8
Highest class score: 92.5
Lowest class score: 85.0

Name of students who earned the highest score:
1. Jane Smith

Name of student/s who earned the lowest score:
1. John Doe
```
