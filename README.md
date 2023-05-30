# Food Cost Recommendation System (FOCORECS)

Kelompok 1 Analisis dan Desain Sistem P3

## Anggota dan Role:
|  | Nama  | NIM | Role |
| - | ------------- | ------------- | -
| 1 | Sekar Daru Mahanani  | G64199001 | System Analyst |
| 2 | Eka Hero Ramadhani  | X1004222001  | Project Manager |
| 3 | Muhammad Jundi Fathan  | G6401201105 | Back End Developer |
| 4 | Syabil Rofilah Alif Permana | G6401201020 | Front End Developer, UI/UX |
| 5 | Tiar Iswanti | G6401201050 | UI Designer |

## Deskripsi Aplikasi
Aplikasi kami merupakan aplikasi yang memberikan rekomendasi makanan berdasarkan budget yang dimiliki pengguna. Pengguna juga dapat memasukkan rekomendasi makanan dan minuman untuk membantu menambahkan database rekomendasi dari aplikasi kami.

## Latar Belakang
Sebagai mahasiswa, budget yang mereka miliki tentu saja terbatas, terutama bagi mereka yang merantau dan harus memanajemen uangnya sendiri agar cukup setiap bulannya. Untuk membantu para mahasiswa, kami mengembangkan sistem yang membantu mahasiswa dalam memanajemen keuangan pada pengeluaran terkait kebutuhan makan dan minum sehari-hari. Sistem yang kami kembangkan tersebut berupa aplikasi web yang dapat diakses oleh mahasiswa melalui browser smartphone, laptop, dll.

## Tujuan
Aplikasi kami memberikan rekomendasi makanan sesuai budget agar pengguna dapat menghemat pengeluaran melalui penghematan budget makanan.

## User Story
| No. | Aktor | User Story | Acceptance Criteria |
| - | ------------- | ------------- | -
| 1 | Mahasiswa | Sebagai mahasiswa, saya ingin mendapatkan rekomendasi tempat dan  menu makanan sesuai dengan budget yang saya miliki, agar saya dapat memanajemen keuangan saya dengan baik. | Mahasiswa mendapatkan rekomendasi menu makan dan tempat makan yang sesuai dengan saldo yang di input oleh aplikasi. |
| 2 | Pemberi Rekomendasi | Sebagai pemberi rekomendasi, saya ingin memvalidasi hasil input, agar sistem dapat memberikan data yang bisa diandalkan untuk  user. | Informasi yang di input oleh pemberi rekomendasi akan tampil di aplikasi untuk direkomendasikan kepada Mahasiswa (User). |
| 3 | Administrator | Sebagai administrator, saya ingin mengetahui  masalah (bug) pada sistem yang dilaporkan oleh user, agar dapat mengambil tindakan dan penanganan yang akan dilakukan untuk memperbaiki bug. | Masalah (Bug) yang terdapat di aplikasi terselesaikan sehingga user dapat menggunakan aplikasi dengan normal. |

## Ruang Lingkup
Batasan-batasan yang diterapkan untuk proyek ini adalah:

## Lingkungan Pengembangan
CPU : AMD A9 Radeon R5
RAM : 12 GB

## Metodologi
Aplikasi kami menggunakan Model-View-Controller (MVC) untuk architecture pattern dan Factory Method Pattern untuk design pattern.
Alasan mengapa dipilih MVC sebagai Architecture Pattern yang digunakan adalah karena pemisahan tugas yang jelas, bisa melakukan skalabilitas dengan baik, dapat dilakukan reusabilitas (penggunaan kembali) dalam frekuensi yang lebih tinggi, dan pengujian yang lebih mudah pada rancangan aplikasi karena dilakukan pemisahan tugas yang jelas, sedangkan alasan mengapa dipilih Factory Method Pattern sebagai Design Pattern yang digunakan adalah karena superclass ClassUser menurunkan atribut-atribut ke subclass nya yaitu ClassMahasiswa dan ClassPemberiRekomendasi yang memiliki atribut dan metode khusus sesuai dengan perannya.

## Research Plan
### Empathy Map
![Playground Empathy Map](https://github.com/cakhero/adskelompok1/assets/93716487/21172025-2230-4ed2-9576-a688b429a884)
### Customer Journey
![Playground Persona](https://github.com/cakhero/adskelompok1/assets/93716487/886b201b-2111-4c3c-aeca-a69eb0b1c644)
### User Persona
![Playground Persona (1)](https://github.com/cakhero/adskelompok1/assets/93716487/97914a09-c1de-4932-8a13-060567bf2f73)

## System Analysis
### Use Case Diagram
![Use Case Diagram rev](https://github.com/cakhero/adskelompok1/assets/93716487/dd3999cd-4164-42f8-9f21-ccd88b342f7f)
### Activity Diagram
![Activity Diagram rev](https://github.com/cakhero/adskelompok1/assets/93716487/20c42589-fa7f-492a-965e-45d187839ae5)
### ERD

### Class Diagram
![class diagram](https://github.com/cakhero/adskelompok1/assets/93716487/0c1c7559-6013-4805-89ea-37e259a83f87)

## Prototype
Dapat dilihat pada link berikut <a href="https://www.figma.com/file/gcUKB7RcQx19ERXhswvnHx/focorecs?type=design&node-id=0%3A1&t=VJhKGHbW8O4yl5W5-1" target="_blank">Prototype FOCORECS</a>

## Link Video Demo

## Link Aplikasi
Dapat diakses pada link berikut <a href="https://ipb.link/focorecs" target="_blank">Website FOCORECS</a>

## Testing

## Documents
