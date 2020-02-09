import streamlit as st
import numpy as np
import pandas as pd

st.header("TheraPal")
st.markdown("Getting to know your therapist before scheduling an appointment")

# user input preferences
#gender = st.radio(label='Gender Preference', options=('M', 'F'))

option_1 = st.radio(label='Setting',
         options=('Hospital',
         'Private Practice'))

#make multiselect checkboxes
option_2 = st.multiselect('Which of the following are you struggling with? (Select All)',
('sleep', 'bipolar', 'stress',
'depression', 'anxiety', 'relationship', 'anxiety' ))
st.write('You selected:', option_2)

option_3 = st.multiselect('Types of therapies (Select All)',
('group','psychoanalytic','psychotherapy','medication','couple','psychiatry'))
st.write('You selected:', option_3)

user_input = ""
input=option_1 + option_2 + option_3
user_input.join(input) 

#load user_df, dfr, matrix and therapist_bio
user_df = pd.read_csv('user_blank.csv')
user_df.rename(index={0: 'user'}, inplace=True)
dfr = pd.read_csv('topic_words.csv')
matrix = pd.read_csv('topic_matrix.csv')
matrix.set_index('Provider')
bio = pd.read_csv('therapist_bio.csv')
bio.set_index('Provider')

#fill in 1 based on user input
for word in user_input:
    user_df[word] = 1

#append user_df with topic words to compare
compare = pd.concat([dfr, user_df])

#compute cosine similarity
sim = cosine_similarity(compare.to_numpy())
df_sim = pd.DataFrame(data=sim,
                      index=compare.index.tolist(),
                      columns=compare.index.tolist())

#get the cluster number
cluster = str(df_sim[df_sim.user == df_sim.user[:-1].max()].index[0]) #str

#pull therapist from the respective cluster
def top_therapist(cluster, top_n=3, df=matrix):
    name_list = df.sort_values(cluster, ascending=False)[:top_n].index.tolist()
    return name_list
therapist = top_therapist(cluster) #list of therapist
result = bio.loc[therapist,:] #df
result[['Location', 'Insurance']] #df

#display the results 
for i in range(3):
    provider = results.index[i]
    location = results.Location[i]
    insurance = results.Insurance[i]
    st.write(f'Provider: {provider}\nLocation: {location}\nInsurance: {insurance}\n')
