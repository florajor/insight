st.title('Find My Therapist')

df=pd.read_csv("zocdoc_01232020.csv")
#db=pd.read_csv("david-brendel-md-phd-64658.txt.csv")
#df[df["comment"]==np."NaN"]['comment'] = 0
#df["comment"]
df1=df.copy()
df1["comment"]=df["comment"].replace(np.nan," ")
#create temp dataset that replace missing values now read as nan to strring variable

#sentiment analysis
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()

def sentiment_analyzer_scores(comment):
    score = analyser.polarity_scores(comment)
    print("{:-<40} {}".format(comment, str(score)))
    return score

#db.comment=db.comment.apply(sentiment_analyzer_scores)
df1['score']=df1.comment.apply(sentiment_analyzer_scores)

df1['score_neg'] = df1['score'].map(lambda t:t['neg'])
df1['score_pos'] = df1['score'].map(lambda t:t['pos'])
df1['score_neu'] = df1['score'].map(lambda t:t['neu'])
df1['score_comp'] = df1['score'].map(lambda t:t['compound'])
df1.head()

#st.title('Find My Therapist')
model_input = st.text_input("What services are you looking for?","Try CBT")
st.write(model_input)
model_input = st.text_input("Insurance","Try Blue Cross Blue Shield")
st.write(model_input)
st.write(df1['score_comp'])

#do app related stuff, savinging model in lda_model_pkl
pkl_filename = "ldamodel.pkl"
with open(pkl_filename, 'rb') as file:
   ldamodel=pickle.load(file)

#st.title('Find My Therapist')
#model_input = st.text.input("Enter Provider Name","David-Brendel")
#st.write(ldamodel, score_neg, score_pos, score_neu, score_comp)
