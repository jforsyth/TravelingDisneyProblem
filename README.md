# TravelingDisneyProblem
Repo to hold contents for the KEEN card for Traveling Salesman Problem at Disney

**tspdb/** contains a python module that implements the "traveling salesman" database for all information related to Disney's Magic Kingdom.

**demo.py**: is an example file that shows how to make calls to the database.

**greedy_distance.py**: an implementation of a greedy search algorithm to find the best path around the Magic Kingdom based upon selecting the nearest attraction.

**greedy_time.py**: an implementation of a greedy search algorithm to find the best path around the Magic Kingdom based upon selecting the ride where the user can get on fastest.

**random_search.py**: a "random" algorithm that finds paths through the Magic Kingdom. Is useful as a "worst case" estimator.

**validator.py**: given a path around the park, and a particular date, the program will determine the total time required to complete the park.
