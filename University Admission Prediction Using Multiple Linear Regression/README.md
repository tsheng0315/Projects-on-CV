# University Admission Prediction Using Multiple Linear Regression

## Project Overview: 

This project aims at predicting the chance of being admitted into a particular University using regression.

## Project Structure

### Task 1: Problem Statement and Background

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/University%20Admission%20Prediction%20Using%20Multiple%20Linear%20Regression/graphs/intro.png)

### Task 2: Check data-sets

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/University%20Admission%20Prediction%20Using%20Multiple%20Linear%20Regression/graphs/raw%20data.png)

As shown in the table, the column 'Chance of Admit' is the result we hope to predict.

And as the value in column 'Chance of Admit' is continuous, here I use Regression Model (If it is binary values like True/False, then we go for Classfication). 

### Task 3: Perform Exploratory Data Analysis 

Here I perform exploratory data analysis and standardize the training and testing data.

The desciption of data:

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/University%20Admission%20Prediction%20Using%20Multiple%20Linear%20Regression/graphs/description%20of%20raw%20data.png)

Group the data by university ratings to show more detailed information.

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/University%20Admission%20Prediction%20Using%20Multiple%20Linear%20Regression/graphs/raw%20data%20group%20by%20rating.png)

As we can see from the table, on average, the higher reating the university is, the higher GRE/TOEFL/GPA score, longer SOP, more strengh on Letter Of Recommendation and REsearch Experience students are. And chances of getting admitted are higher as well.

### Task 4: Perform Data Visualization

Create  histographs to obtain a general look of the distribution of data.

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/University%20Admission%20Prediction%20Using%20Multiple%20Linear%20Regression/graphs/hist1.png)

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/University%20Admission%20Prediction%20Using%20Multiple%20Linear%20Regression/graphs/hist2.png)

A general outlook of the relationships between `Chances of Admission` and other variables

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/University%20Admission%20Prediction%20Using%20Multiple%20Linear%20Regression/graphs/task%204%20chance%20of%20admission%20vs%20reat.png)

It seems that as GRE scores get higher, the chances of admission get higher. Positive relationship.

Create the heatmap to show the correlation between variables.

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/University%20Admission%20Prediction%20Using%20Multiple%20Linear%20Regression/graphs/task%204%20heatmap%20of%20variables.png)

Here we can find some hidden relationships between variables. 

For example, the correlation between GRE score and TOEFL score is 0.83. This means there is a strong relationship between them.

And `CGPA`, `GRE Score`, and `TOEFL Score` have higher influence on `Chance of Admission` than `Research Experience`.  

### Task 5: Create Training And Testing Datasets

As the range of each variable is different, we need to standardize features by removing the mean and scaling to unit variance, incase they cause any bia to the model.

### Task 6: Train And Evaluate A Linear Regression Model

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/University%20Admission%20Prediction%20Using%20Multiple%20Linear%20Regression/graphs/simple%20regression.png)

* b: the intercept
* m: the slope

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/University%20Admission%20Prediction%20Using%20Multiple%20Linear%20Regression/graphs/multiple%20linear%20regression.png)

Least Squares Method

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/University%20Admission%20Prediction%20Using%20Multiple%20Linear%20Regression/graphs/obtain%20parameter%20of%20model.png)

After training, the accuracy( coefficient of determination R^2 of the prediction) of Linear Regression Model is 0.8181.

### Task 7: Train And Evaluate an Artificial Neural Networks Model

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/University%20Admission%20Prediction%20Using%20Multiple%20Linear%20Regression/graphs/task%207%20artifical%20NN.png)

We are trying to optimise weights inside Neural Network to minimse the output error.

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/University%20Admission%20Prediction%20Using%20Multiple%20Linear%20Regression/graphs/Task%207%20loss%20graph.png)

The error in the beginning of trainning is high, over 100 epoches training, I was able to reduce the error significantly. 

The accuracy (coefficient of determination R^2 of the prediction) of Neural Network Model is 0.7970

### Task 8: Train And Evaluate A Random Forest and Decision Tree Regressors

#### Decision tree: 
* A regression or classification model in the form of a tree structure. 
* Desicion tree breaks down a dataset into smaller subset of data, and try to increamently build a decision tree consists of decision node and leaf node. 

The accuracy (coefficient of determination R^2 of the prediction) of Decison Tree Model is 0.6038

#### Random forest model: 
* A regression or classification model in the form of a forest (multiple trees) structure. 
* Instead of reply on the result of one tree, I combined the outcome of all decision trees to reduce overfitting of the data. 

The accuracy (coefficient of determination R^2 of the prediction) of Random Forest Model is 0.7895

### Task 9: The difference between regression KPIs

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/University%20Admission%20Prediction%20Using%20Multiple%20Linear%20Regression/graphs/Task%209%20access%20model%20performance.png)

#### MAE

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/University%20Admission%20Prediction%20Using%20Multiple%20Linear%20Regression/graphs/task%209%20model%20mertric%20MAE.png)

#### MSE
* MSE is more sensitive to error (residual) than MAE

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/University%20Admission%20Prediction%20Using%20Multiple%20Linear%20Regression/graphs/task%209%20model%20metric%20MSE.png)

#### RMSE
* RMSE is easier to interpret compared to MSE, as the unit of this KPI is same as the input data. 

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/University%20Admission%20Prediction%20Using%20Multiple%20Linear%20Regression/graphs/task%209%20model%20metric%20RMSE.png)

#### R Squared-Coefficient of Determination
* A statistical measure that represents the proportion of the variance for a dependent variable that's explained by an independent variable or variables in a **regression*** model.

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/University%20Admission%20Prediction%20Using%20Multiple%20Linear%20Regression/graphs/task%209%20model%20metric%20R2.png)

Tell you how good is your fit. (How well unseen samples are likely to be predicted by the model)

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/University%20Admission%20Prediction%20Using%20Multiple%20Linear%20Regression/graphs/task%209%20model%20metric%20R2-2.png)

#### Adjusted R Square

* If we add one more independent variable to our model, and if that model doesn't improve the performance of our model, then we penaltise it. 
* take into account how many independent variables are added to calculate our model.

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/University%20Admission%20Prediction%20Using%20Multiple%20Linear%20Regression/graphs/task%209%20model%20metric-%20adjust%20R2.png)

### Task 10: Calculate regression model KPIs


1. Understand the theory and intuition behind Multiple Linear Regression.

6. Understand the difference between various regression models KPIs such as MSE, RMSE, MAE, R2, and adjusted R2.

7. Assess the performance of regression models and visualize the performance of the best model using various KPIs.
