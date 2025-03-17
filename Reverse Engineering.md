# Flag Hunters

<h3>ĐỀ BÀI: Lyrics jump from verses to the refrain kind of like a subroutine call. There's a hidden refrain this program doesn't print by default. Can you get it to print it? There might be something in it for you. The program's source code can be downloaded here. Connect to the program with netcat: $ nc verbal-sleep.picoctf.net 56688</h3>

source code: https://github.com/ceram1c/Picoctf.2025/blob/dca014c0df5fea885db838137eae4cddd29ed5c7/Picofile/lyric-reader.py

**Phân tích**: đề bài bảo host là 1 đoạn nhạc ta có thể tương tác thông qua `Crow`, ta cần in ra được 1 đoạn được ẩn trong bài không

**hướng giải**: phân tích code trong host và tìm ra lỗ hổng để khai thác nhằm in ra phần secret intro ![image](https://github.com/user-attachments/assets/fde11af6-f4c2-43ff-9676-e15c03425bb0)

**giải**:

1. sau khi đọc source code của bài có dòng ![image](https://github.com/user-attachments/assets/cc4b8881-36c6-4fba-aa0e-84a5cb782e6d)

dòng này nhằm phân tách các câu lệnh bằng dấu `;`, nghĩa là 2 câu lệnh được tách nhau bằng dấu `;` sẽ được hoạt động bình thường, riêng biệt

2. sử dụng lỗ hổng này nhằm nhập vào `Crow` lệnh được ngăn cách bằng dấy `;` để đọc flag

![image](https://github.com/user-attachments/assets/48984fba-88f8-43ea-b383-0b91e4861399)


# Tap into Hash

<h3>ĐỀ BÀI: Can you make sense of this source code file and write a function that will decode the given encrypted file content? Find the encrypted file here. It might be good to analyze source file to get the flag.</h3>


source code: https://github.com/ceram1c/Picoctf.2025/blob/30ee188cc218a68803709e61e902e67181358e1e/Picofile/block_chain.py
source encrypted: https://github.com/ceram1c/Picoctf.2025/blob/250e9c06f1e242b3bc83620e285a12eddfe0340d/Picofile/enc_flag

**Phân tích**: theo đề bài ta cần đọc source code để hiểu được đây là loại mã hóa gì và dịch mã hóa từ file encrypted

**hướng giải**: sử dụng mã hóa từ file encrypted decode nó để lấy flag

**giải**:

viết 1 đoạn code python để giải mã đoạn code đó rồi lấy flag

![image](https://github.com/user-attachments/assets/97b25312-ddce-4d20-bc01-d8e36d64354e)


https://github.com/ceram1c/Picoctf.2025/blob/8f1c60cefb7f71bf67782d0d12bf14c2da632ee1/Picofile/blockchain_slove.py
