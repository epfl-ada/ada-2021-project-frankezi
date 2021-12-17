import interactive
from interactive import predicate_quote_similarity, get_analysis
import numpy as np
from PIL import Image
import streamlit as st
from streamlit.components import v1 as comp

from pathlib import Path
import base64

st.markdown("""
<style>
a, a:hover, a:active, a:visited, a:link {
    font-weight:bold;
    color:inherit;
    text-decoration:none;
}
</style>
""",
    
    unsafe_allow_html=True)

st.sidebar.markdown("""<h2 align="center" style="color:white;">Table of contents</h2>""", unsafe_allow_html=True)
st.sidebar.markdown(
"""
<ol style="color:white; text-decoration:none; margin-left:8%">
    <li><a href="#asian-hate-an-american-horror-story">Introduction</a></li>
    <li><a href="#american-dream-always-a-national-ethos-of-the-united-states">American Dream</a></li>
    <li><a href="#motivations-and-data-sorting">Motivations and data sorting</a></li>
    <li><a href="#sinophobia-through-the-usa-evolution-from-2015-to-2020">Sinophia evolution from 2015 to 2020</a></li>
    <li><a href="#did-it-exist-prior-to-the-covid-crisis">Did it exist prior to the COVID crisis?</a></li>
    <li><a href="#racism-underlying-explanations">Racism: underlying explanations</a></li>
    <li><a href="#age-range-education-and-citizen-status">Age, Education and Citizen status</a></li>
    <li><a href="#jobs">Positions of influence</a></li>
    <li><a href="#conclusion">Conclusion</a></li>
    <li><a href="#is-this-quote-sinophobic">Is this quote sinophobic...? (Interactive)</a></li>
    <li><a href="#not-so-fun-fact">(Not so) Fun fact</a></li>
    <li><a href="#about-us">About Us</a></li>
    <li><a href="#tools-used">Tools used</a></li>
    
<ol>
""", unsafe_allow_html=True)

#st.sidebar.radio("", ["Intro", "Evolution"])

title_image = Image.open("assets/stophateasian.jpg")
st.image(title_image, use_column_width='always',
         caption="Dia Dipasupil/Getty Images/AFP")

st.markdown("""
    <h1 align="center" style="h1">
    Asian hate: an American (Horror) story?</h1>
""", unsafe_allow_html=True
)

st.markdown("""
<p align="center">Applied Data Analysis project 2021-2022 by <a href="https://github.com/epfl-ada/ada-2021-project-frankezi">frankezi</a></p>

***
""", unsafe_allow_html=True)

#---------------------------------------------------------------#
# ANALYSIS
#---------------------------------------------------------------#

st.header("Introduction")
st.subheader("American Dream: always a national ethos of the United States ?")
st.markdown(
    """
    the past few decades, China’s domestic growth and worldwide growing influence,
    along with economic and social instability in the US, have presented a threat to the idea of American exceptionalism:“Make America Great Again!”.
    As a result, several prominent American political figures and media outlets have been fearmongering about the consequences of a stronger Chinese state.
    This, in turn, has increased anti-Asian and anti-Chinese sentiment (called Sinophobia) among the general population,
    as exemplified in 2020 by the creation of #StopAsianHate, which aimed to bring to light the violent effect of scapegoating
    China for the Covid-19 pandemic on Asian-American citizens (6% of the United States population).

    According to Wikipedia, the Sinophobia is defined as: “a sentiment against China, its people, overseas Chinese, or Chinese culture. It often targets Chinese minorities living outside of China and involves immigration, [...] disparity of wealth,
    the past central tributary system, majority-minority relations, imperial legacies, and racism."

It should be noted that Donald Trump, president of the USA from 2017 to 2020, referred to the new coronavirus as the “Chinese virus” or the “kung flu”, publicly expressing what can only be considered as racist comments...

    """
    )


st.subheader("Motivations and data sorting")
st.markdown(
    """
    The most obvious question raised is : When did Sinophobia originate in the USA? The recent COVID-19 crisis raised this question and made it a public case. But is it really a new phenomenon?
    
    After researching the evolution of the American Sino phobic sentiment through the years, it would be interesting to see the exact origins of this Sinophobia. Racism, as a concept originating from a major event (i.e. the COVID crisis, the fear of war, etc.), can often be explained by underlying factors: prejudice of a bygone era, political factions relying on racism to obtain support, the occupation of the speaker, etc. On the end of the spectrum, does the lack of a racist undertone depend on the level of education?
    
    In order to answer these questions, quotes related to China made between 2015 and 2020 were pulled using an Information Retrieval tool from the Quotebank dataset: an open corpus of 178 million quotes attributed to their speakers, extracted from 162 million English news articles. To gain a better understanding of the source, the quotes pulled were be sorted by their attributed speaker, keeping only those of American nationality, and further sorted by their occupation. To further the analysis, unattributed quotes coming from American papers were also added to the data pool. The monitoring tool, VADER, was then used to analyse the sentiment of the pooled quotes to obtain their scores of sentiments.
    """
    )

st.header('Sinophobia through the USA: evolution from 2015 to 2020')
st.subheader("Did it exist prior to the COVID crisis?")

st.markdown(
    """
    In order to understand the origins of this racism against Asian-American citizens, it is crucial to learn more about the evolution of the Sino phobic sentiment in the USA.
    
    Using the dataset, we will plot a graph of the numbers of Sino phobic quotes through time.
    """
    )
#plot

analysis_throught_time = Image.open("assets/analysis_through_time.jpeg")
st.image(analysis_throught_time, use_column_width='auto')

analysis_throught_time_boxplot = Image.open("assets/analysis_through_time_boxplot.png")
st.image(analysis_throught_time_boxplot,use_column_width='auto')


st.markdown(
    """
    We calculated the average compound of the quotes per day, and we plotted it. As demonstrated by the graph, in 2015, there was an average around 0.2. From 2016 to 2017, we can observe that the quotes compounds are more extreme on both sides. At the beginning of 2019, we can start to notice a small decrease in the quote’s positivity. The increase in Sinophobia is clearly seen in 2020 with a decrease in the quote’s compound. We believe that the increased Sinophobia is the consequence of the COVID-19 crisis. Since Quote Bank doesn’t provide quotes after April 2020, we can only imagine that Sinophobia continued increasing with the spread of the pandemic.
    
    From the boxplots we computed, we can notice a decrease in the average compound in 2016. That same year, Donald Trump, campaigning for the Republican Party's presidential nomination, publicly accused China of “raping” the US on the topic of exportations. After he became president of the USA, he continued to spew horrors about China. This could have led to an increase of feelings of a lack of security and feeling threatened by other groups, which are insecurities believed to increase racism.
    
    From 2020 we can verify that there is an evident lower median in the quote’s compound, meaning that more Sino phobic quotes have been published in the media.
    """
    )

evolution2020 = Image.open("assets/evolution2020.jpeg")
st.image(evolution2020 , use_column_width='auto')

st.markdown(
    """
    In this section, we have looked specifically at the quotes from 2020, seen as the beginning of the worldwide COVID-19 crisis. We can notice that there is an increase in both categories. However, it should be noted that once looked more attentively the date suggests that in January the positives quotes were double the amount of the Sino phobic ones. When looking at the other months of that year, one can see that the difference between the two diminished and that the number of Sino phobic quotes increased.
    """
    )

st.header("Racism: underlying explanations")
st.subheader("Age range, Education and Citizen status?")
st.markdown(
    """
    As explained in the introduction, racism can often be due to underlying reasons. We want to answer the following question: What is the background of people who publicly engage in Sino phobic behaviour online. We first focused on looking at the age ranges, their education and their citizenship status.
    
    For instance, we could imagine to see an increase of sinophobic sentiment within people that didn't study because they may have been exposed to less diversity during their life. Or we could imagine seeing an increase of sinophobic sentiment within older people, which are often less world-friendly, open-minded, or on the contrary, seeing an increase of sinophobic sentiment in younger people, who may equate immigration and loss of jobs.


 
    """
    )
#plots
ages_ranges = Image.open("assets/ages_ranges.jpeg")
st.image(ages_ranges, use_column_width='auto')
ages_boxplot = Image.open("assets/ages_boxplot.jpeg")
st.image(ages_boxplot, use_column_width='auto')

st.markdown(
    """
    In these plots, we wanted to visualize if there was a difference in the ages from the sinophobic or non-sinophobic quotes’ speakers. We remark that the average age for sinophobic speakers is sensibly higher. After performing a t-test, we conclude that the difference is significant. In average, sinophobic speakers are older… We think that it is a typical example of the definition of “being from a different time”.  
    """
    )

education = Image.open("assets/education.jpeg")
st.image(education, use_column_width='always')

st.markdown(
    """
    Then, we thought to look if sinophobia could be explained by the education background the speaker received. We looked in a difference between positive and negative quotes but nothing that could explain the difference is seen because both parties have quite the same repartition. 
    """
    )

gender = Image.open("assets/gender.jpeg")
st.image(gender, use_column_width='always')

st.markdown(
    """
    The next feature that we thought that could explain the difference in the speaker’s sentiments is their gender. But no major difference is seen because both types of sentiment have the same gender repartition.
    """
    )


political_ideas = Image.open("assets/political_ideas.jpeg")
st.image(political_ideas, use_column_width='always')

st.markdown(
    """
    Finally we wanted to look at the political parties through the speakers, however this feature doesn't seems have an influence on the anti-Asian hate.
        """
    )

st.subheader("Jobs?")
st.markdown(
    """
    It is known that the fear of job loss represents a potentially important source of racism. In order to prove or 
    discard this theory on our dataset, we will look at the most sinophobic jobs versus the least sinophobic jobs. 
    There could be an interesting relation between the jobs and their rhetoric. For example, we could 
    imagine that people that do more highly-educated jobs that require more studies and a lot of reflection could be 
    less sinophobic compared to people that do more manual jobs and didn't study. However, this could be
    counterbalanced by the fact that often politicians, which have a highly-educated job, can engage in and weaponize
    sinophobia and therefore influence many others.
    
    For example, we could imagine that people with intellectual jobs that require more ethical considerations could be less
    sinophobic compared to people with manual jobs. It is also link with their studies: less study, more manual jobs.
    Anyway, this theory about intellectual jobs could be counterbalanced by the fact that often politicians, can be
    tend to be appreciated by the electors and also to say what a certain part of America want to hear.
    
    """
    )
#plots
jobs = Image.open("assets/jobs.jpeg")
st.image(jobs, use_column_width='always')

st.markdown(
    """
    The next feature which we thought could explain the difference in the speaker’s sentiments is their job.
    From the pie chart that we plotted we can't see any significative evidence.
    However, we decided to look further into one of the most high-profile jobs: politician.
    """
    )

political_evolution = Image.open("assets/politician_evolution.jpeg")
st.image(political_evolution, use_column_width='always')

st.markdown(
    """
    We can see that at the beginning of 2020, the compound score had more variance and was mainly positive.
    Within a few months we can see that it starts to converge towards a lower score. This shows that there are more sinophobic quotes.
    With these results we could imagine that if we had data which extends to later in 2020,  we could see a bigger difference in the sinophobic rhetoric.
    """
    )

st.header("Conclusion")
st.subheader("")
st.markdown(
    """
    Through our analysis, we have determined that the rhetoric from politicians
    has become increasingly sinophobic in recent times. This increase is not necessarily linked
    to COVID-19 as it can be traced back to 2015. Some contributing factors to the generally
    negative sentiment from politicians are their age and gender, as US politicians are mostly white males.
    These contributing factors could be further analyzed to gain a better understanding of their correlation.
    Perhaps with additional datasets, which include the location of the speaker, we could map out regions from
    which the negative rhetoric is originating.
    Furthermore, anti-Asian racism is not the only form of racism in the US. The racism against African-Americans
    is predominant, as exemplified in 2020 by the creation of  #BlackLivesMatter following the murder of George 
    Floyd by a police officer. Another prevalent form of racism exists against the Latino population, who have been called “rapists” by Donald Trump.
    
    Our analysis only scratches the surface of the social dynamics and race relations of US society. With additional datasets
    and more reliable methods, we could establish more solid relationships between different factors.
    
    """
    )

st.header("Is this quote sinophobic...?")
st.subheader("")
st.markdown(
    """
    In this final section, you can give our model a try by writing any sentence into the form.
    Our model will then assess whether the sentence is related to China and analyze the overall
    sentiment.
    """
    )

# Interactive part

form = st.form(key='my_form')
form_input = form.text_input(label='Write a statement!', placeholder='I love China!')
form_submit = form.form_submit_button(label='Analyze')

china_rel = st.write("")

sentiment_analysis = st.write("")

if (form_submit):
    rel = None
    sent = None
    if (predicate_quote_similarity({'quotation': form_input})):
        rel = " indeed "
    else:
        rel = " not "

    sentiments = get_analysis(form_input)

    c_score = sentiments['compound']
    if (c_score <= -0.1):
        sent = " negative"
    elif (c_score >= 0.1):
        sent = " positive"
    else:
        sent = " neutral"
    
    china_rel = st.write(f'Our model has determined that this quote is**{rel}**related to China.')
    sentiment_analysis = st.write(f'The quote is perceived as **{sent}**. (VADER compound score: {c_score})')



st.header("(Not so) Fun fact")
st.subheader("")
st.markdown("""Donald Trump called himself the “latest racist on earth”... We let you judge this fact.
             """)




st.header(" ")
st.subheader("About us")
st.slider("How ADAorable are we", min_value=0, max_value=100, value=None, step=None, format=None, key=None, help=None, on_change=None,
          args=None, kwargs=None)

col1,col2 = st.columns(2)

group = Image.open("assets/group.jpeg")
col1.image(group, use_column_width='always')

col2.markdown(
    """
    - **Francesca Trifoni:** MSc in Life Sciences \[ [email](mailto:francesca.trifoni@epfl.ch) | [github](https://www.github.com/francescatrifoni) \]
    - **Anne Bissay:** MSc in Life Sciences, specialized in Neurocomputing \[ [email](mailto:anne.bissay@epfl.ch) | [github](https://www.github.com/bissay) \]
    - **Kepler Warrington-Arroyo:** MSc in Data Science \[ [email](mailto:kepler.warrington-arroyo@epfl.ch) | [github](https://www.github.com/bitshrine) \]
    - **Zied Mustapha:** MSc in Data Science \[ [email](mailto:zied.mustapha@epfl.ch) | [github](https://www.github.com/Laniakea1999) \]      
    """
    )


st.markdown("## Tools used")
st.markdown("""
- [VADER sentiment](https://github.com/cjhutto/vaderSentiment) for sentiment analysis
> **Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.**
- [gensim](https://radimrehurek.com/gensim/) for topic modelling
> **Rehurek, R., & Sojka, P. (2011). Gensim–python framework for vector space modelling. NLP Centre, Faculty of Informatics, Masaryk University, Brno, Czech Republic, 3(2).
**
"""
)
