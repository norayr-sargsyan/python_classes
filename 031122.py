from datetime import datetime


class Country:
    def __init__(self, name_country, continent, *args, **kwargs):
        self.country_name = name_country
        self.continent = continent
        super().__init__(*args, **kwargs)

    def present(self):
        return f"This is {self.country_name}, which is located in {self.continent}."


class Brand:
    def __init__(self, brand_name, business_start_date, *args, **kwargs):
        self.brand_name = brand_name
        self.date = business_start_date
        super().__init__(*args, **kwargs)

    def present(self):
        return f"We present to you the {self.brand_name} brand, which was opened in {self.date}."


class Season:
    def __init__(self, season_name, average_temperature, *args, **kwargs):
        self.season_name = season_name
        self.temperature = average_temperature
        super().__init__(*args, *kwargs)

    def present(self):
        return f"The average temperature in {self.season_name} is {self.temperature}."


class Product(Country, Brand, Season):
    def __init__(self, product_name, product_type, product_price, product_quantity, *args, **kwargs):
        self.product_name = product_name
        self.type = product_type
        self.price = product_price
        self.quality = product_quantity
        super().__init__(*args, **kwargs)

    def present(self):
        return f"{self.product_name}: whose price is {self.price}. from the {self.type}."

    def discount(self) -> int:

        if (datetime.now().year - self.date) % 100 == 0:
            new_discount_price = self.price * 50 / 100
        elif (datetime.now().year - self.date) % 10 == 0:
            new_discount_price = self.price - (self.price * 10 / 100)
        else:
            new_discount_price = self.price

        return new_discount_price

    def increase_quality(self):

        if self.type == "food" and self.season_name == "summer":
            quality_new = self.quality + (self.quality * 50 / 100)
        elif self.type == "car_pants" and self.continent == "Asia":
            quality_new = self.quality * 3
        elif self.type == "clothes" and self.brand_name == "Adidas" and self.temperature < 0:
            quality_new = self.quality + (self.quality * 30 / 100)
        else:
            quality_new = self.quality

        return quality_new

    def decrease_quality(self):
        if self.continent == "Antarctica" and self.type == "car_pants":
            quality_new = 0
        elif self.type == "clothes" and self.continent == "Africa":
            quality_new = self.quality * 2 / 100
        elif self.type == "food" and self.product_name == "Ananas" and self.season_name == "summer":
            quality_new = self.quality - (self.quality * 70 / 100)
        else:
            quality_new = self.quality

        return quality_new


class Hotel:
    def __init__(self, hotel_name, hotel_please, mid_room_price, lux_room_price, *args, **kwargs):
        self.hotel_name = hotel_name
        self.hotel_please = hotel_please
        self.mid_room_price = mid_room_price
        self.lux_room_price = lux_room_price
        super().__init__(*args, **kwargs)
        self.mid_room = {"room1": self.mid_room_price, "room2": self.mid_room_price, "room3": self.mid_room_price}
        self.lux_room = {"room1": self.lux_room_price, "room2": self.lux_room_price, "room3": self.lux_room_price}

    def presentation(self):
        return f"Welcome {self.hotel_name} which is located in {self.hotel_please},\n" \
               f"you can relax in our luxury rooms which cost {self.lux_room_price} dollars and standard rooms which " \
               f"\n cost {self.mid_room_price} dollars. "

    def booking(self):
        if len(self.mid_room) == 0:
            self.lux_room.popitem()
            book = "Booked"
        elif len(self.lux_room) == 0:
            book = "Busy"
        else:
            self.mid_room.popitem()
            book = "Booked"

        return book

    def available_room_check(self):
        if len(self.mid_room) != 0:
            available_room = "Yes"
        else:
            available_room = "no"

        return available_room

    def discount(self):
        if 20 > datetime.now().hour > 9:
            discount_price = self.mid_room_price - (self.mid_room_price * 5 / 100)
        else:
            discount_price = self.mid_room_price
        return discount_price


class Taxi:
    def __init__(self, taxi_name, car_types, price_for_tour, *args, **kwargs):
        self.taxi_name = taxi_name
        self.car_types = car_types
        self.price_for_tour = price_for_tour
        super().__init__(*args, **kwargs)

    def presentation(self):
        return f"Taxi {self.taxi_name}\n{self.car_types} cars will serve you for only {self.price_for_tour} dollars"

    def discount(self):
        if 7 > datetime.now().hour > 4:
            discount_taxi = self.price_for_tour - (self.price_for_tour * 5 / 100)
        else:
            discount_taxi = self.price_for_tour
        return discount_taxi


class Your(Hotel, Taxi):
    def __init__(self, tour_name, *args, **kwargs):
        self.tour_name = tour_name
        super().__init__(*args, **kwargs)
        self.lux = self.price_for_tour + self.lux_room_price
        self.mid = self.price_for_tour + self.mid_room_price

    def presentation(self):
        return f"Hello we offer {self.tour_name} tour we have two options {self.lux} and {self.mid}\n" \
               f"which includes transport with {self.taxi_name} company which provides {self.car_types} cars and price \n" \
               f"for it is {self.price_for_tour}\n" \
               f"we will stay at {self.hotel_name} which offers tw"
