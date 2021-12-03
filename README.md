# *Final project:* Evolution of sinophobic sentiment and propaganda in the United States of America from 2015 to 2020

## Table of Contents
1. [Abstract](#Abstract)
2. [Research Questions](#Research-Questions)
3. [Proposed additional datasets](#Proposed-additional-datasets)
4. [Methods](#Methods)
5. [Proposed timeline](#Proposed-timeline)
6. [Organization within the team](#Organization-within-the-team)
7. [Contributions of all group members](#Contributions-of-all-group-members)


## Abstract
For the past few decades, China’s domestic growth and worldwide influence augmentation, along with economic and social instability in the US, have presented a threat to the idea of American exceptionalism. As a result, several prominent American political figures and media outlets have been fearmongering about the consequences of a stronger Chinese state. This, in turn, has increased anti-Asian and anti-Chinese sentiment among the general population, as exemplified in 2020 by the creation of *#StopAsianHate*, which aimed to bring to light the violent effect of scapegoating China for the Covid-19 pandemic on Asian-American citizens.
> TO DO: written down a conclusion explaining better what the analysis is about and given a brief statement of your project's main objective.


## Research Questions 
During this project, we would like to, firstly, analyse more the **sinophobic sentiment in the USA** through the quotes.
* Can we see an evolution of the sinophobic sentiment in the USA?
* What form/distribution does it have?
* If yes, is it correlated with some special events (COVID crisis, ...)? Are there sudden spikes?
* From which part of the population does the sinophobic sentiment come from: citizens? Political parties? From which generation/range of ages?

Secondly, we want to analyse the opposite part: those who raise theirs voices **against this anti-Chinese sentiment in the USA**.
* Who has been advocating for the anti-racism?
* From where does it come from: Politicians or citizens?
* And how these defenses takes place: through accusations (more violent) or by showing the absurdity of this sentiment (by pedagogy)?

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
The aim of this project would be to analyse the sentiment of quotes related to China thanks to an appropriate pre-trained model (*Empath tool, see in [additional datasets](#Proposed-additional-datasets) section*): ideally, we would be able to observe both the strength of the sentiment and the amount of polarised quotes within the dataset through time.
In order to do it, we will:
* to extract the quotations related to China, we implement an Information Retrieval tool. (TO DO)
* To gain a better understanding of the source, quotes would be sorted by their most likely speaker, keeping only those of American nationality, and further sorted by their occupation.
* In addition, to have more data, We add to the quotes those without most likely speaker but that come from an american paper.
* Show main evolutions of sinophobic sentiment throug graphs.
What | How | For what
| :--- | ---: | :---:
Content Cell  | Content Cell | Content Cell
Content Cell  | Content Cell | Content Cell


* 	USA Map, with scale of color (darker where there is more sinophobic sentiment), Widget to change the year (2015 2020)
-	Explain some sudden increase in the Sinophobia (Covid …)
-	Show categories of population (age range, education type, citizen status) that are sinophobic (ex: pie chart, bar chart)
-	Same Map but with anti-racist 
-	 maybe plot them next to each other to see if it is the same type of people or not, or in the same state
* We use the tool VADER to analyse the sentiment of our quotes and obtain their scores of sentiment (from -1 to 1) (see [Proposed additional datasets](#Proposed-additional-datasets)).
* We oppose analysis about sinophobic sentiment in the USA and analysis about anti-sinophobic sentiment.

> "Based on the research questions, the steps you intend to follow are not clear enough. For example, which kind of analysis do you want to perform? And, which tools are you going to use? For instance, you could explain your procedure better by making use of some workflow charts."

## Proposed timeline
For the Milestone 2 we only used the quotes of 2020 to simplify our research. However, for Milestone 3, we will use quotes from 2015 to 2020 .

* Milestone 3.1 (week 9 & 10): Add quotations from american papers, statistical & graphical analysis for answering [Research Questions](#Research-Questions)
* Milestone 3.2 (week 11): Finish & review of research questions
* Milestone 3.3 (week 12 & 13): Notebook presentation & explanations, and bonus (Quotebank issue reporting) <br/>
=> Due: 17 Dec 2021

## Organization within the team 
Until project Milestone 3:
* *Zied:* finish to find which speaker is the good one + finish sort and filter the quotes
* *Kepler:* categorization of quotes with the Empath dataset
* *Francesca:* main evolutions of sinophobic sentiment + main observations
* *Anne:* oppose analysis about sinophobic sentiment in the USA and analysis about anti-sinophobic sentiment
* *all:* Bonus (Quotebank issue reporting)

## Contributions of all group members 
> TO DO

