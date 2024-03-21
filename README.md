# Recipeze 

Welcome to Recipeze, your go-to destination for discovering and sharing delicious recipes. Whether you're a seasoned chef or a beginner in the kitchen, Recipeze is here to inspire your cooking adventures.

Our platform is brimming with inspiration to transform your kitchen into a playground of flavors. Join our vibrant community of food enthusiasts and embark on a cooking odyssey filled with endless possibilities.

Don't forget to leave comments and reviews on your favorite recipes, sharing your thoughts and insights to help others discover their next culinary masterpiece.

- responsive picture here all devices

## **Table of Contents**
1. [Introduction](#introduction)
2. [Features](#features)
3. [Planning](#planning)
4. [Wireframes](#wireframes)
5. [Testing](#testing)
6. [Deployment](#deployment)
7. [Credits](#credits)

## **Introduction**
Recipeze is a Django-based recipe website designed to simplify the process of discovering, saving, and sharing your favorite recipes. The platform encourages a community of food enthusiasts to connect and exchange culinary experiences.

## **Features**
- **User Authentication:** Sign up, log in, and manage your profile.
- **Recipe Management:** Create, edit, delete, and save your favorite recipes.
- **Recipe Categories:** Organize recipes into categories for easy browsing.
- **Responsive Design:** Access Recipeze from any device, ensuring a seamless experience on desktops, tablets, and mobile phones.

- homepage screenshot, short description
  picture here
- about screenshot, short description
  picture here
- recipies screenshot, short description
  picture here 
- register screenshot, short description
  picture here
  
### **Features Left to Implement**

- Other feature ideas

## **Planning**
The Recipeze planning process involved creating user stories for both users, logged in and logged out. The creation of wireframes was made on Balsamiq , the database schema was created on https://lucid.app . Project management tools i used were Github projects to organize tasks efficiently.

### **User stories** 

| I want to | So i can | Acceptance Criteria | Achieved | Next Iteration | 
| -------- | -------- | -------- | -------- | -------- |
| Create an account  | Edit my profile, create recipes, and comment/review recipes  | Users should be able to create an account with a username, password, and potentially an email address.| :white_check_mark: | -------- |
|--------|--------|Logged-in users should have access to features like saving recipes, creating recipes, and potentially rating/commenting on recipes  | :white_check_mark: | Add saved recipes section |
| Create/add new recipes   | Share them with everyone else   | I can create new recipes by adding a title, description, ingredients, instructions, image, and category.| :white_check_mark: | Enhance recipe categorization |
| Edit my posted recipes | ammend any issues/details | I can edit my existing recipes | :white_check_mark: | -------- |
| Delete my posted recipes | so they are removed | I can delete my own recipes. | :white_check_mark: | -------- |
| View all the recipes | so i can see which one i like the most | The website should have a section or page displaying a list of the all added recipes. | :white_check_mark: | Implement search and filter functionality |
| -------- | -------- | This list should update automatically as new recipes are created. | :white_check_mark: | -------- |
| View a detailed view | see all the information in the recipe | Clicking on a recipe in list should display a detailed page for that recipe. | :white_check_mark: | Implement related recipes section |
| -------- | -------- | The recipe details page should display the recipe's title, description, ingredients, instructions, image (if uploaded), and category. | :white_check_mark: | -------- |
| leave a review | people can see if it is good or not | Logged-in users should be able to rate recipes using a star rating system or similar method. | -------- | :white_check_mark: |
| -------- | -------- | Users should be able to write a review for a recipe along with their rating (optional). | -------- | :white_check_mark: |
| -------- | -------- | The average rating and potentially some user reviews should be displayed on the recipe detail page. | -------- | :white_check_mark: |
| dispaly messages | see feedback updates | I want to display a message when posted a new recipe | :white_check_mark: | Improve messaging interface |
| -------- | -------- | i want to display a warning message if you are about to delete a recipe | -------- | :white_check_mark: |

### **Models**

This was my original planned model 

![ERD](static/images/readme/recipe.png)

and this is the model i am using 

## **Wireframes**
Explore the visual representation of Recipeze's layout and user interface. These blueprints provide insights into the application's design, ensuring a user-friendly experience and will be fully responsive and accessible on mobile, tablet and desktop devices.

| Home | About |
|---|---|
| ![Home](static/images/readme/Home.png)<br>View of the home wireframe with logged in/ logged out view | ![About](static/images/readme/About.png)<br>View of the home wireframe with logged in/ logged out view |

| Recipes List | Recipes Detail |
|---|---|
| ![Recipes List](static/images/readme/Recipie-list.png)<br>View of the recipe list with logged in/ logged out view  | ![Recipes Detail](static/images/readme/Recipie-view.png)<br>View of the recipe detail with logged in/ logged out view |

| Add Recipe | Profile |
|---|---|
| ![Add Recipe](static/images/readme/Add-recipe.png)<br>View of the add recipe page  | ![Profile](static/images/readme/Profile.png)<br>View of profile page|

| Register | Sign in |
|---|---|
| ![Register](static/images/readme/Register.png)<br>View of the register page  | ![Sign in](static/images/readme/Sign-in.png)<br>View of the sign in page|


## **Testing**
Recipeze is fortified with unit tests to guarantee the reliability and functionality of its core features. 

go over all of your project’s features and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

how your project looks and works on different browsers and screen sizes.

bugs or problems you discovered during your testing, even if you haven't addressed them yet.

### **Validator Testing** 

- **HTML**
  - No errors were returned when passing through the official [W3C validator] 
- **CSS**
  - No errors were found when passing through the official [(Jigsaw) validator]

### **Unfixed Bugs**

unfixed bugs and why they were not fixed. 

- print button, printing out the page and not just the form.

## **Deployment**

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub) 

**The live link can be found here :** 
- **github** - https://github.com/CiaranBrain/Recipeze
- **heroku** - https://recipeze-da8be575c94f.herokuapp.com

## **Credits**

This project incorporates content and media from various sources. Here's a detailed breakdown:

**Content:**

* **Recipes:** This project uses recipes generated by ChatGPT: [https://openai.com/blog/chatgpt/](https://openai.com/blog/chatgpt/).
  -While ChatGPT assisted with recipe generation, the content was reviewed and curated for accuracy and quality.  

**Media:**

* **Logo:** Logo sourced from: [https://logo.com](https://logo.com) 
* **Recipe Images:** Sourced from Freepik: [https://www.freepik.com](https://www.freepik.com)

**Tutorials and Reference:**

* **Videos:** Thanks to the following YouTube channels for providing helpful tutorials:
    - Tech With Tim ([https://www.youtube.com/@TechWithTim](https://www.youtube.com/@TechWithTim))
    - Iona Frisbee ([https://www.youtube.com/@IonaFrisbee](https://www.youtube.com/@IonaFrisbee))
    - Net Ninja ([https://www.youtube.com/@NetNinja](https://www.youtube.com/@NetNinja))
    - dominicvacchiano ([https://www.youtube.com/@dominicvacchiano](https://www.youtube.com/@dominicvacchiano))

* **Code:** Some inspiration was used from the Code Institue blog, the content was reviewed and modified to suit my needs ([https://github.com/Code-Institute-Org](https://github.com/Code-Institute-Org))
* **General Guidance:** [https://www.w3schools.com/django/index.php](https://www.w3schools.com/django/index.php) for providing a comprehensive Django reference.
