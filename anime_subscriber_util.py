
class Anime:

    # add status tuples here (for our standard data format)
    def __init__(self, anilist_id, title, status, tot_num_ep,# iss: pick which params are req and default vals
                 ext_links, cover_med_imglink, cover_lg_imglink, cover_xl_imglink, last_updated,
                 stream_options=None, num_eps_released=None, latest_ep_stream_links=None,
                 next_air_ep=None, time_until_air=None, subscribers=None):
        self.anilist_id = anilist_id
        self.title = title
        self.status = status
        self.tot_num_ep = tot_num_ep
        self.ext_links = ext_links
        self.cover_med_imglink = cover_med_imglink  # iss: image links need to be a method, question: how to avoid sending many requests to api to retrieve image link
        self.cover_lg_imglink = cover_lg_imglink
        self.cover_xl_imglink = cover_xl_imglink
        self.last_updated = last_updated
        # optional
        self.stream_options = stream_options
        self.num_episodes_released = num_eps_released  # maybe not optional
        self.latest_ep_stream_links = latest_ep_stream_links  # maybe not optional, this should be a dict, { site_name : "name", url : "url" }
        self.next_air_ep = next_air_ep
        self.time_until_air = time_until_air

        # Relationships with other objs
        self.subscribers = subscribers  # these should be a list of user objects
        # question: should there be relationship between anime and streamingsite?

    def get_latest_ep_stream_links(self):
        """ returns a dictionary with all latest episode streaming option links according to last update """
        stream_links = self.latest_ep_stream_links
        return stream_links

    # iss: needs fixing
    def get_stream_options(self):
        """ returns dictionary of sites (name, link) that stream anime """
        stream_options = self.stream_options
        return stream_options

    def add_subscriber(self, user):
        """ adds a user to anime subscribers list. returns true if added else false (user already subscribed) """
        pass

    def remove_subscriber(self, user):
        """ removes a user from anime subscribers list. returns true if removed else false (user wasn't subscribed) """
        pass

    def is_airing(self):
        """ returns true if airing, else false """
        status = self.status
        if status == 'RELEASING':
            return True
        return False

    # this logic belongs in site
    def get_num_eps_released(self):
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

    def check_new_episode(self, anime_site):
        ''' returns true if new episode has been released
        may need to update self.info before returning
        '''
        pass


class Subscriber:

    def __init__(self, email, phone, site_tokens_dict=None, anime_list=None):
        self.email = email
        self.phone = phone

        # relationships with obj
        self.site_tokens_dict = site_tokens_dict  # site tokens, not an obj
        self.anime_list = anime_list

    def has_site_tokens(self):
        """ returns true if user has any site tokens """
        if self.site_tokens_dict:
            return True
        return False

    def add_site_token(self, endpoint_url, token_val):
        """ adds token to site_tokens_dict if in correct format, replaces if already existing for site """
        # check valid format
        # check for endpoint_url in self.site_tokens_dicts
        # if exists, replace token val
        # if not, add new key,val pair to dict
        pass

    def remove_site_token(self, endpoint_url):
        """ removes token from site_tokens_dict if present. if not, returns false """
        # check for endpoint_url in self.tokens_dict
        # if present, remove and return true
        # if not, remove and return false
        pass

    def get_authorized_sites(self):
        """ returns list of endpoint_urls that user has tokens for """
        pass
