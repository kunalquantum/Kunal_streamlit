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
    page="views/project1.py",
    title="Project 1",
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
       "Projects":[project1_page,project2_page],
   }
    )

st.logo("assets/logo3.png")
st.sidebar.text("Made with ❤ by Kunal")
logo_url="assets/logo3.png"

pg.run()