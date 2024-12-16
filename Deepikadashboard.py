import streamlit as st

# Function to save new user credentials
def signup_page():
    st.title("📝 Sign Up")
    st.write("Create a new account to access the Power BI Dashboard.")

    # Input fields for sign-up
    new_username = st.text_input("Username", placeholder="Enter a unique username")
    new_password = st.text_input("Password", type="password", placeholder="Enter a password")
    confirm_password = st.text_input("Confirm Password", type="password", placeholder="Re-enter your password")

    # Initialize session state to store users if it doesn't exist
    if "users" not in st.session_state:
        st.session_state["users"] = {}

    # Button to sign up
    if st.button("Sign Up"):
        if new_username in st.session_state["users"]:
            st.error("Username already exists. Please choose a different one.")
        elif not new_username or not new_password:
            st.error("Username and password cannot be empty.")
        elif new_password != confirm_password:
            st.error("Passwords do not match. Please try again.")
        else:
            # Save the new user credentials
            st.session_state["users"][new_username] = new_password
            st.success("Sign-up successful! You can now log in.")
            st.info("Go back to the Sign In page.")

# Function for login page
def login_page():
    st.title("🔐 Sign In")
    st.write("Please log in to access the Power BI Dashboard.")

    # Input fields for login
    username = st.text_input("Username", placeholder="Enter your username")
    password = st.text_input("Password", type="password", placeholder="Enter your password")

    # Login button
    if st.button("Sign In"):
        # Check user credentials
        if "users" not in st.session_state or username not in st.session_state["users"]:
            st.error("User not found. Please sign up first.")
        elif st.session_state["users"][username] == password:
            st.session_state["authenticated"] = True
            st.session_state["current_user"] = username
            st.success("Login successful! Redirecting...")
        else:
            st.error("Invalid username or password. Please try again.")

# Power BI Dashboard Page
def dashboard_page():
    st.title("Interactive Air Quality Index (2018 -2022)")
    st.write(f"Welcome *{st.session_state['current_user']}*! Air Quality Index Dashboard!")

    # Power BI Embed URL
    power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiMWE2YWFiYzYtMjM2Ny00YTg1LTg3MmMtZTM4ZGNkMjlhZTQ4IiwidCI6ImY1YjcxNDhiLTNmYzYtNDYwNi04MjgzLWM3MjJmNDQzOGYxMiJ9"
    # Embed Power BI Dashboard using iframe
    st.markdown(
        f"""
        <iframe 
            src="{power_bi_url}" 
            width="100%" 
            height="600" 
            frameborder="0" 
            allowfullscreen="true">
        </iframe>
        """,
        unsafe_allow_html=True
    )

    # Sign-out button
    if st.button("Sign Out"):
        st.session_state["authenticated"] = False
        st.session_state["current_user"] = None
        st.experimental_rerun()

# Main App Logic
def main():
    # Initialize session state for authentication and user management
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False
    if "current_user" not in st.session_state:
        st.session_state["current_user"] = None
    if "users" not in st.session_state:
        st.session_state["users"] = {}  # Store users as username: password

    # Navigation between Sign In and Sign Up
    menu = ["Sign In", "Sign Up"]
    choice = st.sidebar.selectbox("Navigation", menu)

    if st.session_state["authenticated"]:
        dashboard_page()
    elif choice == "Sign In":
        login_page()
    elif choice == "Sign Up":
        signup_page()

# Run the Streamlit App
if _name_ == "_main_":
    main()
