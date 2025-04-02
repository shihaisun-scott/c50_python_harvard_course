# get afl fantasy statistics from API
import requests

def get_all_players():
    url = "https://api.silverlight.fantasy.afl.com.au/aflfantasy/players"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch players list.")
        return []

def find_player_id(players, player_name):
    for player in players:
        full_name = f"{player['first_name']} {player['last_name']}"
        if player_name.lower() in full_name.lower():
            return player['player_id'], full_name
    return None, None

def get_stats_by_round():
    stats_by_round = []
    for round_id in range(1, 25):  # Assuming max 24 rounds
        url = f"https://api.silverlight.fantasy.afl.com.au/aflfantasy/stats-centre?roundId={round_id}"
        response = requests.get(url)
        if response.status_code == 200:
            round_data = response.json()
            stats_by_round.append((round_id, round_data))
        else:
            print(f"Failed to fetch stats for Round {round_id}")
    return stats_by_round

def main():
    player_name = input("Enter player name: ")
    players = get_all_players()
    player_id, full_name = find_player_id(players, player_name)

    if not player_id:
        print("Player not found.")
        return

    all_rounds = get_stats_by_round()

    print(f"Fantasy Stats & CBAs for {full_name}:")
    for round_id, data in all_rounds:
        player_stats = next((p for p in data if p['player_id'] == player_id), None)
        if player_stats:
            fantasy_points = player_stats.get("fantasy_score", 0)
            cbas = player_stats.get("centre_bounces", 0)
            print(f"Round {round_id}: {fantasy_points} pts | {cbas} CBAs")

if __name__ == "__main__":
    main()
