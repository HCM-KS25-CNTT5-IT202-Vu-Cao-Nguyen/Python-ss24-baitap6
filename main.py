class Drink:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.__price = price
        self.is_available = True

    @property
    def price(self):
        return self.__price

    def toggle_available(self):
        self.is_available = not self.is_available

    def status_text(self):
        return "Đang bán" if self.is_available else "Ngừng bán"

menu = [
    Drink("CF01", "Cà phê sữa", 35000),
    Drink("TS01", "Trà sữa matcha", 45000),
    Drink("TD01", "Trà đào cam sả", 40000),
]

def show_menu():
    print("\n--- DANH SÁCH ĐỒ UỐNG ---\n")
    print(f"{'Mã món':<7}| {'Tên món':<17}| {'Giá bán':<8}| Trạng thái")
    print("-" * 50)
    for drink in menu:
        print(f"{drink.code:<7}| {drink.name:<17}| {drink.price:<8}| {drink.status_text()}")


def add_drink():
    code = input("\nNhập mã món: ").strip()
    name = input("Nhập tên món: ").strip()
    price_input = input("Nhập giá bán: ").strip()

    for drink in menu:
        if drink.code.lower() == code.lower():
            print("\nMã món đã tồn tại trong hệ thống!")
            return
    try:
        price = float(price_input)
    except ValueError:
        print("\nGiá bán không hợp lệ!")
        return

    if price <= 0:
        print("\nGiá bán không hợp lệ!")
        return

    new_drink = Drink(code, name, price)
    menu.append(new_drink)
    print(f"\nThành công: Đã thêm món {name} vào thực đơn!")


def update_status():
    code = input("\nNhập mã món cần cập nhật: ").strip()

    for drink in menu:
        if drink.code.lower() == code.lower():
            drink.toggle_available()
            print(f"\nĐã cập nhật trạng thái món {drink.code}.")
            print(f"Trạng thái hiện tại: {drink.status_text()}")
            return

    print("\nKhông tìm thấy món có mã này!")


def show_options():
    print("\n=== HỆ THỐNG QUẢN LÝ THỰC ĐƠN RIKKEI COFFEE ===\n")
    print("1. Xem danh sách đồ uống")
    print("2. Thêm đồ uống mới")
    print("3. Cập nhật trạng thái kinh doanh")
    print("4. Thoát chương trình")
    print("\n==============================================")


def main():
    while True:
        show_options()
        choice = input("Chọn chức năng (1-4): ").strip()

        if choice == "1":
            show_menu()
        elif choice == "2":
            add_drink()
        elif choice == "3":
            update_status()
        elif choice == "4":
            print("\nCảm ơn bạn đã sử dụng hệ thống quản lý thực đơn Rikkei Coffee!")
            break
        else:
            print("\nLựa chọn không hợp lệ, vui lòng chọn từ 1 đến 4!")


if __name__ == "__main__":
    main()