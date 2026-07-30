# Data Structures
## Arrays
- Typically a linear data storage of a single type
- Can store generics, which may allow for multiple data types (given casting and conversions)
- Definition "A series or arrangement"
## List
- An array that dynamically allocates additional memory for new objects/items being added
## Stacks
- Last In, First Out (LIFO)
- Typically has Push (add), Peek (get @ -1 index), and Pop (get last [-1] index, and removes it from the stack)
## Queues
- First In, First Out (FIFO) data type
- Typically has the same functions as a Stack
## Sets
- Stores only unique data without any particular order
## Maps
- Represents an unordered collection of key-value pair elements
## LinkedLists
- Types
    - Singly Linked List
        - (Standard) Head -> A (Contains Data & Next) -> B (Contains Data & Next) -> C (Contains Data & Next) -> ...
        ![](https://media.geeksforgeeks.org/wp-content/uploads/20240726165319/Singly-Linked-List.webp)
    - Doubly Linked List
        - Head -> A (Contains Prev, Data, Next) <-> B (Contains Prev, Data, Next) <-> C (Contains Prev, Data, Next) <-> ...
        ![](https://media.geeksforgeeks.org/wp-content/uploads/20240809124907/Node-Structure-of-Doubly-Linked-List.webp)
    - Circular Linked List
        - Last node connects to first node
        - A (Contains Data, Next) -> B (Contains Data, Next) -> C (Contains Data, Next) -> A (Contains Data, Next) -> ...
        ![](https://media.geeksforgeeks.org/wp-content/uploads/20240806130914/Representation-of-circular-linked-list.webp)
    - Circular Doubly Linked List
        - Node connects to next & previous, plus last node's `next` connects to first node (and first node's previous connects to last node)
        ![](https://media.geeksforgeeks.org/wp-content/uploads/20240806145223/Representation-of-circular-doubly-linked-list.webp)
    - Header Linked List
        - Head -> A (May contain multiple data fields, and next) -> B (May contain multiple data fields, and next) -> C (May contain multiple data fields, and next) -> ...
        ![](https://media.geeksforgeeks.org/wp-content/uploads/20191110220317/Polynomial.jpg)
## Trees (B-Tree)
- Abstract data type that represent a hirearchial tree structure with a set of connected nodes, nodes can have many child nodes (depending on the type of tree)
- Some Applications
    - File System structure
    - Class hierarchy
    - Abstract syntax trees
    - Natural Language Processing (NLP)
        - Parse trees
        - Modeling utterances in a generative grammar
        - Dialog tree for generating conversations
    - DOM (Document Object Models) of XML / HTML documents
    - Search Trees (Most common for interviews)

## Tries (B+Tree)
- Best used for dictionaries, autocorrect, or predictive text
- basically a Tree with a set number of child nodes (n)
![](https://upload.wikimedia.org/wikipedia/commons/c/c0/Trie_representation.png)

## Graphs
- Meant to implement the undirected graph and directed graph concepts from the field of graph theory within Mathematics
- Graph Theory
    - Mathematical Structures used to model pairwise relations between objects
    - Directed Graph (digraph) is a graph which edges have orientations
        - An Edge is a relationship between 'nodes'
        - A Vertex is a 'node' in a graph that may represent some amount of data
### Visual Representation of a Graph
![](https://upload.wikimedia.org/wikipedia/commons/5/5b/6n-graf.svg)
### UML Diagram of a Graph
![](https://upload.wikimedia.org/wikipedia/commons/d/d7/UML_graph_ADT.svg)

# TODO (Research topics)
- Adjacency List
- Adjacency Matrix
- Incidence Matrix
- Specific data type Applications / use-cases
