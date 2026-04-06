import streamlit as st
import pandas as pd
st.set_page_config(page_title="Edli | The Bias-Free Engine", page_icon="🛡️", layout="wide")
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #fcfcfc;
    }
    
    /* Hero Section */
    .hero {
        background-color: #001f3f;
        padding: 60px;
        border-radius: 20px;
        text-align: center;
        color: white;
        margin-bottom: 40px;
    }
    
    /* POC Cards */
    .poc-card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #e0e0e0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        transition: 0.3s;
    }
    .poc-card:hover {
        box-shadow: 0 8px 24px rgba(0,0,0,0.1);
        border-color: #FFD700;
    }

    /* Typography */
    h1, h2, h3 { font-family: 'Inter', sans-serif; }
    .gold-text { color: #FFD700; font-weight: bold; }
    
    /* Buttons */
    .stButton>button {
        background-color: #FFD700 !important;
        color: #001f3f !important;
        border-radius: 8px;
        border: none;
        padding: 10px 24px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
    <div class="hero">
        <h1 style="font-size: 3.5rem; margin-bottom: 10px;">🛡️ Edli</h1>
        <p style="font-size: 1.2rem; opacity: 0.9;">
            The Anti-Consultant Engine. Transparent. Data-Driven. <span class="gold-text">Bias-Free.</span>
        </p>
    </div>
    """, unsafe_allow_html=True)

st.write("## 🚀 The Vision")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### 🚫 No Commissions
    Edli doesn't take referral fees from colleges. Our data is pure and unbought.
    """)
with col2:
    st.markdown("""
    ### 📊 Real ROI
    We prioritise placements and fees over marketing brochures and expensive campuses.
    """)
with col3:
    st.markdown("""
    ### 🤝 Extended Support
    Edli subscription helps you to apply to your dream college easily.
    """)

st.divider()

st.write("## 🛠️ Proof of Concept )")
st.write("Try the logic I built during my 24-hour sprint from knowing nothing about websites to deploying one myself")

df = pd.read_csv('colleges.csv')

with st.container():
    st.markdown('<div class="poc-card">', unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2])
    
    with c1:
        st.write("### Filter Logic")
        city_input = st.multiselect("Target Cities", options=df['City'].unique())
        min_ctc = st.slider("Min Placement (LPA)", 0, 200, 20)
        CS_Mandatory = st.toggle("Only with CSE")
    
    with c2:
        # Filtering Logic
        res = df[df['City'].isin(city_input)]
        res = res[res['Highest CTC (LPA)'] >= min_ctc]
        if CS_Mandatory:
            res = res[res['CSE'] == "Yes"]
            
        st.write(f"### Found {len(res)} matches")
        st.dataframe(res[['College Name', 'City', 'Highest CTC (LPA)']], use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

st.write("")
st.write("---")
st.caption("Built in public by an 18-year-old non-tech founder. Edli is 100% independent.")
