# Khai báo danh sách khách hàng
DataCustomer = [
    {"Họ và tên": "Đỗ Quang Vinh", "Năm sinh": 2005, "Tuyến xe": 1, "Mã số thẻ": 1},
    {"Họ và tên": "Nguyễn Quốc Khánh", "Năm sinh": 2005, "Tuyến xe": 1, "Mã số thẻ": 2},
    {"Họ và tên": "Phạm Anh Tú", "Năm sinh": 2000, "Tuyến xe": 3, "Mã số thẻ": 3},
    {"Họ và tên": "Đỗ Minh Đức", "Năm sinh": 2002, "Tuyến xe": 15, "Mã số thẻ": 4},
]

checkData = False

# Người dùng lựa chọn đăng nhập/đăng ký
while True:
    print("------------------------------------------------------------") #60
    print("|                 CHÀO MỪNG ĐẾN VỚI TEKYBUS                |")
    print("------------------------------------------------------------")
    print("Đăng nhập hoặc Đăng ký")
    print("Nhấn 1 để đăng nhập, nhấn 2 để đăng ký", end=": ")
    start = int(input())
    if start == 1 or start == 2:
        break

# Truy cập thông tin người dùng
if start == 1:
    while True:
        indexCustomer = 0
        print("Nhập tên người dùng: ", end="")
        inpName = str(input())
        print("Nhập mã số thẻ: ", end="")
        inpCode = int(input())
        # Kiểm tra thông tin có tồn tại không
        for customer in DataCustomer:
            indexCustomer += 1
            if inpName == customer["Họ và tên"] and inpCode == customer["Mã số thẻ"]:
                print("------------------------------------------------------------")
                print(f"|| Chào mừng bạn {customer['Họ và tên']} đã trở lại", " "*(60-32-len(customer["Họ và tên"])), "||")
                print("|| Dưới đây là thông tin cá nhân của bạn                  ||")
                print("------------------------------------------------------------")
                print(f"|| Họ và tên: {customer['Họ và tên']}", " "*(60-18-len(customer["Họ và tên"])), "||")
                print(f"|| Năm sinh: {customer['Năm sinh']}", " "*(60-21), "||")
                print(f"|| Tuyến xe: {customer['Tuyến xe']}", " "*(60-17-len(str(customer["Tuyến xe"]))), "||")
                print(f"|| Mã số thẻ (KHÔNG ĐƯỢC THAY ĐỔI): {customer['Mã số thẻ']}", " "*(60-40-len(str(customer["Mã số thẻ"]))), "||")
                print("------------------------------------------------------------")
                checkData = True
                break
        else:
            print("-------------------------------")
            print("|  Tên hoặc mã số không đúng  |")
            print("|       Yêu cầu nhập lại      |")  
            print("-------------------------------")
            continue
        break
# Đăng ký   
elif start == 2:
    print("Bạn chọn đăng ký")
    print("Nhập họ và tên: ", end="")
    name = input()
    print("Nhập năm sinh: ", end="")
    year = int(input())
    print("Nhập tuyến xe bạn muốn đăng ký: ", end="")
    bus = int(input())
    
    newCustomer = {
        "Họ và tên": name,
        "Năm sinh": year,
        "Tuyến xe": bus,
        "Mã số thẻ": len(DataCustomer)+1
    }
    
    DataCustomer.append(newCustomer)
    print("------------------------------------------------------------")
    print("||Chúc mừng bạn đã đăng ký thành công                     ||")
    print("|| Dưới đây là thông tin cá nhân của bạn                  ||")
    print("------------------------------------------------------------")
    print(f"|| Họ và tên: {newCustomer['Họ và tên']}", " "*(60-18-len(newCustomer["Họ và tên"])), "||")
    print(f"|| Năm sinh: {newCustomer['Năm sinh']}", " "*(60-21), "||")
    print(f"|| Tuyến xe: {newCustomer['Tuyến xe']}", " "*(60-17-len(str(newCustomer["Tuyến xe"]))), "||")
    print(f"|| Mã số thẻ (KHÔNG ĐƯỢC THAY ĐỔI): {newCustomer['Mã số thẻ']}", " "*(60-40-len(str(newCustomer["Mã số thẻ"]))), "||")
    print("------------------------------------------------------------")
    
# Sửa dữ liệu người dùng
if checkData:
    print("Bạn có muốn sửa thông tin không? Nhấn phím 1 nếu có, 2 nếu không: ", end="")
    changeInfor = int(input())
    if changeInfor == 1:
        print("Nhập phần dữ liệu cần sửa:  ", end="")
        changeKey = input()
        print("Nhập giá trị mới: ", end="")
        changeValue = input()        
        
        DataCustomer[indexCustomer-1].update({changeKey: changeValue})
        customer = DataCustomer[indexCustomer-1]
        
        print("------------------------------------------------------------")
        print("|| Chúc mừng bạn đã thay đổi thông tin thành công         ||")
        print("|| Dưới đây là thông tin cá nhân của bạn                  ||")
        print("------------------------------------------------------------")
        print(f"|| Họ và tên: {customer['Họ và tên']}", " "*(60-18-len(customer["Họ và tên"])), "||")
        print(f"|| Năm sinh: {customer['Năm sinh']}", " "*(60-21), "||")
        print(f"|| Tuyến xe: {customer['Tuyến xe']}", " "*(60-17-len(str(customer["Tuyến xe"]))), "||")
        print(f"|| Mã số thẻ (KHÔNG ĐƯỢC THAY ĐỔI): {customer['Mã số thẻ']}", " "*(60-40-len(str(customer["Mã số thẻ"]))), "||")
        print("------------------------------------------------------------")
        
    
