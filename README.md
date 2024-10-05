# AirMed

## Overview 

A powerful AI health diagnosis interface(website) that leverages machine learning to interpret symptoms and predict potential medical conditions. Designed to improve healthcare accessibility, this interface offers instant, reliable health insights, guiding users towards informed medical decisions.

## Table of Contents

Description\
Features\
Usage\
Dataset\
Model Architecture\
Future Work\
Troubleshooting\
Credits\
Contact Info


## Description

This project implements a HealthCare interface(website) for disease detection based on symptoms. The website utilizes machine learning algorithms, particularly Decision Trees and Support Vector Classification (SVC), for disease prediction. It analyzes user-reported symptoms to identify potential diseases and provides relevant recommendations.

## Features

1. *Symptom Analysis*: Users can input their symptoms, and the model will analyze them to identify potential diseases.

2. *Recommendations*: The website interface provides recommendations based on the identified diseases, including precautions and possible treatments.

3. *User-Friendly Interface*: The website is designed with a user-friendly interface to facilitate easy interaction and understanding.

## Usage

1. Login  to the patient appointment page.
2. Enter the symptoms you are experiencing when prompted.
3. Follow the website's instructions to provide additional information if necessary.
4. Receive disease predictions and recommendations as result.

## Dataset

The project utilizes a dataset containing symptom-disease mappings for disease prediction. The dataset is included in this repository (https://github.com/gautham-here/edgetra/tree/main/Data) and can be obtained from sources like kaggle. 

## Model Architecture

The disease detection model is built using machine learning algorithms, specifically Decision Trees and Support Vector Classification (SVC). It analyzes user-reported symptoms to predict potential diseases based on learned patterns.

## Future Work

1. Enhance the Model's accuracy by incorporating more comprehensive symptom-disease mappings.
2. Integrate additional features such as user history tracking and personalized recommendations.
3. Deploy the model as a mobile application for broader accessibility.

## Troubleshooting

If you encounter any issues while running the website, try the following troubleshooting steps:

1. Check that all dependencies are properly installed.
2. Ensure that the dataset is accessible and formatted correctly.


## Credits

1. Numpy and pandas for mathematical operations.
2. For reading csv dataset files: csv module.
3. Regular expression for pattern matching.
4. sklearn library for preprocessing, building models, and evaluating performance.
5. Seaborn and Matplotlib for visualization.
6. intel's scikit-learn-intelex sklearnex for patchwork().

## About

Developed by Team EDGETRA.