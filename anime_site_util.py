#class StreamingSite:
    #def get_episode_streaming_link(self, anime):
class AnimeListSite:
    import requests
    #def can_connect(self):
    #def auth_user(self):
    def get_user_anime(self, user):
        query = '''
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

        variables = {
            'id': user
        }

        url = 'https://graphql.anilist.co'

        response = requests.post(url, json={'query': query, 'variables': variables})

        json_response = response.json()

        user_anime_data = json_response['data']['MediaListCollection']['lists'][0]['entries']

        return user_anime_data

class AnimeChecker:
    #def start(self):
        #while True:
            #get_all_subscribed_anime
            #for each
                # check if airing
                    # get num released ep
                    # check_new_episode
                    # if new
                        # send notification and update num_released episodes
    #def stop(self):
    #def get_status(self):
    #def add_anime(self, id):
        #''' adds anime from list to check for new eps '''
        # will add this later when I've learned more about abstracting data interfaces
    #def remove_anime(self, id):
        #''' removes anime from list to check for new eps '''
        # will add this later when I've learned more about abstracting data interfaces
    def get_all_subscribed_anime(self):
        ''' gets anilist IDs of all anime that users have requested to be notified about '''
        # will add this later when I've learned more about abstracting data interfaces
        # using static list of current seasons anime for now
        subscribed_anime = [21,97940,108632,116006,97938]
        return subscribed_anime
    def check_anime_airing(self, anime_dict):
        ''' returns true if currently airing, else false '''
        if anime_dict['status'] == 'RELEASING':
            return True
        return False
    #def check_new_episode(self, prev_num_episodes, anime_dict):
        ''' returns true if new episode has been released '''
        # if no prev_num_episodes
    #def get_num_released_episodes(self, anime_dict):
    #def get_anime_streaming_sites(self):
#class AnimeSiteUser:
    #def get_user_anime(self):
    ## return, id, title, image, num_episodes released, time til next release
    #def get_synced_sites(self):

class Anime:
    def __init__(self, id, num_episodes):
        self.id = id
        self.num_episodes = num_episodes

