# BlackJack

This project provides a Python script to play blackjack against the dealer and a Python script to provide visualizations for the win rate of the user vs the dealer

## Features

- Displays ASCII art of playing cards from ASCII Playing Cards repo by Naivoder
- Provides barebones blackjack gameplay, excluding ability to split a dealt hand and betting functionality
- Logs all round results to enable up-to-date representation of gameplay data through multiple visualization methods

## Requirements

To run this script, you need Python 3.x. Other libraries needed are listed as follows:

- matplotlib
- pandas
- numpy

## Usage 

- main.py can be used to play Blackjack against the dealer
- visualizations.py can be used to display the game data in the following formats:
  
  - A bar chart displaying win/loss/tie counts as integers

    ![bar chart image](https://github.com/BrandonL02/BlackJack/blob/d25a26021fa382d8ddd05adb361fde7cf29752f3/visuals/bar%20chart.png)
  
  - A pie chart displaying win/loss/tie rates

    ![pie chart image](https://github.com/BrandonL02/BlackJack/blob/d25a26021fa382d8ddd05adb361fde7cf29752f3/visuals/pie%20chart.png)
