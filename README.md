# LZW-Compressor
LZW-Compressor merupakan webapp yang dapat mengkompres masukan string ASCII, dan mendekompresnya dengan algoritma LZW (Lempel-Ziv-Welch). Algoritma LZW merupakan algoritma yang menggunakan sebuah kamus yang menyimpan grup sekuens karakter yang muncul dalam metode kompresinya.

# Feature
Webapp dapat melakuan kompresi dan dekompresi dengan metode:
1. LZW
2. LZW dan BWT
3. LZW, BWT, dan RLE
Format kompres dan dekompres dapat diubah menjadi decimal atau binary. Selain itu, Webapp juga dapat menyimpan hasil kompres dan dekompres. 

# How Does It Works?
## Untuk proses kompresi, program akan menerima input berupa string ascii. Input tersebut diproses dengan langkah-langkah berikut:
1. Program akan menginisialisasi variabel entries dengan karakter ascii (terdiri dari 256 karakter seperti pada web: https://www.ascii-code.com/) dengan index merupakan angka decimal dari karakter ascii (misal: index 97 pada entries merupakan karakter "a").
2. Program akan menginisialisasi variabel output berupa list kosong.
3. Program akan menginisialisasi variabel currentCharacters dengan karakter pertama dari input (index 0).
4. Jika currentCharacters ada di entries, maka karakter selanjutnya akan ditambahkan ke currentCharacters (misal: currentCharacters = "a" dan karakter selanjutnya "b", maka currentCharacters menjadi "ab").
5. Jika currentCharacters tidak ada di entries, maka currentCharacters ditambahkan ke entries dan index entries dengan currentCharacters selain karakter terakhir ditambahkan ke output lalu nilai dari currentCharacters diganti dengan karakter terakhir (misal: currentCharacters = "ab" tidak ada di entries, maka "ab" ditambahkan ke entries dan index entries dari "a" akan ditambahkan ke output lalu currentCharacters menjadi "b").
6. Program akan mengulangi proses dari langkah keempat sampai semua karakter dari input sudah diproses.
Setelah semua karakter input diproses, maka hasil kompresi akan ditampilkan ke webapp

## Untuk proses dekompresi, program akan menerima input berupa angka decimal atau binary bergantung pada pilihan user. input lalu diproses dengan langkah-langkah berikut:
1. Program akan menginisialisasi variabel entries dengan karakter ascii (terdiri dari 256 karakter seperti pada web: https://www.ascii-code.com/) dengan index merupakan angka decimal dari karakter ascii (misal: index 97 pada entries merupakan karakter "a").
2. Program akan menginisialisasi variabel output berupa string kosong.
3. Program akan menginisialisasi variabel currentCode dengan decimal input pertama.
4. Jika iterasi bukan merupakan iterasi pertama (bukan merupakan decimal pertama pada input), maka karakter dengan index terakhir pada entries akan dikonkatenasi dengan karakter pertama entries dengan index currentCode (misal: currentCode = 97 dan karakter index terakhir entries = "a", maka karakter entries dengan index terakhir menjadi "aa").
5. Program akan menambahkan entries dengan index currentCode ke dalam entries (misal: currrentCode = 97, maka karakter a akan ditambahkan ke entries).
6. Output akan dikonkatenasi dengan karakter entries dengan index currentCode (misal: output = "" dan currentCode = 97, maka output menjadi "a").
7. currentCode akan diganti menjadi nilai decimal berikutnya. Program lalu akan menjalankan kembali proses dari langkah 4. Proses ini berulang sampai semua nilai decimal input telah diproses.
Setelah semua nilai decimal input diproses, maka hasil dekompresi akan ditampilkan ke webapp. Untuk proses 

# Requirements
Requirements hanya diperlukan jika ingin menjalankan program secara lokal. Requirements dapat dilihat pada file ```requirements.txt``` pada folder ```src/Backend```

# How To Run
Untuk mengakses webapp, dapat mengakses link berikut: https://lzw-compressor.up.railway.app/. Untuk menjalankan secara lokal dapat mengubah ```backendUrl``` pada file ```script.js``` di folder ```src/Frontend/Static``` menjadi ```http://127.0.0.1:8000```. Lalu jalankan backend terlebih dahulu dengan mengetikkan ```python manage.py runserver``` pada terminal di directory ```src/Backend```. Setelah itu, jalankan file ```index.html``` pada folder frontend dengan port yang berbeda.
