import requests
import time


# checker service always running
# list of anime to check for new
# to add new anime must pass first sub
# each anime has list of subscribers
def get_user_current_anime(user):
    query = '''
    query ($id: Int) {
        MediaListCollection(userId: $id, userName:"", 
                                    type:ANIME, status:CURRENT){
            user {
              id
            } 
            lists {
              entries {
                media {
                  id
                }
              }
            }
        }
    }
    '''

    id_array = None
    # get data
    # if has entries
    # delete duplicates and return
    # return, id, title, image, num_episodes released
    return id_array

def get_new_episode_data(anime_dict, prev_num_ep, prev_ep_link):
    link = None
    title = anime_dict["title"]["romaji"]
    num_episode = prev_num_ep + 1
    # get id from link
    prev_id = int(prev_episode_link[-6:])
    new_id_str = str(prev_id + 1)
    link = prev_episode_link[0:-6] + new_id_str

    return title, num_episode, link

def get_general_link(anime_data):
    external_links = anime_data["externalLinks"]
    for link in external_links:
        if link["site"] == "Crunchyroll":
            return link["url"]
    return "No Link Available"

next_ep_num = None
prev_status = None
while True:
    query = '''
    query ($id: Int, $page: Int, $perPage: Int, $search: String) {
        Page (page: $page, perPage: $perPage) {
            pageInfo {
                total
                currentPage
                lastPage
                hasNextPage
                perPage
            }
            media (id: $id, search: $search, type:ANIME) {
                id
                type
                status
                episodes
                externalLinks {
                    site
                    url
                }
                nextAiringEpisode {
                    timeUntilAiring
                    episode
                }
                streamingEpisodes {
                    site
                    url
                }
                title {
                    romaji
                }
            }
        }
    }
    '''
    variables = {
        'id': 114236,
        'page': 1,
        'perPage': 3
    }
    url = 'https://graphql.anilist.co'

    response = requests.post(url, json={'query': query, 'variables': variables})
    json_stuff = response.json()
    anime_data = json_stuff['data']['Page']['media'][0]
    if not next_ep_num:
        prev_status = anime_data["status"]
        prev_episode_link = anime_data["streamingEpisodes"][0]["url"]
        next_ep_num = anime_data["nextAiringEpisode"]["episode"]
        if prev_status == "FINISHED":
            num_episodes = anime_data["episodes"]
            title = anime_data["title"]["romaji"]
            #get external crunchylink
            general_link = get_general_link(anime_data)
            print("%s has finished airing!\nThere are %s episodes\nView them here: %s" % (title, num_episodes, general_link))
            break

        print("starting new episode monitor")
    new_next_ep_num = anime_data["nextAiringEpisode"]["episode"]
    if next_ep_num != new_next_ep_num:
        #get anime data and print
        print("New episode aired, waitin an hour for crunchyroll link.")
        time.sleep(3600)
        print("New %s episode!\nEpisode: %s\nWatch it here: %s" % (get_new_episode_data(anime_data, next_ep_num, prev_episode_link)))
        #set prev = new
        next_ep_num = new_next_ep_num

    time.sleep(60)

