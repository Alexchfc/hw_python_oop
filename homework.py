import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, Record):
        self.Record = Record
        self.records.append(self.Record)

    def get_today_stats(self):

        amount_sum_today = 0

        for i in self.records:
            if i.date == dt.datetime.now().date():
                amount_sum_today += i.amount
        return amount_sum_today

    def get_week_stats(self):

        amount_sum_week = 0
        week_range = dt.date.today() - dt.timedelta(days=7)

        for i in self.records:
            if i.date >= week_range:
                amount_sum_week += i.amount
        print(amount_sum_week)
        return amount_sum_week


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.datetime.now().date()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()


class CaloriesCalculator(Calculator):

    def get_calories_remained(self):

        remain = self.limit - self.get_today_stats()
        if self.get_today_stats() >= self.limit:
            return 'Хватит есть!'
        elif self.get_today_stats() < self.limit:
            return ('Сегодня можно съесть что-нибудь '
                    'ещё, но с общей калорийностью '
                    f'не более {remain} кКал')


class CashCalculator(Calculator):
    EURO_RATE = 70.0
    USD_RATE = 60.0

    def get_today_cash_remained(self, currency):

        remain = self.limit - self.get_today_stats()
        if currency == 'rub':
            remain_rub = round(remain, 2)
            if remain_rub > 0:
                return f'На сегодня осталось {remain_rub} руб'
            elif remain_rub < 0:
                remain_rub = remain_rub * -1
                return f'Денег нет, держись: твой долг - {remain_rub} руб'
            else:
                return 'Денег нет, держись'

        if currency == 'usd':
            remain_usd = remain / CashCalculator.USD_RATE
            remain_usd = round(remain_usd, 2)
            if remain_usd > 0:
                return f'На сегодня осталось {remain_usd} USD'
            elif remain_usd < 0:
                remain_usd = remain_usd * -1
                return f'Денег нет, держись: твой долг - {remain_usd} USD'
            else:
                return 'Денег нет, держись'

        if currency == 'eur':
            remain_eur = remain / CashCalculator.EURO_RATE
            remain_eur = round(remain_eur, 2)
            if remain_eur > 0:
                return f'На сегодня осталось {remain_eur} Euro'
            elif remain_eur < 0:
                remain_eur = remain_eur * -1
                return f'Денег нет, держись: твой долг - {remain_eur} Euro'
            else:
                return 'Денег нет, держись'
