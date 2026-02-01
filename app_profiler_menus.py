import streamlit as st
import pandas as pd
import numpy as np

# Set page title
st.set_page_config(page_title="Eastern Cape Research Dashboard", layout="wide")

# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Researcher Profile", "Research Publications", "Eastern Cape Data Explorer", "Contact"],
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
if menu == "Researcher Profile":
    st.title("Reseacher Profile")
    st.sidebar.header("Profile Options")

    # Basic profile info
    name = "Mr Celokuhle Ntete"
    institution = "University of Fort Hare"
    field = "Mathematics"
    province_name = "Eastern Cape"
    country = "South Africa"
    capital = "Bisho"
    
    st.write(f"**Name:** {name}")
    st.write(f"**Institution:** {institution}")
    st.write(f"**Field:** {field}")
    st.write(f"**Province Name:** {province_name}")
    st.write(f"**Country:** {country}")
    st.write(f"**Capital City:** {capital}")
    
    st.image(
        "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg",
        caption="Eastern Cape Landscape (Pixabay)"
    )

elif menu == "Research Publications":
    st.title("Research Publications")
    st.sidebar.header("Upload and Filter")

    uploaded_file = st.file_uploader("Upload a CSV of Eastern Cape publications", type="csv")
    if uploaded_file:
        publications = pd.read_csv(uploaded_file)
        st.dataframe(publications)

        keyword = st.text_input("Filter by keyword", "")
        if keyword:
            filtered = publications[
                publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
            ]
            st.write(f"Filtered Results for '{keyword}':")
            st.dataframe(filtered)
        else:
            st.write("Showing all publications")

        if "Year" in publications.columns:
            st.subheader("Publication Trends")
            year_counts = publications["Year"].value_counts().sort_index()
            st.bar_chart(year_counts)
        else:
            st.write("The CSV does not have a 'Year' column to visualize trends.")

elif menu == "Eastern Cape Data Explorer":
    st.title("Eastern Cape Data Explorer")
    st.sidebar.header("Data Selection")
    
    data_option = st.sidebar.selectbox(
        "Choose a dataset to explore", 
        ["Population & Unemployment", "Education Levels", "Monthly Rainfall"]
    )

    if data_option == "Population & Unemployment":
        st.write("### Population and Unemployment by District")
        st.dataframe(population_data)

        pop_filter = st.slider("Filter by Minimum Population (Millions)", 0.0, 2.0, 0.5)
        filtered_pop = population_data[population_data["Population (Millions)"] >= pop_filter]
        st.write(f"Filtered Results for Population ≥ {pop_filter} Million:")
        st.dataframe(filtered_pop)

    elif data_option == "Education Levels":
        st.write("### Education Levels in Eastern Cape")
        st.dataframe(education_data)
        st.bar_chart(education_data.set_index("Level"))

    elif data_option == "Monthly Rainfall":
        st.write("### Average Monthly Rainfall in Eastern Cape (mm)")
        st.dataframe(climate_data)
        st.area_chart(climate_data.set_index("Month"))

elif menu == "Contact":
    st.header("Contact Information")
    st.markdown("""
    ### 📬 Get in Touch
    **Email:** sandisentete@gmail.com
    **Phone:** +27 67 306 3895
    **Institution / Affiliation:** University of Fort Hare
    **Location:** Eastern Cape, South Africa

    You can reach out for collaborations, publications, or data inquiries.
    """)



