from utils.logger import log_and_print

#Helper function to add a goal to the first goalie to simular a change for testing
def simulate_goalie_stat_change(stats_dict):
    for player in stats_dict:
        stats_dict[player]["goals"] += 1
        break
    return stats_dict 

def handle_test_mode(current_stats_dict, args):
    test_mode = "--test" in args

    if test_mode:
        log_and_print("Test Mode: Faking a stat change...")
        current_stats_dict = simulate_goalie_stat_change(current_stats_dict)
    return current_stats_dict
