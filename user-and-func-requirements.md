# User Requirements

1. Anime List Management
    1. authorize/unauthorize anime lists access from list site (anilist, animelist, etc.)
        1. behavioral requirements
            - user will enter notification method info and get re-directed to list site for auth so we can view their list info,
                OR: if user already has notification method they will get sent a link to landing page where they have options to authorize/unauthorize list sites
        2. data requirements
            - phone or email
    2. disable/enable notifications for anime lists, and associated anime
        1. behavioral requirements
            - user will enter notification method info and receive link to landing page with synce anime list info and options to enable/disable notifications of entire lists or specific anime
        2. data requirements
            - none


2. Subscriber Notification Methods Management
    1. add a notification method
        1. behavioral requirements
           - users will add notification methods by typing in info, which will redirect to login page of list site to authorize viewing of list data. After login they be redirected back to site and see message saying "Congrats! you will now be notified, here is a link to modify notification settings"
        2. data requirements
           - phone or email
    2. remove notification method
        1. behavioral requirements
           - users should be able to remove their notification method by typing in their notification method info which triggers a notification messages (containing links) 
        2. data requirements
           - phone or email
    3. edit a notification method
        1. behavioral requirements
           - users should be able to edit their notification method by typing in their notification method info which triggers a notification messages (containing links to landing page) 
        2. data requirements
           - phone or email
    

3. Notification Content Management
    1. edit notification message content
        1. behavioral requirements
           - users will be able to edit notification message content via the landing page. There will be checkboxes determining whether or not certain data is included (streaming links, images, etc.)
        2. data requirements
           - phone or email

# Functional Requirements
1. Currently Airing Anime and Release Date Data Retrieval
    1. Currently airing anime and their data will be retrieved from the anilist.co API
    
2. Sending Notifications
    1. text messages will be sent through twilio API
    2. emails will be sent via a no-reply gmail account of some kind
