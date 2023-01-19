import streamlit as st
from PIL import Image

st.set_theme('dark')

st.title("Guitar Gallery")

# Add a selectbox to the sidebar
guitars = ["Gibson Les Paul", "Fender Stratocaster", "Ibanez RG"]
guitar_choice = st.sidebar.selectbox("Select a guitar", guitars)

# Show the selected image
if guitar_choice == "Gibson Les Paul":
    st.image("gibson_les_paul.jpg")
elif guitar_choice == "Fender Stratocaster":
    st.image("fender_stratocaster.jpg")
elif guitar_choice == "Ibanez RG":
    st.image("ibanez_rg.jpg")
