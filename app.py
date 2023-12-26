import streamlit as st #pip install streamlit
import plotly.graph_objects as go #pip install plotly

#-----------------------settings------------------------

incomes = ["Salary", "Blog", "Other income"]
expenses = ["Rent", "Utilities", "Groceries", "Car", "Other Expenses", "Saving"]

currency = "LKR"

page_title = "Income and Expense Tracker"
page_icon = ":money_with_wings:"
layout = "centered"

#-------------------------------------------------

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)
