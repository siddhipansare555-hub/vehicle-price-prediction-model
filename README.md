# vehicle-price-prediction-model
# 🚗 Car Price Predictor

## 📖 Overview
The **Car Price Predictor** is a Machine Learning web application that estimates the selling price of a used car based on its specifications. By entering details like the car's age, mileage, engine size, fuel type, and kilometers driven, the app uses a trained AI model to give you an estimated price and a realistic price range.

## ✨ Features
* **User-Friendly Interface**: Built with Streamlit for a clean, modern web experience.
* **Instant Predictions**: Get car price estimates in seconds.
* **Comprehensive Inputs**: Takes into account various factors like transmission type, ownership history, engine power, and more.
* **Smart Estimations**: Displays the predicted price in Indian Rupees (₹) and provides a realistic ±10% expected selling range.

---

## 📁 Project Structure (What each file does)
Here is a simple breakdown of the files in this project:

* **`app.py`**: The main brain of the web app. This file uses Streamlit to create the user interface, takes your inputs, talks to the trained model, and displays the final price.
* **`models.ipynb`**: The Jupyter Notebook where the Machine Learning model was created. It contains the code for loading the data, training the Random Forest algorithm, and saving the final model.
* **`Car Dataset Processed.csv`**: The cleaned historical data of used cars. The AI model studied this data to learn how different features affect a car's price.
* **`final_model.pkl`**: The trained Machine Learning model saved as a file. Think of it as the "brain" that has already learned how to predict prices.
* **`columns.pkl`**: A helper file that remembers the exact names and order of the data columns used during training. It ensures the web app formats your input exactly how the model expects it.
* **`requirements.txt`**: A simple text file listing all the Python libraries needed to run this project.

---

## 🚀 How to Install and Run the Project

Follow these steps to run the application on your own computer:

### Step 1: Install Python
Make sure you have Python installed on your computer. You can download it from [python.org](https://www.python.org/).

### Step 2: Open your Terminal / Command Prompt
Navigate to the folder where you saved these project files. 

### Step 3: Install the required libraries
Run the following command to install all the necessary tools (like Streamlit, Pandas, and Scikit-Learn):
```bash
pip install -r requirements.txt
