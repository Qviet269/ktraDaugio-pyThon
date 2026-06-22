from abc import ABC, abstractmethod

class BaseCharacter(ABC):
    def __init__(self, base_hp):
        self.__base_hp = base_hp

    @property
    def base_hp(self):
        return self.__base_hp

    @abstractmethod
    def attack_enemy(self):
        pass

    def __add__(self, other):
        return self.base_hp + other.base_hp
    
class MagicalStance:
    def attack_enemy(self):
        return 150.0
    
class Warrior(BaseCharacter):
    def __init__(self, base_hp, strength):
        super().__init__(base_hp)
        self.strength = strength

    def attack_enemy(self):
        return self.strength * 2.5
    

class Spellblade(Warrior, MagicalStance):
    def attack_enemy(self):
        physical_damage = Warrior.attack_enemy(self)
        magical_damage = MagicalStance.attack_enemy(self)

        return physical_damage + magical_damage

class VolcanoZone:
    def activate_buff(self, character):
        print(
            "[Volcano Zone Effect]: Sức nóng dung nham kích hoạt! "
            "Gia tăng +20% sát thương cho Warrior!"
        )

def apply_battleground_effect(environment, character):
    environment.activate_buff(character)

def create_spellblade():
    hp = int(input("Nhập lượng máu cơ bản (HP): "))
    strength = int(input("Nhập chỉ số sức mạnh (Strength): "))

    hero = Spellblade(hp, strength)

    print("\n[Thành công]: Khởi tạo nhân vật Spellblade thành công!")

    print("[MRO Architecture]: ", end="")
    mro_chain = " -> ".join(cls.__name__ for cls in Spellblade.__mro__)
    print(mro_chain)

    total_hp = hero + hero
    print(f"[Overloading __add__]: Tổng HP tích lũy khi gộp đội hình: {total_hp}")

    return hero

def battle(hero):
    if hero is None:
        print("Chưa khởi tạo nhân vật!")
        return

    print("\n--- THI THIẾT KẾ GIAO TRANH & DUCK TYPING ---")

    damage = hero.attack_enemy()

    print(
        f"[Đa hình] Spellblade vung kiếm ma thuật gây tổng sát thương: "
        f"{damage} DMG"
    )

    zone = VolcanoZone()

    print("[Duck Typing]: Xác thực môi trường trận đấu thành công!")
    apply_battleground_effect(zone, hero)

def main():
    current_hero = None

    while True:
        print("\n===== RPG GAME CORE MENU =====")
        print("1. Khởi tạo Ma kiếm sĩ Spellblade & Xem cấu trúc MRO")
        print("2. Ra lệnh tấn công & Kích hoạt chiến trường (Duck Typing)")
        print("0. Thoát")

        choice = input("Chọn chức năng (0-2): ")

        match choice:
            case "1":
                print("\n--- KHỞI TẠO MA KIẾM SĨ SPELLBLADE ---")
                current_hero = create_spellblade()

            case "2":
                battle(current_hero)

            case "0":
                print("Thoát chương trình.")
                break

            case _:
                print("Lựa chọn không hợp lệ!")


main()