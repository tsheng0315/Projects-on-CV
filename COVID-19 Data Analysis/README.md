# COVID-19-Data-Analysis

* This project is based on COVID-19 dataset published by John Hopkins University, which consist of the data related to cumulative number of confirmed cases, per day, in each Country. 

* The second dataset consist of various life factors, scored by the people living in each country around the globe. 

* The target of this project is to see if there is any relationship between the spread of the the virus in a country and how happy people are, living in that country.

### Task 1: Check COVID-19 dataset 
* Get a general outlook of COVID-19 dataset

### Task 2: Finding a good Measure
* Decide on and calculate a good measure for our analysis.
* Transmission of COVID-19 in China, Italy, and the UK

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/COVID-19%20Data%20Analysis/graph/cases%20in%20three%20countries%20in%20total%20.png)

* Infection rate in China

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/COVID-19%20Data%20Analysis/graph/infection%20rate%20in%20china.png)

* Aggregate Rows and Get The Maximum Infection Rate in Each Country

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/COVID-19%20Data%20Analysis/graph/max%20infection%20rate.png)

### Task 3: Importing World happiness report dataset
* Merge World happiness report dataset, dropping useless columns, with COVID19 dataset to find correlations among our data.
* Happiness Report

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/COVID-19%20Data%20Analysis/graph/Happiness%20.png)

* Merged Table

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/COVID-19%20Data%20Analysis/graph/joined%20table.png)

* Correlation Matrix of Merged Table

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/COVID-19%20Data%20Analysis/graph/correlation%20matrix%20between%20happiness%26infection.png)

### Task 4: Visualizing the results
* Visualize results using `Seaborn`.
* The relationship between `Max Infection Rate` and `GDP` in each country.

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/COVID-19%20Data%20Analysis/graph/New%20infection%20%26%20gdp.png)

* The relationship between `Max Infection Rate` and `Social support` in each country.

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/COVID-19%20Data%20Analysis/graph/new%20infection%26social.png)

* The relationship between `Max Infection Rate` and `Healthy life expectancy` in each country.

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/COVID-19%20Data%20Analysis/graph/new%20infection%26%20life%20expexctancy.png)

* From the graph, it seems the infection rate in well developed countries are higher. But people may say it is because in developing countries many cases haven't been detected. So we turn to maximum death rate for help.

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/COVID-19%20Data%20Analysis/graph/death%20rate%26%20GDP%20in%203.png)

## Summary
As we can see from the graphs, the infection rate and death rate in developed countries are slightly higher than in developing countries.

According to my analysis, I think developed nations have more people who travel - and hence the 'initial wave' of infections would generally hit devceloped nations first. 

Now that much more time has passed, we see developing nations are only now getting their exposure to the virus. Case in point Mexico. While USA had a large quantity of cases, Mexico was slow to diagnose patients as having Covid19. 

I personally feel that the death rate will be higher in developing countries than in developed countries. It would be more interesting to re-do this study say in June 2021 after more time has passed to collect a new set of statistics. 

In addition, there are medical doctors going on record in developed country USA stating they were (figuratively) having their arms twisted via some very out-of-the-ordinary directives being sent by CDC to label deaths (without doing proper determination of cause) as being due to covid19 - which would SKEW the death rates in such a developed country. While I can not say for sure, but possibly a similar agenda took place in other developed nations.
