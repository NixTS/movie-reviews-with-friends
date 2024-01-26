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

- [Python](https://www.python.org/)
    - Backend development using Django.

### **Front-end**

- [Bootstrap](https://getbootstrap.com/)
    - Front-end framework for responsive design and styling.

- [HTML/CSS](https://developer.mozilla.org/en-US/docs/Web/HTML)
    - Structure and styling of the website.

### **Database**

- [ElephantSQL](https://www.elephantsql.com/)
    - PostgreSQL as a Service. Cloud database hosting service for PostgreSQL databases.

### **Hosting & Deployment**

- [Heroku](https://www.heroku.com/)
    - Cloud platform for hosting and deploying web applications.

### **Tools**

- [Django](https://www.djangoproject.com/)
    - Python web framework for building the application.

### **Packages**

- [asgiref](https://pypi.org/project/asgiref/) (3.7.2)
    - ASGI (Asynchronous Server Gateway Interface) reference implementation for Django.

- [certifi](https://pypi.org/project/certifi/) (2023.11.17)
    - A collection of Mozilla's CA certificates for certificate authorities.

- [cffi](https://pypi.org/project/cffi/) (1.16.0)
    - Foreign Function Interface for calling C functions from Python.

- [charset-normalizer](https://pypi.org/project/charset-normalizer/) (3.3.2)
    - Library for normalizing and converting between different character sets.

- [cryptography](https://pypi.org/project/cryptography/) (41.0.7)
    - Library for secure communication and cryptography protocols.

- [defusedxml](https://pypi.org/project/defusedxml/) (0.7.1)
    - XML parsing library that protects against various XML vulnerabilities.

- [dj-database-url](https://pypi.org/project/dj-database-url/) (0.5.0)
    - Django utility for parsing database URLs.

- [Django](https://www.djangoproject.com/) (4.2.1)
    - The Django web framework for building robust and scalable web applications.

- [django-allauth](https://pypi.org/project/django-allauth/) (0.57.0)
    - Django package for handling authentication, registration and account management.

- [gunicorn](https://pypi.org/project/gunicorn/) (20.1.0)
    - WSGI HTTP server for running Django applications in production.

- [idna](https://pypi.org/project/idna/) (3.6)
    - Library for handling Internationalized Domain Names in Applications (IDNA).

- [oauthlib](https://pypi.org/project/oauthlib/) (3.2.2)
    - Generic implementation of the OAuth 1.0 and OAuth 2.0 authorization protocols.

- [psycopg2](https://pypi.org/project/psycopg2/) (2.9.9)
    - PostgreSQL adapter for Python, allowing Django to interact with PostgreSQL databases.

- [pycparser](https://pypi.org/project/pycparser/) (2.21)
    - Parser for the C language written in Python.

- [PyJWT](https://pypi.org/project/PyJWT/) (2.8.0)
    - JSON Web Token implementation in Python.

- [python3-openid](https://pypi.org/project/python3-openid/) (3.2.0)
    - Set of Python packages for working with OpenID.

- [requests](https://pypi.org/project/requests/) (2.31.0)
    - HTTP library for making requests in Python.

- [requests-oauthlib](https://pypi.org/project/requests-oauthlib/) (1.3.1)
    - OAuthlib support for Python Requests.

- [setuptools](https://pypi.org/project/setuptools/) (69.0.3)
    - Package for installing Python projects, including package management.

- [sqlparse](https://pypi.org/project/sqlparse/) (0.4.4)
    - Non-validating SQL parser for Python, for formatting and analyzing SQL queries.

- [tzdata](https://pypi.org/project/tzdata/) (2023.4)
    - Time zone database for Python.

- [urllib3](https://pypi.org/project/urllib3/) (2.1.0)
    - HTTP client for Python.

- [whitenoise](https://pypi.org/project/whitenoise/) (5.3.0)
    - Middleware for serving static files directly through Django, for production use.

### **APIs Used**

- [The Movie Database (TMDb) API](https://www.themoviedb.org/documentation/api)
    - Integration of TMDb API for fetching movie-related data, including posters, titles, and additional information.
***

## **Testing**

### Manual Tests

#### **HTML Validation**
  + *Description*: Validate HTML code using the W3 HTML Checker.
  + *Steps*:
    1. Copy the HTML code of the templates.
    2. Visit the [W3 HTML Checker](https://validator.w3.org/).
    3. Paste the HTML code and check for any validation errors.
    4. Fix any warnings or errors.
  + *Expected Result*: No validation errors found in the core structure and syntax of HTML.

    **Note**: Due to the dynamic nature of Django templates and the usage of template tags, some errors related to undefined variables or attributes may be expected.

#### **Python Linter**
  + *Description*: Ensure Python code adheres to coding standards using a linter (CI Python Linter).
  + *Steps*:
    1. Run the linter on each Python code file.
    2. Review the output for any warnings or errors.
    3. Fix any warnings or errors.
  + *Expected Result*: The code complys with coding standards without any major issues.

### **Automated Tests**

#### **Registration**
The registration process is tested to ensure that users can successfully register with the required information and that proper validation checks are in place.

**Requirements**
+ **Username**
    + Required.
    + Must be unique, will be checked back with the database.
    + Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.

+ **E-Mail Adress**
    + Required.
    + Valid E-Mail Address format.

+ **Password**
    + Required.
    + Password can’t be too similar to your other personal information.
    + Password must contain at least 8 characters.
    + Password can’t be a commonly used password.
    + Password can’t be entirely numeric.

+ **Password Confirmation**
    + Required.
    + Password confirmation must match passsword entered beforehand.


**Test Case 1: Valid Registration**
+ **Scenario:** User provides valid registration details.
+ **Steps:**
  1. Navigate to the registration page.
  2. Enter a unique username.
  3. Provide a valid email address (no email confirmation required).
  4. Enter a strong password.
  5. Confirm the password.
  6. Click the "Register" button.
+ **Expected Result:** User is successfully registered and redirected to the login page.

**Test Case 2: Missing Username**
+ **Scenario:** User attempts registration without providing a username.
+ **Steps:**
  1. Navigate to the registration page.
  2. Leave the username field empty.
  3. Provide a valid email address.
  4. Enter a strong password.
  5. Confirm the password.
  6. Click the "Register" button.
+ **Expected Result:** User receives an error message indicating that a username is required.

**Test Case 3: Password Mismatch**
+ **Scenario:** User provides mismatched passwords during registration.
+ **Steps:**
  1. Navigate to the registration page.
  2. Enter a unique username.
  3. Provide a valid email address.
  4. Enter a strong password.
  5. Confirm the password with a different value.
  6. Click the "Register" button.
+ **Expected Result:** User receives an error message indicating that passwords do not match.

**Test Case 4: Invalid Email Address**
+ **Scenario:** User provides an invalid email address during registration.
+ **Steps:**
  1. Navigate to the registration page.
  2. Enter a unique username.
  3. Provide an invalid email address (e.g., user@example).
  4. Enter a strong password.
  5. Confirm the password.
  6. Click the "Register" button.
+ **Expected Result:** User receives an error message indicating that the provided email address is not valid.


### **Unresolved Errors, Issues and Bugs**

+

## **Deployment**

### **Project Creation**

The project was started by navigating to the [template provided](https://github.com/Code-Institute-Org/ci-full-template) and clicking 'Use this template'. Under Repository name I input "movie-reviews-with-friends" and checked the 'Include all branches' checkbox. I then navigated to the new [repository](https://github.com/NixTS/movie-reviews-with-friends). I then clicked the Open with GitHub Desktop button.

After GitHub Desktop opened this repository, i cloned the repository to a directory on my PC and clicked "Open in Visual Studio Code"

Opening [Visual Studio Code](https://code.visualstudio.com/). The following commands were used throughout the project:

+ git add filename - This command was used to add files to the staging area before committing.
+ git commit -m *"commit message explaining the updates"* - This command was used to commit changes to the local repository.
+ git reset HEAD^ - This command was used to delete the last commit but keep all the changes.
+ git push - This command is used to push all committed changes to the GitHub repository.

### **Run Locally**

To launch the Django application locally, follow these steps:
1. Open the terminal in Visual Studio Code.
2. Enter the command: "python manage.py runserver" without the quotes.
2. Copy the URL displayed next to "Starting development server at" (e.g., http://127.0.0.1:8000).
3. Paste the copied URL into your browser's address bar.
4. The browser will then render the provided templates, showcasing the app.

To halt the Django development server, follow these steps:
1. Click on the terminal running the development server.
2. Press "Ctrl + C" to stop the server.

### **Deployment to Live Service**

1. Get the project ready for deployment

    + Ensure the project is ready for deployment and includes all necessary dependencies in a requirements.txt file using this command.

    + pip3 freeze > requirements.txt

    + In the settings, set "Debug" to "False" and save the file.

2. Pushing GitHub

    + Make a commit and push the current version of the program to GitHub.

    + git commit -m "..."  
    + git push

3. Set Up ElephantSQL (PostgreSQL)

   + Visit [ElephantSQL](https://www.elephantsql.com/) and create a new PostgreSQL instance.
   + Obtain the database URL provided by ElephantSQL.

4. Heroku starting a new project

    + Visit the [Heroku](https://dashboard.heroku.com/) dashboard and click "New App" after that, give the project a name and select a region, next.

5. Heroku project settings

    + In the project dashboard click "Settings" and head to the "Project Vars" section. CLick "Reveal Config Vars" opening two input fields.
    + Put in the following:
        + DATABASE_URL - *postgres://your-database-link"
        + DISABLE_COLLECTSTATIC - *1*
        + SECRET_KEY - *you-secret-key from the env.py file*
        + TMDB_API_KEY - *The Movie Database api key from the env.py file*

6. Connecting to GitHub

    + Click the "Deploy" tab and select "GitHub" and then "Connect to Github".

7. Selecting the Project

    + After successfully connecting to GitHub a search bar opens. Type the name of the repository your project is in. A dropdown menu will open, click on the correct repository. This links up the repository from GitHub to heroku.

8. Deployment

    + Scroll down and select either "Automatic deploys" or "Manual deploy". After the deployment is finish, head over to the "Overview" tab on heroku. On the top right, click "Open app" a new tab will open with the deployed project.

***

## **Credits**

### **Project Idea**

The inspiration behind this project originates from my deep passion for movies and the joy I find in sharing my views and thoughts about cinema. As a cinema enthusiast, discussing and exploring movies is not just a hobby but a source of immense delight in my daily life. The challenge of discovering new and exciting films further fueled my idea to create a website.

The concept revolves around users forming groups centered on specific movie themes, facilitating collaborative reviews and discussions. By creating an interactive platform where like-minded individuals share their opinions, the website aims to serve as a valuable resource for discovering new movies that align with personal interests and preferences.

### **Content**

The content of this website was created by [NixTS](https://github.com/NixTS/).

The Movie Reviews with Friends website utilizes The Movie Database [TMDB API](https://developer.themoviedb.org/docs/getting-started) for content, and all rights to the data belong to TMDB. This project is not intended for commercial use, and the usage of [TMDB](https://www.themoviedb.org/) data is in compliance with [TMDB's API terms of use](https://www.themoviedb.org/api-terms-of-use) and [TMDB's terms of use](https://www.themoviedb.org/terms-of-use).

The Python code provided was made with the knowledge gained through the CodeInstitute Full Stack Developer course.

### **Acknowledgements**

I'd like to thank my mentor [Daisy McGirr](https://github.com/Dee-McG) for her guidance throughout my project.
