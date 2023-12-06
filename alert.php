<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Customized Style Button</title>
  <!-- Menggunakan CDN dari Ant Design untuk Button dan message -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/antd/dist/antd.min.css">
</head>
<body>
  <button id="customButton">Customized Style</button>

  <!-- Memasukkan skrip JavaScript -->
  <script>
    // Menambahkan event listener ke tombol
    document.getElementById('customButton').addEventListener('click', function() {
      // Membuat pesan sukses dengan gaya khusus
      const openSuccessMessage = () => {
        const messageApi = window.antd.message; // Mengambil referensi API message dari Ant Design
        messageApi.open({
          type: 'success',
          content: 'This is a prompt message with custom className and style',
          className: 'custom-class',
          style: {
            marginTop: '20vh',
          },
        });
      };

      // Memanggil fungsi untuk menampilkan pesan sukses saat tombol diklik
      openSuccessMessage();
    });
  </script>

  <!-- Menggunakan CDN dari React, ReactDOM, dan Ant Design untuk message -->
  <script src="https://cdn.jsdelivr.net/npm/react@17/umd/react.development.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/react-dom@17/umd/react-dom.development.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/antd/dist/antd-with-locales.min.js"></script>
</body>
</html>
