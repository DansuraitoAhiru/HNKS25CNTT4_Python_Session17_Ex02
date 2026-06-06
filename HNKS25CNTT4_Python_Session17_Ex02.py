# Phân tích:
# key trong sort() có nhiệm vụ trả về giá trị dùng để so sánh khi sắp xếp, chứ không phải trả về True/False
# Python sẽ so sánh tuple từ trái sang phải:
# So sánh -rating trước, mặc định sort là tăng dần nên thêm - để xếp theo giảm dần
# Nếu bằng nhau thì so sánh price, để nguyên thì xếp theo giá tăng dần

from functools import reduce

product_list = [
    "P01-Tai Nghe Bluetooth-550000-4.5",
    "P02-Chuột Không Dây-250000-4.8",
    "P03-Bàn Phím Cơ-850000-4.5"
]

def display_labels(products):
    if not products:
        print("Danh sách tem nhãn hiện đang trống")
        return
    
    print("--- DANH SÁCH TEM NHÃN ---")
    for label in products:
        parts = label.split("-")

        try:
            id = parts[0]
            name = parts[1]
            price = parts[2]
            rate = parts[3]

        except IndexError:
            print(f"Bỏ qua sản phẩm {parts[0]} do sai cấu trúc dữ liệu")
            continue

        if not price.isdigit():
            print(f"Bỏ qua sản phẩm {id} do giá tiền không hợp lệ")
            continue

        product = {
            "id": id,
            "name": name,
            "price": f"{int(price):,} VND",
            "rate": float(rate)
        }

        print('Mã: {id:<10} | Tên: {name:<20} | Giá: {price:<15} | Rating: {rate}*'.format_map(product))

def sort_product(products):
    if not products:
        print("Danh sách tem nhãn hiện đang trống")
        return
    
    products.sort(key=lambda product: (-float(product.split("-")[3]), int(product.split("-")[2])))

    print("--- SẮP XẾP SẢN PHẨM ---")
    for index, product in enumerate(products):
        print(f"{index+1}. {product}")

def calculate_total(products):
    if not products:
        print("Danh sách sản phẩm hiện đang trống")
        return

    prices = []

    for product in products:
        parts = product.split("-")

        try:
            price = parts[2]

            if not price.isdigit():
                print(f"Bỏ qua sản phẩm {parts[0]} do giá tiền không hợp lệ")
                continue

            prices.append(int(price))

        except IndexError:
            print(f"Bỏ qua sản phẩm {parts[0]} do sai cấu trúc dữ liệu")

    if not prices:
        print("Không có dữ liệu hợp lệ để tính toán")
        return

    total = reduce(lambda x, y: x + y, prices)

    print("--- TỔNG GIÁ TRỊ KHO ---")
    print(f"Tổng giá trị các mặt hàng hiện tại là: {total:,} VND")
    return total

def main():
    while True:
        choice = input('''
============= E-COMMERCE ANALYTICS =============
1. Hiển thị tem nhãn sản phẩm (format_map & F-String)
2. Sắp xếp sản phẩm thông minh (sort key)
3. Tính tổng giá trị kho hàng (reduce)
4. Đóng hệ thống
================================================
Chọn chức năng (1-4): ''').strip()
        
        match choice:
            case "1":
                display_labels(product_list)

            case "2":
                sort_product(product_list)

            case "3":
                calculate_total(product_list)

            case "4":
                print("Kết thúc chương trình, see u soon")
                break
            case _:
                print("Lựa chọn không hợp lệ, vui lòng nhập 1-4")
main()