# Cookie Monster Secret Recipe

![image](https://github.com/user-attachments/assets/7e833cc6-02ab-429e-a247-af91a9d8dbfd)

1. bài cho 1 số hint về cookie của trang web này => điều đầu tiên ta nghĩ tới là kiếm tra cookie của trang web này

![image](https://github.com/user-attachments/assets/7c4fb121-335a-49c4-8311-b06819b21f6e)

2. có vẻ cookie của trang web chưa có gì, thử đăng nhập với tên và mật khẩu bất kì, ta sẽ thấy 1 đoạn base64 xuất hiện trong data cookie
3. decode đoạn base64 rồi nộp flag

# head-dump

![image](https://github.com/user-attachments/assets/3d6c6438-bf1c-4002-a84a-8979b00251cc)

1. đề bài nói rằng đây là 1 trang blog bao gồm cả 'API Documentation' khá là đáng ngờ khi chỉ riêng điều này được liệt kê

![image](https://github.com/user-attachments/assets/d9cbce66-0ee1-43dc-9014-613d4b3dccf2)

2. cố gắng truy cập vào cuối trang web khi bấm vào #API Documentation ta sẽ được di chuyển tới 1 trang web khác
3. kéo xuống cuối sẽ có 1 mục 'heap-dump' giống như đề bài 'try it out' -> 'excute' -> tải file trên trang web về rồi `ctrl + f` để tìm flag

# n0s4n1ty 1

![image](https://github.com/user-attachments/assets/91e5a6b3-7f82-402c-8c9f-81bd5fe1987b)
![image](https://github.com/user-attachments/assets/7a6c379d-a600-4c89-a5b1-e24b764ced1b)

1. dựa theo đề bài và hint 1, trang web này là 1 trang web tải lên ảnh đại điện nhưng bị lỗi và các file được gửi lên không được lọc định dạng
2. đây là cơ hội cho ta để thâm nhập vào trang web để đọc flag từ thư mục `/root`
3. ta sẽ bypass trang wep này bằng 1 file `.php`

        php: là một ngôn ngữ lập trình web, các file thường có đuổi `.php`
        ta cần tạo 1 file web shell .php để điều khiển trang web từ xa

4. tạo 1 file text và ghi dòng lệnh `<?php system($_GET['cmd']); ?>` rồi `save as` với đuôi `.php`

        $_GET['cmd'] lấy dữ liệu từ đường link URL.
        system() thực thi lệnh hệ thống trên server.

5. vì đây là 1 file crack trang web, tự như mã độc lên windown security sẽ xóa nó ngay, ta cần tắt đi trước khi tạo
6. upload file này lên trang web sau đó dùng đường link để ghi lệnh `http://expico.com/uploads/shell.php?cmd=sudo ls -l` để liệt kê file trong web
7. rồi cat file flag từ thư mục `root` ra

# SSTI1

![image](https://github.com/user-attachments/assets/50e41e6e-2d21-4f36-8169-8c3255af2fed)

1. `ssti` 












