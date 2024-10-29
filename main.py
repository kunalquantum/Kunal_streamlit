import streamlit as st

#--page setup 
about_page=st.Page(
    #linking of the page 
    page="views/aboutMe.py",
    title="About Me",
    icon=":material/thumb_up:",
    default=True

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

project2_page=st.Page(
    #linking of the page 
    page="views/project2.py",
    title="Project 2",
    icon=":material/thumb_up:",
    

)


# navigation bar 

pg=st.navigation(
   {
       "Info":[about_page],
       "Smart Data Hub":[project1_page,predictor],
       
   }
    )

st.logo("assets/logo3.png")
st.sidebar.text("Made with ❤ by Kunal")
logo_url="assets/logo3.png"

pg.run()