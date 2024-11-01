class Artikel:
    def __init__(self):
        self.prices = {}

    def add(self, name, price = None):
        if price is None:
            raise ValueError("kein Preis angegeben")
        else:
            self.prices[name] = price

    def get_price(self, name):
        return self.prices.get(name, 0)


class Warenkorb:
    def __init__(self):
        self.korb = {}
        self.article = None

    def set_article(self, article):
        self.article = article

    def add_Artikel(self, name, quantity=1):
        if name in self.korb:
            self.korb[name] += quantity
        else:
            self.korb[name] = quantity

    def get_Inhalt(self):
        return self.korb

    def get_Summe(self):
        if self.article is None:
            raise ValueError("Article instance not set in Warenkorb")
        summe = sum(quantity * self.article.get_price(name) for name, quantity in self.korb.items())
        return summe


class Discount:
    def __init__(self):
        self.rules = {}

    def add_discountrule(self, name, amount):
        self.rules[name] = amount

    def get_amountofdiscountrule(self, name):
        return self.rules.get(name, 0)

    def use_discount(self, name, warenkorb):
        sum_without_discount = warenkorb.get_Summe()
        discount_amount = self.get_amountofdiscountrule(name)
        if discount_amount > 0:
            total_sum = (sum_without_discount * (100 - discount_amount)) / 100
            return total_sum
        return sum_without_discount