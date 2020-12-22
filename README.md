
# drbigproject  
GMIT Higher Diploma Data Analytics  
Data Representation Module 52954  
Assignment: DR Big Project 
Lecturer: Andrew Beatty  
Student: Fiona O'Riordan
Due Date: 29 December 2020  
---
## Purpose  

The purpose of this repository is to implement a Web Appliation as follows:  
(tick marks indicate objectives attempted.)  
1.  
    i. A basic Flask server that has a - [x]   
    ii. REST API, (to perform CRUD operations) - [x]    
    iii. One database table and   - [x]  
    iv. Accompanying web interface, using AJAX calls, to perform these CRUD operations 
    - [x]  
2. With more than one database table - [x]  
3. With authorization (logging in) - [ ]  
4. Same as 3, working very smoothly e.g. User error checking, logs, hosting etc Something you can publish.  - [x]  

Extras: 
a The web page looks nice - [x]  
A more complicated API - [x]  
If the third party API requires authentication - []   
Hosted online (e.g. Azure, Pythonanywhere)  - [x]  

## Repository Contents  
1. gitignore  
2. README.md  
3. LICENSE  
4. ToysDAO.py  
5. dbconfigtemplate  
6. init.sql  
7. requirements.txt  
8. server.py  
9. staticpages  
    * christmas-elf.jpg  
    * dispatches.html
    * index.html   

## Santa's Workshop Functionality:  
1. View toys from the database  
2. Create a new toy and add to the database  
3. Update existing toys.  
    * For toys without a dispatch you can change any attribute (field value).
    * For toys where a dispatch exists, you can only update the toys quantity as Santa likes to keep record of all toys as they were at dispatch but sometimes Elves must make inventory adjustments either to add to inventory when they have made a toy or deplete inventory when they accidentally (oops) damage toys(an alert will remind you of this and you will be prevented from updating any field except quantity).  
4. Only toys where a dispatch does not exist can be deleted.  
5. View dispatches from the database.  
6. Create a new dispatch (send a toy to a someone.)  Only toys where quantity is greater than zero can selected for dispatch.  


## Implementing this web application on your local machine:  
### Prequisites  
*  Python ( I have used Python 3.8.3 for this project). I would recommend anaconda installation [Anaconda](https://www.anaconda.com/products/individual).  
*  Install MySQL. 

### Cloning the repository  
Cloning allows you to create and use a copy of this repositiory on your local machine. 

1. In this [repository](https://github.com/fionaoriordan/drbigproject). 
2. Click on the green button "Code". Select "Clone with HTTPS". Copy the URL.  
3. In your terminal on your machine navigate to your preferred directory (folder). Type git clone https://github.com/fionaoriordan/drbigproject.git ( this is the URL you have copied).  
4. The repository is now installed.  
5. To install the necessary packages in the same folder/directory excecute the following: pip install -r requirements.txt
6. Verify that the packages have been installed using command: pip freeze.
7. In MySQL create a database called datarepresentation. Use the init.sql to create the tables & insert records for testing in a database called datarepresentation. 
8. Create a file called dbconfig.py using dbconfigtemplate.py as a template. Enter your own username & password here.  


## Executing & using this repository  
1. In your terminal navigate to the the folder where you cloned this repository.  
2. In terminal execute this command: python server.py  
3. In your browser navigate to http://127.0.0.1:5000/index.html  
4. You are now ready to use this web application.   

## Using on host site pythonanywhere.com.  TO BE COMPLETED.  
http://fionaoriordan.pythonanywhere.com/index.html  

Best Wishes,  
Fiona  


