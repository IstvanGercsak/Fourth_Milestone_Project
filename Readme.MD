# Fourth Milestone Project 

- DEV branch: 
[![Build Status](https://travis-ci.org/IstvanGercsak/Fourth_Milestone_Project-Online-shop.svg?branch=DEV)](https://travis-ci.org/IstvanGercsak/Fourth_Milestone_Project-Online-shop)

- QA branch: 
[![Build Status](https://travis-ci.org/IstvanGercsak/Fourth_Milestone_Project-Online-shop.svg?branch=QA_branch)](https://travis-ci.org/IstvanGercsak/Fourth_Milestone_Project-Online-shop)

## Description

## Index

- I. [UX](#ux)
- II. [Technologies_Used](#technologies_used)
- III. [Features](#features)
- IV. [AWS](#aws)
- V. [Test](#test)
- VI. [Application_hosts_and_databases](#application_hosts_and_databases)

## UX

### Colors



### Icons



### Responsive



### User story



#### Accounts

- As a user, I want to register on the site
- As a user, I want to log in the site
- As a user, I want to log out from the site
- As a user, I want to change my details
- As a user, I want to change my password
- As a user, I want to reset my password in that case if I forget it.
- As a user, I want to get email after password reset

#### Cart

- As a user, 

#### Checkout

- As a user, 

#### Products

- As a user, 

### #Responsive

- As a user, 


### Mock up

- **Created with [Balsamiq Mockups 3](https://balsamiq.com/) that is a user interface design tool**
    - **Log in page**:
    ![Log in page](project-description/mockups/login.png)
    - **Register page**:
    ![Sign out page](project-description/mockups/register.png)
    
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

- Admin can can add new product
- The user can add product in the cart
- User can login
- User can make payment
- User can give review 
- User can modify password
- User can reset password if it is forgotten
- 404 error page 
- Store everything under the static folder on AWS
- Branches (DEV, QA_branch, master)
- Automated test and test coverage
- Database sqlite for local and travis. PostgreSQL on Heroku for QA_branch and master brancy
- Travis CI running on sqlite database with DEV and QA_branch codebase
- Blog (Public)
- Check the orders
- Search on the site after the items
- Timeline after I log in
- User comment timeline
- Auction or bidding (Maybe)
- Pagination if there is too much (Maybe) 

### AWS

You can see the AWS Setup description under this link [link](https://github.com/IstvanGercsak/Fourth_Milestone_Project-Online-shop/blob/master/Setup-AWS.MD)
       
### Test

You can see the test description under this link [link](https://github.com/IstvanGercsak/Fourth_Milestone_Project-Online-shop/blob/master/Testing.MD)

- Note that for historical reasons .travis.yml needs to be present on all active branches of your project.
- Automated testing with Travis CI [link](https://travis-ci.org/)
- run test locally:
    - python manage.py test
- Coverage:
    - Install "pip install coverage"
    - Coverage check "coverage run --source='.' manage.py test"
    - Run Report with "coverage report"
    - "coverage html" -> Creates htmlcov report folder 
    
### Deployment and version control:

I use git for version control

- Local version control on DEV branch
- Git commit after every given useful part of the project
- Git push into my github repository (Parallel travis tests )
- Merge from DEV branch to QA_branch
- Automatic deploy on Heroku to QA application when the running Travis test is passed
- Merge from QA_branch to master
- Automatic deploy to Heroku master
- Run the additional commands ("migrate","makemigration" when the database schema changed) 

#### Branches
- DEV:
    - Branch for developing new features locally
    - Database: Local DB (sqlite3)
    - Tests: Travis automation tests 
    - Static files: no bucket -> local static files
- QA 
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
    - Localhost with sqlite3 (DEV)
    
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