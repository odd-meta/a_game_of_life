# A(gent) Game of Life

The game of life using an agent model


## AGENTS
Each live cell will be defined as an Agent

Each agent keeps track of it's own position, as well as the environment

Every agent is visited in the list of agents and told to run against the defined rules based on it's environment

The changes are buffered until all changes are collected from all agents, then all changes are applied in the sequence they were collected

An environment is desired to save the headache of visiting an agent, then walking down the entire list to find what is near it

have the environment keep track of, agent locations

in the form of

[( (X, Y), Agent )]

give the environment a set of coordinates and a range bounding (list of tuples containing points)
the environement returns a list of agents that are within that range, you can simply ask each agent what their coordinates are

how does the environment figure that out

given a list of x,y coordinates

search them for X coordinates within a +/- range, drop the rest
then look for Y coordinates within a +/- range, this is your list to return
a step here could be added for Z, and t, if desired


## CHANGE BUFFER

step through the agents for an area and evaluate their actions for this step based on rules
put those actions into the first-stage change buffer

evaluate the actions in the first stage change buffer for actions that will create conflicts
process the conflicts according to the rules
fill back into first stage buffer
repeat

this might lockup if actions and conflicts interact to create a never-ending loop of conflict resolutions


## ENVIRONMENT

a container for a given area that knows about adjacent areas

coordinates in a global sense are defined as

area, area-coordinates

where all area-coordinates are an x by y grid, this, prefixed with an area identifier, defines a position in global space

every area has a bounding fuction that will return the "edges" of the area; this is a list of lists of coordinate tuples

each list of tuples defines a bounding 

also know about agents within it

if it is found that an agent will move to another area


## RULES

based off of the definitions in "Growing Artificial Societies"

agent-agent
* govern agent's interactions with each other
* behavior such as mating, fighting, socializing, etc
* the game of life is focused on mating behavior

environment-environment
* these involve properties of the environment, ambient resources, weather, etc
* not really applicable to the classic game of life

agent-environment
* these control how the agents react to properties of their environment, eating sugar in sugarscape, for example
* not really applicable to the classic game of life

TODO

* create the agent class
** define 