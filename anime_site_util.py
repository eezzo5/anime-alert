class StreamingSite:
    def __init__(self, url, ep_id_template):
        self.url = url
        self.ep_id_template = ep_id_template

    def get_episode_streaming_link(self, anime):
        pass


class AnimeListSite:
    import conf
    # question: should animelistsite and animedatasource be two separate objects?

    def __init__(self, endpoint_url='https://graphql.anilist.co',
                 # auth stuff is for site's anime data retrieval requirements, not end user auth stuff
                 req_auth=False, auth_req_captcha=False, auth_user=conf.UNAME, auth_pass=conf.PW, token=None,
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
        self.req_auth = req_auth
        self.auth_req_captcha = auth_req_captcha
        self.auth_user = auth_user
        self.auth_pass = auth_pass
        self.app_token = token

        self.query_method = query_method
        self.anime_query_template = anime_query_template
        self.anime_bulk_query_template = anime_bulk_query_template
        self.user_anime_list_query_template = user_anime_list_query_template

    def can_connect(self):
        """ tests if site can be connected to """
        pass

    def authenticate_app_to_site(self):
        """ auths site for API usage if auth is required and no captcha """
        pass

    def get_anime_data(self, anime_id):
        """ returns anime object with data from anime site """
        pass

    def get_bulk_anime_data(self, anime_id_list):
        """ returns list of anime objects matching list of ids given """
        pass

    def subscriber_has_token(self, subscriber):
        """ checks if subscriber has token for this site """
        pass

    def get_subscriber_token(self, subscriber):
        """ gets subscriber token value or returns false, error """
        pass

    def is_subscriber_auth(self, subscriber):
        """ checks if subscriber's token is valid and usable. if token expired this will attempt to refresh token
        returns True/False, error
        """
        # maybe this calls self.subscriber_has_token?
        pass

    # this may belong in api code
    def refresh_site_token(self, subscriber):
        """ attempts to refresh subscriber's site token using old token value or returns False, error """
        pass

    def get_subscriber_user_id(self, subscriber):
        """ gets the user id for the site or return None, error """
        # maybe this calls self.is_subscriber_auth?
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
        """ gets streaming site options listed in anime site and returns it in a dictionary """
        pass

    def get_latest_ep_stream_links(self, anime_obj):
        pass

    def calc_released_ep_stream_link(self, anime_obj):
        pass
