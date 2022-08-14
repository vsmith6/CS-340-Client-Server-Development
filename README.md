# CS-340-Client-Server-Development
Coursework for the CS-340 Client Server Development course
```
How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One,
which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could
you use this CRUD Python module in the future?
In order to keep the program for the Project Two project maintainable, readable, and adaptable, it was important to realize the structure
of the data and how to create the various database access commands as well as the CRUD functionality.  It was cleaner to ensure that the
driver functioned as was expected by thoroughly testing the functions with test data to ensure that they were returning what was expected
prior to using the driver to help provide the required functionality of the dashboard for Project Two. I do see the use of a Python crud
module in the future, however, the Dash dashboard would probably not be something specifically developed for a future client. 

How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso
Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies
would you use in the future to create databases to meet other client requests?
Approaching the requested requirements for this assignment was based on an introductory view of Mongo and Mongo Client, as well as an 
introductory view to the Dash components used to build the dashboard. The difference in this course versus previous courses is that we
got to create and test the Python driver to ensure that it was connecting to the database properly as well as returning the results 
from the CRUD functionality properly before creating the dashboard implementation. This way of working I would highly recommend as the
Python module could be used to interact with various other interfaces outside of the Dash framework. It is a good stepping stone to build
on for future projects, and supports the maintainability and reuseability factors that are important in computer science related fields. 
With future clients, it would be important that they have a really good understanding of the data that they have and that the data is 
accurate and sanitized.

What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare,
to do their work better?
Computer scientists help their clients by recommending strategies and tools to enable them to utilize the data that they have.  
A client may not be able to understand how to visualize their data. A computer scientist can work with the client to recommend 
the best technology solution to suit their project goals in a more timely manner than the client trying to do it on their own. 
The dashboard created for this project would be very helpful to the company as they would have a read only view of the data that 
is being utilized to help them make a decision or help one of the customers that is interested in adopting a specific breed of 
dog for a specific purpose. The dashboard interface helps to abstract the various direct queries from the user and ensures that
the data cannot be corrupted or altered in the database by user error. This is valuable to the company as it saves them a lot
of time, effort, and cost, providing their needed answers quickly.
```
