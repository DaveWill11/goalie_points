from utils.scraper import fetch_goalie_stats

if __name__ == "__main__":
    stats = fetch_goalie_stats()
    for goalie in stats:
        print(f"{goalie['player']}: {goalie['goals']} G / {goalie['assists']} A")
