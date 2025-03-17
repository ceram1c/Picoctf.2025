# hashcrack
<h3>ĐỀ BÀI: A company stored a secret message on a server which got breached due to the admin using weakly hashed passwords. Can you gain access to the secret stored within the server? Access the server using nc verbal-sleep.picoctf.net 51759 </h3>

**Phân tích**: đơn giản là bài này sử dụng 1 số đoạn mã khác nhau là password

**hướng giải**: ta cần decode để rồi trả về input cho bài để nhận flag

**Giải**:
sử dụng 1 số công cụ như chatgpt để phân biệt loại hash và decode theo loại hash đó

![image](https://github.com/user-attachments/assets/8d898bed-b3bb-4dfa-9c99-56d7faf4b04a)


# EVEN RSA CAN BE BROKEN???

![image](https://github.com/user-attachments/assets/5efc8ef8-6b7c-462d-881c-1589163d59ee)

source code: [https://github.com/ceram1c/Picoctf.2025/blob/a7133174999319296f39aedef46e176fb966b16a/RSA_crypto](https://github.com/ceram1c/Picoctf.2025/blob/3740b415533de498933032954b6f4be1c3fe9a77/Picofile/RSA_source)

1. source code bài này là code mã hóa RSA file flag.txt rồi trả về 3 output N, e, ciphertext
2. sau đó ta có thể dùng 3 output của bài để giải mã RSA bằng python để đọc nội dung trước khi bị mã hóa

source slove: [https://github.com/ceram1c/Picoctf.2025/blob/ddef5134f4875756290488a9e0186ac4a869dd17/RS488a9e0186](https://github.com/ceram1c/Picoctf.2025/blob/575a7a79312bb1b35c5a09500efe6c6eeccc448a/Picofile/RSA_slove)

# Guess My Cheese (Part 1)

![image](https://github.com/user-attachments/assets/14afb021-905c-49d7-8355-1c0c89bb05b1)

1. theo như đề bài ta cần giải mã được mật mã từ host để nhận flag
2. theo như hint ta có thể xác định đây là loại mã `Affine Cipher`
![image](https://github.com/user-attachments/assets/3e7da9f5-38ad-4992-8a10-97c03095fb54)


3. theo như minigame của host cho phép ta được phép hỏi mật mã của tên loại phô mai là gì 2 lần, dựa vào 2 kết quả trên ta có thể tính ra được a và b để giải mã ngược lại mật mã host muốn ta giải từ đầu
![image](https://github.com/user-attachments/assets/89e26d0d-bee1-4612-a913-782222b25add)


