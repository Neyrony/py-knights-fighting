from app.warrior.stats import Stats


class Armour:
    def __init__(self, armour_list: list[dict]) -> None:
        self.armour_name_list = [part.get("part") for part in armour_list]
        self.stats = Stats(
            protection=sum([part.get("protection", 0) for part in armour_list])
        )
