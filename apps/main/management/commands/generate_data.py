# Python modules
from typing import Any
from datetime import datetime

# Django
from django.core.management.base import BaseCommand

# Project modules
from dictionaries.models import (
    Department,
    Management,
    Degree
)


class Command(BaseCommand):
    """ Command for filling data up database """
    def __init__(
        self,
        *args: list,
        **kwargs: dict
    ) -> None:
        self.departmens: list = [
           "ДП Карагандинской области",
           "Октябьрский ОП",
           "Центральный ОП",
           "Кировский ОП",
           "Михайловский ОП",
           "Юго-Восточный ОП",
           "Ново-Майкудукский ОП",
           "УП г.Караганды",
           "Восточный ОП",
           "Старогородской ОП",
           "УП г.Темиртау",
           "ОП г.Шахтинск",
           "ОП г.Сарань",
           "ОП г.Балхаш",
           "ОП Абайского района",
           "Топарский ОП",
           "ОП Бухар-Жырауского района",
           "ОП им.Мустафина",
           "ОП Нуринского района",
           "ОП Каркаралинского района",
           "ОП Шетского района",
           "ОП Актогайсокого района",
           "ОП Осакаровского района",
        ]

        self.managements: list = [
            "Подразделение специального назначения",
            "Управление по внутренним и внешним коммуникациям",
            "Управление специализированной охранной службы",
            "Управление информатизации и связи",
            "Руководство",
            "Второй спец. отдел",
            "Оперативно-криманилистическое управление",
            "Местная полицейская служба",
            "Седьмое управление",
            "Юридический отдел",
            "Управление кадровой политики",
            "Центр кинологической службы",
            "Управление криминальной полиции",
            "Управление миграционной службы",
            "Медицинский отдел",
            "ОВВК",
            "Десятое управление",
            "ППП",
            "Следственное управление",
            "Управление тылового обеспечения",
            "Секретариат",
            "Штаб управление",
            "Управление по борьбе с экстремизмом",
            "Управление финансового обеспечения",
            "Управление документообеспечения",
            "Управление по борьбе с организованной преступностью",
            "Управление административной полиции",
            "Управление собственной безопасности",
        ]

        self.degrees: str = [
            "генарал-лейтенант полиции",
            "генерал-майора полиции",
            "полковник полиции",
            "подполковник полиции",
            "майор полиции",
            "капитан полиции",
            "старший лейтенант полиции",
            "лейтенант полиции",
            "старший сержант полиции",
            "сержант полиции",
            "младший лейтенант полиции",
            "рядовой полиции",
        ]

    def generate_dicts(self):
        for d in self.departmens:
            department = Department.objects.filter(title=d).first()

            if not department:
                Department.objects.create(title=d)

        for m in self.managements:
            management = Management.objects.filter(title=m).first()

            if not management:
                Management.objects.create(title=m)

        for d in self.degrees:
            degree = Degree.objects.filter(title=d).first()

            if not degree:
                Degree.objects.create(title=d)

    def handle(self, *args: Any, **kwargs: Any) -> None:
        """Handles data filling."""
        start: datetime = datetime.now()

        self.generate_dicts()

        print(
            f'Generated in: {(datetime.now()-start).total_seconds()} seconds'
        )
