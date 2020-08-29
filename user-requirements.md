# User Requirements

1. Anime List Management
    1. create an Anime list  
        1. behavioral requirements
            - only users with account can create public lists that other users can subscribe to
        2. data requirements
            - must have: owner account, list name, last updated
            - optional: description, anime (this should come from anime source and should not be editable)
    2. delete an Anime list
        1. behavioral requirements
            - only anime lists with no other subs can be deleted
        2. data requirements
            - None
    3. edit an Anime list
        - add an anime
            1. behavioral requirements
                - only the owner of the anime list can do this
            2. data requirements
                - anime data should come from anime source and should not be editable by anyone
        - remove an anime
            1. behavioral requirements
                - only the owner of the anime list can do this
            2. data requirements
                - none
    4. get existing anime lists
        1. behavioral requirements
            - everyone can do this
        2. data requirements
            - none
    8. get existing anime in anime list
        1. behavioral requirements
            - everyone can do this
        2. data requirements
            - none
    9. clone an existing anime list under new owner    
        1. behavioral requirements
            - only people with accounts can do this
        2. data requirements
            - none
    10. archive/unarchive anime list 
        1. behavioral requirements
            - owner can not make changes to list until unarchived
            - this should only happen when owner user is deleted or if owner chooses to to show that the list is not actively maintained.
        2. data requirements
            - list is uneditable until unarchived
            - must have: archival/unarchival date
            - optional: reason

1. Subscriber Management
    1. create a user
        1. behavioral requirements
            - username and email must be unique
        2. data requirements
            - username and email must be unique
            - must have: username, email, password
            - optional: phone, 
    2. delete a user
        1. behavioral requirements
           - Anime lists associated with user will show "(deleted)" for owner
        2. data requirements
           - All user data and subscriptions removed, associations with owned anime lists removed
    3. edit a user
        1. behavioral requirements
           - when changing email and password, action must be continued by using link sent to old email to continue process
           - email change should also send link to new email to complete process
        2. data requirements
           - can not change username
    4. get existing users
        1. behavioral requirements
           - usernames are searchable by anyone
           - normal user may not search by email or see email associated with any account
        2. data requirements
           - none
        
    5. subscribe user to anime list
        1. behavioral requirements
           - user will be notified via enabled notification methods about new episodes for all anime on list
           - users w/o an account should still be able to subscribe by submitting their email or phone
           - user w/o account subscribing via phone will first be asked if the action was legit and no other notifications will be sent until a response is received (spam prevention)
        2. data requirements
           - if user with account: none
           - if user w/o account: phone or email
    6. remove user from anime list
        1. behavioral requirements
           - user will be removed from notification list for all anime in list
           - users without account will have options to unsubscribe in notification messages
        2. data requirements
           - none
    7. subscribe user to specific anime
        1. behavioral requirements
           - user will be notified via enabled notification methods about new episodes for all anime on list
           - users w/o an account should still be able to subscribe by submitting their email or phone
           - user w/o account subscribing via phone will first be asked if the action was legit and no other notifications will be sent until a response is received (spam prevention)
        2. data requirements
           - if user with account: none
           - if user w/o account: phone or email
    8. unsub user from specific anime
        1. behavioral requirements
           - user with account can unsubscribe through website or using notification messages
           - users w/o an account can only unsub through notification messages. If messages were deleted there should be a way to enter email or phone to send an unsubscribe confirmation message. These should be rate limited to prevent spam
        2. data requirements
           - if user with account: none
           - if user w/o account: phone or email

2. Subscriber Notification Methods Management
    1. edit an email
        1. behavioral requirements
           - when changing email and password, action must be continued by using link sent to old email to continue process
           - email change should also send link to new email to complete process
        2. data requirements
           - none
    2. get email 
        1. behavioral requirements
           - users should only be able to see their own email address. there should be absolutely no way to view email address before authenticating with account
        2. data requirements
           - none
    2. turn off anime email notifications 
        1. behavioral requirements
           - stops anime notifications to email
           - done after authentication or via notification message
           - if user does not have an account, email will be removed completely from notification list
           - if account, just disabled and not removed
        2. data requirements
           - email
    3. add a phone number
        1. behavioral requirements
           - users should only be able to see their own phone number. there should be absolutely no way to view phone number before authenticating with account
        2. data requirements
           - phone num
    6. remove a phone number
        1. behavioral requirements
           - users should only be able to remove their phone number after authenticating
        2. data requirements
           - phone
    6. turn off anime phone number notifications
        1. behavioral requirements
           - users should be able to disable their phone number after authenticating or via notification messages
           - users w/o an account can only unsub through notification messages. If messages were deleted there should be a way to enter phone to send a disable anime notifications confirmation message. These should be rate limited to prevent spam
           - users w/o an account disabling notifications should remove the number completely from database
        2. data requirements
           - phone
    7. edit a phone number
        1. behavioral requirements
           - if active subscriptions, must send confirmation message before continuing sending anime notifications
        2. data requirements
           - phone
    8. get phone
        1. behavioral requirements
           - users should only be able to see their own phone. there should be absolutely no way to view phone before authenticating with account
        2. data requirements
           - none
    10. send confirmation notification
        1. behavioral requirements
           - this should be sent anytime a phone or email is changed. anime notification will cease until confirmation response is received.
           - users w/o accounts must verify every time they subscribe to new list or anime
        2. data requirements
           - none

3. Notification Content Management (LOW PRIORITY, may not even include)
    1. add a notification message
    2. remove a notification message
    3. edit a notification message
    4. get existing notification messages


# Admin Requirements
1. Anime Streaming Options Info Management
    1. add a streaming platform to check if the anime can be viewed there
        1. behavioral requirements
           - admin user can add the required information needed to check whether a streaming platform provides a specific anime
        2. data requirements
           - name
           - web request host
           - file path
           - creds (if applicable)
           - parameters
           - desired response fields
           - response regex
           - info request rate
    2. remove a data source
        1. behavioral requirements
           - only admin user can do this
        2. data requirements
           - none
    3. edit a data source
        1. behavioral requirements
           - only admin user can do this
        2. data requirements
           - none
    4. get existing anime data sources
        1. behavioral requirements
           - only admin user can do this
        2. data requirements
           - none

