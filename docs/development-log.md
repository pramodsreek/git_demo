# **Development Log**

**Status Updates**

**Week 1 (22nd June - 28 June 2019)**

Identifying the best interface to retrieve the share price took longer than expected. 

Google was chosen as the interface and a simple code was written to get the stock prices. In many cases, google interface came back with errors for the ASX listed share prices. 

Yahoo was tried out next. Yahoo had another issue. ASX listed shares were not working with the Python interface, but the US listed shares were working. Going by the comments online, it looked like yahoo works for ASX. It required more searches and trial. Finally, the solution was found. Adding .AX at the end was the solution.

Yahoo was finalised as the interface. 



**Week 2 (29 June - 05 June 2019)**

Writing the common modules for the share application took longer than expected. Dictionary was used initially for storing the data from csv file. But maintaining the sort order was not practical. There was time spent on researching other data structures online.

Ordered dictionary was found. This needed some pre testing. There was time spend on writing code for Ordered dictionary and testing before making the decision. It worked well for the requirement. 

There was another delay caused due to pylint on the code generating a lot of warning. There was code refactoring required to fix these warnings. This added another day to the schedule. 

Testing has started. 