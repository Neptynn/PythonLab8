# myapp1/management/commands/generate_data.py

import random
from faker import Faker
from datetime import date, timedelta
from django.core.management.base import BaseCommand
from myapp1.models import Client, Product, Sale

class Command(BaseCommand):
    help = 'Generate test data for Clients, Products, and Sales'

    def handle(self, *args, **kwargs):
        fake = Faker('uk_UA')  # Встановіть мову відповідно до потреби

        # Генерація та додавання клієнтів
        for _ in range(4):
            client_name = fake.company()
            entity_type = random.choice(['юридична', 'фізична'])
            address = fake.address()
            phone = fake.numerify(text='+38(0##)-##-##-###')
            contact_person = fake.name()
            account_number = fake.unique.numerify(text='#############')
            Client.objects.create(
                client_name=client_name,
                entity_type=entity_type,
                address=address,
                phone=phone,
                contact_person=contact_person,
                account_number=account_number
            )

        # Генерація та додавання товарів
        for _ in range(10):
            product_name = fake.word()
            price = round(random.uniform(5, 100), 2)
            stock = random.randint(50, 500)
            Product.objects.create(
                product_name=product_name,
                price=price,
                stock=stock
            )

        # Генерація та додавання продажів
        clients = list(Client.objects.all())
        products = list(Product.objects.all())
        start_date = date(2024, 10, 1)
        for _ in range(19):
            sale_date = start_date + timedelta(days=random.randint(0, 30))
            client = random.choice(clients)
            product = random.choice(products)
            quantity = random.randint(1, 20)
            discount = round(random.uniform(0.03, 0.20), 2)
            payment_form = random.choice(['готівковий', 'безготівковий'])
            delivery_needed = random.choice([True, False])
            delivery_cost = round(random.uniform(0, 150), 2) if delivery_needed else 0
            Sale.objects.create(
                sale_date=sale_date,
                client=client,
                product=product,
                quantity=quantity,
                discount=discount,
                payment_form=payment_form,
                delivery_needed=delivery_needed,
                delivery_cost=delivery_cost
            )

        self.stdout.write(self.style.SUCCESS('Дані успішно згенеровано та додано до таблиць!'))
