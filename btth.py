# # bài 1
# so_luong=int(input('nhập số lượng tồn kho'))

# if so_luong >= 50:
#     print( "Tình trạng: Hàng đầy kho")
# elif so_luong <50 and so_luong >10:
#     print("Tình trạng: Mức an toàn")
# elif so_luong < 10:
#     print("Tình trạng: Sắp hết hàng, cần báo cáo nhập thêm")
# else:
#     print("Tình trạng: không hợp lệ!")
# # bài 2
# count_erro =0
# while True:
#     so_luong_loi=int(input('nhập số lỗi'))
#     if so_luong_loi != -1:
#         count_erro+=1
#         print('lỗi đã được cộng thêm')
#         continue
#     else:
#         break
# print(f"Tổng số hàng lỗi thu hồi trong ngày là: {count_erro}")
# bài 3
ton_kho = 100

while ton_kho >0:
    xuat_kho=int(input('nhập vào số lượng hàng muốn nhập:'))
    if xuat_kho <0:
        print("Không được nhập số âm, vui lòng nhập lại!")

    elif xuat_kho > ton_kho:
        print("Kho không đủ hàng, vui lòng nhập lại!")
    else:
        ton_kho =ton_kho-xuat_kho
        print("Xuất kho thành công!")
        print(f"Tồn kho còn lại {ton_kho}")
        break
