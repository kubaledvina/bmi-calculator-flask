#  BMI Calculator Web App

A simple web application for calculating Body Mass Index (BMI), storing user data in a database, and visualizing statistics through charts and tables.

##  Project Structure
```
bmi_project/ 
├── app.py             # Main Flask application 
├── stats.py           # Module for data loading and BMI chart generation 
├── bmi_data.db        # SQLite database 
├── requirements.txt   # List of dependencies 
├── static/ 
│ ├── style.css        # CSS styling 
│ └── bmi_chart.png    # Generated BMI chart 
├── templates/ 
│ ├── index.html       # Homepage with input form 
│ ├── stats.html       # Page displaying BMI chart 
│ └── table.html       # Page displaying BMI data table 
└── .venv/ # Virtual environment (do not upload to GitHub)
```

##  Getting Started

Clone the repository:

``` bash
  git clone https://github.com/your_username/bmi_project.git
  cd bmi_project
```

Create and activate a virtual environment:


 **Linux / macOS**
```bash
  python3 -m venv .venv
  source .venv/bin/activate
```  
  **Windows**
```bash
  python -m venv .venv
  .venv\Scripts\Activate
``` 
  

Install dependencies:

``` bash
  pip install -r requirements.txt
```
Run the application:

``` bash
  python app.py
  Open your browser and go to: http://localhost:5000
```

## Features
- Calculate BMI from user input (age, height, weight)
- Store data in a SQLite database
- Visualize average BMI by age (bar chart)
- Display all recorded entries in a table

## Technologies Used
- Python 3
- Flask
- SQLite
- Matplotlib
- HTML & CSS

License
This project is licensed under the MIT License — feel free to use, modify, and share it.
