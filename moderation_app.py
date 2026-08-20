import pandas as pd
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Moderation Tracking Sheet", page_icon="📋", layout="wide"
)

st.title("📋 Question Paper Moderation Tracker")
st.markdown("Year 2 and Year 3 Question Papers for Moderation")

# Define the dataset
initial_data = [
    {
        "Grade": "Y2",
        "Subject & Task Description": "Afrikaans Huistaal Taak 3 (Eksamen)",
        "Moderator": "",
        "Status": "Pending",
        "Date Submitted": None,
        "Revisions/Comments": "",
        "Date Finalized": None,
    },
    {
        "Grade": "Y2",
        "Subject & Task Description": "English FAL Task 3 (Exam)",
        "Moderator": "",
        "Status": "Pending",
        "Date Submitted": None,
        "Revisions/Comments": "",
        "Date Finalized": None,
    },
    {
        "Grade": "Y2",
        "Subject & Task Description": "Wiskunde Taak 7",
        "Moderator": "",
        "Status": "Pending",
        "Date Submitted": None,
        "Revisions/Comments": "",
        "Date Finalized": None,
    },
    {
        "Grade": "Y2",
        "Subject & Task Description": "Wiskunde Taak 8",
        "Moderator": "",
        "Status": "Pending",
        "Date Submitted": None,
        "Revisions/Comments": "",
        "Date Finalized": None,
    },
    {
        "Grade": "Y2",
        "Subject & Task Description": "Wiskunde Taak 9 (Eksamen)",
        "Moderator": "",
        "Status": "Pending",
        "Date Submitted": None,
        "Revisions/Comments": "",
        "Date Finalized": None,
    },
    {
        "Grade": "Y2",
        "Subject & Task Description": "Natuurwetenskap Taak 5 (Prakties)",
        "Moderator": "",
        "Status": "Pending",
        "Date Submitted": None,
        "Revisions/Comments": "",
        "Date Finalized": None,
    },
    {
        "Grade": "Y2",
        "Subject & Task Description": "Natuurwetenskap Taak 6 (Eksamen)",
        "Moderator": "",
        "Status": "Pending",
        "Date Submitted": None,
        "Revisions/Comments": "",
        "Date Finalized": None,
    },
    {
        "Grade": "Y2",
        "Subject & Task Description": "Liggaamlike Opvoeding Taak 2 (Prakties)",
        "Moderator": "",
        "Status": "Pending",
        "Date Submitted": None,
        "Revisions/Comments": "",
        "Date Finalized": None,
    },
    {
        "Grade": "Y3",
        "Subject & Task Description": "Afrikaans Huistaal Taak 3 (Eksamen)",
        "Moderator": "",
        "Status": "Pending",
        "Date Submitted": None,
        "Revisions/Comments": "",
        "Date Finalized": None,
    },
    {
        "Grade": "Y3",
        "Subject & Task Description": "English FAL Task 3 (Exam)",
        "Moderator": "",
        "Status": "Pending",
        "Date Submitted": None,
        "Revisions/Comments": "",
        "Date Finalized": None,
    },
    {
        "Grade": "Y3",
        "Subject & Task Description": "Wiskunde Taak 7",
        "Moderator": "",
        "Status": "Pending",
        "Date Submitted": None,
        "Revisions/Comments": "",
        "Date Finalized": None,
    },
    {
        "Grade": "Y3",
        "Subject & Task Description": "Wiskunde Taak 8",
        "Moderator": "",
        "Status": "Pending",
        "Date Submitted": None,
        "Revisions/Comments": "",
        "Date Finalized": None,
    },
    {
        "Grade": "Y3",
        "Subject & Task Description": "Wiskunde Taak 9 (Eksamen)",
        "Moderator": "",
        "Status": "Pending",
        "Date Submitted": None,
        "Revisions/Comments": "",
        "Date Finalized": None,
    },
    {
        "Grade": "Y3",
        "Subject & Task Description": "Natuurwetenskap Taak 5 (Prakties)",
        "Moderator": "",
        "Status": "Pending",
        "Date Submitted": None,
        "Revisions/Comments": "",
        "Date Finalized": None,
    },
    {
        "Grade": "Y3",
        "Subject & Task Description": "Natuurwetenskap Taak 6 (Eksamen)",
        "Moderator": "",
        "Status": "Pending",
        "Date Submitted": None,
        "Revisions/Comments": "",
        "Date Finalized": None,
    },
    {
        "Grade": "Y3",
        "Subject & Task Description": "Liggaamlike Opvoeding Taak 2 (Prakties)",
        "Moderator": "",
        "Status": "Pending",
        "Date Submitted": None,
        "Revisions/Comments": "",
        "Date Finalized": None,
    },
]

# Moderator List Options
moderators = [
    "",
    "B. KOENZE",
    "D. DAVIDS",
    "K. ABRAHAMS",
    "S. ST JERRY",
    "U. DE VILLIERS",
    "A. PRESSEND",
    "M. MURRAY",
]
statuses = ["Pending", "In Review", "Approved"]

# Initialize Session State for persistence while app runs
if "tracker_df" not in st.session_state:
    st.session_state.tracker_df = pd.DataFrame(initial_data)

# Sidebar filters or actions
st.sidebar.header("Controls & Filters")
selected_mod = st.sidebar.selectbox(
    "Filter by Moderator", ["All"] + moderators[1:]
)

df_display = st.session_state.tracker_df.copy()
if selected_mod != "All":
    df_display = df_display[df_display["Moderator"] == selected_mod]

# Editable Dataframe UI
st.markdown("### Edit and Update Tracking Details Below:")
edited_df = st.data_editor(
    df_display,
    column_config={
        "Moderator": st.column_config.SelectboxColumn(
            "Moderator", options=moderators, required=False
        ),
        "Status": st.column_config.SelectboxColumn(
            "Status", options=statuses, required=True
        ),
    },
    hide_index=True,
    num_rows="fixed",
    use_container_width=True,
)

# Update main session state from editor changes
st.session_state.tracker_df.update(edited_df)

# Export options
st.markdown("---")
col1, col2 = st.columns(2)


# Function to convert df to CSV
@st.cache_data
data
def convert_df(df):
    return df.to_csv(index=False).encode("utf-8")


csv_data = convert_df(st.session_state.tracker_df)

with col1:
    st.download_button(
        label="📥 Export Tracking Sheet to CSV",
        data=csv_data,
        file_name="moderation_tracker.csv",
        mime="text/csv",
    )