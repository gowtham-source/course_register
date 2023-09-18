import streamlit as st
from mail import send_email
from PIL import Image
from mongodb import insert, find

st.write("## Welcome to the course✨")

image = Image.open('ideogram (51).jpeg')


st.image(image)


with st.form("Registration Form"):
    # Input fields
    name = st.text_input('Enter your name')
    mail_id = st.text_input('Enter your mail id')
    ph_no = st.text_input("Enter your Phone no.")

    # "Register" button to submit the form
    submitted = st.form_submit_button("Register")

    # Validation checks upon form submission
    if submitted:
        # Validation checks
        if name == '':
            st.error("Please enter your name.")
        elif not mail_id or "@" not in mail_id or "." not in mail_id:
            st.error("Please enter a valid email address.")
        elif not ph_no or not ph_no.isdigit() or len(ph_no) != 10:
            st.error("Please enter a valid 10-digit phone number.")
        elif find(mail_id)!=None:
            st.error('This mail id has been already registered!')
        else:
            # All inputs are valid, proceed with registration
            # Assuming you have a send_email function
            insert(name=name,ph_no=ph_no, mail_id=mail_id)
            send_email(name=name, receiver_email=mail_id)
            st.success("Registration successful!")