
import streamlit as st
import pandas as pd
import csv
import os
from datetime import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Coffee House | Order System",
    page_icon="☕",
    layout="wide"
)

CSV_FILE = "data.csv"

COFFEE_MENU = {
    "Espresso": 120,
    "Cappuccino": 150,
    "Caffe Latte": 180,
    "Americano": 190,
    "Coconut Coffee": 350,
    "Salt Coffee / Egg Coffee": 380,
    "Phin Black Coffee": 240
}

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

.stApp {
    background: linear-gradient(135deg, #1c100b, #382016, #21140f);
    color: #fff3e0;
    font-family: 'Poppins', sans-serif;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}

/* Main Banner */
.hero {
    background: linear-gradient(120deg, #603813, #a66a35, #d49a5b);
    padding: 38px;
    border-radius: 20px;
    text-align: center;
    margin-bottom: 30px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
}

.hero h1 {
    color: #fff7ed;
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 8px;
}

.hero p {
    color: #ffead2;
    font-size: 16px;
}

/* Section Heading */
h2, h3 {
    color: #e9b77e !important;
    font-weight: 700 !important;
}

/* Cards */
.coffee-card {
    background: #38251b;
    border: 1px solid #765035;
    border-radius: 15px;
    padding: 20px;
    text-align: center;
    margin-bottom: 15px;
    transition: 0.3s;
}

.coffee-card:hover {
    border-color: #e5a45e;
    transform: translateY(-3px);
}

.coffee-card h3 {
    color: #f4c28c !important;
    font-size: 19px;
}

.coffee-card p {
    color: #f7e6d5;
    font-size: 17px;
    font-weight: 600;
}

/* Inputs */
.stTextInput input, 
.stSelectbox div[data-baseweb="select"] {
    background-color: #fff3e0 !important;
    color: #382016 !important;
    border-radius: 10px !important;
}

label {
    color: #f4c28c !important;
    font-weight: 600 !important;
}

/* Buttons */
.stButton > button,
.stFormSubmitButton > button {
    background: linear-gradient(90deg, #a65e2e, #d99a55);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 12px 25px;
    font-weight: 700;
    transition: 0.3s;
}

.stButton > button:hover,
.stFormSubmitButton > button:hover {
    background: #e7ad70;
    color: #27170f;
    border: none;
}

/* Metrics */
div[data-testid="stMetric"] {
    background: #38251b;
    border: 1px solid #765035;
    padding: 20px;
    border-radius: 15px;
}

div[data-testid="stMetricLabel"] {
    color: #e9b77e;
}

div[data-testid="stMetricValue"] {
    color: #fff3e0;
}

/* Dataframe */
div[data-testid="stDataFrame"] {
    border: 1px solid #765035;
    border-radius: 12px;
}

/* Footer */
.footer {
    text-align: center;
    color: #c5a58a;
    padding: 25px;
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)


# ---------------- CSV SETUP ----------------
COLUMNS = ["Customer Name", "Phone Number", "Coffee", "Price", "Order Time"]

if not os.path.exists(CSV_FILE):
    pd.DataFrame(columns=COLUMNS).to_csv(CSV_FILE, index=False)


# ---------------- HERO SECTION ----------------
st.markdown("""
<div class="hero">
    <h1>☕ COFFEE HOUSE</h1>
    <p>Fresh Coffee • Happy Moments • Beautiful Experiences</p>
    <p>Welcome to Our Premium Coffee Ordering System</p>
</div>
""", unsafe_allow_html=True)


# ---------------- COFFEE MENU ----------------
st.header("☕ Our Coffee Menu")

menu_columns = st.columns(4)

for index, (coffee_name, price) in enumerate(COFFEE_MENU.items()):
    with menu_columns[index % 4]:
        st.markdown(f"""
        <div class="coffee-card">
            <h3>☕ {coffee_name}</h3>
            <p>₹ {price}</p>
        </div>
        """, unsafe_allow_html=True)


st.divider()


# ---------------- ORDER FORM ----------------
st.header("🛒 Place Your Order")

left, right = st.columns([1.3, 0.7], gap="large")

with left:
    with st.form("coffee_order_form"):

        name = st.text_input("Customer Name", placeholder="Enter your name")

        phone = st.text_input(
            "Phone Number",
            placeholder="Enter your phone number"
        )

        coffee = st.selectbox(
            "Select Your Coffee",
            list(COFFEE_MENU.keys())
        )

        price = COFFEE_MENU[coffee]

        st.markdown(
            f"### Total Price: <span style='color:#e9b77e'>₹ {price}</span>",
            unsafe_allow_html=True
        )

        submit = st.form_submit_button(
            "☕ Place Order",
            use_container_width=True
        )

        if submit:
            if not name.strip() or not phone.strip():
                st.warning("Please fill in all the fields.")

            elif not phone.strip().replace("+", "").replace(" ", "").isdigit():
                st.error("Please enter a valid phone number.")

            else:
                with open(CSV_FILE, "a", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerow([
                        name.strip(),
                        phone.strip(),
                        coffee,
                        price,
                        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    ])

                st.success(f"🎉 Thank you {name}! Your coffee order has been received.")


with right:
    st.markdown("""
    <div class="coffee-card">
        <h3>☕ Coffee Experience</h3>
        <p>Every cup tells a story.</p>
        <p>Freshly prepared coffee, made with love.</p>
        <hr>
        <p>✨ Quality Coffee</p>
        <p>✨ Premium Experience</p>
        <p>✨ Happy Customers</p>
    </div>
    """, unsafe_allow_html=True)


st.divider()


# ---------------- CUSTOMER DASHBOARD ----------------
st.header("📊 Customer Dashboard")

st.header(" Customer Recordes")

try:
    data =pd.read_csv(CSV_FILE)
    st.dataframe(data)
except:
    st.warning("No data available yet")


# ---------------- CLEAR DATA ----------------
st.divider()

st.subheader("⚙️ Admin Settings")

if st.button("🗑️ Clear All Customer Data"):
    pd.DataFrame(columns=COLUMNS).to_csv(CSV_FILE, index=False)
    st.success("All customer records have been cleared!")
    st.rerun()


# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
    ☕ Coffee House Ordering System | Built with Python & Streamlit
    <br>
    Made with ❤️
</div>
""", unsafe_allow_html=True)
