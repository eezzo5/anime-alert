# Anime-Alert Software Design Document

## Project Goals  
The anime-alert projects goal is to create a flexible python package for developers that will do the following in multiple contexts (CLI, REST API, etc.):  
- Create and manage lists of Anime to receive notifications about (new episodes, options for watching, etc.). 
- Allow end users to subscribe to, clone and/or modify created Anime lists    
- Allow end users to manage how they will be notified (email or text)  
- Allow developers to manage the content of notifications
- Allow developers to manage which data sources they use to obtain Anime data

This project will include a REST API and CLI interface. Whether these will be in separate repos or the same one as the domain logic stuff is TBD.

## Deliverables  
1. Milestone - Domain Logic (Rough Draft)
    1. User requirements - expected operations (user stories) for the following functionality:
        - anime list management
        - anime list subscriber management  
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
        4. Completed code
    2. CLI - Portable command line tool
        1. General approach and data storage
        2. Commands specifications
        3. Class and function descriptions for CLI interface
        4. Unit tests
        5. Completed code

