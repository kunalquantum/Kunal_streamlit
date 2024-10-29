import streamlit as st  

predictor=st.Page(
    #linking of the page 
    page="project1/predictor.py",
    title="predictor",
    icon=":material/thumb_up:",



)

cleaner=st.Page(
    #linking of the page 
    page="project1/cleaner.py",
    title="Project 2",
    icon=":material/thumb_up:",
    

)
# Check if the 'page' key exists in the session_state; if not, default to 'home'  
if 'page' not in st.session_state:  
    st.session_state.page = 'home'  

# Navigation Logic  
def navigate_to(page):  
    st.session_state.page = page  

# Title of the application  
st.title("SmartData Hub")  

# Depending on the selected page, render the respective content  
if st.session_state.page == 'home':  
    # Description of the project  
    st.markdown("""  
    **Automated Model Training**:   
    This project aims to provide intelligent selection and training of regression and classification models tailored to the specific characteristics of your dataset.  
    """)  

    # Features Section  
    st.header("Key Features")  

    # Feature 1: Automated Model Training  
    with st.expander("1. Automated Model Training", expanded=True):  
        col1, col2 = st.columns(2)  

        with col1:  
            st.image("assets/automated.jpeg", caption="Automated Model Training", use_column_width=True)  

        with col2:  
            st.write("- Intelligent model selection.")  
            st.write("- Adaptation to specific dataset characteristics.")  
            st.write("- Regression and classification capabilities.")  

    # Feature 2: Automated Clustering  
    with st.expander("2. Automated Clustering", expanded=False):  
        col1, col2 = st.columns(2)  

        with col1:  
            st.image("assets/clustering.jpeg", caption="Automated Clustering", use_column_width=True)  

        with col2:  
            st.write("- Choose from 6 clustering algorithms.")  
            st.write("- Specify the number of clusters.")  
            st.write("- Tailored clustering approaches.")  

    # Feature 3: Ensemble Learning Comparisons  
    with st.expander("3. Ensemble Learning Comparisons", expanded=False):  
        col1, col2 = st.columns(2)  

        with col1:  
            st.image("assets/ensemble.jpeg", caption="Ensemble Learning", use_column_width=True)  

        with col2:  
            st.write("- Evaluate ensemble techniques.")  
            st.write("- Identify the optimal model.")  
            st.write("- Compare model performances.")  

    # Feature 4: Multivariate Analysis  
    with st.expander("4. Multivariate Analysis", expanded=False):  
        col1, col2 = st.columns(2)  

        with col1:  
            st.image("assets/multivariate.jpeg", caption="Multivariate Analysis", use_column_width=True)  

        with col2:  
            st.write("- In-depth analysis of multiple variables.")  
            st.write("- Uncover hidden relationships.")  
            st.write("- Insightful data exploration.")  

    # Feature 5: Data Cleaning  
    with st.expander("5. Data Cleaning", expanded=False):  
        col1, col2 = st.columns(2)  

        with col1:  
            st.image("assets/cleaning.jpeg", caption="Data Cleaning", use_column_width=True)  

        with col2:  
            st.write("- Automated data cleaning processes.")  
            st.write("- Ensure high-quality training inputs.")  
            st.write("- Prepare datasets efficiently.")  

    # Feature 6: Interactive Visualization Dashboards  
    with st.expander("6. Interactive Visualization Dashboards", expanded=False):  
        col1, col2 = st.columns(2)  

        with col1:  
            st.image("assets/vizualizer.jpeg", caption="Visualization Dashboards", use_column_width=True)  

        with col2:  
            st.write("- User-friendly visualizations.")  
            st.write("- Understand data distributions.")  
            st.write("- Analyze model performance easily.")  
