# Fourth Milestone Project 

- DEV branch: 
[![Build Status](https://travis-ci.org/IstvanGercsak/Fourth_Milestone_Project-Online-shop.svg?branch=DEV)](https://travis-ci.org/IstvanGercsak/Fourth_Milestone_Project-Online-shop)

- QA branch: 
[![Build Status](https://travis-ci.org/IstvanGercsak/Fourth_Milestone_Project-Online-shop.svg?branch=QA_branch)](https://travis-ci.org/IstvanGercsak/Fourth_Milestone_Project-Online-shop)

## Description

This project created as my fourth and last Milestone project at Code Institute. From technical perspective, the project
is a full stack web application. From the business perspective this site is an online shop where we can buy training classes with secure payment. 
Next to this main functionality we can manage our account, we can access for the feed page after login and there 
we can see the news, sales and discounts. On the product page we can buy classes and we can filter between the given technologies 
which we are interested in. After to pick a technology class we can put it on the cart and buy it. 
We can write review or feedback for the product in order to inform the others about that class. There is a 
blog section where we can read about. After we logged in we can write comments for those blog posts as well.

- [View QA environment](https://online-shop-qa-branch.herokuapp.com/)
- [View Master(Prod) environment](https://last-milestone-online-shop.herokuapp.com/)

## Index

- I. [UX](#ux)
- II. [Technologies_Used](#technologies_used)
- III. [Features](#features)
- IV. [AWS](#aws)
- V. [Test](#test)
- VI. [Application_hosts_and_databases](#application_hosts_and_databases)

## UX

### Colors & Icons

- The four dominant color on the page is the grey, brown, green and the black letters.
- I use favicon for the pages and use font awesome icons for the button/menu items/interactions to easily
distinguish those elements on the pages.

### Responsive

The web application is fully responsive and works properly and looks good on Mobile/Tablet/PC devices respectively.

### User stories

#### Accounts

- As a user, I want to register on the site
- Aa a user, I want to get feedback after I register on the website 
- As a user, I want to logged in right after the registration
- As a user, I want to get feedback when there is something wrong in during the registration (Unique username and password,fields)
- As a user, I want to log in the site
- As a user, I want to log out from the site
- As a user, I want to see my details
- As a user, I want to change my details
- As a user, I want to change my password
- As a user, I want to reset my password in that case if I forget it.
- As a user, I want to get email after password reset
- As a user, I want to get feedback when I logged in
- As a user, I want to get feedback if the password is wrong

#### Feed

- As a user, I don't want to reach the page until I am not logged in
- As a user, I want to see the Feeds after I logged in

#### Products

- As a user, I want to choose between product
- As a user, I want to filter the product
- As a user, I want to get feedback after I put an item into the cart
- As a user, I want to see the product separately
- As a user, I want to put the product from the separate product page
- As a user, after the login I want to write review on the separate product page
- As a user, I want to get feedback if I write a review

#### Cart

- As a user, I want to give one item in the cart
- As a user, I want to give two or more item in the cart
- As a user, I want to amend the quantity
- As a user, I want to see next to cart item in the navigation bar that how many items I picked 
- As a user, I want to see the sum products and sum value that I have to pay on the cart page
- As a user, I want to reach the checkout page after clicking on the Checkout button
- As a user,

#### Checkout

- As a user, I want to pay with my card details
- As a user, I want to get feedback after the payment
- As a user, I want to get feedback if there is something wrong with the payment(Field, Card, etc.)
- As a user, I want to see the summary page about what I bought and how much should I pay

#### Blog

- As a user, I want to see the blog posts on the Blog page
- As a user, I want to open a single blog post on a different page
- As a user, I want to write comment for the blog post (After I logged in)
- As a user, I want to get feedback if I commented a blog post.

#### Search

- As a user, I want to search after the products
- As a user, I get feedback if there is no matching product on the page

### Mock up

- **Created with [Balsamiq Mockups 3](https://balsamiq.com/) that is a user interface design tool**
    - **Log in page**:
    ![Landing page](project-description/mockups/image.png)
    - **Register page**:
    ![Login page](project-description/mockups/)
    - ****:
    ![Feed page](project-description/mockups/)
    - ****:
    ![Register page](project-description/mockups/)
    - ****:
    ![Change password page](project-description/mockups/)
    - ****:
    ![Password reset page ?????](project-description/mockups/)
    - ****:
    ![Profile page](project-description/mockups/)
    - ****:
    ![Update profile page](project-description/mockups/)
    - ****:
    ![Product page](project-description/mockups/)
    - ****:
    ![View product page](project-description/mockups/)
    - ****:
    ![Cart page](project-description/mockups/)
    - ****:
    ![Checkout page](project-description/mockups/)
    - ****:
    ![Blog page](project-description/mockups/)
    - ****:
    ![Blog article page](project-description/mockups/)
    - ****:
    ![404 error page](project-description/mockups/)
        
## Technologies_Used

- [HTML5](https://www.w3.org/html/)
    - Hypertext Markup Language is the standard markup language for creating web pages and web applications.
- [CSS3](https://www.w3.org/Style/CSS/)
    - Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a 
    markup language like HTML.
- [BootStrap 3.3.7](https://getbootstrap.com/docs/3.3/)
    - Front End Framework for developing responsive websites.
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
    - JavaScript is a lightweight interpreted or just-in-time compiled programming language with first-class functions. While it is most well-known as the scripting language for Web pages.
- [JQuery 3.4.1](https://jquery.com)
    - The project uses to simplify DOM manipulation.
- [Git](https://git-scm.com/)
    - Git is a distributed version-control system for tracking changes in source code during software development.
- [GitHub](https://github.com/)
    - GitHub Inc. is a web-based hosting service for version control using Git.
- [Django version=1.11.25](https://www.djangoproject.com/)
    -  Django is a Python-based free and open-source web framework, which follows the model-template-view architectural pattern. Django's primary goal is to ease the creation of complex, database-driven websites.
- [Python](https://www.python.org/)
    - Python is an interpreted, high-level, general-purpose programming language
- [Heroku](https://www.heroku.com/)
    - Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud
- [PostgreSQL](https://www.postgresql.org/)
    - PostgreSQL, also known as Postgres, is a free and open-source relational database management system emphasizing extensibility and technical standards compliance. It is designed to handle a range of workloads, from single machines to data warehouses or Web services with many concurrent users.
- [SQLite](https://www.sqlite.org/)
    - SQLite is a relational database management system    
- [Jinja2](https://palletsprojects.com/p/jinja/)
    - Jinja is a web template engine for the Python programming language. Jinja2 is a modern and designer-friendly templating language for Python, modelled after Django's templates.
- [Amazon Web Services (AWS)](https://aws.amazon.com/)
    - Amazon Web Services is a subsidiary of Amazon that provides on-demand cloud computing platforms and APIs to individuals, companies, and governments, on a metered pay-as-you-go basis.
- [Amazon S3](https://aws.amazon.com/s3/)
    - Amazon Simple Storage Service (Amazon S3) is an object storage service that offers industry-leading scalability, data availability, security, and performance. This means customers of all sizes and industries can use it to store and protect any amount of data for a range of use cases, such as websites, mobile applications, backup and restore, archive, enterprise applications, IoT devices, and big data analytics.
- [Amazon IAM (Identity and Access Management)](https://aws.amazon.com/iam/)
    - AWS Identity and Access Management (IAM) enables you to manage access to AWS services and resources securely. Using IAM, you can create and manage AWS users and groups, and use permissions to allow and deny their access to AWS resources. IAM is a feature of your AWS account offered at no additional charge.

## Features

- Admin can can add new product/blogpost/create feed
- The user can add product in the cart
- User can write review under the product
- Filter between the technologies on the product page
- User can login/logout
- User can make payment
- User can give review 
- User can modify/reset password
- 404 error page when there is a mistype in the url
- Blog (Public)
- Comment blogpost with logged in user
- Search functionality between the products
- Timeline after I log in
- Store the static and media files on AWS
- Branches (DEV, QA_branch, master)
- Automated test and test coverage
- Database sqlite for local and travis. PostgreSQL on Heroku for QA_branch and master branch
- Travis CI running on sqlite database with DEV and QA_branch codebase
- Responsive design

### AWS

You can see the AWS Setup description under this link [link](https://github.com/IstvanGercsak/Fourth_Milestone_Project-Online-shop/blob/master/Setup-AWS.MD)
       
### Test

You can see the test description under this link [link](https://github.com/IstvanGercsak/Fourth_Milestone_Project-Online-shop/blob/master/Testing.MD)

- Information about why I commit the .travis.yml file (Copied from the Travis official site):
    - "Note that for historical reasons .travis.yml needs to be present on all active branches of your project."
    
### Deployment and version control:

I use git for version control

- Local version control on DEV branch
- Git commit after every given useful part of the project
- Git push into my github repository (Parallel runs the travis tests)
- Merge from DEV branch to QA_branch
- Automatic deploy on Heroku to QA application when the running Travis test is passed
- Merge from QA_branch to master branch
- Automatic deploy on Heroku to master branch
- Run the additional commands ("migrate","makemigration" when the database schema changed. And run the "colletcstatic" command if it is necessary) 

#### Branches
- DEV:
    - Branch for developing new features locally
    - Database: Local DB (sqlite3)
    - Tests: Locally runs test and run test on Travis to automate tests 
    - Static files: no bucket -> local static files
- QA:
    - Branch for test the new features on Heroku
    - Database: PostgreSQL for the QA_branch
    - Tests: Travis automation tests
    - Static files: AWS bucket for QA
- master:
    - Branch for stable production environment on Heroku
    - Database: PostgreSQL for the master branch
    - Tests: There is no running test on master
    - Static files: AWS bucket for QA 

- Before every deployment:
    - Upload database schema:
        - Deploy new version of code to QA or PROD
        - Change url in env.py and type the "migrate" and "makemigrations" command to upgrade db schema
        - Run "collectstatic" command for the right branches
    - **env.py file**:
    ![Log in page](project-description/additional_pictures_for_readme/env_file.JPG)


#### Application_hosts_and_databases

- For Architecture design I use MVT design pattern (Model-View-Template). Thanks for this I don't have to write raw sql queries.
- Application and Database
    - Heroku with PostgreSQL (QA and master)
    - Localhost with sqlite3 (DEV) (Automated test with travis is running on sqlite3 as well.)
    
#### Security

- Django authentication
- Secret keys and confidential data:
    - Locally:
        - env.py file contains
            - Environmental information
            - Secret keys
            - Database connection details
            - AWS authentication
            - Stripe paying information
    - Online:
        - Storing as environmental variables (Travis CI and Heroku)