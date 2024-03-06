import streamlit as st
import joblib
import numpy as np
st.set_page_config(layout='wide')
# Custom CSS to position the sidebar at the top
model = joblib.load("model.pkl")
st.markdown("""
    <style>
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
            color: black;
            text-decoration: none;
        }
        .navigation-link:hover {
            color: blue;
        }
    </style>
""", unsafe_allow_html=True)


def main():


    # Main content
    page_options = ["Data", "Power BI Report","Declaration"]
    page_selection = st.radio("Go to", page_options)

    if page_selection == "Data":
        display_home_page1()
    elif page_selection == "Power BI Report":
        display_power_bi_report()
    elif page_selection == "Declaration":
        Declaration()

def Declaration():
    st.markdown('<h2 id="data">Declaration</h2>', unsafe_allow_html=True)
    st.write("Done By : Pavan Pyla ,IInd MSc in Data Science and Computing")
    # st.write("")
    st.write("Guided By: Sri Satya Sai Baba Mudigonda and DR Pallav Baruah")
def display_home_page1():
    st.markdown('<h2 id="data">Insurance Claim Predictor </h2>', unsafe_allow_html=True)
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
    # Power BI report URL
    power_bi_report_url = "https://app.powerbi.com/reportEmbed?reportId=8cfe6010-5acc-4355-aea8-b6cbb050a840&autoAuth=true&ctid=ac3e678e-12eb-4e3a-b90d-7d99f7151e12"

    # Display Power BI report using iframe
    st.components.v1.iframe(power_bi_report_url, width=1450, height=750)

if __name__ == "__main__":
    main()
