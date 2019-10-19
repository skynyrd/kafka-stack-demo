import random
import string
import uuid
from datetime import datetime


class Product:
    def __init__(self, name, brand, sku, price, image_urls, description, short_description):
        self.id = uuid.uuid1()
        self.name = name
        self.image_urls = image_urls
        self.description = description
        self.price = price
        self.sku = sku
        self.brand = brand
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        self.short_description = short_description

    def to_kafka_model(self):
        return {
            "id": self.id.__str__(),
            "name": self.name,
            "imageUrls": self.image_urls,
            "description": self.description,
            "price": self.price,
            "sku": self.sku,
            "brand": self.brand,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
            "shortDescription": self.short_description
        }

    @classmethod
    def load_random(cls):
        brand = random.choice(["Apple", "Samsung", "Huawei", "Xiaomi", "Sony", "LG", "Asus", "Google", "Microsoft"])

        letters = string.ascii_letters
        sku = ''.join(random.choice(letters) for i in range(5))

        name = brand + " Phone " + sku

        description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vitae neque varius, vulputate " \
                      "tortor at, posuere magna. Phasellus elementum imperdiet ligula sit amet tristique. Donec " \
                      "vulputate venenatis neque at tincidunt. Nulla nec feugiat leo, sit amet fermentum nunc. Sed " \
                      "sed malesuada tellus. Cras in orci id lorem sagittis facilisis at sit amet diam. Nam justo " \
                      "arcu, consequat et scelerisque sit amet, volutpat ac ex. Nam tempor commodo nulla vitae " \
                      "bibendum. Mauris id odio convallis, imperdiet nulla a, placerat diam. Nam nec rutrum nulla. "

        price = round(random.uniform(700, 1200), 2)

        return cls(name, brand, sku, price, [], description, None)
