import pandas as pd
import streamlit as st

st.set_page_config(page_title="Moderation Tracking Sheet", layout="wide")
st.title("📋 Question Paper Moderation Tracker")

initial_data = [
    {
        "Grade": "Y2",
        "Subject & Task Description": "Afrikaans Huistaal Taak 3 (Eksamen)",
        "Moderator": "",
        "Status": "Pending",
        "Revisions/Comments": "",
    },
    {
        "Grade": "Y2",
        "Subject & Task Description": "English FAL Task 3 (Exam)",
        "Moderator": "",
        "Status": "Pending",
        "Revisions/Comments": "",
    },
    {
        "Grade": "Y2",
        "Subject & Task Description": "Wiskunde Taak 7",
        "Moderator": "",
        "Status": "Pending",
        "Revisions/Comments": "",
    },
    {
        "Grade": "Y2",
        "Subject & Task Description": "Wiskunde Taak 8",
        "Moderator": "",
        "Status": "Pending",
        "Revisions/Comments": "",
    },
    {
        "Grade": "Y2",
        "Subject & Task Description": "Wiskunde Taak 9 (Eksamen)",
        "Moderator": "",
        "Status": "Pending",
        "Revisions/Comments": "",
    },
    {
        "Grade": "Y2",
        "Subject & Task Description": "Natuurwetenskap Taak 5 (Prakties)",
        "Moderator": "",
        "Status": "Pending",
        "Revisions/Comments": "",
    },
    {
        "Grade": "Y2",
        "Subject & Task Description": "Natuurwetenskap Taak 6 (Eksamen)",
        "Moderator": "",
        "Status": "Pending",
        "Revisions/Comments": "",
    },
    {
        "Grade": "Y2",
        "Subject & Task Description": (
            "Liggaamlike Opvoeding Taak 2 (Prakties)"
        ),
        "Moderator": "",
        "Status": "Pending",
        "Revisions/Comments": "",
    },
    {
        "Grade": "Y3",
        "Subject & Task Description": "Afrikaans Huistaal Taak 3 (Eksamen)",
        "Moderator": "",
        "Status": "Pending",
        "Revisions/Comments": "",
    },
    {
        "Grade": "Y3",
        "Subject & Task Description": "English FAL Task 3 (Exam)",
        "Moderator": "",
        "Status": "Pending",
        "Revisions/Comments": "",
    },
    {
        "Grade": "Y3",
        "Subject & Task Description": "Wiskunde Taak 7",
        "Moderator": "",
        "Status": "Pending",
        "Revisions/Comments": "",
    },
    {
        "Grade": "Y3",
        "Subject & Task Description": "Wiskunde Taak 8",
        "Moderator": "",
        "Status": "Pending",
        "Revisions/Comments": "",
    },
    {
        "Grade": "Y3",
        "Subject & Task Description": "Wiskunde Taak 9 (Eksamen)",
        "Moderator": "",
        "Status": "Pending",
        "Revisions/Comments": "",
    },
    {
        "Grade": "Y3",
        "Subject & Task Description": "Natuurwetenskap Taak 5 (Prakties)",
        "Moderator": "",
        "Status": "Pending",
        "Revisions/Comments": "",
    },
    {
        "Grade": "Y3",
        "Subject & Task Description": "Natuurwetenskap Taak 6 (Eksamen)",
        "Moderator": "",
        "Status": "Pending",
        "Revisions/Comments": "",
    },
    {
        "Grade": "Y3",
        "Subject & Task Description": (
            "Liggaamlike Opvoeding Taak 2 (Prakties)"
        ),
        "Moderator": "",
        "Status": "Pending",
        "Revisions/Comments": "",
    },
]

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

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(initial_data)

edited_df = st.data_editor(
    st.session_state.df,
    column_config={
        "Moderator": st.column_config.SelectboxColumn(
            "Moderator", options=moderators, required=False
        ),
        "Status": st.column_config.SelectboxColumn(
            "Status", options=statuses, required=True
        ),
    },
    hide_index=True,
    use_container_width=True,
)

st.session_state.df.update(edited_df)
