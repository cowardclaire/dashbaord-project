import streamlit as st

st.set_page_config(
    page_title="Global Movers",
    page_icon="🌍",
)

def main():
    st.sidebar.title("Navigation")


    choice=st.sidebar.radio("Go to", ["Dashboard","Tool"])
                                     
    if choice=="Dashboard":
        show_dashboard()
    elif choice=="Tool":
        show_converter()

def show_dashboard():  
    """Function to display the dashboard page."""
    st.header("Company Dashboard")
    st.info("Welcome to the company dashboard! Here you can find insights and analytics about our operations.")

    col1,col2 = st.columns(2)

    with col1:
        st.subheader("Speed Limits")
        st.write("Urban: 50 km/h")
        st.write("Highway: 100 km/h")

    with col2:
        st.subheader("Cargo Safety")
        st.write("Maximum load: 20,000 kg")
        st.write("Take breaks every 4 hours")

def show_converter():
    st.header("Weight Converter")
    st.write("-----------------------")
    st.write("Convert between kilograms and pounds.")

    weight = st.number_input("Enter weight", min_value=0.0, step=0.1)
    conversion_type = st.selectbox("Conversion type", ["Kilograms to Pounds", "Pounds to Kilograms"])

    if st.button("Convert"):
        if conversion_type == "Kilograms to Pounds":
            result = weight * 2.20462
            st.success(f"{weight} kg is equal to {result:.2f} lbs")
        else:
            result = weight / 2.20462
            st.success(f"{weight} lbs is equal to {result:.2f} kg") 

main()