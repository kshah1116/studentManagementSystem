# studentManagementSystem
I have developed a Student Management System using Python for the backend, Tkinter for the graphical user interface, and MySQL for efficient data storage. The primary goal of this project was to streamline the management of student and teacher information within an educational institution. By automating tasks such as mark calculations and providing an organized platform for administrators, teachers, and students, the system enhances efficiency and accuracy in educational administration.

The system features three distinct login portals: one for administrators, one for teachers, and one for students. This separation ensures that each user type has access only to relevant functions and data. 

Administrators can perform various tasks, such as looking up detailed information about teachers, including the subjects they teach, the classes they handle, and their contact details. They can also access class-specific information, which includes a list of students along with their roll numbers, names, and contact information. Additionally, administrators have the ability to add new users as needed, maintaining system security.

Teachers can log in to manage specific tasks, primarily entering and updating students' marks or grades. The system uses Python-based internal logic to automatically calculate the final marks for each student, reducing the burden of manual computations.

Students have their own dedicated login portal where they can view their marks or grades, allowing them to track their academic progress over time.

**Components:**
<br/>

· Frontend (User Interface) - Tkinter:

Login Screen: A secure login interface for administrators and teachers to access the system.
Forms and Tables: Interactive forms for adding, updating, and deleting student records, and tables for viewing student data.

· Backend (Database) - MySQL:

Database Schema: Tables to store student information, including personal details, academic records, attendance, and any other relevant data.
SQL Queries: SQL commands to perform CRUD (Create, Read, Update, Delete) operations on the student data.

· Backend (Logic) - Python:

Database Connectivity: Using libraries like mysql-connector-python to connect Python with the MySQL database.
Data Processing: Scripts to handle user inputs, process data, and interact with the database.
Validation and Error Handling: Ensuring data integrity and providing feedback for incorrect or incomplete data entries.
