# Milesone 2: Project proposal and initial analyses

## Table of Contents
1. [Abstract](#Abstract)
2. [Research Questions](#Research-Questions)
3. [Proposed additional datasets](#Proposed-additional-datasets)
4. [Methods](#Methods)
5. [Proposed timeline](#Proposed-timeline)
6. [Organization within the team](#Organization-within-the-team)
7. [Questions for TAs](#Questions-for-TAs)


## Abstract
**Evolution of sinophobic sentiment and propaganda in the United States of America from 2015 to 2020** <br/>
For the past few decades, China’s domestic growth and increased worldwide influence, along with economic and social instability in the US, have presented a threat to the idea of American exceptionalism. As a result, several prominent American political figures and media outlets have been fearmongering about the consequences of a stronger Chinese state. This, in turn, has increased anti-Asian and anti-Chinese sentiment among the general population, as exemplified in 2020 by the creation of *#StopAsianHate*, which aimed to bring to light the violent effect of scapegoating China for the Covid-19 pandemic on Asian-American citizens.

## Research Questions 
During the project, first we would like to analyse a bit more the **sinophobic sentiment in the USA** through the quotes.
* Can we see an evolution of the sinophobic sentiment in the USA?
* What form/distribution does it have?
* If yes, is it correlated with some special events (COVID crisis, ...)? Are they sudden spikes?
* From which part of the population does the sinophobic sentiment come from: citizens? Political parties? From which generation/range of ages?

Secondly, we want to analyse the opposite part: those who raise theirs voices **against this anti-Chinese sentiment in the USA**.
* who has been advocating for the anti-racism?
* From where does it come from: from the Asian-American citizens or from non-Asian-American citizens? Politicians or citizens?
* And how this defense takes place: through accusations (more violent) or by showing the absurdity of this sentiment (by pedagogy)?

## Proposed additional datasets 
We want to use the tool Empath as an additional dataset, which can  analyse text across hundreds of data-driven categories. It will help us to validate a lexical categories on demand on our quotes. It is a dictionnary-based approaches about sentiment (see [Fast, Ethan, Binbin Chen, and Michael S. Bernstein. "Empath: Understanding topic signals in large-scale text." *Proceedings of the 2016 CHI conference on human factors in computing systems.* 2016.](https://arxiv.org/pdf/1602.06979.pdf)).

## Methods
The aim of this project would be to analyse the sentiment of quotes related to China thanks to an appropriate pre-trained model (*Empath tool, see in [additional datasets](#Proposed-additional-datasets) section*): ideally, we would be able to observe both the strength of the sentiment and the amount of polarised quotes within the dataset through time.

In order to to it, we will:
* To gain a better understanding of the source, quotes would be sorted by their most likely speaker, keeping only those of American nationality, and further sorted by their occupation.
* Show main evolutions of sinophobic sentiment throug graphs.
* We use the tool Empath to analyse our quotes and range them in categories of sentiments.
* We oppose analysis about sinophobic sentiment in the USA and analysis about anti-sinophobic sentiment.

## Proposed timeline
- Milestone 3.1: Statistical & graphical analysis for answering [Research Questions](#Research-Questions)
- Milestone 3.2: Finish & review of research questions
- Milestone 3.3: Notebook presentation & explanations

## Organization within the team 
Until project Milestone 3:

- *Zied:* finish to find which speaker is the good one + finish sorted the quotes
- *Kepler:* categorization of quotes with the Empath dataset
- *Francesca:* main evolutions of sinophobic sentiment + main observations
- *Anne :* oppose analysis about sinophobic sentiment in the USA and analysis about anti-sinophobic sentiment

## Questions for TAs 
- Some quotes have muliple qids referencing the same name, how to be sure wich speaker to choose?
- Pertinance of our analysis?

