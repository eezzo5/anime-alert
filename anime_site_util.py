class StreamingSite:
    def __init__(self, url, ep_id_template):
        self.url = url
        self.ep_id_template = ep_id_template

    def get_episode_streaming_link(self, anime):
        pass

class SiteAuthConfig:
    """ Class that handles Oauth2.0 logic.
    Will define authentication endpoint, client_id, client_secret, redirect_uri,
                                    and code_challenge/verifier generation logic
    Will have methods to generate start auth requests info, generate tokens, and refresh tokens for subscribers
    This may be gratuitous if we cannot make animeListSite querying and response parsing sufficiently flexible to
    onboard sites dynamically without having to extend the class to add new stuff
    """

class AnimeListSite:
    import conf

    def __init__(self, endpoint_url='https://graphql.anilist.co', auth_required=False, app_token=None,
                 query_method='POST',
                 anime_query_template='',
                 anime_bulk_query_template='',
                 user_anime_list_query_template='''
                            query ($id: Int) {
                                MediaListCollection(userId: $id, type:ANIME, status:CURRENT){
                                    lists {
                                        entries {
                                            media {
                                                id
                                                title {
                                                    userPreferred
                                                }
                                                coverImage {
                                                    medium
                                                }
                                                nextAiringEpisode{
                                                    episode
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                            '''
                 ):

        self.endpoint_url = endpoint_url
        # auth stuff
        self.auth_required = auth_required
        self.app_token = app_token

        self.query_method = query_method
        self.anime_query_template = anime_query_template
        self.anime_bulk_query_template = anime_bulk_query_template
        self.user_anime_list_query_template = user_anime_list_query_template

    def can_connect(self):
        """ tests if site can be connected to """
        pass

    def can_get_anime_data(self):
        """ checks if app token is valid and usable if required. if token expired this will attempt to refresh token
        returns True/False, error
        """
        # if app doesn't req auth return false, auth not required error
        # maybe this calls self.get_subscriber_token?
        pass

    def can_get_subscriber_data(self, subscriber):
        """ checks if subscriber token is valid and usable. if token expired this will attempt to refresh token
        returns True/False, error
        """
        # if app doesn't req auth return false, auth not required error
        # maybe this calls self.get_subscriber_token?
        pass

    def set_app_token(self):
        """ sets apps auth token for site and checks if it is usable (calls can_get_anime_data) """
        pass

    def remove_app_token(self):
        """ removes app token """
        pass

    def refresh_token(self, token):
        """
        attempts to refresh subscriber's site token using old token value or returns False, error
        this will remove self.app_token if token cannot be refreshed
        """
        pass

    def get_subscriber_token(self, subscriber):
        """ gets subscriber token value for site or returns false, error """
        pass

    def get_subscriber_user_id(self, subscriber):
        """ gets the user id for the site or return None, error """
        # maybe this calls self.is_subscriber_auth?
        pass

    def get_anime_data(self, anime_id):
        """ returns anime object with data from anime site """
        pass

    def get_bulk_anime_data(self, anime_id_list):
        """ returns list of anime objects matching list of ids given """
        pass

    def get_user_anime_list(self, subscriber):
        """ returns list of anime objects representing anime user currently watching """
        import requests
        # iss: this should return anime objects and perform logic listed in comments below

        # check if subscriber tokens contains token for this site
        # check if token is auth
        sub_user_id, error = self.get_subscriber_user_id(subscriber)
        # do data retrieval
        # do anime obj creation
        # call calculated fields stuff and store in appropriate anime obj attr
        # return

        variables = {
            'id': sub_user_id
        }

        url = self.endpoint_url

        response = requests.post(url, json={'query': self.user_anime_list_query_template, 'variables': variables})

        json_response = response.json()

        user_anime_data = json_response['data']['MediaListCollection']['lists'][0]['entries']

        return user_anime_data

    def calc_num_eps_released(self, anime_obj):
        """ returns the number of released episodes for anime """
        # iss: use tuples for statuses
        status = self.status
        if status == 'RELEASING':
            next_airing = self.next_air_ep
            latest_episode_num = next_airing - 1
        elif status == 'NOT_YET_RELEASED':
            latest_episode_num = 0
        elif status == 'CANCELLED' or status == 'FINISHED':
            latest_episode_num = self.tot_num_ep
            if not latest_episode_num:
                latest_episode_num = 0
        return latest_episode_num

    def get_stream_options(self, anime_obj):
        """ returns dictionary of sites (name, link) that stream anime """
        pass

    def get_latest_ep_stream_links(self, anime_obj):
        pass

    def calc_released_ep_stream_link(self, anime_obj):
        pass
