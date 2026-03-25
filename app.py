import streamlit as st
import pandas as pd

# 1. Setup Page Config
st.set_page_config(page_title="Bias-Free College Finder", layout="wide")
st.title("🚀 Zero-Bias College Finder")
st.subheader("Exposing the truth behind the 'Highest CTC' numbers.")

# 2. Load Data (IP Unit 1: Pandas)
@st.cache_data
def load_data():
    df = pd.read_csv('colleges.csv')
    # Clean 'Yes/No' to Boolean (Essential for filtering)
    binary_cols = ['Cricket', 'Football', 'Aerospace', 'CSE', 'ECE']
    for col in binary_cols:
        df[col] = df[col].map({'Yes': True, 'No': False})
    return df

df = load_data()

# 3. Sidebar Filters (The 'User Input' part of your project)
st.sidebar.header("Filter Your Future")
city_choice = st.sidebar.multiselect("Select City", options=df['City'].unique(), default=df['City'].unique())
min_ctc = st.sidebar.slider("Minimum Highest CTC (LPA)", 0, 250, 10)

# Branch Requirements
st.sidebar.write("Required Branches:")
needs_cse = st.sidebar.checkbox("Must have CSE")
needs_ece = st.sidebar.checkbox("Must have ECE")

# 4. The Logic (IP Unit 1: Dataframe Filtering)
filtered_df = df[
    (df['City'].isin(city_choice)) & 
    (df['Highest CTC (LPA)'] >= min_ctc)
]

if needs_cse:
    filtered_df = filtered_df[filtered_df['CSE'] == True]
if needs_ece:
    filtered_df = filtered_df[filtered_df['ECE'] == True]

# 5. The Reveal
st.write(f"Showing **{len(filtered_df)}** colleges matching your criteria:")

# Highlight 'Agent Traps' (Manual logic for now)
# If CTC is high but it's a private city, we flag it as 'Verify Data'
st.dataframe(filtered_df.sort_values(by='Highest CTC (LPA)', ascending=False))

# 6. Data Visualization (IP Unit 1: Matplotlib/Plotly)
st.bar_chart(filtered_df.set_index('College Name')['Highest CTC (LPA)'])