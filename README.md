<div align="center">
    <h1>Fitness Tracker</h1>
    <img width="250" src="resources/images/fitness-tracker-logo.png" alt="Fitness Tracker logo">
</div>

# Fitness Tracker v1.0

> [!NOTE]  
> Fitness Tracker is an open-source project developed in Python using Tkinter. It helps users calculate calories burned during exercises like walking and running.

## Features

- User-friendly interface built with Tkinter.
- Supports calorie calculation for:
  - Walking
  - Running
- Provides instant results after inputting data.
- Lightweight and fast to execute.

## Installation [Development Mode]

> [!IMPORTANT]  
> Ensure you have Python 3.7+ installed along with Tkinter (pre-installed with Python). Clone the repository and run the script:

```bash
git clone https://github.com/your-repository/fitness-tracker.git
cd fitness-tracker
python fitness_tracker.py
```

## Usage Instructions

1. Launch the application:
   ```bash
   python fitness_tracker.py
   ```
2. Follow these steps:
   - Select the type of exercise (`Walking` or `Running`).
   - Enter your weight in kilograms.
   - Enter the duration of the exercise in hours.
   - Click "คำนวณ" (Calculate) to get the results.

## Example

- **Input**:
  - Exercise Type: Walking
  - Weight: 70 kg
  - Duration: 2 hours
- **Output**:
  - Calories Burned: `532.00 kcal`

## Formulae

- **Walking**: `Calories = Duration (hours) × Weight (kg) × 3.8`
- **Running**: `Calories = Duration (hours) × Weight (kg) × 9.8`

## Requirements

- Python 3.7 or higher
- Tkinter (pre-installed with Python)

## Optimize for Production Mode

To package the application into a standalone executable:
1. Install `pyinstaller`:
   ```bash
   pip install pyinstaller
   ```
2. Create the executable:
   ```bash
   pyinstaller --onefile fitness_tracker.py
   ```
3. Distribute the executable file located in the `dist/` directory.

## Future Improvements

- Add more types of exercises with adjustable calorie burn rates.
- Extend support for multiple languages.
- Enhance the UI/UX design with advanced Tkinter widgets.
- Add functionality to save and track user progress.

## Project Structure

```
fitness-tracker/
│
├── fitness_tracker.py    # Main application script
└── README.md             # Project documentation
```

## Screenshots

<div align="center">
    <img width="400" src="resources/screenshots/fitness-tracker-ui1.png" alt="Screenshot 1">
    <img width="400" src="resources/screenshots/fitness-tracker-ui2.png" alt="Screenshot 2">
</div>

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

<p align="center">
    Developed With ❤️ by [Your Name or Team Name]
</p>

