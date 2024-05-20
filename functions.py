# Various useful functions for the warehouse problem
import json


def load_data(filename: str) -> tuple:
    """Loads problem data from a file"""
    with open(filename, "r") as data_file:
        data = json.load(data_file)
        return data["items"], data["item_widths"], data["orders"]


def write_solution(item_sequence: list,
                   door_offset: float,
                   orders: list,
                   filename: str="solution.json"):
    """Writes a solution to a file"""
    solution = {"item_sequence": item_sequence,
                "door_offset": door_offset,
                "orders": orders}
    with open(filename, "w") as solution_file:
        json.dump(solution, solution_file)


def total_distance(item_sequence: list,
                   door_offset: float,
                   item_widths: dict,
                   orders: list) -> float:
    """Calculates the total distance for picking all the orders"""
    dist = 0
    item_coordinates = coordinates_from_sequence(item_sequence,
                                                 item_widths)
    for order in orders:
        # Distance from door to first item
        dist += distance(door_offset, item_coordinates[order[0]])

        # Distance between items
        item_pairs = zip(order[:-1], order[1:])
        for pair in item_pairs:
            dist += distance(item_coordinates[pair[0]],
                             item_coordinates[pair[1]])

        # Distance from last item to origin
        dist += distance(item_coordinates[order[-1]], door_offset)
    return dist


def coordinates_from_sequence(item_sequence: dict, item_widths: dict) -> dict:
    """Calculates item coordinates based on a sequence of items"""
    coordinates = dict()
    first_item = item_sequence[0]
    coordinates[first_item] = 0
    prev_coordinate = 0
    prev_width = item_widths[first_item]
    for item in item_sequence[1:]:
        coordinates[item] = prev_coordinate \
                          + prev_width / 2 \
                          + item_widths[item] / 2
        prev_width = item_widths[item]
        prev_coordinate = coordinates[item]
    return coordinates


def distance(x1: float, x2: float) -> float:
    """Returns the distance between two objects"""
    return abs(x1 - x2)
