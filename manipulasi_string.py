# episode 17 - manipulasi string



# mengganti string biasa ke lower
nama = "agus"

# perintah:
nama_lower = nama.lower()

print(f'nama lower : {nama_lower}')

# mengganti string biasa ke upper
nama = "cecep"

# printah:
nama_upper = nama.upper()

print(f'nama upper: {nama_upper}')

# mengganti string biasa ke kapitalis
nama = "jeje"

# perintah:
nama_capital = nama.capitalize()

print(f'nama capital : {nama_capital}')

# ==============================


# isalpha() mengecek semuanya huruf

# isalnum() mengecek semuanya angka dan huruf

# isdesimal() mengecek semuanya angka saja

# isspace() mengecek apakah ada spasi

# istitle() mengecek apabila semua kata dimulai dengan capitalize

# ===================================


judul = "You Are Beauty"

cek_judul = judul.istitle()

print(f'apakah judul ? : {cek_judul}')



# ngecek komponen dengan startswith() dan endswith() :

# startwith() :
cek_start = 'halo warga'.startswith('halo')

print(F'START = {cek_start}')

# endswith() :
cek_ends = 'ujung tombak'.endswith('tombak')

print(f'ENDS = {cek_ends}')


# penggabunggan komponen = join() dan split() :

# join:
daftar_kata = ['aku', 'bisa', 'mandi']

join_daftar = ' '.join(daftar_kata)

print(daftar_kata)
print(f' gabungannya : {join_daftar}')

# split
nama_anda = "goblin"

print(nama_anda.split('b'))


# alokasi karakter :
# pakai rjust(), ljust(), center()
# r = right, l = left, just = justify

# rjust() :
kanan = "kanan".rjust(20)
print(kanan)


# ljust() :
kiri = 'kiriku'.ljust(20)
print(kiri)

# center() :
tengah = 'python'.center(50, '=')
print(f'\n\n {tengah}')



# strip() = untuk menghilangkan karakter


tengah_strip = tengah.strip('=')


print(tengah_strip)