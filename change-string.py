# Nhập chuỗi từ người dùng
str = input()
s = list(str)

# Hoán đổi các cặp ký tự liên tiếp
for i in range(1, len(s), 2):
    s[i-1], s[i] = s[i], s[i-1]

# Chuyển mảng ký tự thành chuỗi và in kết quả
print("".join(s), end='')
