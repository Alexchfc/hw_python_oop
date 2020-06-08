import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        amounts_day = [record.amount for record in self.records
                       if record.date == dt.date.today()]

        return sum(amounts_day)

    def get_week_stats(self):
        week_range = dt.date.today() - dt.timedelta(days=7)
        amounts_week = [record.amount for record in self.records
                        if record.date >= week_range]

        return sum(amounts_week)

    def remain(self):
        return self.limit - self.get_today_stats()


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        if self.remain() <= 0:
            return 'Хватит есть!'

        return ('Сегодня можно съесть что-нибудь '
                'ещё, но с общей калорийностью '
                f'не более {self.remain()} кКал')


class CashCalculator(Calculator):
    EURO_RATE = 70.0
    USD_RATE = 60.0
    RUB_RATE = 1.0

    rate_dict = {'rub': RUB_RATE, 'eur': EURO_RATE, 'usd': USD_RATE}
    cash_dict = {'rub': 'руб', 'eur': 'Euro', 'usd': 'USD'}

    def get_today_cash_remained(self, currency):
        remain = self.remain() / self.rate_dict[currency]
        remain = round(remain, 2)
        cash_name = self.cash_dict[currency]

        if remain > 0:
            return f'На сегодня осталось {remain} {cash_name}'
        elif remain < 0:
            remain = abs(remain)
            return f'Денег нет, держись: твой долг - {remain} {cash_name}'
        return 'Денег нет, держись'
