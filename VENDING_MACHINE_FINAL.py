# DATABASE PRODUK - Pakai Array Paralel (8 produk)
product_ids = [1, 2, 3, 4, 5, 6, 7, 8]
product_names = ["Coca Cola", "Pepsi", "Air Mineral", "Teh Botol", "Kopi Kaleng", "Chitato", "Oreo", "Pocky"]
product_prices = [5000, 5000, 3000, 4000, 6000, 8000, 7000, 9000]
product_stocks = [10, 8, 15, 12, 7, 9, 11, 6]

# DATABASE AKUN - Pakai Array Paralel (2 akun awal)
account_usernames = ["admin", "Eric"]
account_passwords = ["admin123", "eric123"]
account_balances = [50000, 100000]
account_referrals = ["ADMIN001", "ERIC023"]
account_points = [0, 50]

# Session user (index user yang login, -1 = belum login)
logged_in_user_index = -1

# Program utama dengan looping
running = 1

while running == 1:
    print("\n" + "=" * 60)
    print("           VENDING MACHINE TRADISIONAL")
    print("=" * 60)
    
    if logged_in_user_index >= 0:
        print("👤 User:", account_usernames[logged_in_user_index], "| 💰 Saldo: Rp", account_balances[logged_in_user_index], "| ⭐ Points:", account_points[logged_in_user_index])
        print("🎁 Kode Referral Anda:", account_referrals[logged_in_user_index])
        print("=" * 60)
    
    print("\n📋 MENU UTAMA:")
    print("1. Beli Produk (Cash - Tradisional)")
    print("2. Beli Produk (QRIS - Digital)")
    
    if logged_in_user_index >= 0:
        print("3. Beli dengan Saldo Akun")
        print("4. Top Up Saldo Akun")
        print("5. Info Akun & Referral")
        print("6. Logout")
    else:
        print("3. Login")
        print("4. Register")
    
    print("0. Keluar")
    
    choice = input("\n➤ Pilih menu: ")
    
    # ========================================================
    # MENU 1: BELI DENGAN CASH (TRADISIONAL)
    # ========================================================
    if choice == "1":
        print("\n" + "=" * 60)
        print("🏪 VENDING MACHINE - MODE TRADISIONAL")
        print("=" * 60)
        
        # STEP 1: DISPLAY SEMUA PRODUK
        print("\n📦 DAFTAR PRODUK:")
        print("-" * 60)
        
        i = 0
        while i < len(product_ids):
            stock_status = "(" + str(product_stocks[i]) + " pcs)"
            if product_stocks[i] <= 0:
                stock_status = "(HABIS)"
            
            print(str(product_ids[i]) + ". " + product_names[i] + " - Rp " + str(product_prices[i]) + " " + stock_status)
            i = i + 1
        
        print("-" * 60)
        
        # STEP 2: INPUT UANG
        print("\n💵 MASUKKAN UANG TERLEBIH DAHULU")
        print("Denominasi yang diterima: 1000, 2000, 5000, 10000, 20000, 50000, 100000")
        print("Ketik 0 jika selesai memasukkan uang")
        
        inserted_money = 0
        input_selesai = 0
        
        while input_selesai == 0:
            print("\n💰 Saldo saat ini: Rp", inserted_money)
            money_input = input("Masukkan uang: Rp ")
            
            # Validasi input adalah angka
            input_valid = 1
            j = 0
            while j < len(money_input):
                if money_input[j] < '0' or money_input[j] > '9':
                    input_valid = 0
                j = j + 1
            
            if input_valid == 1:
                if len(money_input) > 0:
                    money = int(money_input)
                else:
                    input_valid = 0
            
            if input_valid == 1:
                if money == 0:
                    if inserted_money > 0:
                        input_selesai = 1
                    else:
                        print("❌ Anda belum memasukkan uang!")
                else:
                    # Cek denominasi valid
                    denominasi_valid = 0
                    if money == 1000 or money == 2000 or money == 5000 or money == 10000:
                        denominasi_valid = 1
                    if money == 20000 or money == 50000 or money == 100000:
                        denominasi_valid = 1
                    
                    if denominasi_valid == 1:
                        inserted_money = inserted_money + money
                        print("✅ Uang Rp", money, "diterima!")
                    else:
                        print("❌ Denominasi Rp", money, "tidak valid! Uang dikembalikan.")
            else:
                print("❌ Input tidak valid!")
        
        # STEP 3: TAMPILKAN PRODUK YANG BISA DIBELI
        print("\n" + "=" * 60)
        print("💰 SALDO ANDA: Rp", inserted_money)
        print("=" * 60)
        print("\n✅ PRODUK YANG BISA ANDA BELI:")
        print("-" * 60)
        
        ada_produk = 0
        i = 0
        while i < len(product_ids):
            if product_stocks[i] > 0:
                if product_prices[i] <= inserted_money:
                    print(str(product_ids[i]) + ". " + product_names[i] + " - Rp " + str(product_prices[i]))
                    ada_produk = 1
            i = i + 1
        
        if ada_produk == 0:
            print("❌ Tidak ada produk yang bisa dibeli dengan saldo Anda")
            print("💵 Uang Anda dikembalikan: Rp", inserted_money)
        else:
            print("-" * 60)
            
            # STEP 4: PILIH PRODUK
            product_choice = input("\n➤ Pilih ID produk (atau 0 untuk batal): ")
            
            # Validasi input angka
            input_valid = 1
            j = 0
            while j < len(product_choice):
                if product_choice[j] < '0' or product_choice[j] > '9':
                    input_valid = 0
                j = j + 1
            
            if input_valid == 1:
                if len(product_choice) > 0:
                    product_id = int(product_choice)
                else:
                    input_valid = 0
            
            if input_valid == 1:
                if product_id == 0:
                    print("\n❌ Transaksi dibatalkan")
                    print("💵 Uang dikembalikan: Rp", inserted_money)
                else:
                    # Cari produk
                    found = 0
                    found_index = -1
                    
                    i = 0
                    while i < len(product_ids):
                        if product_ids[i] == product_id:
                            found = 1
                            found_index = i
                        i = i + 1
                    
                    if found == 1:
                        if product_stocks[found_index] <= 0:
                            print("\n❌ Maaf, produk habis!")
                            print("💵 Uang dikembalikan: Rp", inserted_money)
                        else:
                            if product_prices[found_index] > inserted_money:
                                print("\n❌ Saldo tidak cukup!")
                                print("Harga produk: Rp", product_prices[found_index])
                                print("Saldo Anda: Rp", inserted_money)
                                print("Kurang: Rp", product_prices[found_index] - inserted_money)
                                print("💵 Uang dikembalikan: Rp", inserted_money)
                            else:
                                # TRANSAKSI BERHASIL
                                change = inserted_money - product_prices[found_index]
                                product_stocks[found_index] = product_stocks[found_index] - 1
                                
                                print("\n" + "=" * 60)
                                print("✅ TRANSAKSI BERHASIL!")
                                print("=" * 60)
                                print("🛒 Produk      :", product_names[found_index])
                                print("💵 Harga       : Rp", product_prices[found_index])
                                print("💰 Dibayar     : Rp", inserted_money)
                                print("💸 Kembalian   : Rp", change)
                                print("📦 Stok tersisa:", product_stocks[found_index], "pcs")
                                print("=" * 60)
                                
                                # Bonus poin jika login
                                if logged_in_user_index >= 0:
                                    points_earned = product_prices[found_index] // 1000
                                    account_points[logged_in_user_index] = account_points[logged_in_user_index] + points_earned
                                    print("⭐ Poin diterima: +", points_earned, "poin")
                                
                                print("\n🎉 Silakan ambil produk Anda di bawah!")
                                print("💵 Kembalian akan keluar dari mesin...")
                    else:
                        print("\n❌ Produk tidak ditemukan!")
                        print("💵 Uang dikembalikan: Rp", inserted_money)
            else:
                print("\n❌ Input tidak valid!")
                print("💵 Uang dikembalikan: Rp", inserted_money)
        
        input("\nTekan Enter untuk kembali...")
    
    # ========================================================
    # MENU 2: BELI DENGAN QRIS
    # ========================================================
    else:
        if choice == "2":
            print("\n" + "=" * 60)
            print("📱 VENDING MACHINE - MODE QRIS")
            print("=" * 60)
            
            # Display produk
            print("\n📦 DAFTAR PRODUK:")
            print("-" * 60)
            
            i = 0
            while i < len(product_ids):
                if product_stocks[i] > 0:
                    print(str(product_ids[i]) + ". " + product_names[i] + " - Rp " + str(product_prices[i]) + " (Stok: " + str(product_stocks[i]) + ")")
                i = i + 1
            
            print("-" * 60)
            
            product_choice = input("\n➤ Pilih ID produk (atau 0 untuk batal): ")
            
            # Validasi input
            input_valid = 1
            j = 0
            while j < len(product_choice):
                if product_choice[j] < '0' or product_choice[j] > '9':
                    input_valid = 0
                j = j + 1
            
            if input_valid == 1:
                if len(product_choice) > 0:
                    product_id = int(product_choice)
                else:
                    input_valid = 0
            
            if input_valid == 1:
                if product_id == 0:
                    print("\n❌ Transaksi dibatalkan")
                else:
                    # Cari produk
                    found = 0
                    found_index = -1
                    
                    i = 0
                    while i < len(product_ids):
                        if product_ids[i] == product_id:
                            found = 1
                            found_index = i
                        i = i + 1
                    
                    if found == 1:
                        if product_stocks[found_index] > 0:
                            print("\n📦 Produk:", product_names[found_index])
                            print("💰 Harga: Rp", product_prices[found_index])
                            
                            # Tampilkan QR
                            print("\n" + "=" * 60)
                            print("           📱 SCAN QR CODE UNTUK MEMBAYAR")
                            print("=" * 60)
                            print("        ██████████████████████████")
                            print("        ██ ▄▄▄▄▄ █▀ █▀▀██ ▄▄▄▄▄ ██")
                            print("        ██ █   █ █▀▀▄ ▀▄█ █   █ ██")
                            print("        ██ █▄▄▄█ █ ▀▀█ ██ █▄▄▄█ ██")
                            print("        ██▄▄▄▄▄▄▄█▄▀ ▀▄█▄▄▄▄▄▄▄▄██")
                            print("        ████ ▄  ▄▀ ▀█▄▀█▀█ ▀ █▄ ██")
                            print("        ██ ▄▄▄▄▄ █ ▄▀  █  ▀▀▄▀▄███")
                            print("        ██ █   █ █▀ ██▀█▀ ▄█▀█▄███")
                            print("        ██ █▄▄▄█ █ ▄▀█▄█▀ ▄ ▄  ███")
                            print("        ██▄▄▄▄▄▄▄█▄██▄███▄█▄██▄███")
                            print("        ██████████████████████████")
                            print("\n             Total: Rp", product_prices[found_index])
                            print("=" * 60)
                            
                            confirm = input("\n✅ Konfirmasi pembayaran (y/n): ")
                            
                            if confirm == "y" or confirm == "Y":
                                product_stocks[found_index] = product_stocks[found_index] - 1
                                
                                print("\n" + "=" * 60)
                                print("✅ PEMBAYARAN BERHASIL!")
                                print("=" * 60)
                                print("🛒 Produk:", product_names[found_index])
                                print("💵 Harga: Rp", product_prices[found_index])
                                print("📱 Metode: QRIS")
                                print("📦 Stok tersisa:", product_stocks[found_index], "pcs")
                                print("=" * 60)
                                
                                if logged_in_user_index >= 0:
                                    points_earned = product_prices[found_index] // 1000
                                    account_points[logged_in_user_index] = account_points[logged_in_user_index] + points_earned
                                    print("⭐ Poin diterima: +", points_earned, "poin")
                                
                                print("\n🎉 Silakan ambil produk Anda!")
                            else:
                                print("\n❌ Transaksi dibatalkan")
                        else:
                            print("\n❌ Produk tidak tersedia atau stok habis!")
                    else:
                        print("\n❌ Produk tidak ditemukan!")
            else:
                print("\n❌ Input tidak valid!")
            
            input("\nTekan Enter untuk kembali...")
        
        # ========================================================
        # MENU 3: LOGIN / BELI DENGAN SALDO
        # ========================================================
        else:
            if choice == "3":
                if logged_in_user_index >= 0:
                    # BELI DENGAN SALDO AKUN
                    print("\n" + "=" * 60)
                    print("💳 BELI DENGAN SALDO AKUN")
                    print("=" * 60)
                    print("💰 Saldo Anda: Rp", account_balances[logged_in_user_index])
                    print("⭐ Poin Anda:", account_points[logged_in_user_index])
                    print("=" * 60)
                    
                    # Display produk
                    print("\n📦 DAFTAR PRODUK:")
                    print("-" * 60)
                    
                    i = 0
                    while i < len(product_ids):
                        if product_stocks[i] > 0:
                            affordable = "✅"
                            if product_prices[i] > account_balances[logged_in_user_index]:
                                affordable = "❌"
                            print(str(product_ids[i]) + ". " + product_names[i] + " - Rp " + str(product_prices[i]) + " (" + str(product_stocks[i]) + " pcs) " + affordable)
                        i = i + 1
                    
                    print("-" * 60)
                    
                    product_choice = input("\n➤ Pilih ID produk (atau 0 untuk batal): ")
                    
                    # Validasi
                    input_valid = 1
                    j = 0
                    while j < len(product_choice):
                        if product_choice[j] < '0' or product_choice[j] > '9':
                            input_valid = 0
                        j = j + 1
                    
                    if input_valid == 1:
                        if len(product_choice) > 0:
                            product_id = int(product_choice)
                        else:
                            input_valid = 0
                    
                    if input_valid == 1:
                        if product_id == 0:
                            print("\n❌ Transaksi dibatalkan")
                        else:
                            # Cari produk
                            found = 0
                            found_index = -1
                            
                            i = 0
                            while i < len(product_ids):
                                if product_ids[i] == product_id:
                                    found = 1
                                    found_index = i
                                i = i + 1
                            
                            if found == 1:
                                if product_stocks[found_index] <= 0:
                                    print("\n❌ Maaf, produk habis!")
                                else:
                                    if product_prices[found_index] > account_balances[logged_in_user_index]:
                                        print("\n❌ Saldo tidak cukup!")
                                        print("Harga produk: Rp", product_prices[found_index])
                                        print("Saldo Anda: Rp", account_balances[logged_in_user_index])
                                        print("Kurang: Rp", product_prices[found_index] - account_balances[logged_in_user_index])
                                    else:
                                        # Konfirmasi
                                        print("\n📦 Produk:", product_names[found_index])
                                        print("💵 Harga: Rp", product_prices[found_index])
                                        print("💰 Saldo Anda: Rp", account_balances[logged_in_user_index])
                                        
                                        confirm = input("\n✅ Konfirmasi pembelian (y/n): ")
                                        
                                        if confirm == "y" or confirm == "Y":
                                            # TRANSAKSI BERHASIL
                                            account_balances[logged_in_user_index] = account_balances[logged_in_user_index] - product_prices[found_index]
                                            product_stocks[found_index] = product_stocks[found_index] - 1
                                            points_earned = product_prices[found_index] // 1000
                                            account_points[logged_in_user_index] = account_points[logged_in_user_index] + points_earned
                                            
                                            print("\n" + "=" * 60)
                                            print("✅ TRANSAKSI BERHASIL!")
                                            print("=" * 60)
                                            print("🛒 Produk       :", product_names[found_index])
                                            print("💵 Harga        : Rp", product_prices[found_index])
                                            print("💳 Metode       : Saldo Akun")
                                            print("💰 Saldo tersisa: Rp", account_balances[logged_in_user_index])
                                            print("⭐ Poin diterima: +", points_earned, "poin")
                                            print("⭐ Total poin   :", account_points[logged_in_user_index], "poin")
                                            print("📦 Stok tersisa :", product_stocks[found_index], "pcs")
                                            print("=" * 60)
                                            print("\n🎉 Silakan ambil produk Anda!")
                                        else:
                                            print("\n❌ Transaksi dibatalkan")
                            else:
                                print("\n❌ Produk tidak ditemukan!")
                    else:
                        print("\n❌ Input tidak valid!")
                    
                    input("\nTekan Enter untuk kembali...")
                else:
                    # LOGIN
                    print("\n" + "=" * 60)
                    print("🔐 LOGIN")
                    print("=" * 60)
                    
                    username = input("Username: ")
                    password = input("Password: ")
                    
                    # Cari akun
                    found = 0
                    found_index = -1
                    
                    i = 0
                    while i < len(account_usernames):
                        if account_usernames[i] == username:
                            if account_passwords[i] == password:
                                found = 1
                                found_index = i
                        i = i + 1
                    
                    if found == 1:
                        logged_in_user_index = found_index
                        print("\n✅ Login berhasil!")
                        print("Selamat datang,", account_usernames[logged_in_user_index], "!")
                        print("💰 Saldo: Rp", account_balances[logged_in_user_index])
                        print("⭐ Poin:", account_points[logged_in_user_index])
                        print("🎁 Kode Referral:", account_referrals[logged_in_user_index])
                    else:
                        print("\n❌ Username atau password salah!")
                    
                    input("\nTekan Enter untuk kembali...")
            
            # ========================================================
            # MENU 4: REGISTER / TOP UP
            # ========================================================
            else:
                if choice == "4":
                    if logged_in_user_index >= 0:
                        # TOP UP SALDO
                        print("\n" + "=" * 60)
                        print("💰 TOP UP SALDO AKUN")
                        print("=" * 60)
                        print("💳 Saldo saat ini: Rp", account_balances[logged_in_user_index])
                        print("=" * 60)
                        
                        print("\n💵 MASUKKAN UANG UNTUK TOP UP")
                        print("Denominasi yang diterima: 10000, 20000, 50000, 100000, 200000, 500000")
                        print("Ketik 0 jika selesai")
                        
                        total_topup = 0
                        input_selesai = 0
                        
                        while input_selesai == 0:
                            print("\n💰 Total top up saat ini: Rp", total_topup)
                            money_input = input("Masukkan uang: Rp ")
                            
                            # Validasi
                            input_valid = 1
                            j = 0
                            while j < len(money_input):
                                if money_input[j] < '0' or money_input[j] > '9':
                                    input_valid = 0
                                j = j + 1
                            
                            if input_valid == 1:
                                if len(money_input) > 0:
                                    money = int(money_input)
                                else:
                                    input_valid = 0
                            
                            if input_valid == 1:
                                if money == 0:
                                    if total_topup > 0:
                                        input_selesai = 1
                                    else:
                                        print("❌ Anda belum memasukkan uang!")
                                        cancel = input("Batalkan top up? (y/n): ")
                                        if cancel == "y" or cancel == "Y":
                                            input_selesai = 1
                                else:
                                    # Cek denominasi
                                    denominasi_valid = 0
                                    if money == 10000 or money == 20000 or money == 50000:
                                        denominasi_valid = 1
                                    if money == 100000 or money == 200000 or money == 500000:
                                        denominasi_valid = 1
                                    
                                    if denominasi_valid == 1:
                                        total_topup = total_topup + money
                                        print("✅ Uang Rp", money, "diterima!")
                                    else:
                                        print("❌ Denominasi Rp", money, "tidak valid! Uang dikembalikan.")
                            else:
                                print("❌ Input tidak valid!")
                        
                        if total_topup > 0:
                            account_balances[logged_in_user_index] = account_balances[logged_in_user_index] + total_topup
                            
                            print("\n" + "=" * 60)
                            print("✅ TOP UP BERHASIL!")
                            print("=" * 60)
                            print("💵 Jumlah top up: Rp", total_topup)
                            print("💰 Saldo baru   : Rp", account_balances[logged_in_user_index])
                            print("=" * 60)
                        else:
                            print("\n❌ Top up dibatalkan")
                        
                        input("\nTekan Enter untuk kembali...")
                    else:
                        # REGISTER
                        print("\n" + "=" * 60)
                        print("📝 REGISTER AKUN BARU")
                        print("=" * 60)
                        
                        # Input username
                        username_valid = 0
                        new_username = ""
                        
                        while username_valid == 0:
                            new_username = input("\nUsername baru: ")
                            
                            # Cek duplikat
                            username_exists = 0
                            i = 0
                            while i < len(account_usernames):
                                if account_usernames[i] == new_username:
                                    username_exists = 1
                                i = i + 1
                            
                            if username_exists == 1:
                                print("❌ Username sudah digunakan! Coba yang lain.")
                            else:
                                if len(new_username) < 3:
                                    print("❌ Username minimal 3 karakter!")
                                else:
                                    username_valid = 1
                        
                        # Input password
                        password_valid = 0
                        new_password = ""
                        
                        while password_valid == 0:
                            new_password = input("Password baru: ")
                            if len(new_password) < 5:
                                print("❌ Password minimal 5 karakter!")
                            else:
                                password_valid = 1
                        
                        # Generate kode referral
                        username_upper = ""
                        i = 0
                        while i < len(new_username):
                            if new_username[i] >= 'a' and new_username[i] <= 'z':
                                char_code = ord(new_username[i]) - 32
                                username_upper = username_upper + chr(char_code)
                            else:
                                username_upper = username_upper + new_username[i]
                            i = i + 1
                        
                        # Ambil 4 karakter pertama
                        ref_prefix = ""
                        i = 0
                        while i < 4 and i < len(username_upper):
                            ref_prefix = ref_prefix + username_upper[i]
                            i = i + 1
                        
                        # Nomor urut
                        account_number = len(account_usernames) + 1
                        ref_number = str(account_number)
                        
                        # Pad dengan 0
                        while len(ref_number) < 3:
                            ref_number = "0" + ref_number
                        
                        new_referral = ref_prefix + ref_number
                        
                        # Input kode referral orang lain
                        print("\n🎁 Punya kode referral? Masukkan untuk bonus!")
                        print("(Tekan Enter untuk skip)")
                        ref_input = input("Kode Referral: ")
                        
                        # Convert ke uppercase dan hapus spasi
                        ref_input_upper = ""
                        i = 0
                        while i < len(ref_input):
                            if ref_input[i] >= 'a' and ref_input[i] <= 'z':
                                char_code = ord(ref_input[i]) - 32
                                ref_input_upper = ref_input_upper + chr(char_code)
                            else:
                                if ref_input[i] != ' ':
                                    ref_input_upper = ref_input_upper + ref_input[i]
                            i = i + 1
                        
                        bonus_given = 0
                        
                        if len(ref_input_upper) > 0:
                            # Cari akun dengan kode referral
                            found_ref = 0
                            ref_owner_index = -1
                            
                            i = 0
                            while i < len(account_referrals):
                                if account_referrals[i] == ref_input_upper:
                                    found_ref = 1
                                    ref_owner_index = i
                                i = i + 1
                            
                            if found_ref == 1:
                                # Kasih bonus ke pemilik kode
                                account_balances[ref_owner_index] = account_balances[ref_owner_index] + 10000
                                account_points[ref_owner_index] = account_points[ref_owner_index] + 20
                                bonus_given = 1
                                print("✅ Kode referral valid! Bonus untuk Anda dan", account_usernames[ref_owner_index], "!")
                            else:
                                print("❌ Kode referral tidak valid!")
                        
                        # Tentukan saldo awal
                        new_balance = 10000
                        new_points = 0
                        if bonus_given == 1:
                            new_balance = 20000
                            new_points = 10
                        
                        # Tambahkan akun baru
                        account_usernames.append(new_username)
                        account_passwords.append(new_password)
                        account_balances.append(new_balance)
                        account_referrals.append(new_referral)
                        account_points.append(new_points)
                        
                        print("\n" + "=" * 60)
                        print("✅ REGISTRASI BERHASIL!")
                        print("=" * 60)
                        print("👤 Username      :", new_username)
                        print("🎁 Kode Referral :", new_referral)
                        print("💰 Saldo awal    : Rp", new_balance)
                        print("⭐ Poin awal     :", new_points)
                        print("=" * 60)
                        print("\n💡 Bagikan kode referral Anda untuk mendapat bonus!")
                        print("   Setiap orang yang pakai kode Anda, Anda dapat:")
                        print("   💰 Rp 10.000 saldo")
                        print("   ⭐ 20 poin")
                        
                        input("\nTekan Enter untuk kembali...")
                
                # ========================================================
                # MENU 5: INFO AKUN
                # ========================================================
                else:
                    if choice == "5":
                        if logged_in_user_index >= 0:
                            print("\n" + "=" * 60)
                            print("📊 INFO AKUN & REFERRAL")
                            print("=" * 60)
                            print("\n👤 Username      :", account_usernames[logged_in_user_index])
                            print("💰 Saldo         : Rp", account_balances[logged_in_user_index])
                            print("⭐ Total Poin    :", account_points[logged_in_user_index])
                            print("🎁 Kode Referral :", account_referrals[logged_in_user_index])
                            print("=" * 60)
                            
                            print("\n🎯 SISTEM POIN:")
                            print("   • Setiap Rp 1.000 belanja = 1 poin")
                            print("   • Poin bisa ditukar reward di masa depan")
                            
                            print("\n🎁 SISTEM REFERRAL:")
                            print("   • Bagikan kode referral Anda ke teman")
                            print("   • Saat teman register pakai kode Anda:")
                            print("     - Anda dapat: Rp 10.000 + 20 poin")
                            print("     - Teman dapat: Rp 20.000 + 10 poin")
                            
                            print("\n💡 TIPS:")
                            print("   • Top up saldo untuk belanja lebih mudah")
                            print("   • Login sebelum belanja untuk dapat poin")
                            print("   • Kumpulkan poin untuk reward menarik")
                            
                            input("\nTekan Enter untuk kembali...")
                        else:
                            print("\n❌ Anda harus login terlebih dahulu!")
                            input("\nTekan Enter untuk kembali...")
                    
                    # ========================================================
                    # MENU 6: LOGOUT
                    # ========================================================
                    else:
                        if choice == "6":
                            if logged_in_user_index >= 0:
                                print("\n" + "=" * 60)
                                print("👋 Sampai jumpa,", account_usernames[logged_in_user_index], "!")
                                print("=" * 60)
                                print("💰 Saldo akhir: Rp", account_balances[logged_in_user_index])
                                print("⭐ Total poin :", account_points[logged_in_user_index])
                                print("\n✅ Logout berhasil!")
                                
                                logged_in_user_index = -1
                                input("\nTekan Enter untuk kembali...")
                            else:
                                print("\n❌ Anda belum login!")
                                input("\nTekan Enter untuk kembali...")
                        
                        # ========================================================
                        # MENU 0: KELUAR
                        # ========================================================
                        else:
                            if choice == "0":
                                print("\n" + "=" * 60)
                                print("           TERIMA KASIH!")
                                print("=" * 60)
                                
                                if logged_in_user_index >= 0:
                                    print("\n👋 Sampai jumpa,", account_usernames[logged_in_user_index], "!")
                                    print("💰 Saldo akhir: Rp", account_balances[logged_in_user_index])
                                    print("⭐ Total poin :", account_points[logged_in_user_index])
                                
                                print("\n🎉 Terima kasih telah menggunakan Vending Machine!")
                                print("=" * 60)
                                
                                running = 0
                            
                            # ========================================================
                            # MENU TIDAK VALID
                            # ========================================================
                            else:
                                print("\n❌ Pilihan tidak valid!")
                                input("\nTekan Enter untuk kembali...")

print("\n🔚 Program selesai.")