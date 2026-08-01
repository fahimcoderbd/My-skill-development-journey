def new_func1():
    def new_func():
        # ✨ 1. Duplicate Removal
        print("=" * 50)
        print("✨ DUPLICATE REMOVAL")
        print("=" * 50)
        names = ["Fa", "Fahim", "Fa", "Fahim"]
        print(f"📋 Original: {names}")
        
        unique = set(names)
        print(f"🎯 Unique Names: {unique}\n")

        # 🔐 2. Fast Checking (O(1))
        print("=" * 50)
        print("🔐 FAST CHECKING - Admin Access")
        print("=" * 50)
        users = {"admin", "user1", "user2"}
        print(f"👥 Users: {users}")
        
        if "admin" in users:
            print("\033[92m")
            print("✅ Admin access granted")  # Output: Admin access granted
            print("\033[0m")
        else:
            print("\033[91m")
            print("❌ Access denied")
            print("\033[0m")
        print()

        # 🔀 3. Common / Different Elements
        print("=" * 50)
        print("🔀 COMMON & DIFFERENT ELEMENTS")
        print("=" * 50)
        rahib = {"gamer", "farmer", "boy"}
        fahim = {"gamer", "coder", "boy"}
        print(f"👤 Rahib's interests: {rahib}")
        print(f"👤 Fahim's interests: {fahim}")
        
        print(f"🤝 Common interests: {rahib & fahim}")
        print(f"➖ Different interests (Rahib only): {rahib - fahim}\n")

        # 🏷️ 5. Real-life: Tags, Keywords, Hashtags
        print("=" * 50)
        print("🏷️  TAGS - REMOVING DUPLICATES")
        print("=" * 50)
        tags = {"py", "js", "py", "js"}
        print(f"🎫 Unique Tags: {tags}")
        print("=" * 50)

    new_func()

new_func1()