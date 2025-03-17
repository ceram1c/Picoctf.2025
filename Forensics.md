# Ph4nt0m 1ntrud3r

<h3>ĐỀ BÀI: A digital ghost has breached my defenses, and my sensitive data has been stolen! 😱💻 Your mission is to uncover how this phantom intruder infiltrated my system and retrieve the hidden flag. To solve this challenge, you'll need to analyze the provided PCAP file and track down the attack method. The attacker has cleverly concealed his moves in well timely manner. Dive into the network traffic, apply the right filters and show off your forensic prowess and unmask the digital intruder! Find the PCAP file here Network Traffic PCAP file and try to get the flag. </h3>

**Phân tích**: dựa vào đề bài ta cần phân tích file `PCAP` của bài để tìm lại flag

**hướng giải**: sử dụng tools `Wireshark` để phân tích và dự vào hint `Time is essential` để lọc dư liệu

**Giải**: 

1. sử dụng tool `Wireshark` để đọc file PCAP bài cho

![image](https://github.com/user-attachments/assets/ab186481-92ac-4c22-9158-2d1c013b8e59)

2. ở mỗi thời điểm sẽ có 1 đoạn mã base 64 khác nhau, dựa vào hint bài cho t sắp xếp lại các đoạn base64 theo trình tự thời gian sau đó decode

![image](https://github.com/user-attachments/assets/d9d0d74b-c40a-4640-a1e0-1fa66af107c1)


# RED

<h3>ĐỀ BÀI: RED, RED, RED, RED Download the image: red.png</h3>

![red](https://github.com/user-attachments/assets/75ddc6ff-4671-425a-bf51-17dff6ac604b)

**Phân tích**: đề bài cho ta 1 bức ảnh màu đỏ, có thể trong bức ảnh ẩn chứ flag

**hướng giải**: sử dụng 1 số tools để đọc hình ảnh này tìm manh mối

**giải**:

1. sử dụng tool `aperisolve` để đọc file `.jpg` của bài sẽ thấy 1 đoạn base64 để decode



# flags are stepic

<h3>ĐỀ BÀI: A group of underground hackers might be using this legit site to communicate. Use your forensic techniques to uncover their message Try it here!</h3>


**Phân tích**: trong bài này dẫn ta tới 1 trang web chứa rất nhiều tên và cờ các nước, Stepic là một thư viện Python dùng để giấu tin trong ảnh, dựa vào có 1 nước hoàn toàn không tồn tại mà vẫn có cờ ở đó

**hướng giải**: tìm ra lá cờ của nước không tồn tại rồi giải mã nó

**giải**:

1. tìm kiếm nước không tồn tại nằm trong trang web là

![image](https://github.com/user-attachments/assets/5e160c9b-1b1e-4ec7-9068-b003b403935b)


2. tải tấm ảnh lá cờ về rồi giải mã bằng stepic bức ảnh cờ của nước không tồn tại đó bằng python

![image](https://github.com/user-attachments/assets/28448964-3e43-4187-9f30-3731cceccbc8)


https://github.com/ceram1c/Picoctf.2025/blob/2bbe46a707011a9a776cb1e50892a31f2de21bce/Picofile/stepic_slove.py

# Bitlocker-1

<h3>ĐỀ BÀI: Jacky is not very knowledgable about the best security passwords and used a simple password to encrypt their BitLocker drive. See if you can break through the encryption! Download the disk image here </h3>

**Phân tích**: bài cho ta 1 file ổ đĩa ảo, nhưng để mở được ta cần có mật khẩu


**hướng giải**: bypass ổ đĩa này thông qua việc trích xuất hash của file để tìm mật khẩu, sao đó tìm file flag nằm trogn ổ đĩa

**giải**:

1. sử dụng `bitlocker2john bitlocker-1.dd > bitlocker.hash` để trích xuất hash của ổ đĩa
2. tải file `rockyou.txt` về máy sau đó dùng `hashcat` để tấn công brute-force bypass mật khẩu `hashcat -m 22100 bitlocker.hash rockyou.txt --show`

       rockyou.txt: là file chứa hơn 14 triệu mật khẩu phổ biến được sử dụng trong các cuộc tấn công brute-forceeut

![image](https://github.com/user-attachments/assets/ce67be2a-d415-4876-a651-c064b35a41b0)

   
4. `sudo losetup -fP bitlocker-1.dd` để hiển thị ổ đĩa ảo sau đó dùng mật khẩu đã bypass mở khóa rồi tìm file flag

![image](https://github.com/user-attachments/assets/919cf69b-13da-467a-82d9-71af2e890087)

 

