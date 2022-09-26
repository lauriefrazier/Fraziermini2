# Fraziermini2
## INF 601 - Advanced Programming in Python
### Laurie Frazier

'pip install -r requirements.txt'

### This project is intended to print a quantifiable data graph presenting the shedding level of a Golden Retriever, Bernese Mountain Dog, Poodle, Corgi, and German Shepherds.
#### Code Design
After importing the required packages, the API package from API Ninjas will allow a download of the chosen breed information and will translate into a table.
By defining the breeds and the selection of the shedding data, it will print the data that correlates to the level of shedding, 1 being low shedding to 5 being highest shedding.
The data will then append to be used for a NumPy array. From there, it will use matplotlib to create the graph for each breed on the shedding scale.

#### Creating the Graph
Creating the graph, using matplotlib's ploting package, creating the graph from the array.
The styling choices I made were each graph used the same dots given by the -o input.
1. Golden Retriever is represented as <span style= "color:gold"> gold</span>
2. Bernese Mountain Dog is detailed as <span style= "color:purple"> purple</span>
3. Poodle is colored <span style= "color:blue"> blue</span>
4. Corgis data is <span style= "color:green"> green</span>
5. German Shepherd is <span style= "color:red"> red</span>