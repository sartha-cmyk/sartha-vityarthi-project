AQI Monitoring System – Project Documentation

1. Real World Problem - Rising AQI and Air Pollution :-

Air pollution is one of the most critical environmental issues globally. Millions of people live in
areas where Air Quality Index (AQI) levels frequently exceed safe limits, causing respiratory
diseases, reduced life expectancy, and environmental damage. However, many people are
unaware of daily AQI variations and how they impact health. There is a need for a simple,
user-friendly tool that allows individuals to monitor air quality, understand patterns, and
identify unsafe days quickly.

2. Objectives and Expected Outcomes :-

Objectives :

● To design a Python-based system that collects and analyzes daily AQI data.

● To calculate the average AQI.

● To classify air quality into standard AQI categories.

● To identify days with unsafe pollution levels.

● To help users understand pollution trends and take preventive actions.

Expected Outcomes :

● A working Python program that: Accepts AQI values as input, Uses lists and loops for data processing, Computes average AQI, Displays weekly/daily AQI summary, Detects the most polluted day, Finds days exceeding a pollution threshold

● Users gain insights into pollution exposure and potential health risks.

3. Applied Concepts Learned in the Class to Design the Solution :-

● Lists used to store AQI values

● Functions used to perform modular and reusable calculations

● Loops and iterative statements used to gather user input and evaluate conditions

● Conditional statements used to classify the AQI

● User input handling used for dynamic data collection

● Problem-solving and structured programming techniques

4. Usage of Appropriate Tools and Programming Techniques :-

The project uses only the Python Standard Library. Key techniques include:

● Modular programming (functions)

● Iterative input collection (loops)

● List-based data storage

● Conditional logic for AQI categorization

● Console-based user interaction.

5. Follow a Structured Development Process :-

A. Problem Definition :

Air pollution levels vary significantly from day to day. Without a monitoring tool, individuals
cannot easily track AQI fluctuations. A simple system is needed to input AQI values, analyze
trends, and determine how safe the air is over a given period.

B. Requirement Analysis :

● The system must accept AQI inputs for n days.

● It must calculate : Total values, Average AQI, Highest (worst) AQI day

● It must classify AQI based on established health standards.

● It must detect days exceeding a user-defined AQI threshold.

● It must display results in a structured format.

● Should be simple and user-friendly.

● Must run on any system with Python installed.

● Code must be readable, modular, and maintainable.

C. Top-Down Design and Modularization :

Main Modules -

1. Input Module = Collects AQI values from the user using loops.

2. Processing Module = calculate_average() function computes average AQI. Logic for
highest AQI detection.Threshold-based filtering.

3. Output Module = Displays summary, Shows AQI category, Lists polluted days

Top-Down Approach -

● Begin with the main problem: "Monitor and analyze AQI"

● Break into smaller tasks:
○ Input → Processing → Analysis → Output

● Implement each component step-by-step.

D. Algorithm Development :

Algorithm: AQI Monitoring System -

1. Start
2. Ask user for number of days
3. Initialize an empty list aqi_values
4. Use a loop to input AQI for each day and append to list
5. Call calculate_average(aqi_values)
6. Compute average AQI
7. Determine AQI category using conditional statements
8. Find max AQI and its day index
9. Ask user for a threshold
10. Loop through list to identify days exceeding threshold
11. Display all results
12. End

Algorithm: calculate_average() Function -

1. Accept list as parameter
2. Initialize total = 0
3. Loop through each AQI value
4. Add to total
5. Divide total by number of elements
6. Return result

E. Implementation :

● Uses lists for data storage
● Uses loops for input and analysis
● Uses a function for average calculation
● Uses conditional statements for AQI classification

F. Testing and Refinement :

Test Cases -

1) Input :- AQI: 50, 60, 40 | Output :- Average = 50; Category = Good/Satisfactory
2) Input :- AQI: 120, 150, 200 | Output :- Average = Moderate/Poor
3) Input :- Threshold = 100 | Output :- Days above threshold identified
4) Input :- Highest AQI = 280 | Output :- Displays correct worst day

Refinement Activities -

● Improved category descriptions

● Added threshold-based analysis

● Enhanced textual output formatting

● Ensured code readability and modularity
