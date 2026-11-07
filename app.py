
import streamlit as st
import pandas as pd
import pickle

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------
st.markdown("""
<style>

    .main {
        background-color: #f5f7fa;
    }

    .title {
        text-align: center;
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #666666;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
        margin-bottom: 20px;
    }

    .result-card {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.10);
        margin-top: 25px;
    }

    .result-title {
        font-size: 18px;
        color: #666666;
    }

    .result-price {
        font-size: 38px;
        font-weight: 700;
        margin-top: 10px;
    }

    .footer {
        text-align: center;
        color: #888888;
        font-size: 14px;
        margin-top: 40px;
    }

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.markdown(
    '<div class="title">🏠 House Price Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Machine Learning Based House Price Estimator</div>',
    unsafe_allow_html=True
)

# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------
try:

    with open("house_price_model.pkl", "rb") as file:
        model = pickle.load(file)

    with open("scaler.pkl", "rb") as file:
        scaler = pickle.load(file)

    st.success("✓ Machine Learning Model Loaded Successfully")

except Exception as e:

    st.error(f"Unable to load model: {e}")
    st.stop()

# --------------------------------------------------
# EXCHANGE RATE
# --------------------------------------------------
USD_TO_INR = 83.50

st.info(
    f"💱 Currency Conversion: 1 USD = ₹{USD_TO_INR:.2f}"
)

# --------------------------------------------------
# HOUSE DETAILS
# --------------------------------------------------
st.markdown(
    '<div class="card">',
    unsafe_allow_html=True
)

st.subheader("🏡 Enter House Details")

st.write(
    "Enter the following property details to estimate the house price."
)

col1, col2 = st.columns(2)

with col1:

    CRIM = st.number_input(
        "CRIM",
        value=0.00632,
        format="%.5f"
    )

    ZN = st.number_input(
        "ZN",
        value=18.0
    )

    INDUS = st.number_input(
        "INDUS",
        value=2.31
    )

    CHAS = st.number_input(
        "CHAS",
        value=0.0
    )

    NOX = st.number_input(
        "NOX",
        value=0.538
    )

    RM = st.number_input(
        "RM",
        value=6.575
    )

    AGE = st.number_input(
        "AGE",
        value=65.2
    )

with col2:

    DIS = st.number_input(
        "DIS",
        value=4.09
    )

    RAD = st.number_input(
        "RAD",
        value=1.0
    )

    TAX = st.number_input(
        "TAX",
        value=296.0
    )

    PTRATIO = st.number_input(
        "PTRATIO",
        value=15.3
    )

    B = st.number_input(
        "B",
        value=369.90
    )

    LSTAT = st.number_input(
        "LSTAT",
        value=4.98
    )

st.markdown("</div>", unsafe_allow_html=True)

# --------------------------------------------------
# PREDICTION
# --------------------------------------------------
if st.button(
    "🔮 Predict House Price",
    use_container_width=True
):

    user_input = pd.DataFrame(
        [[
            CRIM,
            ZN,
            INDUS,
            CHAS,
            NOX,
            RM,
            AGE,
            DIS,
            RAD,
            TAX,
            PTRATIO,
            B,
            LSTAT
        ]],
        columns=[
            "CRIM",
            "ZN",
            "INDUS",
            "CHAS",
            "NOX",
            "RM",
            "AGE",
            "DIS",
            "RAD",
            "TAX",
            "PTRATIO",
            "B",
            "LSTAT"
        ]
    )

    # Scale input
    user_input_scaled = scaler.transform(user_input)

    # Predict
    prediction = model.predict(user_input_scaled)

    # Boston Housing prediction is in $1000s
    price_1000_usd = prediction[0]

    # Convert to USD
    price_usd = price_1000_usd * 1000

    # Convert USD to INR
    price_inr = price_usd * USD_TO_INR

    # --------------------------------------------------
    # RESULT
    # --------------------------------------------------

    st.markdown(
        '<div class="result-card">',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="result-title">🏠 Estimated House Price</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="result-price">₹{price_inr:,.2f}</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <p style="color:#777777;">
        Approx. USD Value: ${price_usd:,.2f}
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)

    st.success("✓ Prediction Completed Successfully!")

# --------------------------------------------------
# INFORMATION
# --------------------------------------------------
with st.expander("ℹ️ About This Prediction"):

    st.write("""
    This application uses a Machine Learning model to estimate
    house prices based on property-related features.

    The model was trained using the Boston Housing dataset.

    The original model prediction is represented in thousands
    of US dollars. The application converts this value into
    Indian Rupees for easier understanding.

    **Note:** The USD to INR conversion rate used by this
    application is ₹83.50 per USD and is provided for
    demonstration purposes.
    """)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown(
    """
    <div class="footer">
        🏠 House Price Prediction | Machine Learning Project<br>
        Built with Python, Pandas, Scikit-learn & Streamlit
    </div>
    """,
    unsafe_allow_html=True
)
