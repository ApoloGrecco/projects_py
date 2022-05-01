from datetime import datetime, timedelta


class Datesbr:
    def __init__(self):
        self.registration_moment = datetime.today()

    def registration_month(self):
        months_of_the_year = [
            "janeiro", "fevereiro", "março",
            "abril", "maio", "junho",
            "julho", "agosto", "setembro",
            "outubro", "novembro", "dezembro"
        ]
        regist_month = self.registration_moment.month - 1
        return months_of_the_year[regist_month]

    def week_day(self):
        week_day_list = [
            "segunda", "terça", "quarta",
            "quinta", "sexta", "sabado",
            "domingo"
        ]
        week_day = self.registration_moment.weekday()
        return week_day_list[week_day]

    def format_date(self):
        return self.registration_moment.strftime("%d/%m/%Y  %H:%M")

    def registration_time(self):
       return (datetime.today() + timedelta(days=30)) - self.registration_moment
