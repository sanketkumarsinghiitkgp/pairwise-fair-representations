# Operationalizing-Individual-Fairness
Implementation of ["Operationalizing Individual Fairness with Pairwise Fair Representations"](https://arxiv.org/abs/1907.01439v2)\
[Link to Google Slides presentation](https://docs.google.com/presentation/d/1QSwfH2c0MTJWop7g0ccYhEow9cjaF5wQHw5lEaTU2f8/edit?usp=sharing)


# Setup
| Dataset | Number of Records \(Paper\) | Number of Records \(Our Implementation\) | Number of Features \(Paper\) | Number of Features \( Our Implementation \) | True Rank  | Protected Attribute     |
|---------|-----------------------------|------------------------------------------|------------------------------|---------------------------------------------|------------|-------------------------|
| Compas  | 8803                        | 6903                                     | 429                          | 456                                         | 117        | Race\_African\-American |

# Requirements
A list of packages required to run is mentioned in requirements.txt file.


# Results

Reproduced Results :

| Original Representation                                     | Pairwise Fair Representation \(Gamma = 0\.5\)              |
|-------------------------------------------------------------|------------------------------------------------------------|
| Accuracy: 69\.56%                                           | Accuracy: 66\.01%                                          |
| ROC\-AUC score: 69\.04%                                     | ROC\-AUC score: 65\.68                                     |
| Positive Prediction Rate for African Americans: 0\.419      | Positive Prediction Rate for African Americans: 0\.434     |
| Positive Prediction Rate for Non\-African Americans: 0\.406 | Positive Prediction Rate for Non\-African Americans: 0\.5  |
| Prediction Error Rate for African Americans: 0\.323         | Prediction Error Rate for African Americans: 0\.34         |
| Prediction Error Rate for Non\-African Americans: 0\.304    | Positive Prediction Rate for Non\-African Americans: 0\.75 |
| False Positive Rate for African Americans: 0\.3             | False Positive Rate for African Americans: 0\.285          |
| False Positive Rate for Non\-African Americans: 0\.226      | False Positive Rate for Non\-African Americans: 0\.667     |




# NOTE
Concerns Faced in the experimentation :
1. We did not experiment on the Crime and Communities due to the requirement of of ratings columns for the neighbourhoods from niche.com    which is not available as a public dataset.
2. We performed trial and error methods to tune parameters k( for kth quantile ) and p( for p nearest neighbours ) for maximum value of    AUC score.



## Team Members

| Name                    | Roll Number |
|-------------------------|-------------|
| Harshvardhan Srivastava | 17EE10058   |
| Sanket Kumar Singh      | 17EE30016   |

