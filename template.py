import streamlit as st

# Page configurations
# st.set_page_config(
#     page_title="Interactive Streamlit Home",
#     page_icon=":house:",
#     layout="wide"
# )

# Function to create a navigation link
def create_navigation_link(label, target_section):
    return f'<a href="#{target_section}">{label}</a>'

# Function to create a card
def create_card(title, content, color):
    return f"""
    <div style='padding: 20px; margin-bottom: 20px; border-radius: 5px; box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1); background-color: {color};'>
        <h2>{title}</h2>
        <p>{content}</p>
    </div>
    """



# # Navigation links
# st.markdown(create_navigation_link("Section 1", "section1"), unsafe_allow_html=True)
# st.markdown(create_navigation_link("Section 2", "section2"), unsafe_allow_html=True)
# st.markdown(create_navigation_link("Section 3", "section3"), unsafe_allow_html=True)

# # Section 1
# st.write("<h1 id='section1'>Section 1</h1>", unsafe_allow_html=True)
# st.markdown(create_card("Card 1", "Content for Card 1 in Section 1"))
# st.markdown(create_card("Card 2", "Content for Card 2 in Section 1"))

# # Section 2
# st.write("<h1 id='section2'>Section 2</h1>", unsafe_allow_html=True)
# st.markdown(create_card("Card 3", "Content for Card 3 in Section 2"))
# st.markdown(create_card("Card 4", "Content for Card 4 in Section 2"))

# # Section 3
# st.write("<h1 id='section3'>Section 3</h1>", unsafe_allow_html=True)
# st.markdown(create_card("Card 5", "Content for Card 5 in Section 3"))
# st.markdown(create_card("Card 6", "Content for Card 6 in Section 3"))
