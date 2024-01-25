# **Movie Reviews with Friends**

Live Website: [Movie Reviews with Friends](https://movie-reviews-with-friends-96186426856b.herokuapp.com/)


## **Purpose**

Movie Reviews with Friends is a web application built with Django that brings movie enthusiasts together to discuss and review their favorite films. The platform allows users to create or join groups centered around specific movie subjects, fostering a community where members can share their passion for cinema.

## **Project Goals**

### **User/Visitor Goals**

+ **Facilitate Community Building**  
Enable users to create and join groups based on specific movie subjects, fostering a sense of community among like-minded individuals.

+ **Curate Movie Catalogs**  
Provide a space within each group for users to add and explore movies related to the group's theme, creating a curated catalog of films.

+ **Enable Movie Reviews**  
Allow users to post reviews for movies within the groups, providing a platform for expressing opinions.

### **Site Owner Goals**

+ **Community Growth**  
Increase the number of registered users and groups on the platform.

+ **Content Curation**  
Promote the creation of high-quality content within groups, ensuring that the movie catalogs and discussions offer value to the community.

+ **Positive User Experience**  
Prioritize a positive and user-friendly experience, making the platform enjoyable and accessible for users of varying levels of technical expertise.

By achieving these goals, the Movie Reviews with Friends website aims to become a go-to platform for movie enthusiasts to connect, discuss, and share their passion for cinema within a vibrant and supportive community.



## **User Stories**

### **First Time Users Goals**

+ As a 
+ As a 
+ As a 

### **Frequent User Goals**

+ As a 
+ As a 
+ As a 

### **All User goals**

+ As a 
+ As a 
+ As a 

### **Fulfillment**

The 
> As a

***

## **Structure**

**Navigation**  
A fully responsive navigation bar positioned at the top of the page displaying essential site functionalities throughout the whole website.

![]()

**Home/Index**  
The Movie Reviews with Friends home page serves as a warm welcome to users, tailored to their login status.  

Not-logged-in-users are presented with a welcome message and encouregement to explore the website and register for an account.

![]()

Logged in users are greeted by their username and groups they are apart of.

![]()

**Register & Login**  
Account registration is designed for simplicity. Users only need to provide a unique username, an email address, and a password with confirmation. This straightforward process allows users to explore the website's features promptly. Note that email confirmation is not required, providing users with immediate access upon registration.

![]()

**Movies**  
The Movies page is intentionally streamlined, showcasing only essential information: the movie poster and title. This design prioritizes a efficient scrolling experience, ensuring users can navigate without the distraction of information overload.

![]()

**Movie Details**  
In the Movie Details section, users can get more comprehensive informations about movies, including a movie description, genres, release date, and runtime. For logged-in users, a feature allowing them to add the movie to any groups they are part of, enhancing their engagement with the Movie Reviews with Friends community.

![]()

**Groups**  
The Groups page provides an overview of all currently available groups.

![]()

**Group details**  
The Group Details page presents users with valuable insights, including the group description, the curated collection of movies added by the group, and a comprehensive list of both the group admin and members. Additionally, for users not yet part of the group, a prominent "Join Group" button is provided. Conversely, for those already part of the group, a convenient "Leave Group" option is available.

![]()

**Reviews**  
Upon selecting a movie within a group, the Reviews page unfolds, showcasing user-generated reviews. Users can express their thoughts through written reviews, accompanied by the option to assign a numerical rating from 1 to 10. This interactive feature empowers users to share their insights and opinions.

![]()

**Users**  
The Users page, fashioned similarly to the Groups list, provides a comprehensive roster of all currently registered users on the website.

![]()

**User details**
The User Details page provides a personalized glimpse into each user's interests, featuring their username, a self-written bio, and the date they joined the community. 

![]()

## **Features**

### **Existing Features**

**Movies**
+ 

**Groups**
+ 

**Users**
+ 

**Database**
+ 

### **Features left to implement**

+ 
> 

***

## **Technologies**

### **Language**

+ [Python](https://www.python.org/)
    - Main programming language used in this project

### **Packages**

+ []()
    - 

### **Tools**

+ []()
    - 

***

## **Testing**

+ 

### **Authentication**

+ 

### **Other Tests**

+

### **Unresolved Errors, Issues and Bugs**

+

## **Deployment**

### **Project Creation**

The project was started by navigating to the [template provided]() and clicking 'Use this template'. Under Repository name I input _________ and checked the 'Include all branches' checkbox. I then navigated to the new [repository](). I then clicked the Open with GitHub Desktop button.

After GitHub Desktop opened this repository, i then clicked "Open in Visual Studio Code"

Opening [Visual Studio Code](https://code.visualstudio.com/). The following commands were used throughout the project:

+ git add filename - This command was used to add files to the staging area before committing.
+ git commit -m *commit message explaining the updates* - This command was used to commit changes to the local repository.
+ git reset HEAD^ - This command was used to delete the last commit but keep all the changes.
+ git push - This command is used to push all committed changes to the GitHub repository.

### **Run Locally**

1. Navigate to the file to be run in Visual Studio Code
2. 

To stop the :
+ "Ctrl + C" - To stop 

### **Deployment to Live Service**

1. Get ________ ready for deployment

> Ensure the ___________ is ready for deployment and includes all necessary dependencies in a requirements.txt file using this command.

> pip3 freeze > requirements.txt

2. Pushing GitHub

> Make a commit and push the current version of the program to GitHub.

> git commit -m "..."  
> git push

3. Heroku starting a new project

> Visit the [Heroku](https://dashboard.heroku.com/) dashboard and click "New App" after that, give the project a name and select a region, next.

4. Heroku project settings

> In the project dashboard click "Settings" and head to the "Project Vars" section. CLick "Reveal Config Vars" opening two input fields. In the first field "KEYS" insert "___________". The second field "VALUE" copy and paste the contents of ___________ file. This file is not accessible to the public and must be kept secret.

5. Heroku Buildpacks

> Head to "Buildpacks" section and click "Add Buildpack". In the newly opened window, select "Python" then "Add Buildpack". Repeat this step and add "Nodejs" next.

6. Connecting to GitHub

> Click the "Deploy" tab and select "GitHub" and then "Connect to Github".

7. Selecting the Project

> After successfully connecting to GitHub a search bar opens. Type the name of the repository your project is in. A dropdown menu will open, click on the correct repository. This links up the repository from GitHub to heroku.

8. Deployment

> Scroll down and select either "Automatic deploys" or "Manual deploy". After the deployment is finish, head over to the "Overview" tab on heroku. On the top right, click "Open app" a new tab will open with the deployed project.

***

## **Credits**

### **Project Idea**

The inspiration for this project 

### **Content**

The content of this tool was created by [NixTS](https://github.com/NixTS/).

The __________ provided was made with the knowledge gained through the CodeInstitute Full Stack Developer course.

### **Acknowledgements**

I'd like to thank my mentor [Daisy McGirr](https://github.com/Dee-McG) for her guidance throughout my project.