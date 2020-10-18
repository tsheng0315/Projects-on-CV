## Simulating Viral Transmission

This project aims in implementing an agent-based simulation of the SIR epidemiological model of contagion transmission in Python to simulating the pandemic spread.

### Project Structure
* Task 1: Exploring the basics of the SIR model
* Task 2: Build the Basic Structure of SIR Model
* Task 3: Run First Basic Simulation
* Task 4: Simulating Mitigation Policies and Asymptomatic Populations
* Task 5: Implement a real-world data for scientific simulations

### Task 1:  SIR Model for Spread of Disease
* An SIR model is an epidemiological model that computes the theoretical number of people infected with a contagious illness in a **closed** population over time. 
* The name of this models derives from the fact that they involve coupled equations relating the number of susceptible people S(t), number of people infected I(t), and number of people who have recovered R(t).

#### S: 
* The number of susceptible individuals. 
* When a susceptible and an infectious individual come into "infectious contact", the susceptible individual contracts the disease and transitions to the infectious compartment.

#### I: 
* The number of infectious individuals. 
* These are individuals who have been infected and are capable of infecting susceptible individuals.

#### R：
* The number of removed (and immune/recovered) or deceased individuals. 
* These are individuals who have been infected and have either recovered from the disease and entered the removed compartment, or died. It is assumed that the number of deaths is negligible with respect to the total population.

The first step in the modeling process is to identify the independent and dependent variables. 

* The independent variable is time `t`, measured in days.
* The first set of dependent variables counts people in `S, I, R` respectively. 

* The second set of dependent variables represents the fraction of the total population in each of the three categories.  `N` is the total population

