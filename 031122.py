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
        return f"{self.product_name}: whose price is {self.price}. from the {self.type}.\n" \
               f"{Country.present(self)}\n{Brand.present(self)}\n{Season.present(self)}"

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
            self.quality = self.quality + (self.quality * 50 / 100)
        elif self.type == "car_pants" and self.continent == "Asia":
            self.quality = self.quality * 3
        elif self.type == "clothes" and self.brand_name == "Adidas" and self.temperature < 0:
            self.quality = self.quality + (self.quality * 30 / 100)

        return self.quality

    def decrease_quality(self):
        if self.continent == "Antarctica" and self.type == "car_pants":
            self.quality = 0
        elif self.type == "clothes" and self.continent == "Africa":
            self.quality = self.quality * 2 / 100
        elif self.type == "food" and self.product_name == "Ananas" and self.season_name == "summer":
            self.quality = self.quality - (self.quality * 70 / 100)

        return self.quality


x = Product(name_country="Armenia", continent="Asia", brand_name="Aregi", business_start_date=2020,
            season_name="winter", average_temperature=2, product_name="dried fruit", product_type="fruit",
            product_price=10000, product_quantity=90000)


# print(x.present())


class Hotel:
    mid_room = [1, 1, 1, 1, 1]
    lux_room = [1, 1, 1, 1, 1]

    def __init__(self, hotel_name, hotel_please, mid_room_price, lux_room_price, *args, **kwargs):
        self.hotel_name = hotel_name
        self.hotel_please = hotel_please
        self.mid_room_price = mid_room_price
        self.lux_room_price = lux_room_price
        super().__init__(*args, **kwargs)

    def presentation(self):
        return f"Welcome {self.hotel_name} which is located in {self.hotel_please},\n" \
               f"you can relax in our luxury rooms which cost {self.lux_room_price} dollars and standard rooms which " \
               f"\n cost {self.mid_room_price} dollars. "

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

    def discount_taxi(self):
        if 7 > datetime.now().hour > 4:
            discount_taxi = self.price_for_tour - (self.price_for_tour * 5 / 100)
        else:
            discount_taxi = self.price_for_tour
        return discount_taxi


class Tour(Hotel, Taxi):
    book_l = []
    book_m = []

    def __init__(self, tour_name, lux_tour, mid_tour, *args, **kwargs):
        self.tour_name = tour_name
        self.lux_tour = lux_tour
        self.mid_tour = mid_tour
        super().__init__(*args, **kwargs)
        self.lux = self.price_for_tour + self.lux_room_price
        self.mid = self.price_for_tour + self.discount()

    def presentation(self):
        return f"Hello we offer {self.tour_name} tour we have two options {self.lux}dollar and {self.mid}dollar\n" \
               f"which includes transport with {self.taxi_name} company which provides {self.car_types} cars and price \n" \
               f"for it is {self.discount_taxi()}dollar\n" \
               f"we will stay at {self.hotel_name} which offers tw"

    def lux_booking(self):

        if self.lux_tour == 1 and len(self.lux_room) != 0:
            self.book_l.append(1)
            self.lux_room.remove(1)
            book1 = f"Booked lux room,there are {len(self.lux_room)} rooms available"
        elif self.lux_tour == 0 and len(self.book_l) != 0:
            self.lux_room.append(1)
            self.book_l.remove(1)
            book1 = f"Endid Tour, booked rooms is {len(self.book_l)}"
        else:
            book1 = "All rooms are booked"
        return book1, self.lux_room, self.book_l

    def mid_booking(self):

        if self.mid_tour == 1 and len(self.mid_room) != 0:
            self.book_m.append(1)
            self.mid_room.remove(1)
            book2 = f"Booked lux room,there are {len(self.lux_room)} rooms available"
        elif self.mid_tour == 0 and len(self.book_m) != 0:
            self.mid_room.append(1)
            self.book_m.remove(1)
            book2 = f"Endid Tour, booked rooms is {len(self.book_l)}"
        else:
            book2 = "All rooms are booked"
        return book2, self.mid_room, self.book_m


order = Tour(tour_name="Agata", lux_tour=1, mid_tour=1, taxi_name="TaTul", car_types="Sprinter", price_for_tour=100,
             hotel_name="Marriott", hotel_please="Tsaghkadzor", mid_room_price=500, lux_room_price=1000)

print(order.lux_booking())
print(order.mid_booking())

order1 = Tour(tour_name="Agata", lux_tour=1, mid_tour=1, taxi_name="TaTul", car_types="Sprinter", price_for_tour=100,
             hotel_name="Marriott", hotel_please="Tsaghkadzor", mid_room_price=500, lux_room_price=1000)

print(order1.lux_booking())
print(order1.mid_booking())

order3 = Tour(tour_name="Agata", lux_tour=1, mid_tour=1, taxi_name="TaTul", car_types="Sprinter", price_for_tour=100,
             hotel_name="Marriott", hotel_please="Tsaghkadzor", mid_room_price=500, lux_room_price=1000)

print(order3.lux_booking())
print(order3.mid_booking())

order1 = Tour(tour_name="Agata", lux_tour=0, mid_tour=0, taxi_name="TaTul", car_types="Sprinter", price_for_tour=100,
             hotel_name="Marriott", hotel_please="Tsaghkadzor", mid_room_price=500, lux_room_price=1000)

print(order1.lux_booking())
print(order1.mid_booking())