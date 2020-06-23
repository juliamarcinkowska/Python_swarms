# Python_swarms

Implementation of particle swarm optimization algorithm in python. It is used to optimize the design for cylindrical receptacle for the products stored under pressure with consideration for constraints.

This algorithm tries to find a minimum in a four-dimensional search space,  simulating  the  flight  of  a  swarm  of  creatures in that search space. Each particle has a position and a velocity associated with it. A particle is attracted both by its best neighbour and by its own best position previously found in the search space. The values of velocity and position are updated at each iteration. Neighbourhoods of three closest particles were created, among them leader that satisfied the constraints was found - if no such leader could be chosen, to update the values in this neighbourhood current population’s leader was used. Finally plot of best evaluation value in each iteration is shown.

Project was co-created with Weronika Górecka (https://github.com/wgorecka).
