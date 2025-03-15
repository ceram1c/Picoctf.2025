# Ph4nt0m 1ntrud3r

![image](https://github.com/user-attachments/assets/38f14341-5e39-4399-99b2-8134bc57ad51)

1. sử dụng tool `Wireshark` để đọc file PCAP bài cho

![image](https://github.com/user-attachments/assets/ab186481-92ac-4c22-9158-2d1c013b8e59)

2. ở mỗi thời điểm sẽ có 1 đoạn mã base 64 khác nhau, dựa vào hint bài cho t sắp xếp lại các đoạn base64 theo trình tự thời gian sau đó decode

# RED

![image](https://github.com/user-attachments/assets/e72e8590-1b87-4cda-bd26-3c499ac2cb1b)

1. sử dụng tool `aperisolve` để đọc file `.jpg` của bài sẽ thấy 1 đoạn base64 để decode

# flags are stepic

![image](https://github.com/user-attachments/assets/11415750-0931-413e-a3d5-fc4ba57a3aa2)

1. trong bài này dẫn ta tới 1 trang web chứa rất nhiều tên và cờ các nước, nhưng có 1 nước hoàn toàn không tồn tại mà vẫn có cờ ở đó
2. Stepic là một thư viện Python dùng để giấu tin trong ảnh
3. vậy việc ta là giải mã bằng stepic bức ảnh cờ của nước không tồn tại đó bằng python

https://github.com/ceram1c/Picoctf.2025/blob/2bbe46a707011a9a776cb1e50892a31f2de21bce/Picofile/stepic_slove.py

# Bitlocker-1

![image](https://github.com/user-attachments/assets/a749992d-03fb-449c-a9ce-90aad8cbcd47)

1. bài cho ta 1 file ổ đĩa ảo
2. nhưng để mở được ta cần có mật khẩu
3. vậy việc ta cần làm là bypass ổ đĩa này thông qua việc trích xuất hash của file để tìm mật khẩu
4. sử dụng `bitlocker2john bitlocker-1.dd > bitlocker.hash` để trích xuất hash của ổ đĩa
5. tải file `rockyou.txt` về máy sau đó dùng `hashcat` để tấn công brute-force bypass mật khẩu `hashcat -m 22100 bitlocker.hash rockyou.txt --show`

       rockyou.txt: là file chứa hơn 14 triệu mật khẩu phổ biến được sử dụng trong các cuộc tấn công brute-force

6. `sudo losetup -fP bitlocker-1.dd` để hiển thị ổ đĩa ảo sau đó dùng mật khẩu đã bypass mở khóa rồi tìm file flag

 

