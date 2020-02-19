# TheraPal - Getting to Know Your Mental Health Providers
A web app that recommends mental health providers, created using StreamLit and deployed using heroku

## Motivation
One in four Americans experience a mental illness in the past year, yet half of them remain untreated. One of reasons for this treatment gap is the difficulty to find a therapist. Currently, people in search of therapists would have to go to at least two sites, to gather information on the clinicians’ expertise from directories as well as patients’ experience with the providers from review sites. 

## Data
The database constitutes 382 reviews that contain 15K words provided by patients scraped from health grades and zoc doc, as well as 25 clinician bios from Psychology Today, using Beautiful Soup. 

## Analyses
In TheraPal_Sentiment.ipynb, I used VADER to performed sentiment analyses to better communicate patients’ experience.

In TheraPal_LDA.ipynb, I used Gensim to conduct Latent Dirichlet Allocation (LDA) on the clinicians' bio to get a better idea of what the clinicians actually specialized in. 

## Recommender
App.py contains a content-based recommender that compares the key words of the clinicians expertise (stored in topic_words.csv and topic_matrix.csv) with the app user input of their needs (stored in user_blank.csv) using cosine similarity. 

##References
https://towardsdatascience.com/evaluate-topic-model-in-python-latent-dirichlet-allocation-lda-7d57484bb5d0
https://towardsdatascience.com/how-to-build-from-scratch-a-content-based-movie-recommender-with-natural-language-processing-25ad400eb243

##Credit
Special thanks to Yang Li on the step-by-step guide in her project that used similiar approaches:
https://github.com/yangli53/happy_meals
