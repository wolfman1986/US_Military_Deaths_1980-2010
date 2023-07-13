# US_Military_Deaths_1980-2010
Python Data Science Midterm Project

## Overview
This project analyzes a dataset obtained from www.kaggle.com, which contains a historical numerical record of all U.S. military deaths from 1980 to 2010. The objective of the analysis was to develop visual charts based on the data points and provide insights into trends and patterns observed in the dataset.

## Project Details
Dataset: The dataset contains information on U.S. military fatalities, including columns such as Calendar Year, Total Military FTE, Total Deaths, Accident, Hostile Action, Homicide, Illness, Self-Inflicted, and Terrorist Attack.

## Questionnaire and Analysis
### 1. Main Objective
The main objective of the analysis was to develop visual charts based on the data points and provide a generalized observation of trends in U.S. military fatalities. The analysis aimed to explore trends related to specific conflicts, economic activity, military force restructuring, program implementation, medical treatment, and other factors.

### 2. Visualizations and Observations

a. Line plot showing year-by-year changes in total military strength.
![total_mil_strength_line](https://github.com/wolfman1986/US_Military_Deaths_1980-2010/assets/36992236/0090d61a-7460-4f7d-95a3-1071e98c6a94)


#### Observed a steep decline in total military strength from the 1980s to the lowest level in 1999, followed by a slight increase in the following decade due to the war on terror.

b. Three doughnut charts illustrating force distribution in 1980, 1990, and 2010.

![1980_pop_doughnut](https://github.com/wolfman1986/US_Military_Deaths_1980-2010/assets/36992236/ab0d7199-b18d-43f3-acb4-37915dc2ee96)

![1990_pop_doughnut](https://github.com/wolfman1986/US_Military_Deaths_1980-2010/assets/36992236/88a92063-bbd2-413e-aa3a-78c999ec7f8a)

![2010_pop_doughnut](https://github.com/wolfman1986/US_Military_Deaths_1980-2010/assets/36992236/d7200b56-09fe-4304-b5e9-370497bae488)

### Noted a decrease in the percentage of active duty force and an increase in Guard and Reserve components from 1980 to 2010.

c. Doughnut chart representing the categorical breakdown of U.S. military fatalities.

![fatality_category_breakdown](https://github.com/wolfman1986/US_Military_Deaths_1980-2010/assets/36992236/de24ef2e-0290-49d0-a8d9-fd8690d1859b)

### Found that accidents accounted for the majority (52.10%) of all fatalities, followed by illnesses, self-inflicted incidents, hostile actions, homicides, and terrorist attacks.

d. Line charts representing trends in different categories of fatalities per 100,000 soldiers.

![accident_line](https://github.com/wolfman1986/US_Military_Deaths_1980-2010/assets/36992236/75806fa6-aa39-4e50-969b-1b820396409f)

![homicide_line](https://github.com/wolfman1986/US_Military_Deaths_1980-2010/assets/36992236/3e983c36-ce27-4b28-a237-848bdb9e4204)

![hostile_action_line](https://github.com/wolfman1986/US_Military_Deaths_1980-2010/assets/36992236/3a665f59-762d-48e1-8dbf-7c7ba073937c)

![illness_line](https://github.com/wolfman1986/US_Military_Deaths_1980-2010/assets/36992236/646e0a7d-3612-4805-be9c-8f41f83ca968)

![self_infliected_line](https://github.com/wolfman1986/US_Military_Deaths_1980-2010/assets/36992236/fc208382-0d72-494d-89b0-f9c6dcb0128a)

![terrorist_attacks_line](https://github.com/wolfman1986/US_Military_Deaths_1980-2010/assets/36992236/eb7eb48b-0606-4e22-85d5-93ec6e9fc8e6)

Accidents and illnesses showed significant decreases over time.
Self-inflicted incidents had spikes in the mid-1980s, 1996, and during the late 2000s.
Hostile actions had significant events, such as the 1983 Beirut Barracks Bombing and the War on Terror.
Homicides had fluctuations with a spike in the early 1990s and a sharp decline afterward.
Terrorist attacks had spikes associated with notable incidents such as the Beirut U.S. Embassy Bombing, Oklahoma City Bombing, USS Cole Bombing, and the September 11th attacks.

e. Bar charts showing the average annual decrease in fatalities per 100,000 soldiers over 10-year periods.

![total_deaths_avg](https://github.com/wolfman1986/US_Military_Deaths_1980-2010/assets/36992236/cece1bc3-9408-42e4-8460-758043409e64)

### Accident deaths showed a decreasing trend over the three 10-year time periods.

![accident_decrease_bar](https://github.com/wolfman1986/US_Military_Deaths_1980-2010/assets/36992236/c4f67f3b-9206-4e7a-99c9-956d473cf7de)

### Self-inflicted deaths had minimal decreases in the 1980s, a rise in the early 1990s, a sharp drop in the late 1990s, and a final spike in the late 2000s.

![self_inflicted_10_year](https://github.com/wolfman1986/US_Military_Deaths_1980-2010/assets/36992236/be98b8b0-135a-4269-b269-0c2a59c3bb13)

3. Data Visualization Techniques

### Various data visualization techniques were employed:

Line plots to show year-by-year changes.
Doughnut charts to illustrate force distribution and categorical breakdown.
Line charts to represent trends over time.
Bar charts to show changes over time periods.
Visualization choices were made to ensure an accurate representation of the data and effectively highlight trends.

### 4. Data Preprocessing and Cleaning

The dataset was already well-structured, with no missing values. However, some column names had leading or trailing whitespaces, which were removed using the .strip() method.

### 5. Challenges Faced

The challenges during the analysis included determining the story to tell based on the available data, minimizing wasted space in the graphs, and calculating accurate representations of data through ratioed calculations.

### 6. Key Findings

The most significant finding was the significant decline in the rate of fatal accidents from 1980 to 2010. This decrease can be attributed to safety programs, enhanced military training, protective equipment, policy implementation, and cultural shifts.

### 7. Interpretation and Utilization of Results

The results provide historical insights into the U.S. military population, culture, and the impact of various factors on the statistical data. They can be used to understand changes in military operations, policy initiatives, training, technology adoption, and demographic shifts over time.

Running the Code

To run the code for this analysis:

Make sure you have Python and the required dependencies installed.
Download the dataset from www.kaggle.com and place it in the same directory as the code.
Run the Python script to execute the analysis and generate the visualizations.

Additional Notes

The code provided is for reference purposes only and may require adjustments based on your specific environment and dataset.
Feel free to modify the code or adapt it to suit your requirements.
Make sure to provide appropriate credits and references for the dataset used in your analysis.
Enjoy analyzing the U.S. military fatalities dataset!
