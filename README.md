# CS-340-Client-Server-Development
Coursework for the CS-340 Client Server Development course

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

------------------------Project Overview----------------------------------------------------------------------------

     The dashboard was created with a Python module that contains the database connection functionality as well as the implementation of the CRUD functions.  Python was chosen as the language that will author the script to provide the “glue” to bridge the dashboard to the database.  PyMongo was chosen to access the MongoClient, which imports the Python module to allow the Dashboard to interact with the data in the database.  The Dash components were chosen to provide the visuals requested by the user and allow interaction between the user and the data.  The combination reflects the Model-View-Controller aspect of Object-Oriented Programming. 
     In the project, the MVC controller action uses the models to retrieve the necessary information from the database. Once the database returns the data, it is loaded into the dashboard, which is referred to as a view. The user can then see the requested data in the view. 

-----------------------Getting Started------------------------------------------------------------------------------

     **Note: ensure the mongo server is running**
![Getting started data](https://github.com/vsmith6/CS-340-Client-Server-Development/blob/main/images/gettingstarted1.png "Getting Started title")

![Getting started data](https://github.com/vsmith6/CS-340-Client-Server-Development/blob/main/images/gettingstarted2.png "Getting Started title")          
-----------------------Script Usage-------------------------------------------------------------------------------

     The module imports MongoClient and creates the AnimalShelter object class.  The module allows the user to sign into the database by entering their username and  password from the driver script. The database shown is the AAC existing database and the animals collection, which can be updated to reflect the needs of the user. The module imports bson to save the created objects to the database in json format. The create function will use this database collection to insert a dictionary of data. It accepts the connection as a self parameter and the data. If the data does not insert, it will return false. If successful, it returns true. The read function uses the find command to search by a valid value of the data. If the search is successful, it returns the _id of the object. If it is not successful, it returns as false.
     The update function takes the self parameter as well as the parameters of the old data and the new data, which represent what the user wants to update the data for that object to be. If the data to update is not found, the method will not execute. If the data is successfully found, the data will be updated to what is passed in as the new data. The delete function takes the parameters of self and data, which is the data that is meant to be deleted.  If the data meant to be deleted is not found, the function will not execute and will raise an exception, printing the message “Nothing to delete, data is empty”. If the data is deleted, the function will return true and print the “Successfully Deleted” message. 

-----------------------Dashboard Features-------------------------------------------------------------------------

     The features of the dashboard include a data table, a location map, and a pie chart that will populate with the data that is chosen by the user using the radio button choices named and selected by the client. The data table also features pagination to provide a cleaner appearance for the client, limiting the rows to 10 at a time. The location map will show an icon for each dog in the visible rows and provide a tooltip with the dog’s name and breed, depending on the selection of the user.
     The client specified the ability to show the animals in his database that are Water Rescue Breeds, which include Labrador Retriever Mix, Chesapeake Bay Retriever, and Newfoundland breeds.  The preferences are Intact Females that are 26 to 156 weeks in training age. This functionality is represented by the following screenshot:

![Getting started data](https://github.com/vsmith6/CS-340-Client-Server-Development/blob/main/images/Screenshot_2022-08-13%20Dash(1).png "Getting Started title") 

     The client specified the ability to show the animals in his database that are Mountain or Wilderness Rescue, which include German Shepherd, Alaskan Malamute, Old English Sheepdog, Siberian Husky, and Rottweiler breeds.  The preferences are Intact Males that are 26 to 156 weeks in training age. This functionality is represented by the following screenshot:
 ![Getting started data](https://github.com/vsmith6/CS-340-Client-Server-Development/blob/main/images/Screenshot_2022-08-13%20Dash(2).png "Getting Started title")
 
 The client specified the ability to show the animals in his database that are Disaster or Individual Tracking, which include Doberman Pinscher, German Shepherd, Golden Retriever, Bloodhound, and Rottweiler breeds.  The preferences are Intact Males that are 20 to 300 weeks in training age. This functionality is represented by the following screenshot:
  ![Getting started data](https://github.com/vsmith6/CS-340-Client-Server-Development/blob/main/images/Screenshot_2022-08-13%20Dash(3).png "Gettinh Started title")
 The client requested the ability to reset the dashboard to the original unfiltered state.  The Reset selection will show the data in the format requested.  The following screenshot demonstrates this functionality:
 ![Getting started data](https://github.com/vsmith6/CS-340-Client-Server-Development/blob/main/images/Screenshot_2022-08-13%20Dash(4).png "Getting Started title")
     
-------Challenges-----------------------------------------------------------------

    The challenges presented in this project were overcome by utilizing the reference material provided by the tools that are listed previously.  Importing the data into the mongo database was straightforward, although creating the Administrator and the user with only read-write access required a good amount of testing to ensure that the correct capabilities were assigned.
     The next major challenge was to create the Python script, or driver, which contains the commands to access the database as well as the CRUD functions.  It was fruitful to test the functionality of the python driver separately and with test data before attempting to connect the dashboard.
     The dashboard components represented here feature a component with an id and various options.  The components are then referred to in a callback function, which is coded to communicate with the component.  Once an understanding of how to pass the various id’s, inputs, and outputs became apparent, it became clearer of how to implement the dashboard according to the client’s specifications. 


----------Tools Used------------------------------------------------------------

The following tools were used to create the dashboard:
1.	Using MongoDB shell version v4.2.6
Go to the download page at https://www.mongodb.com/try/download/community
Choose your OS and your desired MongoDB version.
Click Download.
Go to your ‘Downloads’ folder.
Click on the installer.
Follow the instructions.

2.	Python v3.6 
https://www.howtogeek.com/197947/how-to-install-python-on-windows/

3.	Jupyter Notebook v6.0.1 (optional)
https://jupyter.org/install
4.	Dash, Dash Leaflet, Dash Core Components, Dash HTML Components, Plotly Express, and various Dash dependencies available at: https://plotly.com/

5.	PyMongo: https://pymongo.readthedocs.io/en/stable/index.html





