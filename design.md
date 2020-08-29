# Anime-Alert Software Design Document

## Project Goals  
The anime-alert projects goal is to create a REST API that will do the following:
- Create and manage lists of Anime to receive notifications about (new episodes, options for watching, etc.). 
- Allow end users to subscribe to, clone and/or modify created Anime lists    
- Allow end users to manage how they will be notified (email or text)  
- Allow admins (maybe users too) to manage the content of notifications
- Allow admins to manage which data sources they use to obtain Anime streaming options data

## Deliverables  
1. Milestone - Domain Logic (Rough Draft)
    1. User requirements - expected operations (user stories) for the following functionality:
        - anime list management
        - subscriber management  
        - subscriber notification methods management (email, text, etc.)
        - notification content management (what goes in notifications sent to subscribers)
        - anime data source management (where do we get info about anime?)
    2. Software Design - class and function descriptions that cover all functional requirements
    3. Unit tests - tests written for classes and functions specified in software design document
    4. Complete domain logic code - completed code which passes all unit tests  

2. Milestone - Interface and Data Storage Implementation (Rough Draft)
    1. REST API - Django REST API
        1. Infrastructure and deployment strategy (CI/CD)
        2. API documentation
        3. Unit tests
        4. Regression tests?
        5. Completed code
