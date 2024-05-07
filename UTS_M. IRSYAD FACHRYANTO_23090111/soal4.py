def hasilhitungbmi(berat, tinggi):
    return berat / (tinggi ** 2)

berat = float(input('Masukkan berat badan Anda (kg): '))
tinggi = float(input('Masukkan tinggi badan Anda (m): '))

bmi = hasilhitungbmi (berat, tinggi)
print('berat badan anda:',berat,'kg')
print('tinggi badan anda:',tinggi,'m')
print('nilai BMI Anda adalah:', bmi)

if bmi < 18.5:
    print('kategori BMI : berat badan anda kurang')
elif 18.5 <= bmi < 24.9:
    print('kategori BMI : berat badan normal')
elif 24.9 <= bmi < 29.9:
    print('kategori BMI : anda kelebihan berat badan')
else:
    print('kategori BMI : anda termasuk obesitas')
