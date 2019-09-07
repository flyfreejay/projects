#just boring stuff, setting up the environment to work in
from riotwatcher import RiotWatcher, ApiError
version = "9.17.1"
api_key = 'RGAPI-2d905604-b5d0-4753-a092-53a849818f4d'
region = 'na1' #using NA server
list_of_champs = watcher.data_dragon.champions(version)['data']   #offline copy of champion data sheet

#making watcher with the api key
watcher = RiotWatcher(api_key)

#function to get the key of the champion 
def GetChampKey(champ_name):    #input the name of the champion
    return list_of_champs[champ_name]['key']

#function to get the account id of the summoner
def GetAccountId(summoner_name):    #input the summoner name
    return watcher.summoner.by_name(region, summoner_name)["accountId"]

#function to get the id of the summoner
def GetSummonerId(summoner_name):
    return watcher.summoner.by_name(region, summoner_name)["id"]

#function to get list of 10 ranked games
def GetMatchLists(account_id):
    the_list = []       #empty list to start with
    match_index = 0         #index key to iterate through the games
    matchlist = watcher.match.matchlist_by_account(region, account_id)['matches']       #import the matchlists
    while len(the_list) != 10:          #if there are 10 ranked games in the list, stop
        match = matchlist[match_index]
        if match['queue'] == 420:           #420 means that the game is ranked game
            the_list.append(match['gameId'])
        match_index += 1            #regardlessly increase the index key by 1
    return  the_list            #return the list

#function to get the participant id
def GetParticipantId(match_id, summoner_name):
    match = watcher.match.by_id(region, match_id)
    participant_id = int()
    for i in range(0,9):
        if match['participantIdentities'][i]['player']['summonerName'] == summoner_name:
            participant_id = i
            break
    return participant_id

#function to see if the participant with the id won the game or not
def WinOrLose(match_id, participant_id):
    match = watcher.match.by_id(region, match_id)
    return match['participants'][participant_id]['stats']['win']

#main if ran as main. Read summoner's name and see if his win or lose in his last 10 ranked games
if __name__ == '__main__':
    summoner_name = input("Please enter your Summoner name(CAPS SENSITIVE!): ")
    
    account_id = GetAccountId(summoner_name)
    match_list = GetMatchLists(account_id)
    
    for match_id in match_list:
        participant_id = GetParticipantId(match_id, summoner_name)
        print(WinOrLose(match_id, participant_id))
    
    #GUI... I guess
    print("\n===============================================")
    print("THANK YOU SO MUCH FOR USING OUR FINDTROLLS APP\nNOW GO FUCK YOURSELF!!!")
    print("===============================================")