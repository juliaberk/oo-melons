"""Classes for melon orders."""


class AbstractMelonOrder(object):
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        if self.species == 'Christmas melon':
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super(InternationalMelonOrder, self).__init__(species, qty)
        self.country_code = country_code

    order_type = "international"
    tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        """international orders need an extra $3 fee added to total """
        total = super(InternationalMelonOrder, self).get_total()
        if self.order_type == "international" and self.qty < 10:
            total += 3
        return total


# class GovernmentMelonOrder(AbstractMelonOrder):
    # """Melon order for gov has no tax and needs to pass inspection """