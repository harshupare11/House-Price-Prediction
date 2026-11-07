# 🏠 House Price Prediction

### Machine Learning Based House Price Estimation Web Application

A Machine Learning project developed using **Python, Pandas, Scikit-learn and Streamlit** to estimate house prices based on various property-related features.

The application takes 13 input variables, processes them using a pre-trained scaling model, and predicts an estimated house price. The result is displayed in both US Dollars (USD) and Indian Rupees (INR).

---

## 📸 Application Screenshots

[Application Homepage](screenshots/123.png)

---

## ✨ Features

- Interactive and user-friendly Streamlit interface.
- 13 property-related input parameters.
- Pre-trained Machine Learning prediction model.
- Data scaling using a pre-trained scaler.
- Estimated house price in USD.
- Currency conversion from USD to INR.
- Prediction result displayed in a clean interface.
- Model loading and error handling.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data handling and preprocessing |
| NumPy | Numerical computing |
| Scikit-learn | Machine Learning and feature scaling |
| Streamlit | Web application interface |
| Pickle | Saving and loading trained models |

---

## 📊 Input Features

The application accepts the following 13 features:

| Feature | Description |
|---|---|
| CRIM | Per capita crime rate |
| ZN | Residential land zoned for large lots |
| INDUS | Non-retail business acres per town |
| CHAS | Charles River dummy variable |
| NOX | Nitric oxide concentration |
| RM | Average number of rooms |
| AGE | Proportion of older owner-occupied units |
| DIS | Distance to employment centres |
| RAD | Accessibility to radial highways |
| TAX | Property tax rate |
| PTRATIO | Pupil-teacher ratio |
| B | Boston population-related dataset variable |
| LSTAT | Percentage of lower-status population |

---

## ⚙️ How It Works

1. User enters property-related details.
2. Input data is converted into a Pandas DataFrame.
3. The trained scaler transforms the input features.
4. The pre-trained Machine Learning model generates a prediction.
5. The predicted value is converted into USD.
6. The application converts USD into INR.
7. The estimated house price is displayed on the Streamlit dashboard.

---

## 📁 Project Structure

```text
House-Price-Prediction/
│
├── app.py
├── house_price_model.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
├── .gitignore
│
└── screenshots/
    ├── 123.png
```

---

## 🚀 Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/harshupare11/House-Price-Prediction.git
```

### Step 2: Open Project Directory

```bash
cd House-Price-Prediction
```

### Step 3: Create Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Run the Application

```bash
streamlit run app.py
```

The application will open in your browser at:

`http://localhost:8501`

---

## 💱 Currency Conversion

The application displays the predicted price in both USD and INR.

The current demonstration conversion rate configured in the application is:

**1 USD = ₹83.50**

Note: This is a fixed demonstration value in the code, not a live exchange rate.

---

## ⚠️ Important Disclaimer

- This project uses the Boston Housing dataset for educational and demonstration purposes.
- Predictions are based on the dataset's original features and trained model.
- The model is not designed to provide accurate real-world Indian property valuations.
- Currency conversion uses a fixed demonstration exchange rate.

---

## 🎯 Project Objective

The main objective of this project is to understand the practical implementation of Machine Learning, including data preprocessing, feature scaling, model prediction and deployment through an interactive web application.

---

## 👨‍💻 Developed By

**Harshvardhan Balasaheb Upare**

- GitHub: [@harshupare11](https://github.com/harshupare11)
- LinkedIn: [Harshvardhan Upare](https://www.linkedin.com/in/harshvardhan-upare-19a107338/)

---

⭐ If you find this project interesting, consider giving it a star on GitHub!

**Learn • Build • Innovate** 🚀
