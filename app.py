import streamlit as st
import joblib
import numpy as np
from template import create_navigation_link, create_card
from tapax import tapaxmodel
import time
from statistics import mode
st.set_page_config(layout='wide')
# Custom CSS to position the sidebar at the top
model = joblib.load("rfmodel.pkl")
st.markdown("""
    <style>
        body {
            background-color: white; /* Set the background color of the body */
            color: black; /* Set the text color to black */
        }
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
        Model()
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
def Model():
    st.markdown('<h2 id="data">Next Quarter Premium Predictor</h2>', unsafe_allow_html=True)
    st.write("Please enter the previous quarter detailes:")
    
    # Create two columns for input fields
    col1, col2 = st.columns(2)

    # Input fields for insurance data
    with col1:
        premium_earned = st.number_input("Premium Earned",  step=100000)
        reinsurance_ceded = st.number_input("Reinsurance ceded",  step=10000)
        commission = st.number_input("Commission",  step=50000)
        operating_expenses = st.number_input("Operating Expenses related to Insurance Business",  step=500000)

    with col2:
        benefits_paid = st.number_input("Benefits paid (Net)",  step=5000000)
        surplus_deficit = st.number_input("Surplus/ (Deficit)", step=100000)
        profit_loss = st.number_input("Profit/(Loss) before tax",  step=1000000)
        quarter = st.number_input("Quarter", min_value=1, max_value=4, step=1)
        next_quarter = (quarter + 1) % 5  # Ensuring next_quarter is always 1 greater than quarter, looping back to 1 if quarter is 4
        # Button to submit data
    if st.button("Pridict Claim"):
        # Store submitted data in a list
        submitted_data = [[premium_earned, reinsurance_ceded, commission, operating_expenses, 
                      benefits_paid, surplus_deficit, profit_loss, quarter, next_quarter]]
        
        X_stats = {
        'Premium Earned': {'mean': 41747534.85329082, 'std': 146094084.0133876},
        'Reinsurance ceded': {'mean': -107024.53470663266, 'std': 236078.30073900594},
        'Commission': {'mean': 2475864.940012771, 'std': 9049466.74025776},
        'Operating Expenses related to Insurance Business': {'mean': 4387051.89434949, 'std': 12857930.353998087},
            'Benefits paid (Net)': {'mean': 24469815.146679435, 'std': 90823273.08282025},
        'Surplus/ (Deficit)': {'mean': 868610.6302567394, 'std': 2689396.281981464},
        'Profit/(Loss) before tax': {'mean': 583632.4974712643, 'std': 2259434.401638071},
        'Quarter': {'mean': 0, 'std': 1},
        'next_quarter': {'mean': 0, 'std': 1}
        }
        y_stats = {
        'next_quarter_premium': {'mean': 43094793.73943517, 'std': 149623255.69637465}
        }


        scaled_p = []
        for i, column in enumerate(X_stats.keys()):
            mean = X_stats[column]['mean']
            std = X_stats[column]['std']
            scaled_value = (submitted_data[0][i] - mean) / std
            scaled_p.append(scaled_value)
        scaled_p = np.array(scaled_p).reshape(1, -1)
        print(scaled_p)



        submitted_data = {
        'Premium Earned': premium_earned,
        'Reinsurance ceded': reinsurance_ceded,
        'Commission': commission,
        'Operating Expenses related to Insurance Business': operating_expenses,
        'Benefits paid (Net)': benefits_paid,
        'Surplus/ (Deficit)': surplus_deficit,
        'Profit/(Loss) before tax': profit_loss,
        'Quarter': quarter,
        'next_quarter': next_quarter
            }
    
        # Display submitted data in two columns
        st.write("Submitted Data:")
        columns = st.columns(2)
        with columns[0]:
            st.write("Premium Earned:", premium_earned)
            st.write("Reinsurance ceded:", reinsurance_ceded)
            st.write("Commission:", commission)
            st.write("Operating Expenses related to Insurance Business:", operating_expenses)
        with columns[1]:
            st.write("Benefits paid (Net):", benefits_paid)
            st.write("Surplus/ (Deficit):",surplus_deficit )
            st.write("Profit/(Loss) before tax:",profit_loss )
            st.write("Quarter:", quarter)
        ##################################################################
        


        print('the models output :   ')
        # claim = model.predict(scaled_p)
        claimEarned = (model.predict(scaled_p) * y_stats['next_quarter_premium']['std']) + y_stats['next_quarter_premium']['mean']

        # print("Inverse scaled values:")
        # print(inverse_scaled_values)
        print(claimEarned[0] )
        
        ##################################################################
        # Display submitted data with new feature names
        # st.write("Submitted Data:")
        # for feature_name, value in zip(feature_names, submitted_data):
        #     st.write(f"{feature_name}:", value)

        # Display expected claim in the sidebar with dark green background
        st.markdown(f"<div style='background-color: #072402; padding: 10px; color: #7fa383;'>Expected Next Quarter Premium:</div>", unsafe_allow_html=True)
        st.markdown(f"<div style='background-color: #072402; padding: 10px; color: #25ff00;'>{round(claimEarned[0],2) }</div>", unsafe_allow_html=True)


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
            f'{mode(output).upper()}'
            f'</span>'
            f'</div>',
            unsafe_allow_html=True
        )
    

if __name__ == "__main__":  
    main()


# def Tapax():

