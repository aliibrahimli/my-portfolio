import streamlit as st


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")
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