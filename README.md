# Taxi Fare Prediction Model

This repository contains a machine learning-based solution for predicting taxi fares. The project leverages Ridge Regression and Random Forest Regression algorithms to estimate fares based on input features such as pickup and drop-off locations and passenger count. The project is designed to improve transportation efficiency and enhance user experience in urban areas.

---

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Results](#results)
6. [Technologies Used](#technologies-used)
7. [Contributing](#contributing)
8. [License](#license)

---

## Introduction
Predicting taxi fares in advance is essential to improve passenger experience and driver efficiency. This project demonstrates the development and evaluation of a predictive model using historical taxi data. Key objectives include:
- Providing accurate fare estimates.
- Enabling data-driven decision-making in urban transportation.

---

## Features
- **Data Preprocessing**: Scaling and preparing features for model training.
- **Machine Learning Algorithms**:
  - Ridge Regression
  - Random Forest Regression
- **Performance Evaluation**: Metrics include Mean Squared Error (MSE) and R-squared scores.
- **Visualization**: Compare algorithm performance using charts.
- **Streamlit App**: An interactive user interface for fare prediction.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Abu_abdurrahman/taxi-fare-prediction.git
   cd taxi-fare-prediction
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the Model:
   Before running Streamlit app, download the model from
   ```bash
   https://drive.google.com/file/d/1UQWltwPBiRTzyovbKQ7jXXP33DI_uep1/view?usp=sharing
   ```
4. Run the Streamlit app:
   ```bash
   streamlit run Taxi_st.py
   ```

---

## Usage
1. Load the dataset and preprocess the data.
2. Train models using Ridge Regression and Random Forest Regression.
3. Compare performance metrics (MSE, R-squared).
4. Visualize and interpret results using matplotlib charts.
5. Use the Streamlit app to make predictions.

---

## Results
- **Ridge Regression**:
  - MSE: 36.99
  - R-squared: 0.333
- **Random Forest Regression**:
  - MSE: 8.78
  - R-squared: 0.842

The Random Forest Regression model outperformed Ridge Regression, showcasing better accuracy and predictive capabilities.

---

## Technologies Used
- Python
- scikit-learn
- pandas
- numpy
- matplotlib
- Streamlit

---

## Contributing
Contributions are welcome! If you find a bug or want to add a feature:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
