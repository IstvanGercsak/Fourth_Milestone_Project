# Fourth Milestone Project 
[![Build Status](https://travis-ci.org/IstvanGercsak/Fourth_Milestone_Project-Online-shop.svg?branch=QA_branch)](https://travis-ci.org/IstvanGercsak/Fourth_Milestone_Project-Online-shop)

## Description

## UX

### UI
### User story
### Mock up

## Technologies Used

- [HTML5](https://www.w3.org/html/)
    - Hypertext Markup Language is the standard markup language for creating web pages and web applications.
- [CSS3](https://www.w3.org/Style/CSS/)
    - Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a 
    markup language like HTML.
- [BootStrap 4.3.1](https://getbootstrap.com/docs/3.3/)
    - Front End Framework for developing responsive websites.
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
    - JavaScript is a lightweight interpreted or just-in-time compiled programming language with first-class functions. While it is most well-known as the scripting language for Web pages.
- [JQuery 3.4.1](https://jquery.com)
    - The project uses to simplify DOM manipulation.
- [Git](https://git-scm.com/)
    - Git is a distributed version-control system for tracking changes in source code during software development.
- [GitHub](https://github.com/)
    - GitHub Inc. is a web-based hosting service for version control using Git.
- [Django](https://www.djangoproject.com/)
    -  Django is a Python-based free and open-source web framework, which follows the model-template-view architectural pattern. Django's primary goal is to ease the creation of complex, database-driven websites.
- [Python](https://www.python.org/)
    - Python is an interpreted, high-level, general-purpose programming language
- [Heroku](https://www.heroku.com/)
    - Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud
- [PostgreSQL](https://www.postgresql.org/)
    - PostgreSQL, also known as Postgres, is a free and open-source relational database management system emphasizing extensibility and technical standards compliance. It is designed to handle a range of workloads, from single machines to data warehouses or Web services with many concurrent users.
- [Jinja2](https://palletsprojects.com/p/jinja/)
    - Jinja is a web template engine for the Python programming language. Jinja2 is a modern and designer-friendly templating language for Python, modelled after Django's templates.


## Features

- With use of the admin user we can add new product
    - Picture
- The user can add product in the cart
- User can login
- User can make payment
    - Only after login
- User can give review
    - Only after login
- Store everything in AWS
    - Static folder
    - Pictures
- Branches
- Test and test Coverage
- Database sqlite for local and PostgreSQL on Heroku
- Travis CI running on DEV environment


### Branches
- QA branch for testing and developing
- Master branch for working stable production environment

### Application hosts
- Application and Database
    - Heroku and PostgreSQL
- Data store
    - Amazon S3 Bucket [link](https://aws.amazon.com/s3/)

### Databases

- Upload database schema:
    - Change url in env.py and type the "migrate" and "makemigrations" command to upgrade db schema

- Local
    - sqlite3
- Remote DB for QA and PROD
    - PostgreSQL 

### AWS
- Set up:
    - S3:
        - Create S3 Bucket to storing data (bucket-for-milestone-project)
            - One for the QA one for the master branch
    - IAM:
        - Create a group about who can access our site
- I set up two buckets/policies/groups/user:
    - QA bucket (milestone-bucket-qa)
    - Master bucket (milestone-bucket-master)


I configured the CORS config and bucket policy as below:
- CORS Config:
```
<CORSConfiguration>
    <CORSRule>
    <AllowedOrigin>*</AllowedOrigin>
    <AllowedMethod>GET</AllowedMethod>
    <MaxAgeSeconds>3000</MaxAgeSeconds>
    <AllowedHeader>Authorization</AllowedHeader>
    </CORSRule>
</CORSConfiguration>
```

- Bucket policy:

```
{
    "Version":"2012-10-17",
    "Statement":[{
      "Sid":"PublicReadGetObject",
        "Effect":"Allow",
      "Principal": "*",
      "Action":["s3:GetObject"],
      "Resource":["/*"
      ]
    }
  ]
}
```

- After changes in the static files:
    - Run "collectstatic". It will upload the static files
    - If the QA is ok, we can run the "collectstatic" for the prod.

### Security
- Django authentication
- Secret keys and confidential data:
    - Locally:
        - env.py file contains
            - Secret keys
            - Database connection details
            - AWS authentication
    - Online:
        - Storing as environmental variables (Travis CI and Heroku)

### Test

You can see the test description under this link [link]()

- Note that for historical reasons .travis.yml needs to be present on all active branches of your project.
- Automated testing with Travis CI [link](https://travis-ci.org/)
- run test locally:
    - python manage.py test
- Coverage:
    - Install "pip install coverage"
    - Coverage check "coverage run --source='.' manage.py test"
    - Run Report with "coverage report"
    - "coverage html" -> Creates htmlcov report folder 