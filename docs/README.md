# Simdak

Simdak adalah aplikasi CLI untuk membantu memasukand data ke aplikasi web simdak khususnya simdak paud.

## Cara Menginstall

Cara menginstall simdak bisa dilihat [di sini](install.md)

## Cara Menggunakan

### Menjalankan simdak

Pastikan anda telah [menginstall simdak](install.md)!

Buka cmd ([cara membuka cmd](./install#cara-membuka-cmd)),

Masukan perintah

```bash
python -m simdak
```

### Menambahkan data RPD ke simdak

Langkahnya

1. [Eksport data](#mengesksport-data) terlebih dahulu
2. Masukan data baru ke file hasil eksport tadi
3. [Import data](#mengimport-data) yang sudah ditambahi

### Mengesksport data

Untuk mengeksport data dari web simdak masukan perintah

```bash
python -m simdak export "nama file"
```

`nama file` bisa diganti sesuka Anda, contoh nama `data simdak 0818181`.

### Mengimport data

Untuk mengimport data ke web simdak masukan perintah

```bash
python -m simdak import "nama file"
```

`nama file` adalah nama dari file yang datanya ingin diimport.

### Membuat template

Untuk membuat template file excel untuk import

```bash
python -m simdak import "nama file"
```
