# Algorithms Specialization
Repo for Algorithms Specialization on Coursera

Content
Algorithms implemented in:
- Python (WIP!)

Algorithms: 

**Karatsuba-Algorithm (multiplication of large integers)**

While the conventional way to multiply integer has a complexity of n squared, the Karazuba algorithm with n powet of log2(3) is much faster. The Karazuba algorithm realizes the runtime advantage by the divide and rule principle by splitting the original factors lengthwise and considering them in smaller multiplications. 
See: https://de.wikipedia.org/wiki/Karazuba-Algorithmus


**MergeSort**

MergeSort is a sorting algorithm that sorts an unsorted list using the Parts and Mastery principle.
MergeSort first halves the unsorted list, sorts these two individual lists and then merges them again. Due to the recursion of the algorithm, MergeSort is also applied to the individual lists again.
    

**QuickSort**

Quicksort selects an element from the list as the pivot element and divides the list to the left and right of the pivot element into smaller and larger elements. The algorithm does this in-place.
https://de.wikipedia.org/wiki/Quicksort


**Strongly-Connected-Components**


 
**Dijkstra-algorithm (Shortest Single Path from source)**

The Dijsktra algorithm finds the shortest path with a given start node. It belongs to the class of Greedy algorithms, because the node that promises the shortest path from the start node is selected iteratively. The Dijkstra algorithm always finds the optimal solution under the assumption of non-negative edge weights. This is based on the assumption that the shortest distances together form the shortest path from source to target. This can be proven by assuming that you did not find the shortest path. If you subsequently found a shorter path, you would also have had to examine its subpaths and therefore there is no shorter path. 


