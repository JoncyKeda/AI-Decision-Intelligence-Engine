import streamlit as st
import pandas as pd

from app.decision_engine import DecisionEngine

st.set_page_config(
    page_title="AI Decision Intelligence Engine",
    layout="wide"
)

st.title(
    "🧠 AI Decision Intelligence Engine"
)

st.sidebar.header("Business Inputs")

marketing_budget = st.sidebar.slider(
    "Marketing Budget Increase (%)",
    0,
    50,
    20
)

product_price = st.sidebar.slider(
    "Product Price Increase (%)",
    0,
    30,
    10
)

employee_count = st.sidebar.slider(
    "Additional Employees",
    0,
    20,
    5
)

engine = DecisionEngine()

scenario = {
    "marketing_budget": marketing_budget,
    "product_price": product_price,
    "employee_count": employee_count
}

result = engine.evaluate_decision(
    scenario
)

st.subheader("📊 Decision Results")

st.write(result)

chart_data = pd.DataFrame({
    "Metric": ["Revenue Growth"],
    "Value": [
        result["Predicted Revenue Growth (%)"]
    ]
})

st.bar_chart(
    chart_data.set_index("Metric")
)
