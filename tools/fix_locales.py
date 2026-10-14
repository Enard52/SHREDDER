r"""
fix_locales.py — приводит все JSON-локали к эталону en.json.

Что делает:
  1. Читает en.json (эталон).
  2. Для каждого файла:
     - сохраняет существующие переводы,
     - добавляет недостающие ключи (значения из en),
     - удаляет лишние ключи (которых нет в en),
     - пересобирает strings в том же порядке, что в en.

Запуск:
    python tools/fix_locales.py
"""

import json
import os


LOCALES_DIR = os.path.join("assets", "locales")
EN_FILE = os.path.join(LOCALES_DIR, "en.json")


def main():
    with open(EN_FILE, "r", encoding="utf-8") as f:
        en_data = json.load(f)
    en_strings = en_data["strings"]
    en_order = list(en_strings.keys())

    files = sorted(f for f in os.listdir(LOCALES_DIR) if f.endswith(".json"))

    fixed = 0
    skipped = 0

    for filename in files:
        if filename == "en.json":
            continue

        path = os.path.join(LOCALES_DIR, filename)
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            print(f"  ПРОПУСК {filename}: {e}")
            skipped += 1
            continue

        old_strings = data.get("strings", {})

        # Собираем strings в порядке en.json.
        new_strings = {}
        for key in en_order:
            if key in old_strings:
                new_strings[key] = old_strings[key]
            else:
                # Добавляем английский текст как заглушку.
                new_strings[key] = en_strings[key]

        data["strings"] = new_strings

        # Сохраняем.
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        fixed += 1

    print(f"✅ Обновлено: {fixed}")
    if skipped:
        print(f"⚠️  Пропущено (ошибки): {skipped}")


if __name__ == "__main__":
    main()