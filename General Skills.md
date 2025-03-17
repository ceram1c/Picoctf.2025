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

source file: https://github.com/ceram1c/Picoctf.2025/tree/3de32438106b69dc68dfa6d372912dc851d206c3/Picofile/fixme2

**hướng giải**: fix hết code bị lỗi tại file `main.rs` sau đó chạy code để nhận flag 

**Giải**:

1. trong quá trình fix luôn có các note hint của bài tìm hiểu và làm theo

![image](https://github.com/user-attachments/assets/15011305-edb3-4384-9914-7dad45d5876a)

trong rust `&String` là tham chiếu bất biến (không thay đổi) nhưng tham số `borrowed_string` cần truyền vào 1 tham số có thể thay đổi nên sử thành `&mut String`

![image](https://github.com/user-attachments/assets/d8e4f1ee-34bd-4a19-91f6-d12eeadddfdb)

điều tương tự cũng xảy ra với tham số `party_foul`

2. source code fix: https://github.com/ceram1c/Picoctf.2025/tree/3de32438106b69dc68dfa6d372912dc851d206c3/Picofile/fixme2_slove

![image](https://github.com/user-attachments/assets/3fcf4f3d-5caf-408f-a371-b723c16e03a9)



# Rust fixme 3

<h3>ĐỀ BÀI: Have you heard of Rust? Fix the syntax errors in this Rust file to print the flag! Download the Rust code here. </h3>

**Phân tích**: bài cho 1 file code bị lỗi và 0 thể chạy được với ngôn ngữ rust

source file: https://github.com/ceram1c/Picoctf.2025/tree/0dbf36185f023b5a23c7151c56b49395986803b6/Picofile/fixme3

**hướng giải**: fix hết code bị lỗi tại file `main.rs` sau đó chạy code để nhận flag 

**Giải**:

1. trong quá trình fix luôn có các note hint của bài tìm hiểu và làm theo

![image](https://github.com/user-attachments/assets/b7edd4cd-0666-4b3b-8080-4516c7a0f1ef)

code bị lỗi vì rust yêu cầu các thao tác không an toàn bọc trong 1 khối `unsafe{}` cụ thể hàm `std::slice::from_raw_parts` trong bài bị cho là 1 thao tác không an toàn vì nó có thể dẫn đến hành vi không xác định nếu con trỏ hoặc độ dài không hợp lệ.

chỉ cần bọc đoạn code trong 1 khối `unsafe{}` như sau:

![image](https://github.com/user-attachments/assets/b40f1ef6-d9dd-4b0c-bf6e-6df27a067706)

3. source code fix: https://github.com/ceram1c/Picoctf.2025/tree/69a61fe08d936eee0e67be1a147fb69f6a86d0f7/Picofile/fixme3_slove

![image](https://github.com/user-attachments/assets/a93808c4-5192-4f35-918a-83be3b4bf175)







