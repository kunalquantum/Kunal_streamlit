import streamlit as st
from streamlit_option_menu import option_menu
from apps import Split_map, home, heatmap, upload # import your app modules here

st.set_page_config(page_title=" MAP",page_icon=":globe_with_meridians:", layout="wide")


# A dictionary of apps in the format of {"App title": "App icon"}
# More icons can be found here: https://icons.getbootstrap.com

apps = [
    {"func": home.app, "title": "Home", "icon": "house"},
    {"func": heatmap.app, "title": "Heatmap", "icon": "map"},
    {"func": upload.app, "title": "Upload", "icon": "cloud-upload"},
    {"func": Split_map.app, "title": "Split_map", "icon": "file-code"},
]

titles = [app["title"] for app in apps]
titles_lower = [title.lower() for title in titles]
icons = [app["icon"] for app in apps]

params = st.experimental_get_query_params()
if "page" in params:
    default_index = int(titles_lower.index(params["page"][0].lower()))
else:
    default_index = 0

with st.sidebar:
    selected = option_menu(
        "Main Menu",
        options=titles,
        icons=icons,
        menu_icon="cast",
        default_index=default_index,
    )

    st.sidebar.title("About")
    st.sidebar.info(
        """
            The Earth map, also known as a world map or a globe, is a representation of our planet's surface, providing a visual depiction of its geographical features, political boundaries, and various natural and man-made landmarks. It serves as a crucial tool for understanding and navigating our complex and diverse world.
        """
    )

for app in apps:
    if app["title"] == selected:
        app["func"]()
        break


