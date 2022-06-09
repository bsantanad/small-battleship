#!/usr/bin/env python
import random

import numpy as np

import lib

np.set_printoptions(formatter={'int': lib.color_sign})

log = lib.log_c()

MAP_SIZE = 3 # grid size nxn
NUM_SHIPS = 3
RANDOM_SEED = 42

P1_HITS = 0
P2_HITS = 0

def set_player_board(grid):
    '''
    iterate NUM_SHIPS times to get the coords of the user, it will print
    the board every time the user enters a coord with the ship already
    in place.

    :params: grid of MAP_SIZE by MAP_SIZE, dtype int

    :returns: grid with numbers updated
    '''
    i = 1
    while True:
        if i > NUM_SHIPS:
            break

        log.separator('-')

        log.info(f'coords for your {i} ship')
        print(grid)

        x = input('x: ')
        y = input('y: ')

        if not validate_coords(x, y):
            continue

        x = int(x)
        y = int(y)

        if grid[x][y] != 0:
            log.error('bad coords, already have a ship there try again')
            continue


        grid[x][y] = 1

        i += 1

    return grid

def set_computer_board(grid):
    log.info('setting computer board')
    i = 1
    while True:
        if i > NUM_SHIPS:
            break
        x = random.randint(0, MAP_SIZE - 1)
        y = random.randint(0, MAP_SIZE - 1)
        if grid[x][y] != 0:
            continue
        grid[x][y] = 1

        i += 1

    log.good('done')
    return grid

def guess(guess_grid, player_grid):
    while True:
        x = input('x: ')
        y = input('y: ')
        if validate_coords(x, y):
            break

    x = int(x)
    y = int(y)

    if player_grid[x][y] == 1:
        log.good('hit')
        guess_grid[x][y] = 8
        return guess_grid

    guess_grid[x][y] = 6
    return guess_grid

def computer_turn(level, player_grid):
    #if level == 'dumb':
    while True:
        x = random.randint(0, MAP_SIZE - 1)
        y = random.randint(0, MAP_SIZE - 1)

        if player_grid[x][y] != 6 and player_grid[x][y] != 8:
            break

    if player_grid[x][y] == 1:
        log.good('hit')
        player_grid[x][y] = 8
        return player_grid

    player_grid[x][y] = 6
    return player_grid

def validate_coords(x, y):
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        log.error('bad coords, try again')
        return False

    if x > MAP_SIZE - 1 or y > MAP_SIZE - 1:
        log.error('bad coords, try again')
        return False

    if x < 0 or y < 0 :
        log.error('bad coords, try again')
        return False

    return True

def game():
    # setting up everything
    p1_board = np.zeros([MAP_SIZE, MAP_SIZE], dtype = int)
    p2_board = np.zeros([MAP_SIZE, MAP_SIZE], dtype = int)

    p1_board = set_player_board(p1_board)
    log.separator('=')
    p2_board = set_computer_board(p2_board)
    log.separator('=')

    p1_guess = np.zeros([MAP_SIZE, MAP_SIZE], dtype = int)

    log.info('game starting')
    log.separator('=')

    turn = 1
    while True:
        log.separator('=')
        log.info(f'turn {turn}')
        print(p1_guess)
        log.separator('-')
        print(p1_board)

        p1_guess = guess(p1_guess, p2_board)
        p1_board = computer_turn('dumb', p1_board)

        turn += 1

game()
