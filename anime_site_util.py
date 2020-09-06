import requests


class StreamingSite:
    def get_episode_streaming_link(self, anime):
        pass



class AnimeListSite:
    def can_connect(self):
        pass
    def auth_user(self):
        pass
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
    def start(self):
        pass
    def stop(self):
        pass
    def get_status(self):
        pass
    def add_anime(self, id):
        pass
    def remove_anime(self, id):
        pass
    def check_anime_status(self, anime_dict):
        pass
    def check_new_episode(self, id):
        pass
    def get_num_released_episodes(self, anime_dict):
        pass
    def get_anime_streaming_sites(self):
        pass



class AnimeSiteUser:
    def get_user_anime(self):
    # return, id, title, image, num_episodes released, time til next release
        pass
    def get_synced_sites(self):
        pass
