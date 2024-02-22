from dataclasses import dataclass

from pos.app.person.customer import Customer, CustomerBuilder
from pos.app.posrandom.attribute_generator import AttributeGenerator
from pos.app.repository.product_repository import BaseProductRepository


@dataclass
class CustomerAtPos:
    builder: CustomerBuilder
    attribute_generator: AttributeGenerator

    def arrive(self, repository: BaseProductRepository) -> Customer:
        return (
            self.builder.with_payment_method(
                self.attribute_generator.get_payment_type()
            )
            .with_items(self.attribute_generator.get_products(repository))
            .build()
        )
