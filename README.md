# Ecosphere-Simulator
The final version of Ecosphere for Data Structure Course Design

## How to use

- Just simply run the *window.py* to start the simulator

## Design Principles

### I. Requirement

This ecosphere system is required to simulate creatures' natural behavior. A creature will die if been preyed, or old enough. An animal will also die if it does not have enough energy. But it can search for food to get its energy, although searching and racing would cost some energy. Every species has its intrinsic characteristics and attributes, like predator, another species as food source, cost of been preyed, energy gain after being preyed, life-span and initial number. As minimum requirements, grass, cow and tiger should be included in the ecosphere program. In addition, a GUI is needed to provide interactive visualization window for user, where each creature is presented as dots with different color and shape.

### II. Function

In our system, user can set the initial number of each species and run the program to observe how the animal act and how the number of each species change as time passing by in ecosphere system. With GUI, user can watch animals chasing for food or running away from predator, they calculate the optimal path with A* algorithm and hen run follow this path.

### III. Assumptions

1.	When a new ecosphere is initialized, creatures randomly and evenly appear on the map. The age of organisms obeys a normal distribution from 0 to half of the life span and the energy obeys a normal distribution from half of the maximum energy to maximum energy. 
2.	Each creature has a maximum number. They will not reproduce when total amount of that creature reaches the upper bound.
3.	It does not take time to eat the food. 
4.	Predators only chase the nearest prey. 
5.	The predator can eat the predator directly within a certain distance. 
6.	The predator can get all the energy of the prey if it catches the prey. 
7.	Creatures do not choose to find food when their energy is full. 
8.	The life span and reproduce rate of each species is fixed. 
9.	Animals and plants reproduce asexually. 
10.	The energy of an individual is reduced by half due to reproduction of offspring. 
11.	The requirements for reproduction are that the energy of the individual is greater than one third of the maximum energy, and that the age is greater than one fifth of the life span.


## Design Details

### Background

We chose the Ecosphere as our topic. For humans, it is important to model the functioning of the ecosphere based on the behavior of organisms and to study the laws of it. It is of great significance to understand nature and to protect it.

In an ecosphere, there are usually multiple species with behaviors including growth, reproduction and death. The most common relation between species is predation. The predators will hunt for energy and preys may try to escape from death. The prey will also look for food to replenish its energy in a dangerous environment. If a creature has enough energy, it may reproduce next generation. However, if it lacks energy, or is predated or gets too old, it will die. In our ecospheres, it is possible for one creature to continue to flourish for a long time, or to become rapidly extinct due to the numbers of other species.

Our objective is to simulate an ecosphere. Each species in this ecosphere has behaviors like growth, reproduction and death. There species will act as predators or preys. Such a relation is reflected through predatory behavior and energy flow. We will simulate the animal behaviors mentioned above and provide GUI to visualize how the creatures behave. The user can see the chase of the predator and the escape of the prey in the window. By setting he initial number of each creature, user can observe how initial number effects the final result of ecosphere.


### Algorithms

We mainly used **A Star** Algorithm to implement the path tracking part. However, the map is set to be a "pixle world" which is made up of blocks. Thus, the distance on the map is considered to be **Diagonal Distance**. In the end, we designed the heuristic function inside A* Algorithm to be the **Octile Distance**. It is a method which calculates the distance which enables diagonal movements.  

## Result

- During the simulation, users can observe different behaviors of creatures. All of the three species has the behaviors below: 

1. Reproduction 

Users can observe that new creatures appear on the map. When the numbers of ach species have not reached the maximum, new creatures will be created in a random empty position of the map. Number of new creatures depends on the origin umber and preset reproduction rate. 

2. Death 

Users can observe that some creatures disappear on the map but they are not eaten by predators (tiger/cow), these creatures die from hunger or aging. As time passes, he energy of living creatures decreases and their age increases as well. Once their energy becomes zero or age reaches the maximum, they will die. 

- Besides the above behaviors, tigers and cows have the behaviors below: 

1. Predatory 

Predators (tiger/cow) will search for prey (cow/grass) in field of view. Once a predator finds the nearest prey, it will search for the shortest path to get to the prey’s current position based on A* Algorithm. If another prey, which is closer than he previous nearest one, appears when the predator is chasing the previous one, the predator will change its path to chase the new one. Users can observe that a predator is moving towards the prey. Sometimes more than one predator is moving towards one prey. 

2. Random movement 

Users may observe that when there is no prey (cow/grass) near a predator tiger/cow), it seems to move aimlessly. If a predator cannot find prey in field of view, will move in a random direction until it finds prey. 

- For cows, they have escape behavior:

A cow will decide whether to eat grass or scape based on the current energy and the distance of predators. If it decides to eat grass, it will go for the nearest grass. If it decides to escape, it will escape in the direction with the fewest predators. With carefully designed algorithms and parameters, our system works well, effectively simulating the evolution of the ecosphere and behaviors of creatures.



## Reference

[1] Amit Patel, Heuristics, Amit’s Thoughts on Pathfinding. http://theory.stanford.edu/~amitp/GameProgramming/Heuristics.html
