# Hackathon Infoviz and Project Management

## Background

This project is part of a country by country view of climate change metrics. Among those metrics *(depending on data availability and relevance for the country)* are:

* GHG emissions: latest, per capita, and trend since 1970
* Latest land surface temperature anomalies
* Latest sea surface temperature *(where relevant)* 👈 **OUR FOCUS**
* Climate risk index
* Detailed net-zero targets *(regional and city-level data where available)*
* And about half a dozen more

> **⚠ IMPORTANT NOTE:**  
> **Again, our focus for this hackathon** is *ONLY* the **'Latest sea surface temperature'** metric!

The overall project will be part of a series which includes this interactive:

[![Screenshot of the interactive](preview-climate-change.png)](https://www.unep.org/explore-topics/climate-action/what-we-do/climate-action-note/state-of-climate.html "Climate Action Note")

## Our raw data: Sea surface temperature

NASA's sea surface temperature product shows the temperature of the top millimeter of the ocean's surface. Scientists monitor sea surface temperature because the ocean's warmth influences Earth's climate system in many different ways. The Moderate Resolution Imaging Spectroradiometer (MODIS) instruments aboard NASA's Terra and Aqua satellites collect global measurements of sea surface temperature accurate to within half a degree Celsius.

Here're [more detailed explanations](https://neo.gsfc.nasa.gov/view.php?datasetId=MYD28M)

You can find the data as `gzipped CSVs` in [`./data/raw`](data/raw)

And in different formats here:

* As [`PNGs`](https://neo.gsfc.nasa.gov/archive/rgb/MYD28M/)
* As [`GEOTIFFs`](https://neo.gsfc.nasa.gov/archive/geotiff/MYD28M/)

## Overall objective

## Scenarios and detailed objectives

### Ocean temperature anomalies

|**Team name:** gerbils 🐹|
|------|
|**Members:** Cédric, Esther, Marc Pérez, Àlex|



### Areas of interest

|**Team name:** koalas 🐨|
|------|
|**Members:** Andrea, Daniel, Marc Rojo, Pau|

How do we find any statistically significant clustering in the spatial patterns of these data?

You don't have the sea surface temperature anomalies yet —team gerbils is working on that. But you have two datasets that can help you in the meantime.

### TK TK

|**Team name:** badgers 🦡|
|------|
|**Members:** Sergi, Jonah, Victor, Guillem|


## Day-of schedule

* 09:00 👋 Welcome, reminder of logistics like lunch, drinks, communication channels ...
* 09:15 🙋‍♀️ Standup meeting with us. Objectives, processes, what you want to achieve in the hackathon and any questions.
* 09:30 👩‍💻 Start of work day!
* 13:15 🙋‍♀️ Short standup
* 13:30 🍱 Lunch
* 14:30 👩‍💻 Back to work, switch PMs
* 19:00 🧑‍🏫 Wrap-up presentation < 6 slides 😜: About 5-10 minutes per team.
  * What was achieved?
  * What was helpful?
  * What’s left to do?
* 19:30 🏆 Awards
* 20:00 🥳 End!!!

*We'll come to you, moving from group to group, and we'll be available for questions and solving blocks.*

## Collaboration recommendations

* Follow the Branch Per Feature model: one feature, one branch.
* Prepend each branch with your team name. For example if you're commiting part of your work cleaning up the data, you would push it to a `gerbils--data-cleaning` branch.
* A nice pattern for commit messages is `type: subject` as in `refactor: use map instead of for loop`.

## The awards

As we all know the [professional jury and the popular vote don't always match](https://www.youtube.com/watch?v=4uGN9efcACw), so we're offering two awards: you all decide one via an open vote, we decide the other —which may or may not be the same, and we won't know until we reveal them simultaneously.

🏆 **Popular vote**
🏆 **Jury fav**
