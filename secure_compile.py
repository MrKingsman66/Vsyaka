import os
import shutil
import subprocess
import json
from pathlib import Path


def compile_secure():
    print("🔒 Создание защищенной версии бота...")

    # Шаг 1: Создаем временную папку
    temp_dir = Path("temp_build")
    temp_dir.mkdir(exist_ok=True)

    # Шаг 2: Копируем необходимые файлы
    shutil.copy("KingsmanRentGlav.py", temp_dir / "bot.py")
    shutil.copy("service_account.json", temp_dir / "service_account.json")

    # Шаг 3: Создаем модифицированную версию для шифрования
    with open(temp_dir / "bot.py", "r", encoding="utf-8") as f:
        content = f.read()

    # Заменяем путь к service_account.json
    content = content.replace(
        "SERVICE_ACCOUNT_FILE = 'service_account.json'",
        "SERVICE_ACCOUNT_FILE = get_service_account_path()"
    )

    # Добавляем функцию для получения пути
    import_section = """import sys
import os
import tempfile
import json

def get_service_account_path():
    \"\"\"Получает путь к service_account.json в EXE\"\"\"
    try:
        # В EXE файле
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.dirname(os.path.abspath(__file__))

        return os.path.join(base_path, 'service_account.json')
    except:
        return 'service_account.json'

"""

    content = import_section + content

    with open(temp_dir / "bot_modified.py", "w", encoding="utf-8") as f:
        f.write(content)

    # Шаг 4: Компилируем с PyInstaller
    print("📦 Компиляция с PyInstaller...")

    pyinstaller_cmd = [
        "pyinstaller",
        "--onefile",
        "--add-data", f"{temp_dir / 'service_account.json'};.",
        "--hidden-import=google.oauth2.service_account",
        "--hidden-import=gspread",
        "--hidden-import=aiogram",
        "--hidden-import=aiogram.filters",
        "--hidden-import=aiogram.types",
        "--hidden-import=asyncio",
        "--name", "KingsmanRentBot",
        str(temp_dir / "bot_modified.py")
    ]

    subprocess.run(pyinstaller_cmd)

    # Шаг 5: Очистка
    shutil.rmtree(temp_dir)
    shutil.rmtree("build", ignore_errors=True)

    print("✅ Защищенный EXE создан: dist/KingsmanRentBot.exe")
    print("🔐 service_account.json встроен в EXE и защищен")


if __name__ == "__main__":
    compile_secure()