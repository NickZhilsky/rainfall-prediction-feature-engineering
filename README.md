# Rainfall Prediction: Feature Engineering Under Real-World Constraints

## Context
This project focuses on predicting rainfall events using historical weather data.
The primary goal was not to maximize leaderboard score, but to design a robust and interpretable solution under real-world data limitations.

## Data
The dataset contains historical meteorological observations with:
- missing values
- noisy measurements
- class imbalance between rainfall and non-rainfall events

These issues significantly influenced modeling and evaluation decisions.

## Problem Statement
Predict whether rainfall will occur on a given day while balancing:
- model performance
- interpretability
- robustness to noisy data

## Approach
Key steps:
- feature engineering based on domain logic rather than brute-force transformations
- careful handling of missing values and outliers
- comparison of multiple model families with a focus on stability

A Random Forest model was selected as the final approach due to its balance between performance and interpretability.

## Evaluation
Model performance was evaluated using metrics aligned with imbalanced classification.
Leaderboard score was treated as a secondary signal rather than the primary optimization target.

## Result
The solution achieved a **Bronze medal** in the Kaggle competition.
More importantly, it demonstrated consistent behavior across validation folds and unseen data.

## Trade-offs and Limitations
- The model prioritizes stability over marginal metric gains
- Rare extreme rainfall events remain difficult to predict
- Additional temporal features could improve performance in production scenarios

## What I Would Improve
- Incorporate external data sources (e.g. climate indices)
- Experiment with time-aware validation strategies
- Add model monitoring for concept drift
