"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730581174"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(og: Point, other: Point) -> int:
        """Distance formula."""
        return sqrt(((other.x - og.x)**2) + ((other.y - og.y)**2))


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE
    
    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.

    def tick(self) -> None:
        """Tick stuff."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
            if self.sickness > constants.RECOVERY_PERIOD:
                self.immunize()

    def contract_disease(self) -> None:
        """Give them bois disease."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """Vulnverable cells."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False

    def is_infected(self) -> bool:
        """Shi got infected."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False
    
    def color(self) -> str:
        """Colors of stuff."""
        if self.is_immune():
            return "blue"
        if self.is_infected():
            return "green"
        if self.is_vulnerable():
            return "gray"
        return "red"

    def contact_with(self, cell_1: Cell) -> None:
        """When they touch."""
        if cell_1.is_vulnerable() and self.is_infected():
            cell_1.contract_disease()
        if self.is_vulnerable() and cell_1.is_infected():
            self.contract_disease()

    def immunize(self) -> None:
        """Make them bois immune."""
        self.sickness = constants.IMMUNE

    def is_immune(self) -> bool:
        """IMMUNEEEE."""
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected: int, immune: int = 0):
        """Initialize the cells with random locations and directions."""
        if infected >= cells or infected <= 0:
            raise ValueError("Some number of the Cell objects must begin infected")
        if immune + infected > cells or immune < 0:
            raise ValueError("Some number of the Cell objects must begin immunne")
        self.population = []
        for _ in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            if _ < infected:
                cell.contract_disease()
            elif _ > infected and _ <= infected + immune:
                cell.immunize()
            self.population.append(cell)

    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()
        
    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def check_contacts(self) -> None:
        """Check."""
        for i in range(len(self.population)):
            for a in range(i + 1, len(self.population)):
                if self.population[i].location.distance(self.population[a].location) < constants.CELL_RADIUS:
                    self.population[i].contact_with(self.population[a])

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for i in self.population:
            if i.is_infected():
                return False
        return True