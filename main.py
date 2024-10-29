import streamlit as st

#--page setup 
about_page=st.Page(
    #linking of the page 
    page="views/aboutMe.py",
    title="About Me",
    icon=":material/thumb_up:",
    default=True

)


clustering=st.Page(
    #linking of the page 
    page="project1/clustering.py",
    title="Clustering",
    icon=":material/thumb_up:",

)
multivariate=st.Page(
    #linking of the page 
    page="project1/multivariate.py",
    title="Multivariate",
    icon=":material/thumb_up:",

)
cleaner=st.Page(
    #linking of the page 
    page="project1/cleaner.py",
    title="cleaner",
    icon=":material/thumb_up:",

)

ensemble=st.Page(
    #linking of the page 
    page="project1/ensemble.py",
    title="ensemble",
    icon=":material/thumb_up:",

)

project1_page=st.Page(
    #linking of the page 
    page="views/SmartDataHub.py",
    title="Home Page",
    icon=":material/thumb_up:",



)
#smart data hub
predictor=st.Page(
    #linking of the page 
    page="project1/predictor.py",
    title="Predictor",
    icon=":material/thumb_up:",



)

Timeseries=st.Page(
    #linking of the page 
    page="project1/TimeSeries.py",
    title="TimeSeries",
    icon=":material/thumb_up:",



)

# navigation bar 

pg=st.navigation(
   {
       "Info":[about_page],
       "Smart Data Hub":[project1_page,predictor,ensemble,cleaner,clustering,multivariate]
   }
    )

st.logo("assets/logo3.png")
st.sidebar.text("Made with ❤ by Kunal")
logo_url="assets/logo3.png"


import streamlit as st

# Your main app code here

# Footer message
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        margin-right:1550px;
        width: 100%;
        text-align: center;
        font-size: large;
        color: gray;
    }
    </style>
    <div class="footer">
        © 2024 Kunal Sharma. All rights reserved.
    </div>
    """,
    unsafe_allow_html=True
)

pg.run()