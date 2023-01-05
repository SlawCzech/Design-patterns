from random import randint

from memento_.memento_.i_heart_42 import I_Heart_42


def main():
    new_game = I_Heart_42('saek')
    print(f'Hero: {new_game.game_state.name}, game level: {new_game.game_state.level}')
    memento = new_game.create_memento()

    new_game.game_state.level = randint(1, 42)
    new_game.game_state.name = 'elo'
    print(f'Hero: {new_game.game_state.name}, game level: {new_game.game_state.level}')

    new_game.set_memento(memento)
    print(f'Hero: {new_game.game_state.name}, game level: {new_game.game_state.level}')

main()