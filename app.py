import streamlit as st
import joblib
import numpy as np
from template import create_navigation_link, create_card
from tapax import tapaxmodel
import time
from statistics import mode

from transformers import pipeline

st.set_page_config(layout='wide')
# Custom CSS to position the sidebar at the top
model = joblib.load("model.pkl")
st.markdown("""
    <style>
        .sidebar {
            background-color: blue; /* Set the background color of the sidebar */
        }
        .streamlit-iframe {
            margin-top: 80px; /* Adjust the margin to make space for the navigation */
        }
        .navigation-container {
            display: flex;
            justify-content: flex-start;
            align-items: center;
            margin-bottom: 20px;
        }
        .navigation-link {
            margin-right: 20px;
            color: red;
            text-decoration: none;
        }
        .navigation-link:hover {
            color: blue;
        }
    </style>
""", unsafe_allow_html=True)
def main():
    st.sidebar.title("Navigation")
    # Main content
    page_options = ["Home","Data", "Power BI Report","tapax"]#"Declaration"]
    page_selection = st.sidebar.radio("Go to", page_options)

    if page_selection == "Data":
        display_home_page1()
    elif page_selection == "Power BI Report":
        display_power_bi_report()
    elif page_selection == "Declaration":
        Declaration()
    elif page_selection == "Home":
        Home()
    elif page_selection == "tapax":
        T()

def Home():
    
    
    # # Navigation links
    # st.markdown(create_navigation_link("Section 1", "section1"), unsafe_allow_html=True)
    # st.markdown(create_navigation_link("Section 2", "section2"), unsafe_allow_html=True)
    # st.markdown(create_navigation_link("Section 3", "section3"), unsafe_allow_html=True)

        # Create a layout with 4 columns
    col1, col2, col3 = st.columns(3)

    # Section 1
    with col1:
        st.write("<h1 id='section1'>Section 1</h1>", unsafe_allow_html=True)
        st.markdown(create_card("Model", " Model for Prediction average Claim", "#FF5733"), unsafe_allow_html=True) # Red
        # st.markdown(create_card("Card 2", "Content for Card 2 in Section 1", "#FFC300"), unsafe_allow_html=True) # Yellow

    # Section 2
    with col2:
        st.write("<h1 id='section2'>Section 2</h1>", unsafe_allow_html=True)
        # st.markdown(create_navigation_link("Go to Model", "display_home_page1"), unsafe_allow_html=True)
        st.markdown(create_card("Dashboard", "Detailed Report of Life insurance Companies in india ", "#32CD32"), unsafe_allow_html=True) # Green
        # st.markdown(create_card("Card 4", "Content for Card 4 in Section 2", "#3498DB"), unsafe_allow_html=True) # Blue

    # Section 3
    with col3:
        st.write("<h1 id='section3'>Section 3</h1>", unsafe_allow_html=True)
        st.markdown(create_card("Tapax", "Chat with our bot for any queries", "#FF5733"), unsafe_allow_html=True) # Red
        # st.markdown(create_card("Card 6", "Content for Card 6 in Section 3", "#FFC300"), unsafe_allow_html=True) # Yellow


def Declaration():
    st.markdown('<h2 id="data">Declaration</h2>', unsafe_allow_html=True)
    st.write("Done By : Pavan Pyla ,IInd MSc in Data Science and Computing")
    # st.write("")
    st.write("Guided By: Sri Satya Sai Baba Mudigonda and DR Pallav Baruah")
def display_home_page1():
    st.markdown('<h2 id="data">Insurance Data Collector</h2>', unsafe_allow_html=True)
    st.write("Please enter the following details:")
    
    # Input fields for insurance data
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", min_value=0, max_value=150, step=1)
        gender = st.selectbox("Gender", [ "female","male"])
        bmi = st.number_input("BMI", min_value=0.0, max_value=1000.0, step=0.1)
        blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=300, step=1)
    with col2:
        diabetic = st.radio("Diabetic", ["Yes", "No"])
        children = st.number_input("Number of Children", min_value=0, max_value=100, step=1)
        smoker = st.radio("Smoker", ["Yes", "No"])
        region = st.selectbox("Region", ["Northeast", "Northwest", "Southeast", "Southwest"])

     # Button to submit data
    if st.button("Pridict Claim"):
        # Store submitted data in a list
        submitted_data = [age, gender, bmi, blood_pressure, diabetic, children, smoker, region]
        encoded_input = np.zeros(14)  # Total number of unique categories across all categorical variables

        # Encode age, bmi, and blood pressure directly
        encoded_input[0] = age
        encoded_input[1] = bmi
        encoded_input[2] = blood_pressure
        encoded_input[3] = children
        # Encode categorical variables using one-hot encoding
        categorical_variables = {
            "gender": {"female": 4, "male": 5},
            "diabetic": {"Yes": 6, "No": 7},
            "smoker": {"No": 8, "Yes": 9},
            "region": {"Northeast": 10, "Northwest": 11, "Southeast": 12, "Southwest": 13}
        }

        # Update the corresponding indices in the encoded input vector
        if gender in categorical_variables["gender"]:
            encoded_input[categorical_variables["gender"][gender]] = 1
        if diabetic in categorical_variables["diabetic"]:
            encoded_input[categorical_variables["diabetic"][diabetic]] = 1
        if smoker in categorical_variables["smoker"]:
            encoded_input[categorical_variables["smoker"][smoker]] = 1
        if region in categorical_variables["region"]:   
            encoded_input[categorical_variables["region"][region]] = 1


        print('encoded ',encoded_input)


        ##################################################################
        encoded_input1 = np.array(encoded_input)
        print('the models output :   ')
        claim = model.predict([encoded_input1])[0]
        print(claim)
        
        ##################################################################
        # Display submitted data
        st.write("Submitted Data:")
        st.write("Age:", age)
        st.write("Gender:", gender)
        st.write("BMI:", bmi)
        st.write("Blood Pressure:", blood_pressure)
        st.write("Diabetic:", diabetic)
        st.write("Number of Children:", children)
        st.write("Smoker:", smoker)
        st.write("Region:", region)

        st.write('the expected claim will be', claim)


def display_power_bi_report():

    st.markdown('<h2 id="power_bi_report">Power BI Report</h2>', unsafe_allow_html=True)
    st.markdown('<div style="margin-top: 60px;"></div>', unsafe_allow_html=True)


    

    # Define the width of the Power BI report
    report_width = 1450 

    # Power BI report URL
    embed_code = f"""<iframe title="Power BI Report" width="{report_width}" height="850" src="https://app.powerbi.com/view?r=eyJrIjoiYjJkY2E0MjEtNjQ3Mi00ZWQ3LTk2OGEtNjkwYjJlZTJiNGY0IiwidCI6ImFjM2U2NzhlLTEyZWItNGUzYS1iOTBkLTdkOTlmNzE1MWUxMiJ9" frameborder="0" allowFullScreen="true"></iframe>"""

    # Display Power BI report
    st.markdown(embed_code, unsafe_allow_html=True)

    # sidebar_closed = not st.sidebar.expander("Navigation Sidebar", expanded=True)
    # Add a dynamic container for the remaining space if the sidebar is closed
    # if sidebar_closed:
    #     col1, col2 = st.columns([1, 2])
    #     print('Opened the dyna')
    #     # Text content to display beside the Power BI report    
    #     with col2:
    #         st.write("This is the dynamic container that fills the remaining space beside the Power BI report.")


    # embed_code = """<iframe title="end final 2" width="1450" height="850" src="https://app.powerbi.com/view?r=eyJrIjoiYjJkY2E0MjEtNjQ3Mi00ZWQ3LTk2OGEtNjkwYjJlZTJiNGY0IiwidCI6ImFjM2U2NzhlLTEyZWItNGUzYS1iOTBkLTdkOTlmNzE1MWUxMiJ9" frameborder="0" allowFullScreen="true"></iframe>"""

    # st.markdown(embed_code, unsafe_allow_html=True)
    
    


def T():
    # Create an empty list to store input questions
    st.markdown('<h2 id="data">Chat with our AI Bot</h2>', unsafe_allow_html=True)
    # st.write('this is tapax page ')
    # Add input box for question
    questions_list = []
    question_input = st.text_input("Enter your question:")

    # Add button to submit question
    if st.button("Submit"):
        # Add the submitted question to the list
        questions_list.append(question_input)
        # Display the output
        output = tapaxmodel(question_input)
        print(' the output received is ',output)

        st.write('Answer to the Question:', output)

    # # Display the list of suggested questions
    # if questions_list:
    #     st.write("Suggested Questions:")
    #     for question in questions_list:
    #         st.write(question)
         # Apply styling to the answer
       # Apply styling to the answer
        st.markdown(
            f'<div style="background-color: #D4EDDA; padding: 10px; border-radius: 5px; border: 1px solid #C3E6CB; margin-top: 10px; font-family: "Courier New", Courier, monospace;">'
            f'<span style="color: #155724; font-size: 16px; text-transform: capitalize;">'  # Applying camel case
            f'{mode(output)}'
            f'</span>'
            f'</div>',
            unsafe_allow_html=True
        )
    

if __name__ == "__main__":  
    main()


# def Tapax():

