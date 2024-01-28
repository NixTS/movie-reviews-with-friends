# **Testing**

## Manual Tests

**HTML Validation**
  + *Description*: Validate HTML code using the W3 HTML Checker.
  + *Steps*:
    1. Copy the HTML code of the templates.
    2. Visit the [W3 HTML Checker](https://validator.w3.org/).
    3. Paste the HTML code and check for any validation errors.
    4. Fix any warnings or errors.
  + *Expected Result*: No validation errors found in the core structure and syntax of HTML.

![w3 hmtl checker](media/readme-images/mrwf-w3-html-checker-results.JPG)

    **Note**: Due to the dynamic nature of Django templates and the usage of template tags, some errors related to undefined variables or attributes may be expected.

**Python Linter**
  + *Description*: Ensure Python code adheres to coding standards using a linter (CI Python Linter).
  + *Steps*:
    1. Run the linter on each Python code file.
    2. Review the output for any warnings or errors.
    3. Fix any warnings or errors.
  + *Expected Result*: The code complys with coding standards without any major issues.

![python linter](media/readme-images/mrwf-python-linter.JPG)

**Responsiveness**

All pages were tested to ensure responsiveness on screen sizes from 320px and upwards. Reflow criteria for responsive design on Chrome, Edge, Firefox and Opera browsers.

Steps to test:

- Open browser and navigate to [movie review with friends](https://movie-reviews-with-friends-96186426856b.herokuapp.com/)
- Open the developer tools (right click and inspect)
- Set to responsive and decrease width to 320px
- Set the zoom to 50%
-  Click and drag the responsive window to maximum width

Expected:

Website is responsive on all screen sizes and no images are pixelated or stretched. No horizontal scroll is present. No elements overlap.

## **Automated Tests**

**Registration**
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
