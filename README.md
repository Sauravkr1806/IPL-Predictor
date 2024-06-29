# IPL-Winner-Predictor
A machine learning project to find out the win probability of team in the IPL matches based on the current situation and deployed on flask web as the backend.This model analyzes various match features, team performance, and player statistics to offer real-time predictions.For the more infromation about the ipl,[Click Here ](https://en.wikipedia.org/wiki/Indian_Premier_League).

# About This Project
The "IPL Predictor" leverages logistic regression to provide insights into the probability of a team winning an IPL match. This model analyzes various match features, team performance, and player statistics to offer real-time predictions.

# Run On Terminal 
Mozilla-Firefox 

# Table Content

[Introduction](https://github.com/Sauravkr1806/IPL-Predictor?tab=readme-ov-file#introduction).

[Dataset](https://github.com/Sauravkr1806/IPL-Predictor?tab=readme-ov-file#Dataset)

[ShowCase](https://github.com/Sauravkr1806/IPL-Predictor?tab=readme-ov-file#showcase).

[Usage](https://github.com/Sauravkr1806/IPL-Predictor?tab=readme-ov-file#Usage).

[Technologies_Used](https://github.com/Sauravkr1806/IPL-Predictor?tab=readme-ov-file#Technologies_Used).

[Conclusion](https://github.com/Sauravkr1806/IPL-Predictor?tab=readme-ov-file#Conclusion).

# Introduction
IPL match analysis using that data from all the IPL matches from the beginning till date. Our main motive is to predict the batting team probability and the losing team probability based on score and the match situation.

# Dataset
The dataset has been obtained from the repository [Indian Premier League (Cricket)](https://www.kaggle.com/manasgarg/ipl) hosted
on Kaggle. The dataset comprised of two csv files
“matches.csv” and “deliveries.csv”. The characteristics of the individual files are as below:

### Matches.csv
This data file comprises of records of all matches played in IPL from season 2008 to 2017. The data file comprises of 18 features. It contains data corresponding to the name of the teams, venue of the match, outcome, umpires and details pertaining to the matches played. There are 636 entries in the data file.

### Deliveries.csv
This data file comprises of records of every delivery bowled in each of the matches. The records are chronologically arranged. The data includes 23 features including the outcome of every delivery and the number of runs scores and the way runs were scored. There are 150460 entries in the data file.

# ShowCase
![Screenshot (159)]

# Usage
To make predictions, provide the following parameters when prompted:

- **Batting Team**: The team currently at bat.
- **Bowling Team**: The team currently bowling.
- **City**: The location of the match.
- **Current runs**: The current score of batting team.
- **Overs Completed**: The number of overs completed.
- **Wickets**: The number of wickets lost.
- **Target Runs**: The total runs scored by a bowling team.

The predictor will calculate the probability of the batting team winning and bowling team winning based on these parameters and the current match situation.

# Technologies_Used
This project leverages the following technologies:

- [Python](https://www.python.org/)
- [Logistic Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)
- [NumPy](https://numpy.org/)
- [pandas](https://pandas.pydata.org/)
- [Flask](https://flask.palletsprojects.com/en/3.0.x/)

# Conclusion
Predicting  a  winner  in  a  sport  such  as  cricket  is especially  challenging  and  involves  very  complex processes. But with the introduction of machine learning, 
this can be made much easier and simpler.We have analyzed IPL data sets  and  predicted  game  results  based  on the 1st inning performance of the team.
