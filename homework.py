import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today = dt.date.today()
        amounts_day = (record.amount for record in self.records
                       if record.date == today)
        return sum(amounts_day)

    def get_week_stats(self):
        week_range = dt.date.today() - dt.timedelta(days=7)
        amounts_week = (record.amount for record in self.records
                        if record.date >= week_range)
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
        cal_count = self.remain()
        if cal_count <= 0:
            return 'Хватит есть!'

        return ('Сегодня можно съесть что-нибудь '
                'ещё, но с общей калорийностью '
                f'не более {cal_count} кКал')


class CashCalculator(Calculator):
    EURO_RATE = 70.0
    USD_RATE = 60.0
    RUB_RATE = 1.0

    cash_dict = {'rub': [RUB_RATE, 'руб'],
                 'eur': [EURO_RATE, 'Euro'],
                 'usd': [USD_RATE, 'USD']}

    def get_today_cash_remained(self, currency):
        # проверка валюты тут, так подсказал наставник.
        if currency not in self.cash_dict:
            raise ValueError('Неверное значение валюты. '
                             'Наберите rub, eur или usd')

        cash_rate, cash_name = self.cash_dict[currency]
        remain = self.remain() / cash_rate
        remain = round(remain, 2)

        if remain == 0:
            return 'Денег нет, держись'
        elif remain < 0:
            remain = abs(remain)
            return f'Денег нет, держись: твой долг - {remain} {cash_name}'
        return f'На сегодня осталось {remain} {cash_name}'
