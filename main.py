from utils.scraper import fetch_goalie_stats
from utils.storage import save_goalie_stats, load_goalie_stats
import sys

def simulate_goalie_stat_change(stats_dict):
    for player in stats_dict:
        stats_dict[player]["goals"] += 1
        break
    return stats_dict 

if __name__ == "__main__":
    current_stats = fetch_goalie_stats()
    saved_stats = load_goalie_stats()
    current_stats_dict = {g["player"]: {"goals": g["goals"], "assists": g["assists"]} for g in current_stats}

    
    test_mode = "--test" in sys.argv

    if test_mode:
        print("Test mode: Faking a stat change...")
        current_stats_dict = simulate_goalie_stat_change(current_stats_dict)

    updated = False

    for player, stats in current_stats_dict.items():
        if player not in saved_stats:
            print(f"New goalie detected: {player}")
            saved_stats[player] = stats
            updated = True
        else:
            saved_player = saved_stats[player]
            if stats["goals"] != saved_player["goals"] or stats["assists"] != saved_player["assists"]:
                print(f"Stat change detected for {player}: {saved_player} -> {stats}")
                saved_stats[player] = stats
                updated = True
    if updated:
        save_goalie_stats(saved_stats)
        print("Saved updated goalie stats")
    else:
        print("No changes detected")