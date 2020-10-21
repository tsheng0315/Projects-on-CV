# Simulating Viral Transmission

This project aims in implementing an agent-based simulation of the SIR epidemiological model of contagion transmission in Python to simulating the pandemic spread.

## Project Structure
* Task 1: Exploring the basics of the SIR model
* Task 2: Build the Basic Structure of SIR Model and Run Basic Simulation
* Task 3: Simulating Mitigation Policies and Asymptomatic Populations
* Task 4: Implement a real-world data for scientific simulations

### Task 1:  SIR Model for Spread of Disease
* An SIR model is an epidemiological model that computes the theoretical number of people infected with a contagious illness in a **closed** population over time. 
* The number of total population is a constant N(t)=c.
* The name of this models derives from the fact that they involve coupled equations relating the number of susceptible people S(t), number of people infected I(t), and number of people who have recovered/deseased R(t). 

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/Simulating%20Viral%20Pandemics%20in%20Python/graph/SIR%20model%20intro.png)

#### S: 
* The number of susceptible individuals. 
* When a susceptible and an infectious individual come into "infectious contact", the susceptible individual contracts the disease and transitions to the infectious compartment.

#### I: 
* The number of infectious individuals. 
* These are individuals who have been infected and are capable of infecting susceptible individuals.

#### R：
* The number of removed (and immune/recovered) or deceased individuals. 
* These are individuals who have been infected and have either recovered from the disease and entered the removed compartment, or died. It is assumed that the number of deaths is negligible with respect to the total population.

#### Identify the independent and dependent variables. 

* The independent variable is time `t`, measured in days.
* The first set of dependent variables is number of people in `S, I, R` respectively. 

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/Simulating%20Viral%20Pandemics%20in%20Python/graph/SIR%20variable.png)

* The second set of dependent variables represents the fraction of the total population in each of the three categories.  

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/Simulating%20Viral%20Pandemics%20in%20Python/graph/SIR%20variable%20fraction.png)


### Three representations of an SIR model

* The relationship between S/I/R sows as follows. 
* `β`represents infection rate.
* `γ` represents removal (recovery+ deceased) rate.

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/Simulating%20Viral%20Pandemics%20in%20Python/graph/SIR%20relationship%20model.png)

* Re-write SIR Model in Differential equations:

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/Simulating%20Viral%20Pandemics%20in%20Python/graph/SIR%20formula.png)

* `N` is the total population. The number of total population is a constant N(t)=c.

We have: `N(t)=c=S(t)+I(t)+R(t)`

This system is non-linear, however it is possible to derive its analytic solution in implicit form.

Firstly note that from:

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/Simulating%20Viral%20Pandemics%20in%20Python/graph/differential%20sum%20to%20zero.png)

It follows that:

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/Simulating%20Viral%20Pandemics%20in%20Python/graph/3%20variablesum%20to%20zero.png)

Expressing in mathematical terms the constancy of population N. 

Note that the above relationship implies that one need only study the equation for two of the three variables.

## Result of Task 1

The following graph integrates equations above for a disease characterised by parameters:
* `β=0.2`, `1/γ=10` days, in a population of `N=1000` (perhaps 'flu in a school). 
* The model is started with a single infected individual on `day 0`: `I(0)=1`

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/Simulating%20Viral%20Pandemics%20in%20Python/graph/SIR%20basic%20graph.png)

## Task 2: Build the Basic Structure of SIR Model and Run Basic Simulation

In this task, I ran an agent based SIR modle simulation to track transmission of viral disease in a community in python

* The infection radius is 0.6, recovery rate is 0.0006, death rate is0.001, in a population of `N=500` (perhaps 'flu in a school). 
* The model is started with a single infected individual on `day 0`: `I(0)=2`
* On day 1:

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/Simulating%20Viral%20Pandemics%20in%20Python/graph/task%202-1.png)

* A few days later:

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/Simulating%20Viral%20Pandemics%20in%20Python/graph/task%202-2.png)


## Task 3: Simulating Mitigation Policies and Asymptomatic Populations

In this task, I ran simulations on with/without masks, sanitary, and social distance. The results are as follows:

In the beginning(without masks):

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/Simulating%20Viral%20Pandemics%20in%20Python/graph/task%204%20without%20mask%201.png)

At the end(without masks):

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/Simulating%20Viral%20Pandemics%20in%20Python/graph/task%204%20without%20mask2.png)

With masks:

![](https://github.com/tsheng0315/Projects-on-CV/blob/main/Simulating%20Viral%20Pandemics%20in%20Python/graph/task%204%20with%20mask.png)

We can find from the graphs above that when people begin to wear masks, pay attention to sanitary, and keep social distance, the recover rate gets higher(more grenn dots appears). This means Mitigation Policies and Asymptomatic Populations do help in preventing transmission of pandemic.
