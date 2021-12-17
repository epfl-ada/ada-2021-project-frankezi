# *Final project:* Evolution of sinophobic sentiment in the United States of America from 2015 to 2020
Our data-Story: https://share.streamlit.io/bitshrine/ada-website/main/app.py#sinophobia-through-the-usa-evolution-from-2015-to-2020

## Table of Contents
1. [Abstract](#Abstract)
2. [Research Questions](#Research-Questions)
3. [Proposed additional datasets](#Proposed-additional-datasets)
4. [Methods](#Methods)
5. [Contributions of all group members](#Contributions-of-all-group-members)


## Abstract
For the past few decades, China’s domestic growth and worldwide influence augmentation, along with economic and social instability in the US, have presented a threat to the idea of American exceptionalism. As a result, several prominent American political figures and media outlets have been fearmongering about the consequences of a stronger Chinese state. This, in turn, has increased anti-Asian and anti-Chinese sentiment among the general population, as exemplified in 2020 by the creation of *#StopAsianHate*, which aimed to bring to light the violent effect of scapegoating China for the Covid-19 pandemic on Asian-American citizens. 

The first evident question that came through our minds is: from when is there Sinophobia in the USA? We want to know if this phenomenon appears during COVID-19 crisis only. After studying a bit more the evolution of the sinophobic sentiment through the years in the USA, it seems interesting to discover from where does this Sinophobia exactly came from. Racism, even if growing from a major event (like the COVID crisis, the fear of a war, etc.), can often be explained by more subjacent reasons: older generations? Political ideas? Jobs? Or against, does racism depend on education...?


## Research Questions 
During this project, we would like to analyse the **sinophobic sentiment in the USA** through the quotes.
* Can we see an evolution of the sinophobic sentiment in the USA?
* What form/distribution does it have?
* If yes, is it correlated with some special events (COVID crisis, ...)? Are there sudden spikes?
* From which part of the population does the sinophobic sentiment more frequently come from: citizens? Political parties? From which generation/range of ages?
* Is your favorite American sinophobic? You can test 20 personnalities, to know if she said something about China.

## Proposed additional datasets 

We were very interesting by coupling our project with the  field  of  natural  language  processing (called NLP)  that  analyzes people's  opinions,  sentiments,  evaluations,  attitudes, and  emotions  via  the  computational  treatment  of  subjectivity  in  text. 

**Milestone 2:** We first wanted to use the tool Empath as an additional dataset to validate lexical categories, on demand, on our quotes (see [Fast, Ethan, Binbin Chen, and Michael S. Bernstein. "Empath: Understanding topic signals in large-scale text." *Proceedings of the 2016 CHI conference on human factors in computing systems.* 2016.](https://arxiv.org/pdf/1602.06979.pdf)). 

**Update for milestone 3:** 
After receiving the feedback of the Milestone 2, we change our plans and decided to use the more effective tool **VADER** (**V**alence  **A**ware  **D**ictionary  for  s**E**ntiment  **R**ea-soning).

> *"VADER  performed  as  well  as (and in most cases, better than) eleven other highly regard-ed sentiment analysis tools."* - [Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.](https://ojs.aaai.org/index.php/ICWSM/article/view/14550/14399)

The tool VADER is using a bag of words approach as seen in the ADA course. It will allow us to quantify the opinion mining of our quotes by obtaining a score for each quote, representing the positivity (if from 0 to 1) or the negativity (from 0 to -1), based on the proportion of positive, neutral or negative word in sentences.
A good point with this tool is that it will take into account little word as for example “really” or “so”, and it will look for negations ("not", "not so", ...) while scoring the sentiment of a sentence. The only disadvantage of this tool is that Out of Vocab words that the sentiment analysis tool has not seen before will not be classified as positive/negative: we decided that it will not be a barrier for our project, considering that typos or very unusual words do not happen frequently in the quotes, and stay rare events.

We decided not looking at the punctuations while analysing the sentiment of quotes.

## Methods
The aim of this project would be to analyse the sentiment of quotes related to China thanks to an appropriate pre-trained model (*VADER tool, see in [additional datasets](#Proposed-additional-datasets) section*): ideally, we would be able to observe both the strength of the sentiment and the amount of polarised quotes within the dataset through time.

In order to do it, we will:

**DATA SORTING**
* Extract the quotations related to China. In order to do so, we implement an Information Retrieval tool. (TO DO)
* To gain a better understanding of the source, quotes would be sorted by their most likely speaker, keeping only those of American nationality, and further sorted by their occupation.
* In addition, to have more data, We add to the quotes those without most likely speaker but that come from an american paper.
* We use the tool VADER to analyse the sentiment of our quotes and obtain their scores of sentiment (from -1 to 1) (see [Proposed additional datasets](#Proposed-additional-datasets)).

**ANALYSIS**
* Show main evolutions of sinophobic sentiment through graphs.
  * Graph of evolution of numbers of sinophobic quotes through time, and explain some sudden increase in the Sinophobia (Covid …)
* Show from which part of the population the Sinophobia comes from.
  * Show categories of population (age range, education type, citizen status) that are sinophobic (through pie chart, bar chart, ...)
  * podium of top jobs that are the most sinophobic vs top jobs that are the less sinophobic
  * Graph of evolution of numbers of sinophobic quotes through time for the top of sinophobic jobs vs top less sinophobic: we found that for sinophobic and non-sinophobic, politicians are the most represented. We also shows evolution of sinophobia of quotes through years ony for politicans.
* Propose a set of American personalities, where you can pich one name
  * Obtained number of sinophobic quotes
  * Obtained number of non-sinophobic quotes

## Contributions of all group members 
* *Zied:* website creation, optimization of notebooks, load of data
* *Kepler:* sentiment analysis, information retrievals
* *Francesca:* writing of functions to collect info about speakers, website optimization
* *Anne:* writing of code for website, collect info about speakers, plotly graphs
* *all:* Bonus (Quotebank issue reporting), corrections of errors, optimization and brain storming



