# Grade Progression Outcome Predictor :school:

## Overview
This is a program that predicts the progression outcome based on the grade credits earned in different modules 'Pass', 'Defer', and 'Fail'. Subsequently, a histogram will appear showing all the results of each student entered, with each bar being colour-coded to their progression outcome. The total credits calculated are predefined conditions which can be found below.

Note  :warning: The program assumes that the user provides valid input within the specified credit ranges below.

![progressionoutcomes2](https://github.com/Bev0408/Weather-program/assets/151802057/a644faaf-fbd8-4b46-8d34-e56d8ce07190)


## Features 💡
- **Histogram visualization:** Utileses the **'graphics'** library by displaying a graphical histogram after the user decided not to predict another outcome, showing all overall results in colour-coded bars.
  
- **Stored Progression Data:** The program prints the stored progression data after the program's main loop has ended, allowing users to view all the outcomes they received.

- **Input collection:** The program continues to collect information from the user to predict the progression outcome of multiple students through the use of a while loop. Collectively the credits input by the user should equal '120'. 


## Functions ✔️

The program itself revolves around two main user-defined functions. 

### 1. show_progression(pass_credits, defer_credits, fail_credits)
This function takes the three arguments represented at the pass, defer and fail credits and checks if the values match any of the predefined values in the table shown above. The outcome is then returned to the user as a string. if the credit values don't match any of the predefined outcomes, the program will display **'outcome not defined'**.


### 2. get_input(message, valid_range)
This function is mainly used for handling input errors and will prompt the user to keep trying again  until a **valid integer** within the correct **credit ranges** is inputted.
  
## Dependencies🚀

* The program relies on the **'graphics'** library for creating the graphical histogram. Ensure it's installed before running the program.
   
Install dependencies: `pip install graphics.py`
   
## How To Use Program 🗒️
1. Run the application.
2. Input the credits for Pass, Defer, and Fail when prompted.
3. After the outcome is displayed, decide whether to predict another outcome or exit the program.
4. After the loop has been ended, a graphical histogram will appear displaying data for all the students collectively
5. The stored progression data is printed at the end.
   
## Error handling :warning:
* If progression credits don't add up to 120, the user will be prompted told the total is **'incorrect'** and prompted to re-enter the values. 

* If one or more of the credits entered aren't either 0,20,40,60,80,100 or 120 user will be told that values are **'out of range'** and promised to try again.

* If the values entered when prompted aren't valid integers the program will display **'Integer required. Try again.'** and will then be prompted to retry.

## Licence 📜

This project is licenced under the [MIT License](LICENCE).
