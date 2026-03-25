import streamlit as st
import pandas as pd

# 1. THE "BRANDING OVERRIDE" (Fixes the Blue Background)
st.set_page_config(page_title="Bias-Free Finder", layout="centered")

st.markdown("""
    <style>
    /* Target the main background and the header */
    [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #001f3f !important;
    }
    
    /* Force the text to be white */
    div[data-testid="stVerticalBlock"] p, label, .stMarkdown {
        color: white !important;
    }

    /* Yellow Headers */
    h1, h2, h3 {
        color: #FFD700 !important;
    }

    /* Black text for inputs (to keep them readable) */
    .stSelectbox div[data-baseweb="select"], .stMultiSelect div[data-baseweb="select"] {
        color: black !important;
    }
    
    /* Yellow Button */
    .stButton>button {
        background-color: #FFD700 !important;
        color: #001f3f !important;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# Rest of your title and logic continues here...
st.title("🛡️ Bias-Free College Finder")
st.write("### 2 Years of Knowledge. 5 Days to Build. 0 Hidden Commissions.")
st.divider()

# 2. DATA LOADING (IP Syllabus: Unit 1)
@st.cache_data
def load_and_clean():
    df = pd.read_csv('colleges.csv')
    # Normalizing binary data for the logic
    cols = ['Cricket', 'Football', 'Aerospace', 'CSE', 'ECE']
    for c in cols:
        df[c] = df[c].astype(str).str.strip().str.capitalize()
    return df

df = load_and_clean()

# 3. THE 4-QUESTION FLOW (Updated for Multi-Choice)
st.subheader("Choose Your Preferences")

# Q1: Cities (Multiple)
all_cities = list(df['City'].unique())
q1_cities = st.multiselect("Q1: Which Cities are you considering?", options=all_cities, default=all_cities)

# Q2: Sports
q2_sport = st.radio("Q2: Preferred Sports Facility?", ["No Preference", "Cricket", "Football"])

# Q3: CTC
q3_ctc = st.select_slider("Q3: Minimum Highest CTC (LPA)?", 
                         options=[0, 10, 20, 30, 40, 50, 100, 200], value=10)

# Q4: Branches (Multiple)
available_branches = ["CSE", "ECE", "Aerospace"]
q4_branches = st.multiselect("Q4: Which branches are you interested in?", options=available_branches)

# 4. THE UPDATED FILTERING LOGIC (IP Syllabus: .isin() and All-Match)
filtered = df.copy()

# Filter by Multiple Cities
filtered = filtered[filtered['City'].isin(q1_cities)]

# Filter by Minimum CTC
filtered = filtered[filtered['Highest CTC (LPA)'] >= q3_ctc]

# Filter by Sports
if q2_sport != "No Preference":
    filtered = filtered[filtered[q2_sport] == "Yes"]

# Filter by Multiple Branches (The 'AND' logic)
if q4_branches:
    for branch in q4_branches:
        filtered = filtered[filtered[branch] == "Yes"]

# 5. THE REVEAL
st.divider()
st.subheader("🎯 Recommended Colleges")

if not filtered.empty:
    # Displaying selected columns for a clean look
    display_cols = ['College Name', 'City', 'Highest CTC (LPA)']
    st.table(filtered[display_cols].sort_values(by='Highest CTC (LPA)', ascending=False))
else:
    st.error("No colleges match all your criteria. Try lowering the CTC or changing the city.")

st.info("Note: This data is sourced directly to bypass agent commissions.")
