from project.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild != self.name and player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."
        elif player not in self.players:
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"
        elif player in self.players:
            return f"Player {player.name} is already in the guild."

    def kick_player(self, player_name: str):
        for current_player in self.players:
            if current_player.name == player_name:
                self.players.remove(current_player)
                current_player.guild = "Unaffiliated"
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        return f"Guild: {self.name}\n" + '\n'.join([current_player.player_info() for current_player in self.players])




