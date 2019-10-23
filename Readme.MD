# Fourth Milestone Project 
[![Build Status](https://travis-ci.org/IstvanGercsak/Fourth_Milestone_Project.svg?branch=master)](https://travis-ci.org/IstvanGercsak/Fourth_Milestone_Project)

# Description

# Branches
- QA branch for testing and developing
- Master branch for working stable production environment

# Application hosts
- Application and Database
    - Heroku
- Data store
    - Amazon S3 Bucket [link](https://aws.amazon.com/s3/)

# Databases
- Local
    - sqlite3
- Remote DB
    - PostgreSQL 

# Security
- Django authentication
- Secret keys and confidential data:
    - Locally:
        - env.py file
    - Online:
        - Storing as environmental variables (Travis CI and Heroku)

# Test
- Automated testing with Travis CI [link](https://travis-ci.org/)