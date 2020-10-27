# Predict Future Product Prices using Facebook Prophet

Developed a time series forecasting model to predictions on the price of avocado accross the US using Facebook Prophet.



## Task 3: EXPLORE DATASET

* To better understand the distribution of average price, here I painted a histograph.

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/Predict%20Future%20Product%20Prices%20using%20Facebook%20Prophet/graph/task%203%20distribution%20of%20average%20price.png)

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/Predict%20Future%20Product%20Prices%20using%20Facebook%20Prophet/graph/task%203%20violin%20graph.png)

* We can find from the violin graph, the average price of organic avocado is higher than the conventional. And the distribution of orgainc avocados and conventional avocados. 

* plot Bar Chart to indicate the number of regions. 

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/Predict%20Future%20Product%20Prices%20using%20Facebook%20Prophet/graph/task%203%20region%20barchart.png)

* As can be found from the bar chart, the distribution between regions is quite even, which is good.


* plot Bar Chart to indicate the count in every year to see whether data equally recorded among years or not.

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/Predict%20Future%20Product%20Prices%20using%20Facebook%20Prophet/graph/task%203%20region%20barchart.png)

Then I use `catplot()` function to provide access to several axes-level functions that show the relationship between a numerical and one or more categorical variables using one of several visual representations. 

* Compare the avocado prices vs. regions for conventional avocados.

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/Predict%20Future%20Product%20Prices%20using%20Facebook%20Prophet/graph/task%203%20conventional.png)

* Compare the avocado prices vs. regions for organic avocados. 

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/Predict%20Future%20Product%20Prices%20using%20Facebook%20Prophet/graph/task%203%20organic.png)
* The price of organic avocado in San Francisco is relatively high, especially in 2017

## TASK 4: PREPARE THE DATA BEFORE APPLYING FACEBOOK PROPHET

The data that I actually need are just `Date` and `Average Price`. Here we drop the rest. 


## Task 5: INTUITION BEHIND FACEBOOK PROPHET

* Prophet is a procedure for forecasting time series data based on an additive model where non-linear trends are fit with yearly, weekly, and daily seasonality, plus holiday effects.
* It works best with time series that have strong seasonal effects and several seasons of historical data. 
* Prophet is robust to missing data and shifts in the trend, and typically handles outliers well.

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/Predict%20Future%20Product%20Prices%20using%20Facebook%20Prophet/graph/task%205%20prophet%201.png)

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/Predict%20Future%20Product%20Prices%20using%20Facebook%20Prophet/graph/task%205%20prophet%202.png)

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/Predict%20Future%20Product%20Prices%20using%20Facebook%20Prophet/graph/task%205%20prophet%203.png)

## TASK 6: DEVELOP MODEL AND MAKE PREDICTIONS - PART A

* Numerical result of prediction: 
![](https://github.com/tsheng0315/Projects-on-CV/blob/main/Predict%20Future%20Product%20Prices%20using%20Facebook%20Prophet/graph/task%206%20prediction%20table.png)

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/Predict%20Future%20Product%20Prices%20using%20Facebook%20Prophet/graph/task%206%20prediction%20visualisation.png)
* Black dots are our data, and also our training data. The blue part is our prodiction in the future. 

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/Predict%20Future%20Product%20Prices%20using%20Facebook%20Prophet/graph/task%206%20overall.png)
* As we can see from the graph, the price actually went down from 2015-02 to 1.3 m dollars, and then went up to reach the peak of 1.6 m dollars. Then truned down afterwards. 
* According to the prediction, the price will turn down in the following days. 

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/Predict%20Future%20Product%20Prices%20using%20Facebook%20Prophet/graph/task6%20yearly.png)

* This graph shows you the yearly pattern. 
* In the beginning of the year, the price peaked up, and reached the peak around October and November. 
* And then price goes down until January. 

## TASK 7: DEVELOP MODEL AND MAKE PREDICTIONS (REGION SPECIFIC) - PART B

In this part, we just focous on the west region of the US to get more accurate predictions. 

* Here I plot `Date` and `Average Price` to give a general idea of what the trend is in the west of the US. 

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/Predict%20Future%20Product%20Prices%20using%20Facebook%20Prophet/graph/task%207%20general%20histograph.png)

* As Prophet making predictions on column `ds` and `y`, here I turn independent variabls and dependent variables into the corresponding column names. 

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/Predict%20Future%20Product%20Prices%20using%20Facebook%20Prophet/graph/task%207%20ds%20and%20y.png)

* Here is the graph showing my predictions, and we can see the price will actually go up here in west of US.

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/Predict%20Future%20Product%20Prices%20using%20Facebook%20Prophet/graph/Task%207%20west%20past%2B%20future.png)


![](https://github.com/tsheng0315/Projects-on-CV/blob/main/Predict%20Future%20Product%20Prices%20using%20Facebook%20Prophet/graph/task%207%20trend%20%26%20yearly.png)
* The trend of average price drops down a little bit from 2015-02 to 2016-02, then it climbs up till 2019-02.
* The price has been fluctuating during a year, reached it's peak around October. 



