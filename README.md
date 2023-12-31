Exam Registration App Documentation
===================================

Table of Contents
-----------------

0.  [Updates And Timeline](#future-updates-and-timeline)
    *   [Version 1 Documentation](#version-1)
    *   [Version 2 Documentation](#version-2)
    *   [Version 3 GUI Version 2.0 Documentation](#version-3)
 <a name="version-1"></a>
----------------------------------
### Version 1:  [student_reg.py](https://github.com/stevehud23/student_reg/blob/main/student_reg.py)
*   This version contains a basic non GUI engineered to show the use of working with.
*   External data sources
*   Storing and Retrieving data
*   Edge cases 'Error Handling'

# Exam Registration System

## Introduction
The Exam Registration System is a Python program that allows users to register students for an exam. It provides an easy and efficient way to handle student registration, error checking, and file management. This documentation provides an overview of the code structure and instructions on how to use the program.

## Code Overview
The code is divided into three main functions:

### 1. `exam_reg()`
<img src="https://github.com/stevehud23/student_reg/blob/main/reg_v1.png " alt="image shows menu options of register app" style="width: 25%; height: auto;">
- This function handles the core functionality of student registration.
- It takes user input for the number of students to register (`name_count`).
- It performs error checks on user input, ensuring that the number of students is at least 2.
- It allows students to enter their IDs and stores them in the "reg_form.txt" file.
- It provides error handling for invalid student IDs.
- It offers options for users to access various functionalities.

### 2. `options()`
<img src="https://github.com/stevehud23/student_reg/blob/main/reg_v1_3.png " alt="image shows menu options of register app" style="width: 25%; height: auto;">
- This function provides a menu of options for users to choose from.
- Users can open and view the "reg_form.txt" and "error_log.txt" files.
- Users can clear the contents of the "reg_form.txt" and "error_log.txt" files.
- Users can reload the student registration process.
- It handles user input and error checking for valid options.

### 3. `main()`
- The `main()` function calls the `exam_reg()` function to initiate the program.

## How to Use
Follow these steps to use the Exam Registration System:

### Step 1: Run the Program
<img src="https://github.com/stevehud23/student_reg/blob/main/reg_v1.png " alt="image shows menu options of register app" style="width: 25%; height: auto;">
- Run the Python script containing the code.
- The program will start, and you will be prompted to enter the number of students to register.

### Step 2: Register Students
- Enter the number of students you want to register.
- You will be prompted to enter the student IDs for each student.
- The student IDs will be stored in the "reg_form.txt" file along with a signature line for each student.

### Step 3: Access Options
<img src="https://github.com/stevehud23/student_reg/blob/main/reg_v1_1.png " alt="image shows menu options of register app" style="width: 25%; height: auto;">
- After completing the registration, you will have the following options:
    - Option 1: Open and view the "reg_form.txt" file.
    - Option 2: Clear the contents of the "reg_form.txt" file.
    - Option 3: Open and view the "error_log.txt" file.
    - Option 4: Clear the contents of the "error_log.txt" file.
    - Option 5: Reload the student registration process.

### Step 4: Follow the Prompts
- Depending on your choice, follow the prompts to view, clear, or reload.
- The program will guide you through the selected option.

### Step 5: Continue or Quit
- After completing an option, you will be asked if you want to continue.
- Type 'y' to continue with another option or 'n' to quit the program.

## Big O Notation
The overall time complexity of the code can be expressed as O(m + n + k), where:
- "m" depends on the initial user input for class size.
- "n" depends on user input within the `options()` function.
- "k" depends on the file sizes involved in file read and write operations.

This code provides an efficient way to manage exam registrations and handle file operations.

---

**Note**: Make sure that the program files, "reg_form.txt" and "error_log.txt," exist in the same directory as the Python script for the program to function correctly.

For any questions or issues, refer to the error logs or seek assistance.

Happy registration!

<a name="version-2"></a>
### Version 2:  [from_kivy_registration.py](https://github.com/stevehud23/student_reg/blob/main/registration/from_kivy_registration.py)
*   This version contains a basic GUI engineered to show the use of working with.
*   Basic level GUI creation
*   OOP's
*   Classe's
*   Function's
*   Inheritance
*   Creating and printing a custom registry form
*   External data sources
*   Storing and Retrieving data
*   Edge cases 'Error Handling'
  
Exam Registration App Documentation
===================================

Table of Contents
-----------------

1.  [Introduction](#introduction-1)
2.  [Getting Started](#getting-started-1)
    *   [Prerequisites](#prerequisites-1)
    *   [Installation](#installation-1)
3.  [User Manual](#user-manual-1)
    *   [Application Overview](#application-overview-1)
    *   [Registering Students](#registering-students-1)
    *   [Options Menu](#options-menu-1)
    *   [Printing Registration Forms](#printing-registration-forms-1)
4.  [Troubleshooting](#troubleshooting-1)
5.  [Contributing](#contributing-1)
6.  [License](#license-1)
7.  [Future Updates And Timeline](#future-updates-and-timeline-1)
    *   [Version 1 Documentation](#version-1)
    *   [Version 2 Documentation](#version-2)
    *   [Version 3 GUI Version 2.0 Documentation](#version-3)

1\. Introduction <a name="introduction-1"></a>
--------------------------------------------

The Exam Registration App is a simple Kivy-based application that allows you to register students for an exam, view registration logs, clear logs, and print registration forms. This documentation provides an overview of the application and how to use it.

2\. Getting Started <a name="getting-started-1"></a>
--------------------------------------------------

### Prerequisites <a name="prerequisites-1"></a>

Before running the Exam Registration App, you need to have the following prerequisites installed on your system:

*   Python (3.x recommended)
*   Kivy library
*   ReportLab library (for PDF generation)

### Installation <a name="installation-1"></a>

1.  Clone the application's repository to your local machine:
    
    bash
    
    ```bash
    git clone https://github.com/yourusername/exam-registration-app.git
    ```
    
2.  Navigate to the project directory:
    
    bash
    
    ```bash
    cd exam-registration-app
    ```
    
3.  Install the required Python packages using pip:
    
    `pip install -r requirements.txt`
    
4.  Run the application:
    
    `python from_kivy_registration.py`
    

3\. User Manual <a name="user-manual-1"></a>
------------------------------------------

### Application Overview <a name="application-overview-1"></a>

The Exam Registration App provides a simple and user-friendly interface for registering students, managing registration logs, and printing registration forms. When you launch the app, you will see the following components:

<img src="https://github.com/stevehud23/student_reg/blob/main/ex_reg1.png " alt="image shows menu options of register app" style="width: 25%; height: auto;">

*   **Register Students Button**: Click this button to open the registration form for entering student information.
    
*   **Options Button**: Access the options menu to view, clear registration logs, view error logs, and clear error logs.         
    
*   **Output Label**: This label displays messages and information about the registration process.
    
*   **Print Registration Form Button**: Click this button to generate and print the registration forms for all registered students.
    

### Registering Students <a name="registering-students-1"></a>

<img src="https://github.com/stevehud23/student_reg/blob/main/ex_reg2.png " alt="image shows menu options of register app" style="width: 25%; height: auto;"><img src="https://github.com/stevehud23/student_reg/blob/main/ex_reg3.png " alt="image shows menu options of register app" style="width: 25%; height: auto;">

1.  Click the "Register Students" button to open the registration form.
    
2.  In the registration form popup:
    
    *   Enter the student's name in the "Enter student name" field.
    *   Enter the student's ID in the "Enter student number" field only.
    *   Click the "Submit" button to register the student.
3.  If the student's information is successfully registered, you will see a confirmation message in the "Output Label."
    
4.  If there is an error or if the student is already registered, appropriate messages will be displayed in the "Output Label."
    

### Options Menu <a name="options-menu-1"></a>

<img src="https://github.com/stevehud23/student_reg/blob/main/ex_reg4.png " alt="image shows menu options of register app" style="width: 25%; height: auto;">

Click the "Options" button to access the options menu, which provides the following features:

*   **View Registration Log**: Opens a popup displaying the registration log. You can scroll through the log to view registered students.<img src="https://github.com/stevehud23/student_reg/blob/main/ex_reg5.png " alt="image shows menu options of register app" style="width: 25%; height: auto;">
    
*   **Clear Registration Log**: Clears the registration log, removing all previously registered students.
    
*   **View Error Log**: Opens a popup displaying the error log. You can scroll through the log to view any error messages. <img src="https://github.com/stevehud23/student_reg/blob/main/ex_reg6.png " alt="image shows menu options of register app" style="width: 25%; height: auto;">
    
*   **Clear Error Log**: Clears the error log, removing all previous error messages.
    

### Printing Registration Forms <a name="printing-registration-forms-1"></a>

<img src="https://github.com/stevehud23/student_reg/blob/main/ex_reg7.png " alt="image shows menu options of register app" style="width: 25%; height: auto;">

1.  Click the "Print Registration Form" button to generate and print registration forms for all registered students.
    
2.  A PDF registration form will be generated, and the default PDF viewer on your system will open, allowing you to print the forms.
    

4\. Troubleshooting <a name="troubleshooting-1"></a>
--------------------------------------------------

If you encounter any issues or errors while using the Exam Registration App, please check the following:

*   Ensure that you have the required prerequisites (Python, Kivy, and ReportLab) installed correctly.
    
*   Check the "Options" menu to view error logs for detailed error messages.
    
*   If you encounter any unexpected behavior or issues, please report them to the application's GitHub repository for assistance.
    

5\. Contributing <a name="contributing-1"></a>
--------------------------------------------

Contributions to the Exam Registration App are welcome! If you have ideas for new features or improvements, feel free to open an issue or submit a pull request on the GitHub repository.

6\. License <a name="license-1"></a>
----------------------------------

The Exam Registration App is open-source and released under the [MIT License](LICENSE). You are free to use, modify, and distribute the application as per the terms of the license.

Thank you for using the Exam Registration App!

<a name="version-3"></a>
 ### GUI version 2.0:  [student_reg_GUI_V2.py](https://github.com/stevehud23/student_reg/blob/main/Student_reg_GUI_V2/student_reg_GUI_V2.py)
*   This version contains an updated GUI engineered for better functionalty.
*   Basic level GUI creation
*   OOP's
*   Classe's
*   Function's
*   Inheritance
*   Creating and printing a custom registry form
*   External data sources
*   Storing and Retrieving data
*   Edge cases 'Error Handling'


Exam Registration App Documentation
===================================

Table of Contents
-----------------

1.  [Introduction](#introduction-2)
2.  [Getting Started](#getting-started)
    *   [Prerequisites](#prerequisites)
    *   [Installation](#installation)
3.  [User Manual](#user-manual)
    *   [Application Overview](#application-overview)
    *   [Registering Students](#registering-students)
    *   [Options Menu](#options-menu)
    *   [Printing Registration Forms](#printing-registration-forms)
4.  [Troubleshooting](#troubleshooting)
5.  [Contributing](#contributing)
6.  [License](#license)
7.  [Future Updates And Timeline](#future-updates-and-timeline)
    *   [Version 1 Documentation](#version-1)
    *   [Version 2 Documentation](#version-2)
    *   [Version 3 GUI Version 2.0 Documentation](#version-3)

1\. Introduction <a name="introduction"></a>
--------------------------------------------

The Exam Registration App is a simple Kivy-based application that allows you to register students for an exam, view registration logs, clear logs, and print registration forms. This documentation provides an overview of the application and how to use it.

2\. Getting Started <a name="getting-started"></a>
--------------------------------------------------

### Prerequisites <a name="prerequisites"></a>

Before running the Exam Registration App, you need to have the following prerequisites installed on your system:

*   Python (3.x recommended)
*   Kivy library
*   ReportLab library (for PDF generation)

### Installation <a name="installation"></a>

1.  Clone the application's repository to your local machine:
    
    bash
    
    ```bash
    git clone https://github.com/yourusername/exam-registration-app.git
    ```
    
2.  Navigate to the project directory:
    
    bash
    
    ```bash
    cd exam-registration-app
    ```
    
3.  Install the required Python packages using pip:
    
    `pip install -r requirements.txt`
    
4.  Run the application:
    
    `python from_kivy_registration.py`
    

3\. User Manual <a name="user-manual"></a>
------------------------------------------

### Application Overview <a name="application-overview"></a>

The Exam Registration App provides a simple and user-friendly interface for registering students, managing registration logs, and printing registration forms. When you launch the app, you will see the following components:

<img src="https://github.com/stevehud23/student_reg/blob/main/reg_gui_v2_5.png " alt="image shows menu options of register app" style="width: 25%; height: auto;">

*   **Register Students Button**: Click this button to open the registration form for entering student information.
    
*   **Options Button**: Access the options menu to view, clear registration logs, view error logs, and clear error logs.         
    
*   **Output Label**: This label displays messages and information about the registration process.
    
*   **Print Registration Form Button**: Click this button to generate and print the registration forms for all registered students.
    

### Registering Students <a name="registering-students"></a>

<img src="https://github.com/stevehud23/student_reg/blob/main/reg_gui_v2.png" style="width: 25%; height: auto;"><img src="https://github.com/stevehud23/student_reg/blob/main/reg_gui_v2_3.png " alt="image shows menu options of register app" style="width: 25%; height: auto;">

1.  Click the "Register Students" button to open the registration form.
    
2.  In the registration form popup:
    
    *   Enter the student's name in the "Enter student name" field.
    *   In this version the student ID auto generates the student ID's, making this app a bit more realistic.
    *   Click the "Submit" button to register the student.
3.  If the student's information is successfully registered, you will see a confirmation message in the "Output Label."
    
4.  If there is an error or if the student is already registered, appropriate messages will be displayed in the "Output Label."
    

### Options Menu <a name="options-menu"></a>

<img src="https://github.com/stevehud23/student_reg/blob/main/reg_gui_v2_1.png " alt="image shows menu options of register app" style="width: 25%; height: auto;">

Click the "Options" button to access the options menu, which provides the following features:

*   **View Registration Log**: Opens a popup displaying the registration log. You can scroll through the log to view registered students.<img src="https://github.com/stevehud23/student_reg/blob/main/ex_reg5.png " alt="image shows menu options of register app" style="width: 25%; height: auto;">
    
*   **Clear Registration Log**: Clears the registration log, removing all previously registered students.
    
*   **View Error Log**: Opens a popup displaying the error log. You can scroll through the log to view any error messages. <img src="https://github.com/stevehud23/student_reg/blob/main/ex_reg6.png " alt="image shows menu options of register app" style="width: 25%; height: auto;">
    
*   **Clear Error Log**: Clears the error log, removing all previous error messages.
    

### Printing Registration Forms <a name="printing-registration-forms"></a>

<img src="https://github.com/stevehud23/student_reg/blob/main/ex_reg7.png " alt="image shows menu options of register app" style="width: 25%; height: auto;">

1.  Click the "Print Registration Form" button to generate and print registration forms for all registered students.
    
2.  A PDF registration form will be generated, and the default PDF viewer on your system will open, allowing you to print the forms.
    

4\. Troubleshooting <a name="troubleshooting"></a>
--------------------------------------------------

If you encounter any issues or errors while using the Exam Registration App, please check the following:

*   Ensure that you have the required prerequisites (Python, Kivy, and ReportLab) installed correctly.
    
*   Check the "Options" menu to view error logs for detailed error messages.
    
*   If you encounter any unexpected behavior or issues, please report them to the application's GitHub repository for assistance.
    

5\. Contributing <a name="contributing"></a>
--------------------------------------------

Contributions to the Exam Registration App are welcome! If you have ideas for new features or improvements, feel free to open an issue or submit a pull request on the GitHub repository.

6\. License <a name="license"></a>
----------------------------------

The Exam Registration App is open-source and released under the [MIT License](LICENSE). You are free to use, modify, and distribute the application as per the terms of the license.

Thank you for using the Exam Registration App!



---

This documentation provides an overview of the Exam Registration App and its usage. For more details about the code implementation, refer to the source code and comments in the application's Python script.
