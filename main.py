from utils.scraper import fetch_goalie_stats
from utils.storage import save_goalie_stats, load_goalie_stats
from utils.notifier import send_notification
from utils.logger import log_and_print
from utils.test_mode import handle_test_mode
import sys

if __name__ == "__main__":
    current_stats = fetch_goalie_stats()
    saved_stats = load_goalie_stats()
    current_stats_dict = {g["player"]: {"goals": g["goals"], "assists": g["assists"]} for g in current_stats}
    current_stats_dict = handle_test_mode(current_stats_dict, sys.argv)
    
    updated = False

    for player, stats in current_stats_dict.items():
        if player not in saved_stats:
            log_and_print(f"New goalie detected: {player}")
            saved_stats[player] = stats
            updated = True
        else:
            saved_player = saved_stats[player]
            if stats["goals"] != saved_player["goals"] or stats["assists"] != saved_player["assists"]:
                log_and_print(f"Stat change detected for {player}: {saved_player} -> {stats}")
                saved_stats[player] = stats
                updated = True

                #Send push notification
                changes = []
                if stats["goals"] != saved_player["goals"]:
                    changes.append(f"Goals: {saved_player['goals']} -> {stats['goals']}")
                if stats["assists"] != saved_player["assists"]:
                    changes.append(f"Assists: {saved_player['assists']} -> {stats['assists']}")
                change_message = "; ".join(changes)

                send_notification(
                    title=f"Goalie Stat Update: {player}",
                    message=change_message
                )
    if updated:
        save_goalie_stats(saved_stats)
        log_and_print("Saved updated goalie stats")
    else:
        print("No changes detected")