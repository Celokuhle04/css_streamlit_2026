import streamlit as st
import pandas as pd
import numpy as np

# Set page title
st.set_page_config(page_title="Eastern Cape Research Dashboard | Celokuhle Ntete", layout="wide", page_icon="📊")
st.caption("Note: Sample/demo data for portfolio demonstration purposes")

# Custom CSS for professional look
st.markdown("""
<style>
    .main {padding-top: 1rem;}
    h1 {color: #0e4d92;}
</style>
""", unsafe_allow_html=True)

# Sidebar Menu
st.sidebar.title("📊 Dashboard")
st.sidebar.markdown("**Celokuhle S. Ntete** | Data & Software Developer")
menu = st.sidebar.radio(
    "Navigation:",
    ["About Me", "Research Publications", "Eastern Cape Data Explorer", "Contact"],
)

# Dummy Eastern Cape data
population_data = pd.DataFrame({
    "District": ["Alfred Nzo", "Amathole", "Buffalo City", "Chris Hani", "Joe Gqabi", "Nelson Mandela Bay", "OR Tambo", "Sarah Baartman"],
    "Population (Millions)": [0.9, 0.9, 0.8, 0.8, 0.4, 1.2, 1.4, 0.5],
    "Unemployment Rate (%)": [35, 36, 32, 38, 40, 34, 37, 33]
})

education_data = pd.DataFrame({
    "Level": ["No Schooling", "Primary", "Secondary", "Tertiary"],
    "Percentage (%)": [12, 28, 45, 15]
})

climate_data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "Average Rainfall (mm)": [85, 90, 70, 55, 40, 30, 25, 35, 45, 60, 75, 80]
})

# Sections based on menu selection
if menu == "About Me":
    st.header("About Me")
    st.subheader("Celokuhle Sandise Ntete | Data & Software Developer")
    st.write("Honours Mathematics student at the University of Fort Hare, passionate about turning data into solutions with Python.")
    st.markdown("---")
    st.markdown("### 🎓 Education")
    st.write("University of Fort Hare - Honours in Mathematics")
    st.markdown("### 💼 Focus")
    st.write("Data Analytics | Software Development | Mathematics")
    st.markdown("### 🛠️ Tech Stack")
    st.write("Python • SQL • Pandas • Streamlit • Power BI • Git")
    st.link_button("View GitHub Profile", "https://github.com/Celokuhle04")
    st.markdown("---")
    st.caption("📍 Alice, Eastern Cape | Open to Data Analyst & Developer roles")

elif menu == "Research Publications":
    st.header("Research Publications")
    st.sidebar.header("Upload and Filter")
    st.info("Upload a CSV with Eastern Cape publications to explore trends")

    uploaded_file = st.file_uploader("Upload a CSV of Eastern Cape publications", type="csv")
    if uploaded_file:
        publications = pd.read_csv(uploaded_file)
        st.dataframe(publications, use_container_width=True)

        keyword = st.text_input("Filter by keyword", "")
        if keyword:
            filtered = publications[publications.apply(lambda row: row.astype(str).str.contains(keyword, case=False).any(), axis=1)]
            st.write(f"Filtered Results for '{keyword}':")
            st.dataframe(filtered, use_container_width=True)

        if "Year" in publications.columns:
            st.subheader("Publication Trends")
            year_counts = publications["Year"].value_counts().sort_index()
            st.bar_chart(year_counts)
    else:
        st.write("No file uploaded - demo data will be shown in Data Explorer tab")

elif menu == "Eastern Cape Data Explorer":
    st.header("Eastern Cape Data Explorer")
    data_option = st.sidebar.selectbox(
        "Choose a dataset to explore", 
        ["Population & Unemployment", "Education Levels", "Monthly Rainfall"]
    )

    if data_option == "Population & Unemployment":
        st.write("### Population and Unemployment by District")
        st.caption("Note: Sample/demo data for portfolio demonstration - not official Stats SA data")
        st.dataframe(population_data, use_container_width=True)
        st.bar_chart(population_data.set_index("District")[["Population (Millions)", "Unemployment Rate (%)"]])

        pop_filter = st.slider("Filter by Minimum Population (Millions)", 0.0, 2.0, 0.5)
        filtered_pop = population_data[population_data["Population (Millions)"] >= pop_filter]
        st.write(f"Filtered Results for Population ≥ {pop_filter} Million:")
        st.dataframe(filtered_pop, use_container_width=True)

    elif data_option == "Education Levels":
        st.write("### Education Levels in Eastern Cape")
        st.caption("Note: Sample/demo data for portfolio demonstration")
        col1, col2 = st.columns(2)
        with col1:
            st.dataframe(education_data, use_container_width=True)
        with col2:
            st.bar_chart(education_data.set_index("Level"))

    elif data_option == "Monthly Rainfall":
        st.write("### Average Monthly Rainfall in Eastern Cape (mm)")
        st.caption("Note: Sample/demo data for portfolio demonstration - illustrative climate pattern")
        st.dataframe(climate_data, use_container_width=True)
        st.area_chart(climate_data.set_index("Month"))

elif menu == "Contact":
   elif menu == "Contact":
    st.header("Contact Information")
    st.subheader("📬 Get in Touch")
    st.write("Feel free to reach out for collaborations or opportunities.")
    st.markdown("---")
    st.link_button("📧 Email Me", "mailto:sandisentete@gmail.com", use_container_width=True)
    st.link_button("💼 LinkedIn Profile", "https://www.linkedin.com/in/celokuhle-sandise-ntete-249480278", use_container_width=True)
    st.link_button("💻 GitHub Portfolio", "https://github.com/Celokuhle04", use_container_width=True)
    st.markdown("---")
