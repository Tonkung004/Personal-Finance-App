# Personal-Finance-App
Fitness Tracker
Overview
Fitness Tracker is a Python application with a Tkinter-based graphical user interface (GUI) that calculates calories burned during physical activities such as walking and running. Users can input their weight and exercise duration to see the estimated energy expenditure.

Features
Calculate calories burned for:
Walking
Running
User-friendly interface with intuitive input fields.
Instant feedback on calories burned after providing the required details.
Prerequisites
Python 3.7 or higher installed on your system.
Tkinter library (bundled with Python by default).
Installation
Clone this repository or download the code file:
bash
Copy code
git clone https://github.com/your-repository/fitness-tracker.git
Navigate to the project directory:
bash
Copy code
cd fitness-tracker
Usage
Run the application:
bash
Copy code
python fitness_tracker.py
Follow these steps:
Select the exercise type (Walking or Running).
Enter your weight in kilograms.
Enter the duration of the activity in hours.
Click "คำนวณ" (Calculate) to see the calories burned.
Example
Input:
Exercise Type: Running
Weight: 70 kg
Duration: 1 hour
Output:
Calories Burned: 686.00 kcal
Formulae
Walking: Calories = Duration (hours) × Weight (kg) × 3.8
Running: Calories = Duration (hours) × Weight (kg) × 9.8
Project Structure
bash
Copy code
fitness-tracker/
│
└── fitness_tracker.py    # Main application script
Future Improvements
Add more exercise types with customizable calorie burn rates.
Include user profiles for tracking progress.
Extend support for additional languages and units.
License
This project is licensed under the MIT License. See the LICENSE file for more information.

Acknowledgments
Developed using Python and Tkinter for the GUI.
