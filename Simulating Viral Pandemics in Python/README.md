## Simulating Viral Transmission

This project aims in implementing an agent-based simulation of the SIR epidemiological model of contagion transmission in Python to simulating the pandemic spread.

### Project Structure
* Task 1: Exploring the basics of the SIR model
* Task 2: Build the Basic Structure of SIR Model
* Task 3: Run First Basic Simulation
* Task 4: Simulating Mitigation Policies and Asymptomatic Populations
* Task 5: Implement a real-world data for scientific simulations

### Task 1:  SIR model
The SIR model is one of the most basic compartmental models, many models are derivatives of this basic form. 

The model consists of three compartments:

#### S: 

* The number of susceptible individuals. 

* When a susceptible and an infectious individual come into "infectious contact", the susceptible individual contracts the disease and transitions to the infectious compartment.

#### I: 

* The number of infectious individuals. These are individuals who have been infected and are capable of infecting susceptible individuals.

#### R：

* The number of removed (and immune/recovered) or deceased individuals. 

* These are individuals who have been infected and have either recovered from the disease and entered the removed compartment, or died. It is assumed that the number of deaths is negligible with respect to the total population.
