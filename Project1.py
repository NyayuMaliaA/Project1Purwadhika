Karyawan = [{'ID':'ABE-001','Nama':'RIAN','Jabatan':'CEO','Divisi':'EXECUTIVE'},
{'ID':'ABE-002','Nama':'JEMMY','Jabatan':'CFO','Divisi':'EXECUTIVE'}]

def data_karyawan():
    while True : 
        menuData = int(input('''
=====Menu Data Karyawan=====
1. Seluruh data karyawan
2. Mencari data karyawan
3. Kembali ke menu utama
Silahkan pilih submenu [1-3] =  '''))
        if menuData == 1 :
            if len(Karyawan) > 0:
                print('=====Data Karyawan ABEIndustries=====')
                print('No\t|NoID \t| Nama\t|Jabatan|Divisi')
                for j,i in enumerate(Karyawan): # j = key , i=value
                    print('{}\t|{}|{}\t|{}\t|{}'.format((j+1),i['ID'],i['Nama'],i['Jabatan'],i['Divisi']))
            else :
                print('\n******Tidak ada data karyawan******\n')
        elif menuData == 2 :
            print('=====Mencari Data Karyawan=====')
            cariKaryawan = input('Silahkan masukan ID karyawan yang dicari : ').upper()
            print(f'Data karyawan dengan ID: {cariKaryawan}')
            cek = False
            for j,i in enumerate(Karyawan): 
                if cariKaryawan == i['ID']:
                    print('{}\t|{}|{}\t|{}\t|{}'.format((j+1),i['ID'],i['Nama'],i['Jabatan'],i['Divisi']))
                    cek = True
                    break
            if cek == False:
                print('\n******Tidak ada data karyawan******\n')
        elif menuData == 3 :
            break
        else :
            print('\n*****Pilihan yang anda masukan salah*****\n')

def tambah_karyawan():
    while True :
        print('=====Menambah Data Karyawan=====')
        print('1.Tambah Data Karyawan\n2.Kembali ke menu utama\n')
        menambah = input('Silahkan pilih submenu [1-2]: ')
        if menambah == '1' :
            confirmUpdate = input('Apakah yakin ingin menambah data (Y/N): ').upper()
            if confirmUpdate == 'Y':
                dataID = input('Masukan ID Karyawan: ').upper()
                for ID_Duplikat in Karyawan:
                    if dataID == ID_Duplikat['ID']:
                        print('\n***ID sudah terpakai silahkan pilih ID lain***\n')
                        break
                else:  
                    dataNama = input('Masukan Nama Karyawan: ').upper()
                    dataJabatan = input('Masukan Jabatan Karyawan: ').upper()
                    dataDivisi = input('Masukan Divisi Karyawan: ').upper()
                    cek = input('Tambahkan data karyawan?(Y/N): ').upper()
                    while True:
                        if cek == 'Y':
                            Karyawan.append({'ID':dataID,'Nama':dataNama,'Jabatan':dataJabatan,'Divisi':dataDivisi}) 
                            print('\n*****Data karyawan berhasil tersimpan*****\n') 
                            break
                        if cek == 'N':
                            tambah_karyawan()
            if confirmUpdate == 'N': 
                tambah_karyawan()
        if menambah == '2' :
            break
        if menambah > '2' :
            print('\n*****Pilihan yang anda masukan salah*****\n')
            break

def update_karyawan():
    while True :
        print('=====Mengubah Data Karyawan=====')
        print('1.Ubah data karyawan\n2.Kembali ke menu utama\n')
        merubah = input('Silahkan pilih submenu [1-2] : ')
        if merubah == '1' :
            cariKaryawan = input('Silahkan masukan ID karyawan yang dicari : ').upper()
            print(f'Data karyawan dengan ID: {cariKaryawan}')
            cek = False
            for j,i in enumerate(Karyawan): # j = key , i=value
                if cariKaryawan == i['ID']:
                    print('{}\t|{}|{}\t|{}\t|{}'.format((j+1),i['ID'],i['Nama'],i['Jabatan'],i['Divisi']))
                    cek = True
                    while True :
                        confirmUpdate = input ('Apakah yakin ingin mengubah data (Y/N): ').upper()
                        if confirmUpdate== 'Y' :
                            while True :
                                inputKeystoUpdate = input('Masukan data apa yang ingin dirubah [Nama\\Jabatan\\Divisi]: ').capitalize()
                                if inputKeystoUpdate == 'Nama' or inputKeystoUpdate == 'Jabatan' or inputKeystoUpdate == 'Divisi':
                                    i[inputKeystoUpdate] = input('Silahkan masukan data baru: ').upper()
                                    print('\n*****Data karyawan berhasil diperbaharui*****\n')
                                    confirmUpdate2 = input('Apakah ingin mengubah data lain [Y/N]: ').upper()
                                if confirmUpdate2 == 'N':
                                    break
                            break
                        elif confirmUpdate == 'N':
                            break   
            if cek == False:
                print('\n******Tidak ada data karyawan******\n')
        elif merubah == '2' :
            break
        elif merubah > '2' :
            print('\n*****Pilihan yang anda masukan salah*****\n')
            break
        
def hapus_karyawan():
    while True :
        print('=====Menghapus Data Karyawan=====')
        print('1.Hapus data karyawan\n2.Kembali ke menu utama\n')
        menghapus = input('Silahkan pilih submenu [1-2] : ')
        if menghapus == '1' :
            cariKaryawan = input('Silahkan masukan ID karyawan yang ingin dihapus : ').upper()
            print(f'Data karyawan dengan ID: {cariKaryawan}')
            cek = False
            for j,i in enumerate(Karyawan): # j = key , i=value
                if cariKaryawan == i['ID']:
                    print('{}\t|{}|{}\t|{}\t|{}'.format((j+1),i['ID'],i['Nama'],i['Jabatan'],i['Divisi']))
                    cek = True
                    while True :
                        confirmUpdate = input ('Apakah yakin ingin menghapus data (Y/N): ').upper()
                        if confirmUpdate == 'Y' :
                            del Karyawan[j]
                            print('\n*****Data karyawan berhasil dihapus*****\n')
                            for k,l in enumerate(Karyawan): # k = key , l=value
                               print('{}\t|{}|{}\t|{}\t|{}'.format((k+1),l['ID'],l['Nama'],l['Jabatan'],l['Divisi']))
                            break                                
                        elif confirmUpdate == 'N':
                            break 
            if cek == False:
                print('\n******Tidak ada data karyawan******\n')
        elif menghapus == '2' :
            break
        elif menghapus > '2' :
            print('\n*****Pilihan yang anda masukan salah*****\n')
            break
        
while True :
    Menu = input('''
====Welcome to ABEIndustries====
==========Menu Utama============
1. Seluruh Data Karyawan
2. Menambahkan Data Karyawan
3. Mengubah Data Karyawan
4. Menghapus Data Karyawan
5. Keluar
Pilih menu yang di butuhkan:  ''')
    if(Menu == '1') :
        data_karyawan()
    elif(Menu == '2') :
        tambah_karyawan()
    elif(Menu == '3') :
        update_karyawan()
    elif(Menu == '4') :
        hapus_karyawan()
    elif(Menu == '5') :
        print('=====Terimakasih Sampai Jumpa=====\n==========ABEIndustries===========')
        break