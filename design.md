# Anime-Alert Software Design Document

## Project Goals  
The anime-alert project's goal is to create a web application (REST API + REACT.js front end) that will allow users to be notified via text or email 
when new anime episodes from their synced anime list (anilist.co, myanimelist.net, etc.) have been released. 
Users will be able to customize notification messages, enable/disable notifications for phone/email, specific anime, or their entire synced anime lists.

## Deliverables  
1. Milestone - Domain Logic
    1. [User and Functional Requirements](user-and-func-requirements.md) - expected application behavior (user stories) and functional requirements to support that behavior
    2. Software Design - class and function descriptions that cover all functional requirements
    3. Unit Tests - tests written for classes and functions specified in software design document
    4. Complete Domain Logic Code - completed code which passes all unit tests  

2. Milestone - Interface and Data Storage Implementation
    1. REST API - Django REST API
        1. Infrastructure and deployment strategy (CD)
        2. API documentation
        3. Unit tests
        4. Regression tests?
        5. Completed code
