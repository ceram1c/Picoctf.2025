# FANTASY CTF

<h3>ĐỀ BÀI: Play this short game to get familiar with terminal applications and some of the most important rules in scope for picoCTF. Connect to the program with netcat: $ nc verbal-sleep.picoctf.net </h3>

**Giải**:

chỉ đơn giản là nc vô host và bấm enter rồi chọn a/b/c cho tới khi nhận flag

![image](https://github.com/user-attachments/assets/ab069c3c-e1e7-4f5d-8935-7ced292d38bd)


# Rust fixme 1

<h3>ĐỀ BÀI: Have you heard of Rust? Fix the syntax errors in this Rust file to print the flag! Download the Rust code here. </h3>

**Phân tích**: bài cho 1 file code bị lỗi và 0 thể chạy được với ngôn ngữ rust

source file: https://github.com/ceram1c/Picoctf.2025/tree/ff74afe287b2cf10baff08cbf2fa9f3019770ee0/Picofile/fixme1

**hướng giải**: fix hết code bị lỗi tại file `main.rs` sau đó chạy code để nhận flag 

**Giải**:

1. trong quá trình fix luôn có các note hint của bài tìm hiểu và làm theo

![image](https://github.com/user-attachments/assets/266d5aad-cf2b-43ae-9060-61b8325c01a3)

trong rust mỗi câu lệnh đều kết thúc bằng dấu `;` 

![image](https://github.com/user-attachments/assets/7d4a81a0-062a-477e-97e1-ce6a84aa1f0e)

`ret` không phải một câu lệnh trong rust, để thoát khỏi hàm main phải dùng `return`

![image](https://github.com/user-attachments/assets/beca8dba-d436-4539-a2a4-1de2b0c64934)

`println!` sử dụng `{}` để in ra giá trị biết nên `:?` không phải cú pháp hợp lệ 



3. souce code fix: https://github.com/ceram1c/Picoctf.2025/tree/3c712ee784f77d1a548c6e769a4d109904f37649/Picofile/fixme1%20_slove

![image](https://github.com/user-attachments/assets/ff048461-b760-49ac-801a-1f7aa2667d59)


# Rust fixme 2

<h3>ĐỀ BÀI: The Rust saga continues? I ask you, can I borrow that, pleeeeeaaaasseeeee? Download the Rust code here. </h3>

**Phân tích**: bài cho 1 file code bị lỗi và 0 thể chạy được với ngôn ngữ rust

source file:

**hướng giải**: fix hết code bị lỗi tại file `main.rs` sau đó chạy code để nhận flag 

**Giải**:

1. trong quá trình fix luôn có các note hint của bài tìm hiểu và làm theo



