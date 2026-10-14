r"""
check_locales.py — проверяет все JSON-локали на корректность.

Что проверяет:
  1. Файл — валидный JSON.
  2. Есть meta.code и meta.name.
  3. Есть strings.
  4. Все ключи из en.json присутствуют (нет пропусков).

Запуск:
    python tools/check_locales.py
"""

import json
import os


LOCALES_DIR = os.path.join("assets", "locales")
EN_FILE = os.path.join(LOCALES_DIR, "en.json")


def main():
    # Загружаем эталон — английский.
    if not os.path.isfile(EN_FILE):
        print("ОШИБКА: не найден en.json")
        return

    with open(EN_FILE, "r", encoding="utf-8") as f:
        en_data = json.load(f)
    required = set(en_data.get("strings", {}).keys())
    print(f"Эталон (en.json): {len(required)} ключей\n")

    files = sorted(f for f in os.listdir(LOCALES_DIR) if f.endswith(".json"))
    print(f"Всего файлов: {len(files)}\n")

    problems = []
    for filename in files:
        path = os.path.join(LOCALES_DIR, filename)
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            problems.append((filename, f"битый JSON: {e}"))
            continue

        # Проверка meta.
        meta = data.get("meta", {})
        if not meta.get("code"):
            problems.append((filename, "нет meta.code"))
        if not meta.get("name"):
            problems.append((filename, "нет meta.name"))

        # Проверка strings.
        strings = data.get("strings", {})
        if not strings:
            problems.append((filename, "нет strings"))
            continue

        missing = required - set(strings.keys())
        if missing:
            problems.append((filename, f"пропущено ключей: {len(missing)}"))

    print("=" * 60)
    if not problems:
        print("✅ Все файлы корректны. Проблем нет.")
    else:
        print(f"⚠️  Найдены проблемы в {len(problems)} файлах:\n")
        for filename, msg in problems:
            print(f"  {filename}: {msg}")


if __name__ == "__main__":
    main()