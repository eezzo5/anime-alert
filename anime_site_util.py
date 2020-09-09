class StreamingSite:
    def __init__(self, url, ep_id_template):
        self.url = url
        self.ep_id_template = ep_id_template

    def get_episode_streaming_link(self, anime):
        pass

class AnimeListSite:
    import conf

    def __init__(self, endpoint_url='https://graphql.anilist.co',
                 # auth stuff is for site's anime data retrieval requirements, not end user auth stuff
                 req_auth=False, auth_req_captcha=False, auth_user=conf.uname, auth_pass=conf.pw, token=None,
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
        self.token = token

        self.query_method = query_method
        self.anime_query_template = anime_query_template
        self.anime_bulk_query_template = anime_bulk_query_template
        self.user_anime_list_query_template = user_anime_list_query_template

    def can_connect(self):
        pass

    def auth_user(self):
        pass

    def get_anime_data(self, anime_id):
        pass

    def get_bulk_anime_data(self, anime_id):
        pass

    def get_user_anime_list(self, user):
        import requests

        variables = {
            'id': user
        }

        url = self.endpoint_url

        response = requests.post(url, json={'query': self.user_anime_list_query_template, 'variables': variables})

        json_response = response.json()

        user_anime_data = json_response['data']['MediaListCollection']['lists'][0]['entries']

        return user_anime_data

class Anime:

    # add status tuples here (for our standard data format)
    def __init__(self, anilist_id, title, status, tot_num_ep,# iss: pick which params are req and default vals
                 next_air_ep, time_until_air, ext_links,
                 cover_med_imglink, cover_lg_imglink, cover_xl_imglink, last_updated,
                 subscribers):
        self.anilist_id = anilist_id
        self.title = title
        self.status = status
        self.tot_num_ep = tot_num_ep
        self.next_air_ep = next_air_ep
        self.time_until_air = time_until_air
        self.ext_links = ext_links
        self.cover_med_imglink = cover_med_imglink
        self.cover_lg_imglink = cover_lg_imglink
        self.cover_xl_imglink = cover_xl_imglink
        self.last_updated = last_updated

        #this may be bad practice, check
        self.num_episodes_released = self.get_num_eps_released()
        self.latest_ep_stream_link = self.get_latest_ep_stream_link()

        # Relationships with other objs
        self.subscribers = subscribers # these should be user objects
        # question: should there be relationship between anime and streamingsite?

    #this method might call AnimeSite method or StreamingSite method
    def get_latest_ep_stream_link(self, stream_site):
        pass

    #this method might call AnimeSite method or StreamingSite method
    def get_released_ep_stream_link(self, stream_site):
        pass

    def get_anime_status(self):
        """ gets anime status when last checked """
        status = self.status
        return status

    def is_airing(self):
        """ returns true if airing, else false """
        status = self.status
        if status == 'RELEASING':
            return True
        return False

    def get_num_eps_released(self):
        """ returns the number of released episodes for anime """
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

    def check_new_episode(self, anime_site):
        ''' returns true if new episode has been released
        may need to update self.info before returning
        '''
        pass

    def get_stream_opts(self, anime_site):
        """
        checks external links for known streaming sites and returns them in a list of dicts
            {
                "name":"CrunchyRoll",
                "url":"https://crunchyroll.com/<anime-name>",
            },
        """
        pass

    def update_data(self, anime_site):
        pass

class User:

    def __init__(self, email, phone, site_tokens_dict=None, anime_list=None):
        self.email = email
        self.phone = phone

        # relationships with obj
        self.site_tokens_dict = site_tokens_dict # site tokens, not an obj
        self.anime_list = anime_list

    def get_saved_user_anime_list(self):
        """ gets local user anime list if it exists (must have called get_fresh_user_anime_list) """
        anime_list = self.anime_list
        return anime_list

    def get_fresh_user_anime_list(self):
        ## return, id, title, image, num_episodes released, time til next release
        # for each site_token
            #create site obj and call isauth
            # if isauth call site.getuseranime()
            # win win win no matta what
            # create anime obj and add to self.anime_list
        pass

    def has_site_token(self):
        pass

    def get_synced_sites(self):
        pass

