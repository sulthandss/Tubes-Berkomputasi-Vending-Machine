# DATABASE PRODUK - Array Paralel (8 produk)
product_ids = [1, 2, 3, 4, 5, 6, 7, 8]
product_names = ["Coca Cola", "Pepsi", "Air Mineral", "Teh Botol", "Kopi Kaleng", "Chitato", "Oreo", "Pocky"]
product_prices = [5000, 5000, 3000, 4000, 6000, 8000, 7000, 9000]
product_stocks = [10, 8, 15, 12, 7, 9, 11, 6]

# DATABASE AKUN - Array Paralel (2 akun awal)
account_usernames = ["admin", "Eric"]
account_passwords = ["admin123", "eric123"]
account_balances = [50000, 100000]
account_referrals = ["ADMIN001", "ERIC023"]
account_points = [0, 50]

# Session user (-1 = belum login)
user_idx = -1

# PROGRAM UTAMA
running = 1
while running == 1:
    print("\n" + "=" * 60)
    print("           VENDING MACHINE TRADISIONAL")
    print("=" * 60)
    
    if user_idx >= 0:
        print("👤", account_usernames[user_idx], "| 💰 Rp", account_balances[user_idx], "| ⭐", account_points[user_idx])
        print("🎁 Referral:", account_referrals[user_idx])
        print("=" * 60)
    
    print("\n📋 MENU:")
    print("1. Beli (Cash) | 2. Beli (QRIS)")
    if user_idx >= 0:
        print("3. Beli (Saldo) | 4. Top Up | 5. Info | 6. Logout")
    else:
        print("3. Login | 4. Register")
    print("0. Keluar")
    
    choice = input("\n➤ Pilih: ")
    
    # === MENU 1: BELI CASH ===
    if choice == "1":
        print("\n" + "=" * 60)
        print("🪙 MODE CASH")
        print("=" * 60)
        
        # Tampilkan produk
        print("\n📦 PRODUK:")
        print("-" * 60)
        i = 0
        while i < len(product_ids):
            if product_stocks[i] > 0:
                print(str(product_ids[i]) + ". " + product_names[i] + " - Rp " + str(product_prices[i]) + " (" + str(product_stocks[i]) + " pcs)")
            i = i + 1
        print("-" * 60)
        
        # Input uang
        print("\nDenominasi: 1000, 2000, 5000, 10000, 20000, 50000, 100000")
        money = 0
        selesai = 0
        while selesai == 0:
            print("💰 Total: Rp", money)
            inp = input("Masukkan uang (0=selesai): Rp ")
            # Validasi angka
            valid = 1
            j = 0
            while j < len(inp):
                if inp[j] < '0' or inp[j] > '9':
                    valid = 0
                j = j + 1
            if valid == 0 or len(inp) == 0:
                print("❌ Input tidak valid!")
            else:
                m = int(inp)
                if m == 0:
                    if money > 0:
                        selesai = 1
                    else:
                        print("❌ Belum memasukkan uang!")
                else:
                    if m == 1000 or m == 2000 or m == 5000 or m == 10000 or m == 20000 or m == 50000 or m == 100000:
                        money = money + m
                        print("✅ Diterima!")
                    else:
                        print("❌ Denominasi tidak valid!")
        
        # Pilih produk
        print("\n💰 Saldo: Rp", money)
        print("\n📦 PRODUK:")
        print("-" * 60)
        i = 0
        while i < len(product_ids):
            if product_stocks[i] > 0 and product_prices[i] <= money:
                print(str(product_ids[i]) + ". " + product_names[i] + " - Rp " + str(product_prices[i]) + " ✅")
            i = i + 1
        print("-" * 60)
        
        inp = input("\n➤ Pilih ID (0=batal): ")
        # Validasi angka
        valid = 1
        j = 0
        while j < len(inp):
            if inp[j] < '0' or inp[j] > '9':
                valid = 0
            j = j + 1
        
        if valid == 1 and len(inp) > 0:
            pid = int(inp)
            if pid == 0:
                print("\n❌ Dibatalkan. Uang dikembalikan: Rp", money)
            else:
                # Cari produk
                idx = -1
                i = 0
                while i < len(product_ids):
                    if product_ids[i] == pid:
                        idx = i
                    i = i + 1
                
                if idx == -1:
                    print("\n❌ Produk tidak ada! Uang dikembalikan: Rp", money)
                else:
                    if product_stocks[idx] <= 0:
                        print("\n❌ Stok habis! Uang dikembalikan: Rp", money)
                    else:
                        if product_prices[idx] > money:
                            print("\n❌ Saldo kurang! Uang dikembalikan: Rp", money)
                        else:
                            # SUKSES
                            kembalian = money - product_prices[idx]
                            product_stocks[idx] = product_stocks[idx] - 1
                            print("\n" + "=" * 60)
                            print("✅ BERHASIL!")
                            print("=" * 60)
                            print("🛒 Produk:", product_names[idx])
                            print("💵 Harga: Rp", product_prices[idx])
                            print("💸 Kembalian: Rp", kembalian)
                            print("📦 Stok: " + str(product_stocks[idx]) + " pcs")
                            if user_idx >= 0:
                                pts = product_prices[idx] // 1000
                                account_points[user_idx] = account_points[user_idx] + pts
                                print("⭐ +", pts, "poin")
                            print("=" * 60)
        else:
            print("\n❌ Input tidak valid! Uang dikembalikan: Rp", money)
        input("\nEnter...")
    
    # === MENU 2: BELI QRIS ===
    elif choice == "2":
        print("\n" + "=" * 60)
        print("📱 MODE QRIS")
        print("=" * 60)
        
        # Tampilkan produk
        print("\n📦 PRODUK:")
        print("-" * 60)
        i = 0
        while i < len(product_ids):
            if product_stocks[i] > 0:
                print(str(product_ids[i]) + ". " + product_names[i] + " - Rp " + str(product_prices[i]) + " (" + str(product_stocks[i]) + " pcs)")
            i = i + 1
        print("-" * 60)
        
        inp = input("\n➤ Pilih ID (0=batal): ")
        # Validasi
        valid = 1
        j = 0
        while j < len(inp):
            if inp[j] < '0' or inp[j] > '9':
                valid = 0
            j = j + 1
        
        if valid == 1 and len(inp) > 0:
            pid = int(inp)
            if pid > 0:
                # Cari produk
                idx = -1
                i = 0
                while i < len(product_ids):
                    if product_ids[i] == pid:
                        idx = i
                    i = i + 1
                
                if idx >= 0 and product_stocks[idx] > 0:
                    # QR Code
                    print("\n" + "=" * 60)
                    print("           📱 SCAN QR CODE")
                    print("=" * 60)
                    print("        ██████████████████████████")
                    print("        ██ █████ ██ ███ █████ ██")
                    print("        ██ █   █ ███ ██ █   █ ██")
                    print("        ██ █▄▄▄█ █ ██ █ █▄▄▄█ ██")
                    print("        ██▄▄▄▄▄▄▄█▄ ▄█▄▄▄▄▄▄▄▄██")
                    print("        ████ ▄  ▄ ▄█▄█▄█ ▄ █▄ ██")
                    print("        ██ █████ █ ▄  █  ██▄▄███")
                    print("        ██ █   █ █ ███ ▄█ █▄ ███")
                    print("        ██ █▄▄▄█ █ ▄█▄█ ▄ ▄  ███")
                    print("        ██▄▄▄▄▄▄▄█▄██▄███▄█▄████")
                    print("        ██████████████████████████")
                    print("\n        Total: Rp", product_prices[idx])
                    print("=" * 60)
                    
                    confirm = input("\n✅ Bayar? (y/n): ")
                    if confirm == "y" or confirm == "Y":
                        product_stocks[idx] = product_stocks[idx] - 1
                        print("\n✅ BERHASIL!")
                        print("🛒 Produk:", product_names[idx])
                        print("💵 Harga: Rp", product_prices[idx])
                        print("📦 Stok:", product_stocks[idx], "pcs")
                        if user_idx >= 0:
                            pts = product_prices[idx] // 1000
                            account_points[user_idx] = account_points[user_idx] + pts
                            print("⭐ +", pts, "poin")
                    else:
                        print("\n❌ Dibatalkan")
                else:
                    print("\n❌ Produk tidak tersedia!")
        input("\nEnter...")
    
    # === MENU 3: LOGIN / BELI SALDO ===
    elif choice == "3":
        if user_idx >= 0:
            # BELI DENGAN SALDO
            print("\n" + "=" * 60)
            print("💳 BELI DENGAN SALDO")
            print("=" * 60)
            print("💰 Saldo: Rp", account_balances[user_idx])
            
            # Tampilkan produk
            print("\n📦 PRODUK:")
            print("-" * 60)
            i = 0
            while i < len(product_ids):
                if product_stocks[i] > 0:
                    mark = "✅" if product_prices[i] <= account_balances[user_idx] else "❌"
                    print(str(product_ids[i]) + ". " + product_names[i] + " - Rp " + str(product_prices[i]) + " " + mark)
                i = i + 1
            print("-" * 60)
            
            inp = input("\n➤ Pilih ID (0=batal): ")
            # Validasi
            valid = 1
            j = 0
            while j < len(inp):
                if inp[j] < '0' or inp[j] > '9':
                    valid = 0
                j = j + 1
            
            if valid == 1 and len(inp) > 0:
                pid = int(inp)
                if pid > 0:
                    # Cari produk
                    idx = -1
                    i = 0
                    while i < len(product_ids):
                        if product_ids[i] == pid:
                            idx = i
                        i = i + 1
                    
                    if idx >= 0 and product_stocks[idx] > 0:
                        if product_prices[idx] <= account_balances[user_idx]:
                            print("\n📦 Produk:", product_names[idx])
                            print("💵 Harga: Rp", product_prices[idx])
                            confirm = input("✅ Beli? (y/n): ")
                            if confirm == "y" or confirm == "Y":
                                account_balances[user_idx] = account_balances[user_idx] - product_prices[idx]
                                product_stocks[idx] = product_stocks[idx] - 1
                                pts = product_prices[idx] // 1000
                                account_points[user_idx] = account_points[user_idx] + pts
                                print("\n✅ BERHASIL!")
                                print("🛒 Produk:", product_names[idx])
                                print("💰 Saldo: Rp", account_balances[user_idx])
                                print("⭐ +", pts, "poin | Total:", account_points[user_idx])
                        else:
                            print("\n❌ Saldo kurang!")
                    else:
                        print("\n❌ Produk tidak tersedia!")
            input("\nEnter...")
        else:
            # LOGIN
            print("\n" + "=" * 60)
            print("🔐 LOGIN")
            print("=" * 60)
            username = input("Username: ")
            password = input("Password: ")
            found = 0
            i = 0
            while i < len(account_usernames):
                if account_usernames[i] == username and account_passwords[i] == password:
                    user_idx = i
                    found = 1
                i = i + 1
            if found == 1:
                print("\n✅ Login berhasil! Selamat datang,", username, "!")
                print("💰 Saldo: Rp", account_balances[user_idx])
            else:
                print("\n❌ Username/password salah!")
            input("\nEnter...")
    
    # === MENU 4: REGISTER / TOP UP ===
    elif choice == "4":
        if user_idx >= 0:
            # TOP UP
            print("\n" + "=" * 60)
            print("💰 TOP UP SALDO")
            print("=" * 60)
            print("💳 Saldo: Rp", account_balances[user_idx])
            print("\nDenominasi: 10000, 20000, 50000, 100000, 200000, 500000")
            
            topup = 0
            selesai = 0
            while selesai == 0:
                print("💰 Total: Rp", topup)
                inp = input("Masukkan (0=selesai): Rp ")
                # Validasi
                valid = 1
                j = 0
                while j < len(inp):
                    if inp[j] < '0' or inp[j] > '9':
                        valid = 0
                    j = j + 1
                if valid == 0 or len(inp) == 0:
                    print("❌ Input tidak valid!")
                else:
                    m = int(inp)
                    if m == 0:
                        if topup > 0:
                            selesai = 1
                        else:
                            print("❌ Belum memasukkan uang!")
                    else:
                        if m == 10000 or m == 20000 or m == 50000 or m == 100000 or m == 200000 or m == 500000:
                            topup = topup + m
                            print("✅ Diterima!")
                        else:
                            print("❌ Denominasi tidak valid!")
            
            account_balances[user_idx] = account_balances[user_idx] + topup
            print("\n✅ TOP UP BERHASIL!")
            print("💰 Saldo: Rp", account_balances[user_idx])
            input("\nEnter...")
        else:
            # REGISTER
            print("\n" + "=" * 60)
            print("📝 REGISTER")
            print("=" * 60)
            username = input("Username (min 3): ")
            while len(username) < 3:
                print("❌ Minimal 3 karakter!")
                username = input("Username: ")
            # Cek duplikat
            exists = 1
            while exists == 1:
                exists = 0
                i = 0
                while i < len(account_usernames):
                    if account_usernames[i] == username:
                        exists = 1
                    i = i + 1
                if exists == 1:
                    print("❌ Username sudah ada!")
                    username = input("Username: ")
            
            password = input("Password (min 5): ")
            while len(password) < 5:
                print("❌ Minimal 5 karakter!")
                password = input("Password: ")
            
            # Generate referral
            ref = ""
            i = 0
            while i < 4 and i < len(username):
                c = username[i]
                if c >= 'a' and c <= 'z':
                    c = chr(ord(c) - 32)
                ref = ref + c
                i = i + 1
            num = str(len(account_usernames) + 1)
            while len(num) < 3:
                num = "0" + num
            ref = ref + num
            
            # Cek referral
            print("\n🎁 Kode referral? (Enter=skip)")
            ref_input = input("Kode: ")
            bonus = 0
            # Uppercase
            ref_up = ""
            i = 0
            while i < len(ref_input):
                c = ref_input[i]
                if c >= 'a' and c <= 'z':
                    c = chr(ord(c) - 32)
                if c != ' ':
                    ref_up = ref_up + c
                i = i + 1
            
            if len(ref_up) > 0:
                i = 0
                while i < len(account_referrals):
                    if account_referrals[i] == ref_up:
                        account_balances[i] = account_balances[i] + 10000
                        account_points[i] = account_points[i] + 20
                        bonus = 1
                        print("✅ Valid! Bonus untuk", account_usernames[i], "!")
                    i = i + 1
            
            balance = 20000 if bonus == 1 else 10000
            points = 10 if bonus == 1 else 0
            account_usernames.append(username)
            account_passwords.append(password)
            account_balances.append(balance)
            account_referrals.append(ref)
            account_points.append(points)
            
            print("\n✅ REGISTRASI BERHASIL!")
            print("👤 Username:", username)
            print("🎁 Kode:", ref)
            print("💰 Saldo: Rp", balance)
            input("\nEnter...")
    
    # === MENU 5: INFO ===
    elif choice == "5":
        if user_idx >= 0:
            print("\n" + "=" * 60)
            print("📊 INFO AKUN")
            print("=" * 60)
            print("👤 Username:", account_usernames[user_idx])
            print("💰 Saldo: Rp", account_balances[user_idx])
            print("⭐ Poin:", account_points[user_idx])
            print("🎁 Kode:", account_referrals[user_idx])
            print("\n🎯 Rp 1.000 = 1 poin")
            print("🎁 Referral: Rp 10.000 + 20 poin")
            input("\nEnter...")
        else:
            print("\n❌ Harus login!")
            input("\nEnter...")
    
    # === MENU 6: LOGOUT ===
    elif choice == "6":
        if user_idx >= 0:
            print("\n👋 Bye,", account_usernames[user_idx], "!")
            user_idx = -1
            input("\nEnter...")
    
    # === MENU 0: KELUAR ===
    elif choice == "0":
        print("\n" + "=" * 60)
        print("TERIMA KASIH!")
        if user_idx >= 0:
            print("👋", account_usernames[user_idx])
        print("=" * 60)
        running = 0
    
    else:
        print("\n❌ Tidak valid!")
        input("\nEnter...")

print("\n📚 Selesai.")