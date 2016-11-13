""""
File         : handler.py
Author           : ian
Created          : 02-15-2016

Last Modified By : ian
Last Modified On : 02-15-2016
***********************************************************************
The MIT License (MIT)
Copyright © 2015 Ian Cooper <ian_hammond_cooper@yahoo.co.uk>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
***********************************************************************
"""

import time

from nutrimatic.exceptions import DispenserException


class Bag:
    """A bag containing tea"""
    def __str__(self):
        return "Tea Bag, English Breakfast"

    def brew(self):
        print("Brewing a cup")
        time.sleep(3)


class Cup:
    """Receptacle for tea"""
    def __init__(self):
        self._contents = []

    def __str__(self):
        buffer = "cup of tea: "
        for ingredient in self._contents:
            buffer += ", " + ingredient
        return buffer

    def drink(self):
        print(self)
        print("What do you think I am, a masochist on a diet!")

    def fill(self, ingredient):
        self._contents.append(ingredient)

    def stew(self):
        for ingredient in self._contents:
            if isinstance(ingredient, Bag):
                ingredient.brew()


class Milk:
    """A cup of tea needs milk"""
    def __str__(self):
        return "Milk"


class Sugar:
    """A cup of tea might need milk"""
    def __str__(self):
        return "Sugar"


class TeaDispenser:
    """ The Nutrimatic Drinks Dispenser
    """
    def __init__(self):
        self._filled = False
        self._water = Water()
        self._cup = Cup()

    def fill(self):
        print("Fill Water Heater")
        self._filled = True
        return ("Water Heater Filled")

    def boil(self):
        print("Boil Water")
        if self._filled:
            self._water.boil()
            time.sleep(10)  # we are boiling the water
        else:
            raise DispenserException("The kettle has not been filled yet")
        return ("Water Boiled")

    def ready_cup(self):
        print("Ready Cup")
        self._cup.fill(Bag())
        return ("Cup Ready with Bag")

    def pour_water(self):
        print("Fill cup with water")
        if self._water.boiled:
            self._cup.fill(self._filled)
            self._cup.stew()
        else:
            raise DispenserException("The water has not boiled")
        return ("Filled Cup with Water")

    def add_milk(self):
        print("Add Milk")
        self._cup.fill(Milk())
        return ("Added milk")

    def add_sugar(self, spoons):
        print("Add Sugar to taste")
        for i in range(1, spoons):
            self._cup.fill(Sugar())
        return ("Added sugar")

    def done(self):
        print("Share and enjoy!")
        return("Drink dispensed")


class Water:
    """A cup of tea needs water"""
    def __init__(self):
        self._boiled = False

    def __str__(self):
        if (self._boiled):
            return "Hot Water"
        else:
            return "Cold Water"

    def boil(self):
        self._boiled = True

    @property
    def boiled(self):
        return self._boiled

