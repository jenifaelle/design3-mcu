from unittest import TestCase
from app.gameboard.gameboard import Coordinate
from app.gameboard.gameboard import ObstacleValueObject
from app.gameboard.gameboard import Tag
from app.pathfinding.grid import Grid
from . import pathfinding


class PathFindingITest(TestCase):
    def test_initialise_weight_one_obstacle(self):
        obstacle = ObstacleValueObject(
            pos_x=4, pos_y=9, radius=2, tag=Tag.CANT_PASS_LEFT)
        grid = Grid(13, 13, [obstacle])

        end_position = grid.game_board[1][1]
        begin_position = grid.game_board[10][10]

        pathfinder = pathfinding.PathFinding(grid, begin_position,
                                             end_position)
        pathfinding.initialise_weight(grid, end_position, 1)
        grid.print_game_board_weight()

    def test_initialise_weight_no_obstacle(self):
        grid = Grid(6, 6, [])

        grid.print_game_board()
        end_position = grid.game_board[1][1]
        begin_position = grid.game_board[2][2]
        pathfinder = pathfinding.PathFinding(grid, begin_position,
                                             end_position)

        pathfinding.initialise_weight(grid, end_position, 1)
        grid.print_game_board_weight()

    def test_find_no_obstacle(self):
        grid = Grid(6, 6, [])

        end_position = grid.game_board[2][2]
        begin_position = grid.game_board[5][5]
        grid.print_game_board()

        pathfinder = pathfinding.PathFinding(grid, begin_position,
                                             end_position)
        pathfinder.find_path()
        grid.print_game_board_weight()
        grid.print_game_board()

    def test_find_obstacle(self):
        obstacle = ObstacleValueObject(pos_x=5, pos_y=19, radius=3, tag='')
        grid = Grid(30, 55, [obstacle])

        end_position = grid.game_board[8][50]
        begin_position = grid.game_board[2][2]

        pathfinder = pathfinding.PathFinding(grid, begin_position,
                                             end_position)
        pathfinder.find_path()
        grid.print_game_board()

    def test_find_left_obstacle(self):
        obstacle = ObstacleValueObject(
            pos_x=14, pos_y=19, radius=3, tag=Tag.CANT_PASS_LEFT)
        grid = Grid(30, 55, [obstacle])

        end_position = grid.game_board[8][50]
        begin_position = grid.game_board[2][2]

        pathfinder = pathfinding.PathFinding(grid, begin_position,
                                             end_position)
        pathfinder.find_path()
        grid.print_game_board()

    def test_find_extrem_left_right_obstacles(self):
        obstacle1 = ObstacleValueObject(
            pos_x=25, pos_y=19, radius=3, tag=Tag.CANT_PASS_LEFT)
        obstacle2 = ObstacleValueObject(
            pos_x=5, pos_y=39, radius=3, tag=Tag.CANT_PASS_RIGHT)
        grid = Grid(30, 55, [obstacle1, obstacle2])

        end_position = grid.game_board[8][50]
        begin_position = grid.game_board[2][2]

        pathfinder = pathfinding.PathFinding(grid, begin_position,
                                             end_position)
        pathfinder.find_path()
        grid.print_game_board()

    def test_find_left_rightx2_obstacles(self):
        obstacle1 = ObstacleValueObject(
            pos_x=25, pos_y=8, radius=3, tag=Tag.CANT_PASS_LEFT)
        obstacle2 = ObstacleValueObject(
            pos_x=5, pos_y=39, radius=3, tag=Tag.CANT_PASS_RIGHT)
        obstacle3 = ObstacleValueObject(
            pos_x=5, pos_y=19, radius=3, tag=Tag.CANT_PASS_RIGHT)
        grid = Grid(30, 55, [obstacle1, obstacle2, obstacle3])

        end_position = grid.game_board[8][50]
        begin_position = grid.game_board[2][2]

        pathfinder = pathfinding.PathFinding(grid, begin_position,
                                             end_position)
        pathfinder.find_path()
        grid.print_game_board()
