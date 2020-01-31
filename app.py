import streamlit as st

st.header("Therapal")
st.markdown("Getting to know your therapist before scheduling an appointment")

# user input preferences
gender = st.radio(label='Gender Preference', options=('M', 'F'))
setting = st.radio(label='Setting',
         options=('Hospital',
         'Private Practice'))

#make multiselect checkboxes
option_1 = st.multiselect('Which of the following are you experiencing? (Select All)',
('Sleep', 'Bipolar disorders', 'Stress',
'Depression', 'Anxiety', 'Relationships'))
st.write('You selected:', option_1)

option_2 = st.multiselect('Types of treatments (Select All)',
('Group therapy','Psychoanalytic','Psychotherapy',
'Medication','Couple’s therapy','Life coaching','Counseling'))
st.write('You selected:', option_2)

#add selecte stuff to this list
user_doc=[option_1 + option_2]
