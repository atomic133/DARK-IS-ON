"""
🔍 BOT VALIDATION SCRIPT
Checks all bot components for proper configuration
"""

import os
import sys
from pathlib import Path

def check_env_file():
    """Check if .env file exists and has required variables"""
    print("\n📁 Checking .env file...")
    env_path = Path('.env')
    
    if not env_path.exists():
        print("   ❌ .env file not found!")
        print("   📝 Create .env with:")
        print("      DISCORD_TOKEN=your_token_here")
        print("      OWNER_ID=your_discord_id")
        print("      PREFIX=!")
        return False
    
    with open(env_path, 'r') as f:
        content = f.read()
    
    required_vars = ['DISCORD_TOKEN', 'OWNER_ID', 'PREFIX']
    missing = []
    
    for var in required_vars:
        if var not in content:
            missing.append(var)
    
    if missing:
        print(f"   ❌ Missing variables: {', '.join(missing)}")
        return False
    
    print("   ✅ .env file is properly configured")
    return True


def check_required_files():
    """Check if all required files exist"""
    print("\n📂 Checking required files...")
    
    required_files = [
        'bot.py',
        'data_manager.py',
        'requirements.txt'
    ]
    
    all_exist = True
    for file in required_files:
        if not Path(file).exists():
            print(f"   ❌ Missing: {file}")
            all_exist = False
        else:
            print(f"   ✅ Found: {file}")
    
    return all_exist


def check_commands_folder():
    """Check if commands folder exists with all modules"""
    print("\n📦 Checking commands folder...")
    
    commands_path = Path('commands')
    if not commands_path.exists():
        print("   ❌ commands/ folder not found!")
        return False
    
    required_commands = [
        'economy.py',
        'teams.py',
        'marketplace.py',
        'moderation.py',
        'server_build.py',
        'help_admin.py'
    ]
    
    all_exist = True
    for cmd_file in required_commands:
        cmd_path = commands_path / cmd_file
        if not cmd_path.exists():
            print(f"   ❌ Missing: commands/{cmd_file}")
            all_exist = False
        else:
            print(f"   ✅ Found: commands/{cmd_file}")
    
    return all_exist


def check_data_folder():
    """Check if data folder exists"""
    print("\n💾 Checking data folder...")
    
    data_path = Path('data')
    if not data_path.exists():
        print("   ⚠️  data/ folder not found, creating...")
        data_path.mkdir()
        print("   ✅ Created data/ folder")
    else:
        print("   ✅ data/ folder exists")
    
    return True


def check_dependencies():
    """Check if dependencies are installed"""
    print("\n📚 Checking Python dependencies...")
    
    try:
        import discord
        print(f"   ✅ discord.py ({discord.__version__})")
    except ImportError:
        print("   ❌ discord.py not installed")
        return False
    
    try:
        import dotenv
        print("   ✅ python-dotenv installed")
    except ImportError:
        print("   ❌ python-dotenv not installed")
        return False
    
    try:
        import aiofiles
        print("   ✅ aiofiles installed")
    except ImportError:
        print("   ❌ aiofiles not installed")
        return False
    
    return True


def main():
    """Run all validation checks"""
    print("=" * 60)
    print("🌑 ATOMIC DARK EMPIRE BOT - VALIDATION")
    print("=" * 60)
    
    checks = [
        ('Environment File', check_env_file),
        ('Required Files', check_required_files),
        ('Commands Modules', check_commands_folder),
        ('Data Folder', check_data_folder),
        ('Dependencies', check_dependencies)
    ]
    
    results = []
    for name, check_func in checks:
        result = check_func()
        results.append((name, result))
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 VALIDATION SUMMARY")
    print("=" * 60)
    
    all_passed = True
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {name}")
        if not result:
            all_passed = False
    
    print("=" * 60)
    
    if all_passed:
        print("✅ ALL CHECKS PASSED! Bot is ready to run.")
        print(f"\n🚀 Start the bot with: python bot.py")
    else:
        print("❌ SOME CHECKS FAILED! Fix the issues above before running.")
        print(f"\n📝 Install dependencies: pip install -r requirements.txt")
    
    print("=" * 60)


if __name__ == "__main__":
    main()
