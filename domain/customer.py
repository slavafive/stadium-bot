from dao.person_dao import PersonDAO
from domain.fan_id_card import FanIDCard
from domain.person import Person


class Customer(Person):

    def __init__(self, username, first_name, last_name, age, fan_id_card):
        super().__init__(username, first_name, last_name, age, "customer")
        self.fan_id_card = fan_id_card

    def buy_ticket(self, ticket):
        self.fan_id_card.reserve_ticket(ticket)

    def return_ticket(self, ticket):
        self.fan_id_card.return_ticket(ticket)

    def increase_balance(self, value):
        self.fan_id_card.increase_balance(value)

    @staticmethod
    def construct(username):
        row = PersonDAO.get_person_by_username(username)
        card = FanIDCard.construct_by_username(username)
        return Customer(row[0], row[2], row[3], row[5], card)
