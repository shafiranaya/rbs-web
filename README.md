# rbs-web

## Background
Perusahaan : Paragon Technology and Innovation

Deskripsi kasus : 
Perusahaan menjual berbagai macam makeup yang diwakili oleh tiga brand yang memiliki target pasar yang berbeda yaitu Wardah, Emina, Make Over. 
Di masa pandemi ini, jumlah pengunjung store offline berkurang. Pelanggan seringkali kesulitan dalam memilih produk yang ingin dibeli dan sesuai dengan preferensi mereka karena tidak dapat datang ke store langsung. Paragon ingin meningkatkan penjualan produk pada online storenya dengan memberikan customer experience yang baru dan berbeda. Paragon ingin pelanggannya dapat memilih lip product yang tepat sesuai dengan preferensinya. Sistem yang akan dibuat adalah sistem untuk memberikan rekomendasi lip product untuk seorang pelanggan 

## Solusi
Sistem yang akan dibuat adalah sistem untuk memberikan rekomendasi lip product untuk seorang pelanggan.
Sistem rekomendasi ini berjalan pada web. Pelanggan perlu memasukkan preferensinya sesuai dengan pertanyaan yang ditanyakan. Jawaban sistem dapat berupa produk spesifik atau belum ada produk yang sesuai dengan preferensi. 
Pada web terdapat 22 pertanyaan terkait spesifikasi produk yang perlu diisi pelanggan.

## Sumber Pengetahuan
### Lip Products Paragon
Pengetahuan terkait produk-produk kecantikan bibir yang dimiliki oleh paragon. Mencakup produk dari brand wardah, emina, dan make over. Pengetahuan diperoleh dari website brand terkait.
### Kandungan Produk Kecantikan
Pengetahuan kandungan produk kecantikan meliputi bahan kimiawi maupun kandungan lainnya dari produk kecantikan. Pengetahuan dari bahan-bahan tersebut didapatkan untuk mengetahui efek samping bahan terhadap kulit. Pengetahuan didapatkan dari deskripsi informasi produk dan studi literatur.

## Rancangan Sistem
1. Sistem menerima kondisi kebutuhan dari user melalui website
2. Sistem memproses kebutuhan dengan aturan knowledge based system
3. Sistem merekomendasikan hasil yang sesuai atau pesan "Tidak ada produk yang sesuai" jika tidak ditemukan
4. Saat sistem menemukan rekomendasi yang sesuai, akan terdapat arahan untuk mencari produk pada shopee atau tokopedia 
Arsitektur: Rule Based System menggunakan library experta pada python dengan implementasi pada web menggunakan flask 

## How to Run
```
pip3 install venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 app.py
```

## Deployment Link
https://lip-product-recommendation.herokuapp.com/ 
