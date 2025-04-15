
import pandas as pd

def store_results(p_score, d_score, result):
    filename = 'blackjack_data.csv'
    columns = ['user score', 'dealer score', 'round outcome']

    try:
        # Try to read existing data
        game_data = pd.read_csv(filename)
    except FileNotFoundError:
        # Create new DataFrame if file doesn't exist
        game_data = pd.DataFrame(columns=columns)

    # Add the new result
    new_row = {'user score': p_score, 'dealer score': d_score, 'round outcome': result}
    game_data.loc[len(game_data)] = new_row

    # Save without writing the index column
    game_data.to_csv(filename, index=False)

# Example usage
store_results(19, 22, 'loss')
