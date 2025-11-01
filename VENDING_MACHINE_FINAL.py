# ============================================================
# VENDING MACHINE TRADISIONAL
# Referensi: Vending machine fisik klasik seperti yang ada
# di sekolah/kampus/kantor dimana user harus input uang dulu
# baru bisa pilih item
# ============================================================

# Database Produk (Array)
products = [
    {"id": 1, "name": "Coca Cola", "price": 5000, "stock": 10},
    {"id": 2, "name": "Pepsi", "price": 5000, "stock": 8},
    {"id": 3, "name": "Air Mineral", "price": 3000, "stock": 15},
    {"id": 4, "name": "Teh Botol", "price": 4000, "stock": 12},
    {"id": 5, "name": "Kopi Kaleng", "price": 6000, "stock": 7},
    {"id": 6, "name": "Chitato", "price": 8000, "stock": 9},
    {"id": 7, "name": "Oreo", "price": 7000, "stock": 11},
    {"id": 8, "name": "Pocky", "price": 9000, "stock": 6}
]

# Database Akun (Array)
accounts = [
    {"username": "admin", "password": "admin123", "balance": 50000, "referral": "ADMIN001", "points": 0},
    {"username": "Eric", "password": "eric123", "balance": 100000, "referral": "ERIC023", "points": 50}
]

# Session user saat ini
current_user = None

# Program utama dengan looping
running = True

while running:
    print("\n" + "=" * 60)
    print("           VENDING MACHINE TRADISIONAL")
    print("=" * 60)
    
    if current_user:
        print(f"👤 User: {current_user['username']} | 💰 Saldo: Rp {current_user['balance']} | ⭐ Points: {current_user['points']}")
        print(f"🎁 Kode Referral Anda: {current_user['referral']}")
        print("=" * 60)
    
    print("\n📋 MENU UTAMA:")
    print("1. Beli Produk (Cash - Tradisional)")
    print("2. Beli Produk (QRIS - Digital)")
    
    if current_user:
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
    # MENU 1: BELI DENGAN CASH (FLOW TRADISIONAL)
    # ========================================================
    if choice == "1":
        print("\n" + "=" * 60)
        print("🏪 VENDING MACHINE - MODE TRADISIONAL")
        print("=" * 60)
        
        # STEP 1: DISPLAY SEMUA PRODUK
        print("\n📦 DAFTAR PRODUK:")
        print("-" * 60)
        print(f"{'ID':<5} {'Nama Produk':<25} {'Harga':<15} {'Stok'}")
        print("-" * 60)
        
        for product in products:
            stock_status = f"({product['stock']} pcs)" if product['stock'] > 0 else "(HABIS)"
            print(f"{product['id']:<5} {product['name']:<25} Rp {product['price']:<10} {stock_status}")
        
        print("-" * 60)
        
        # STEP 2: INPUT UANG DULU (TRADISIONAL FLOW)
        print("\n💵 MASUKKAN UANG TERLEBIH DAHULU")
        print("Denominasi yang diterima: 1000, 2000, 5000, 10000, 20000, 50000, 100000")
        print("Ketik 0 jika selesai memasukkan uang")
        
        inserted_money = 0
        
        # Loop untuk input uang berkali-kali
        while True:
            print(f"\n💰 Saldo saat ini: Rp {inserted_money}")
            money_input = input("Masukkan uang: Rp ")
            
            try:
                money = int(money_input)
                
                if money == 0:
                    if inserted_money > 0:
                        break
                    else:
                        print("❌ Anda belum memasukkan uang!")
                        continue
                
                # Validasi denominasi
                valid_denominations = [1000, 2000, 5000, 10000, 20000, 50000, 100000]
                if money in valid_denominations:
                    inserted_money += money
                    print(f"✅ Uang Rp {money} diterima!")
                else:
                    print(f"❌ Denominasi Rp {money} tidak valid! Uang dikembalikan.")
            
            except:
                print("❌ Input tidak valid!")
        
        # STEP 3: TAMPILKAN PRODUK YANG BISA DIBELI
        print("\n" + "=" * 60)
        print(f"💰 SALDO ANDA: Rp {inserted_money}")
        print("=" * 60)
        print("\n✅ PRODUK YANG BISA ANDA BELI:")
        print("-" * 60)
        
        can_buy = False
        for product in products:
            if product['stock'] > 0 and product['price'] <= inserted_money:
                can_buy = True
                print(f"{product['id']}. {product['name']:<25} Rp {product['price']}")
        
        if not can_buy:
            print("❌ Tidak ada produk yang bisa dibeli dengan saldo Anda")
            print(f"💵 Uang Anda dikembalikan: Rp {inserted_money}")
            input("\nTekan Enter untuk kembali...")
            continue
        
        print("-" * 60)
        
        # STEP 4: PILIH PRODUK
        product_choice = input("\n➤ Pilih ID produk (atau 0 untuk batal): ")
        
        try:
            product_id = int(product_choice)
            
            if product_id == 0:
                print(f"\n❌ Transaksi dibatalkan")
                print(f"💵 Uang dikembalikan: Rp {inserted_money}")
                input("\nTekan Enter untuk kembali...")
                continue
            
            # Cari produk yang dipilih
            selected_product = None
            for product in products:
                if product['id'] == product_id:
                    selected_product = product
                    break
            
            # STEP 5: VALIDASI DAN PROSES
            if selected_product:
                if selected_product['stock'] <= 0:
                    print("\n❌ Maaf, produk habis!")
                    print(f"💵 Uang dikembalikan: Rp {inserted_money}")
                
                elif selected_product['price'] > inserted_money:
                    print(f"\n❌ Saldo tidak cukup!")
                    print(f"Harga produk: Rp {selected_product['price']}")
                    print(f"Saldo Anda: Rp {inserted_money}")
                    print(f"Kurang: Rp {selected_product['price'] - inserted_money}")
                    print(f"💵 Uang dikembalikan: Rp {inserted_money}")
                
                else:
                    # TRANSAKSI BERHASIL
                    change = inserted_money - selected_product['price']
                    selected_product['stock'] -= 1
                    
                    print("\n" + "=" * 60)
                    print("✅ TRANSAKSI BERHASIL!")
                    print("=" * 60)
                    print(f"🛒 Produk      : {selected_product['name']}")
                    print(f"💵 Harga       : Rp {selected_product['price']}")
                    print(f"💰 Dibayar     : Rp {inserted_money}")
                    print(f"💸 Kembalian   : Rp {change}")
                    print(f"📦 Stok tersisa: {selected_product['stock']} pcs")
                    print("=" * 60)
                    
                    # Bonus poin jika login
                    if current_user:
                        points_earned = selected_product['price'] // 1000
                        current_user['points'] += points_earned
                        print(f"⭐ Poin diterima: +{points_earned} poin")
                    
                    print("\n🎉 Silakan ambil produk Anda di bawah!")
                    print("💵 Kembalian akan keluar dari mesin...")
            else:
                print("\n❌ Produk tidak ditemukan!")
                print(f"💵 Uang dikembalikan: Rp {inserted_money}")
        
        except:
            print("\n❌ Input tidak valid!")
            print(f"💵 Uang dikembalikan: Rp {inserted_money}")
        
        input("\nTekan Enter untuk kembali...")
    
    # ========================================================
    # MENU 2: BELI DENGAN QRIS (DIGITAL)
    # ========================================================
    elif choice == "2":
        print("\n" + "=" * 60)
        print("📱 VENDING MACHINE - MODE QRIS")
        print("=" * 60)
        
        # Display produk
        print("\n📦 DAFTAR PRODUK:")
        print("-" * 60)
        for product in products:
            if product['stock'] > 0:
                print(f"{product['id']}. {product['name']:<25} Rp {product['price']:<10} (Stok: {product['stock']})")
        print("-" * 60)
        
        product_choice = input("\n➤ Pilih ID produk (atau 0 untuk batal): ")
        
        try:
            product_id = int(product_choice)
            
            if product_id == 0:
                print("\n❌ Transaksi dibatalkan")
                input("\nTekan Enter untuk kembali...")
                continue
            
            # Cari produk
            selected_product = None
            for product in products:
                if product['id'] == product_id:
                    selected_product = product
                    break
            
            if selected_product and selected_product['stock'] > 0:
                print(f"\n📦 Produk: {selected_product['name']}")
                print(f"💰 Harga: Rp {selected_product['price']}")
                
                # Tampilkan QRIS
                print("\n" + "=" * 60)
                print("           📱 SCAN QR CODE UNTUK MEMBAYAR")
                print("=" * 60)
                print("        █████████████████████████████")
                print("        ██ ▄▄▄▄▄ █▀ █▀▀██ ▄▄▄▄▄ ██")
                print("        ██ █   █ █▀▀▄ ▀▄█ █   █ ██")
                print("        ██ █▄▄▄█ █ ▀▀█ ██ █▄▄▄█ ██")
                print("        ██▄▄▄▄▄▄▄█▄▀ ▀▄█▄▄▄▄▄▄▄▄██")
                print("        ████ ▄  ▄▀ ▀█▄▀█▀█ ▀ █▄ ██")
                print("        ██ ▄▄▄▄▄ █ ▄▀  █  ▀▀▄▀▄███")
                print("        ██ █   █ █▀ ██▀█▀ ▄█▀█▄███")
                print("        ██ █▄▄▄█ █ ▄▀█▄█▀ ▄ ▄  ███")
                print("        ██▄▄▄▄▄▄▄█▄██▄███▄█▄██▄███")
                print("        █████████████████████████████")
                print(f"\n             Total: Rp {selected_product['price']}")
                print("=" * 60)
                
                confirm = input("\n✅ Konfirmasi pembayaran (y/n): ")
                
                if confirm.lower() == 'y':
                    selected_product['stock'] -= 1
                    
                    print("\n" + "=" * 60)
                    print("✅ PEMBAYARAN BERHASIL!")
                    print("=" * 60)
                    print(f"🛒 Produk: {selected_product['name']}")
                    print(f"💵 Harga: Rp {selected_product['price']}")
                    print(f"📱 Metode: QRIS")
                    print(f"📦 Stok tersisa: {selected_product['stock']} pcs")
                    print("=" * 60)
                    
                    if current_user:
                        points_earned = selected_product['price'] // 1000
                        current_user['points'] += points_earned
                        print(f"⭐ Poin diterima: +{points_earned} poin")
                    
                    print("\n🎉 Silakan ambil produk Anda!")
                else:
                    print("\n❌ Transaksi dibatalkan")
            else:
                print("\n❌ Produk tidak tersedia atau stok habis!")
        
        except:
            print("\n❌ Input tidak valid!")
        
        input("\nTekan Enter untuk kembali...")
    
    # ========================================================
    # MENU 3: LOGIN / BELI DENGAN SALDO AKUN
    # ========================================================
    elif choice == "3":
        if current_user:
            # BELI DENGAN SALDO AKUN
            print("\n" + "=" * 60)
            print("💳 BELI DENGAN SALDO AKUN")
            print("=" * 60)
            print(f"💰 Saldo Anda: Rp {current_user['balance']}")
            print(f"⭐ Poin Anda: {current_user['points']}")
            print("=" * 60)
            
            # Display produk
            print("\n📦 DAFTAR PRODUK:")
            print("-" * 60)
            print(f"{'ID':<5} {'Nama Produk':<25} {'Harga':<15} {'Stok'}")
            print("-" * 60)
            
            for product in products:
                if product['stock'] > 0:
                    affordable = "✅" if product['price'] <= current_user['balance'] else "❌"
                    print(f"{product['id']:<5} {product['name']:<25} Rp {product['price']:<10} ({product['stock']} pcs) {affordable}")
            
            print("-" * 60)
            
            product_choice = input("\n➤ Pilih ID produk (atau 0 untuk batal): ")
            
            try:
                product_id = int(product_choice)
                
                if product_id == 0:
                    print("\n❌ Transaksi dibatalkan")
                    input("\nTekan Enter untuk kembali...")
                    continue
                
                # Cari produk
                selected_product = None
                for product in products:
                    if product['id'] == product_id:
                        selected_product = product
                        break
                
                if selected_product:
                    if selected_product['stock'] <= 0:
                        print("\n❌ Maaf, produk habis!")
                    
                    elif selected_product['price'] > current_user['balance']:
                        print(f"\n❌ Saldo tidak cukup!")
                        print(f"Harga produk: Rp {selected_product['price']}")
                        print(f"Saldo Anda: Rp {current_user['balance']}")
                        print(f"Kurang: Rp {selected_product['price'] - current_user['balance']}")
                    
                    else:
                        # Konfirmasi pembelian
                        print(f"\n📦 Produk: {selected_product['name']}")
                        print(f"💵 Harga: Rp {selected_product['price']}")
                        print(f"💰 Saldo Anda: Rp {current_user['balance']}")
                        
                        confirm = input("\n✅ Konfirmasi pembelian (y/n): ")
                        
                        if confirm.lower() == 'y':
                            # TRANSAKSI BERHASIL
                            current_user['balance'] -= selected_product['price']
                            selected_product['stock'] -= 1
                            points_earned = selected_product['price'] // 1000
                            current_user['points'] += points_earned
                            
                            print("\n" + "=" * 60)
                            print("✅ TRANSAKSI BERHASIL!")
                            print("=" * 60)
                            print(f"🛒 Produk       : {selected_product['name']}")
                            print(f"💵 Harga        : Rp {selected_product['price']}")
                            print(f"💳 Metode       : Saldo Akun")
                            print(f"💰 Saldo tersisa: Rp {current_user['balance']}")
                            print(f"⭐ Poin diterima: +{points_earned} poin")
                            print(f"⭐ Total poin   : {current_user['points']} poin")
                            print(f"📦 Stok tersisa : {selected_product['stock']} pcs")
                            print("=" * 60)
                            print("\n🎉 Silakan ambil produk Anda!")
                        else:
                            print("\n❌ Transaksi dibatalkan")
                else:
                    print("\n❌ Produk tidak ditemukan!")
            
            except:
                print("\n❌ Input tidak valid!")
            
            input("\nTekan Enter untuk kembali...")
        
        else:
            # LOGIN
            print("\n" + "=" * 60)
            print("🔐 LOGIN")
            print("=" * 60)
            
            username = input("Username: ")
            password = input("Password: ")
            
            # Cari akun yang cocok
            found_account = None
            for account in accounts:
                if account['username'] == username and account['password'] == password:
                    found_account = account
                    break
            
            if found_account:
                current_user = found_account
                print("\n✅ Login berhasil!")
                print(f"Selamat datang, {current_user['username']}!")
                print(f"💰 Saldo: Rp {current_user['balance']}")
                print(f"⭐ Poin: {current_user['points']}")
                print(f"🎁 Kode Referral: {current_user['referral']}")
            else:
                print("\n❌ Username atau password salah!")
            
            input("\nTekan Enter untuk kembali...")
    
    # ========================================================
    # MENU 4: REGISTER / TOP UP SALDO
    # ========================================================
    elif choice == "4":
        if current_user:
            # TOP UP SALDO AKUN
            print("\n" + "=" * 60)
            print("💰 TOP UP SALDO AKUN")
            print("=" * 60)
            print(f"💳 Saldo saat ini: Rp {current_user['balance']}")
            print("=" * 60)
            
            print("\n💵 MASUKKAN UANG UNTUK TOP UP")
            print("Denominasi yang diterima: 10000, 20000, 50000, 100000, 200000, 500000")
            print("Ketik 0 jika selesai")
            
            total_topup = 0
            
            while True:
                print(f"\n💰 Total top up saat ini: Rp {total_topup}")
                money_input = input("Masukkan uang: Rp ")
                
                try:
                    money = int(money_input)
                    
                    if money == 0:
                        if total_topup > 0:
                            break
                        else:
                            print("❌ Anda belum memasukkan uang!")
                            cancel = input("Batalkan top up? (y/n): ")
                            if cancel.lower() == 'y':
                                break
                            continue
                    
                    # Validasi denominasi
                    valid_denominations = [10000, 20000, 50000, 100000, 200000, 500000]
                    if money in valid_denominations:
                        total_topup += money
                        print(f"✅ Uang Rp {money} diterima!")
                    else:
                        print(f"❌ Denominasi Rp {money} tidak valid! Uang dikembalikan.")
                
                except:
                    print("❌ Input tidak valid!")
            
            if total_topup > 0:
                # Proses top up
                current_user['balance'] += total_topup
                
                print("\n" + "=" * 60)
                print("✅ TOP UP BERHASIL!")
                print("=" * 60)
                print(f"💵 Jumlah top up: Rp {total_topup}")
                print(f"💰 Saldo baru   : Rp {current_user['balance']}")
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
            while True:
                username = input("\nUsername baru: ")
                
                # Cek apakah username sudah ada
                username_exists = False
                for account in accounts:
                    if account['username'] == username:
                        username_exists = True
                        break
                
                if username_exists:
                    print("❌ Username sudah digunakan! Coba yang lain.")
                elif len(username) < 3:
                    print("❌ Username minimal 3 karakter!")
                else:
                    break
            
            # Input password
            while True:
                password = input("Password baru: ")
                if len(password) < 5:
                    print("❌ Password minimal 5 karakter!")
                else:
                    break
            
            # Generate kode referral otomatis
            referral_code = username.upper()[:4] + str(len(accounts) + 1).zfill(3)
            
            # Input kode referral orang lain (opsional)
            print("\n🎁 Punya kode referral? Masukkan untuk bonus!")
            print("(Tekan Enter untuk skip)")
            ref_input = input("Kode Referral: ").strip().upper()
            
            bonus_given = False
            if ref_input:
                # Cari akun dengan kode referral tersebut
                for account in accounts:
                    if account['referral'] == ref_input:
                        # Bonus untuk yang ngasih referral
                        account['balance'] += 10000
                        account['points'] += 20
                        bonus_given = True
                        print(f"✅ Kode referral valid! Bonus untuk Anda dan {account['username']}!")
                        break
                
                if not bonus_given:
                    print("❌ Kode referral tidak valid!")
            
            # Buat akun baru
            new_account = {
                "username": username,
                "password": password,
                "balance": 20000 if bonus_given else 10000,  # Bonus jika pakai referral
                "referral": referral_code,
                "points": 10 if bonus_given else 0
            }
            
            accounts.append(new_account)
            
            print("\n" + "=" * 60)
            print("✅ REGISTRASI BERHASIL!")
            print("=" * 60)
            print(f"👤 Username      : {username}")
            print(f"🎁 Kode Referral : {referral_code}")
            print(f"💰 Saldo awal    : Rp {new_account['balance']}")
            print(f"⭐ Poin awal     : {new_account['points']}")
            print("=" * 60)
            print("\n💡 Bagikan kode referral Anda untuk mendapat bonus!")
            print("   Setiap orang yang pakai kode Anda, Anda dapat:")
            print("   💰 Rp 10.000 saldo")
            print("   ⭐ 20 poin")
            
            input("\nTekan Enter untuk kembali...")
    
    # ========================================================
    # MENU 5: INFO AKUN & REFERRAL
    # ========================================================
    elif choice == "5":
        if current_user:
            print("\n" + "=" * 60)
            print("📊 INFO AKUN & REFERRAL")
            print("=" * 60)
            print(f"\n👤 Username      : {current_user['username']}")
            print(f"💰 Saldo         : Rp {current_user['balance']}")
            print(f"⭐ Total Poin    : {current_user['points']}")
            print(f"🎁 Kode Referral : {current_user['referral']}")
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
    elif choice == "6":
        if current_user:
            print("\n" + "=" * 60)
            print(f"👋 Sampai jumpa, {current_user['username']}!")
            print("=" * 60)
            print(f"💰 Saldo akhir: Rp {current_user['balance']}")
            print(f"⭐ Total poin : {current_user['points']}")
            print("\n✅ Logout berhasil!")
            
            current_user = None
            input("\nTekan Enter untuk kembali...")
        else:
            print("\n❌ Anda belum login!")
            input("\nTekan Enter untuk kembali...")
    
    # ========================================================
    # MENU 0: KELUAR
    # ========================================================
    elif choice == "0":
        print("\n" + "=" * 60)
        print("           TERIMA KASIH!")
        print("=" * 60)
        
        if current_user:
            print(f"\n👋 Sampai jumpa, {current_user['username']}!")
            print(f"💰 Saldo akhir: Rp {current_user['balance']}")
            print(f"⭐ Total poin : {current_user['points']}")
        
        print("\n🎉 Terima kasih telah menggunakan Vending Machine!")
        print("=" * 60)
        
        running = False
    
    # ========================================================
    # MENU TIDAK VALID
    # ========================================================
    else:
        print("\n❌ Pilihan tidak valid!")
        input("\nTekan Enter untuk kembali...")

print("\n🔚 Program selesai.")