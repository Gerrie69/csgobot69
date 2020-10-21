import steam
from steam.steamid import SteamID


def get_matches_page(steam_url: str):
    steam_id = steam.steamid.steam64_from_url(steam_url)
    return f'https://csgostats.gg/player/{steam_id}#/matches'

