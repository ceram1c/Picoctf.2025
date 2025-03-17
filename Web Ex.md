# Cookie Monster Secret Recipe

<h3>ĐỀ BÀI: Cookie Monster has hidden his top-secret cookie recipe somewhere on his website. As an aspiring cookie detective, your mission is to uncover this delectable secret. Can you outsmart Cookie Monster and find the hidden recipe? You can access the Cookie Monster here and good luck </h3>

**Phân tích**: đề bài có đề cập khá nhiều về `cookie`

        cookie: là các tập dữ liệu nhỏ mà trình duyệt lưu trữ trên máy, dùng để lưu trữ thông tim về các phiên làm việc như: lựa chọn or đăng nhập

**hướng giải**: việc đầu tiên nghĩ đến sẽ làm đọc phần dữ liệu cookie của trang web

**Giải**:
1. ta sử dụng dev tool để đọc phần cookie của trang web như phân tích, do chưa có bất kì dữ liệu nào khi mới đăng nhập vào web, nên thử đăng nhập với tài khoản mật khẩu bất kì để cập nhật thêm cookie cho trang web sau đó đọc tệp cookie đó.
2. ta sẽ thấy được 1 đoạn base64 

![image](https://github.com/user-attachments/assets/8a39a8b7-1eab-408a-a2be-86b30cbf7c07)


3. decode đoạn base64 rồi nộp flag

![image](https://github.com/user-attachments/assets/164540f1-2d1c-4efd-a907-1a30909f640f)


# head-dump

<h3>ĐỀ BÀI: Welcome to the challenge! In this challenge, you will explore a web application and find an endpoint that exposes a file containing a hidden flag. The application is a simple blog website where you can read articles about various topics, including an article about API Documentation. Your goal is to explore the application and find the endpoint that generates files holding the server’s memory, where a secret flag is hidden.
Additional details will be available after launching your challenge instance. </h3>

**phân tích**: đề bài nói rằng đây là 1 trang blog, khám phá trang web và tìm đến cuối web để tìm ra flag

**hướng giải**: tìm hiểu các đường dẫn trong trang web để tìm ra flag, khá đáng ngờ khi chỉ có "API Documentation" đề cập 

![image](https://github.com/user-attachments/assets/d9cbce66-0ee1-43dc-9014-613d4b3dccf2)

1. cố gắng truy cập vào cuối trang web khi bấm vào #API Documentation ta sẽ được di chuyển tới 1 trang web khác
2. kéo xuống cuối sẽ có 1 mục 'heap-dump' giống như đề bài 'try it out' -> 'excute' -> tải file trên trang web về rồi `ctrl + f` để tìm flag

![image](https://github.com/user-attachments/assets/b33464c8-8e04-4479-b581-20afd242ebec)

# n0s4n1ty 1

<h3>ĐỀ BÀI: A developer has added profile picture upload functionality to a website. However, the implementation is flawed, and it presents an opportunity for you. Your mission, should you choose to accept it, is to navigate to the provided web page and locate the file upload area. Your ultimate goal is to find the hidden flag located in the /root directory. You can access the web application here! </h3>

**Phân tích**: dựa theo đề bài và hint 1, trang web này là 1 trang web tải lên ảnh đại điện nhưng bị lỗi và các file được gửi lên không được lọc định dạng

**Hướng giải**: tìm cách bypass trang web thông qua file uploads

**Giải**:

1. ta sẽ bypass trang wep này bằng 1 file `.php`

        php: là một ngôn ngữ lập trình web, các file thường có đuổi `.php`
        ta cần tạo 1 file web shell .php để điều khiển trang web từ xa

2. tạo 1 file text và ghi dòng lệnh `<?php system($_GET['cmd']); ?>` rồi `save as` với đuôi `.php`

        $_GET['cmd'] lấy dữ liệu từ đường link URL.
        system() thực thi lệnh hệ thống trên server.

3. vì đây là 1 file crack trang web, tự như mã độc lên windown security sẽ xóa nó ngay, ta cần tắt đi trước khi tạo
4. upload file này lên trang web sau đó dùng đường link để ghi lệnh `http://expico.com/uploads/shell.php?cmd=sudo ls -l` để liệt kê file trong web
5. rồi cat file flag từ thư mục `root` ra

![image](https://github.com/user-attachments/assets/a7cd4b2f-4c69-44b1-ab07-8898f94ee2fb)


# SSTI1

<h3>ĐỀ BÀI: I made a cool website where you can announce whatever you want! Try it out!
Additional details will be available after launching your challenge instance. </h3>

**Phân tích**: `ssti` à viết tắt của Server-Side Template Injection (tấn công chèn mã vào lỗ hổng), đây là 1 lỗ hổng cảu trang web khi xử lý input của người dùng, họ có thể chèn mã độc vào input có thể gây ra nhiều hậu quả

**Hướng giải**: dựa vào tên đề bài ta thử trang web bằng cách nhập `{{ 7*7 }}` và trang web trả lại kết quả là 49 => trang web có lỗ hổng và có thể sử dụng các câu lệnh để bypass trang web

**Giải**:

1. ta cần kiểm tra trang web xem trang web sử dụng framework nào để dùng câu lệnh của framework đó để bypass
2. ta check bằng devtool của trình duyệt và thấy
![image](https://github.com/user-attachments/assets/096a92f3-6960-4326-aa83-9ba60793bc4e)


           Werkzeug là WSGI toolkit phổ biến được Flask sử dụng.
           Python/3.8.10 cho thấy backend chạy bằng Python.
           Flask mặc định dùng Jinja2 để render templates, nên có thể thử khai thác SSTI. 

3. nhập `{{ cycler.__init__.__globals__.os.popen('ls -la').read() }}` để liệt kê các file

           đây là 1 lệnh thuộc Jinja2
           cycle.__init__.__globals__: cho phép ta truy cập tới biến toàn cục bộ python kể các cac mô dun hệ thống
           os.popen(): mở 1 tiến trình con chạy lệnh shell nhắn thực thi lệnh `ls -la`
           .read(): để đọc ra kết quả

4. rồi cat file flag

![image](https://github.com/user-attachments/assets/fff79f31-2307-45e1-93b6-e357e1ee175b)










