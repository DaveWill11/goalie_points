import requests
from bs4 import BeautifulSoup
import datetime

def fetch_goalie_stats():
    DATE = datetime.datetime.now()
    CUR_YEAR = DATE.strftime("%Y")
    url = f'https://hockey-reference.com/playoffs/NHL_{CUR_YEAR}_goalies.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.find("table", {"id": "stats"})

    if not table:
        print("Goalie stats not found")
        return []
    
    stats = []

    for row in table.tbody.find_all("tr"):
        if row.get("class") == ["thead"]:
            continue

        player = row.find("td", {"data-stat": "player"}).text.strip()
        goals = row.find("td", {"data-stat": "goals"}).text.strip()
        assists = row.find("td", {"data-stat": "assists"}).text.strip()

        stats.append({
            "player": player,
            "goals": int(goals) if goals.isdigit() else 0,
            "assists": int(assists) if assists.isdigit() else 0,
        })
    
    return stats
        