import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    image =Image.open("images/photo.png")
    new_image = image.resize((450, 500))
    st.image(new_image)

with col2:
    st.title("Ali Ibrahimli")
    content = """ I am Ali Ibrahimli, a senior student of computer engineering at Ada University, with 
    experience as a developer at Connect Telecommunication Company. I have 
    proficiency in programming languages such as Python and Java, as well as 
    experience working with Django and Flask libraries. I am also familiar with API 
    development and integration. As a student of computer engineering, I have a strong 
    foundation in computer science principles and programming concepts, which allows me 
    to solve complex problems and develop innovative solutions. With my skills and experience, 
    I am excited to take on new challenges and make meaningful contributions to the technology industry.
    """
    st.info(content)

content2 = "Below you can find some of the apps I have built in Python. " \
           "Feel free to contact me!"
st.write(content2)