r"""
i18n.py — система переводов (интернационализация).

Как работает:
  1. Читает все JSON-файлы из assets/locales/.
  2. Хранит их в словаре: { "ru": {...}, "en": {...}, ... }.
  3. Функция t("ключ") возвращает перевод текущего языка.
  4. Если ключа нет — возвращает сам ключ (удобно для отладки).
"""

import json
import os
from src.utils import resource_path

LOCALES_DIR = resource_path("assets/locales")

# Текущий язык и словарь переводов.
_current_lang = "ru"
_translations = {}       # { "ru": {"strings": {...}}, "en": {...} }
_languages_meta = {}     # { "ru": "Русский", "en": "English", ... }


def load_all_locales() -> None:
    """
    Загружает все JSON из assets/locales/ в память.
    Заполняет _translations и _languages_meta.
    """
    global _translations, _languages_meta

    _translations = {}
    _languages_meta = {}

    if not os.path.isdir(LOCALES_DIR):
        return

    for filename in os.listdir(LOCALES_DIR):
        if not filename.endswith(".json"):
            continue

        path = os.path.join(LOCALES_DIR, filename)
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            continue

        code = data.get("meta", {}).get("code")
        name = data.get("meta", {}).get("name", code)
        if not code:
            continue

        _translations[code] = data.get("strings", {})
        _languages_meta[code] = name


def set_language(code: str) -> None:
    """Устанавливает текущий язык."""
    global _current_lang
    if code in _translations:
        _current_lang = code


def get_language() -> str:
    """Возвращает код текущего языка."""
    return _current_lang


def available_languages() -> dict:
    """
    Возвращает словарь доступных языков: { "ru": "Русский", "en": "English", ... }.
    """
    return dict(_languages_meta)


def t(key: str, **kwargs) -> str:
    """
    Возвращает перевод строки с ключом key для текущего языка.

    Если ключа нет в текущем языке, но есть в английском — берём английский.
    Если нет нигде — возвращаем [key] (видно, что ключ потерян).

    Параметры подставляются: t("confirm_text", name="video.mp4")
    """
    strings = _translations.get(_current_lang, {})
    text = strings.get(key)

    # Fallback на английский, если у текущего языка ключа нет.
    if text is None and _current_lang != "en":
        text = _translations.get("en", {}).get(key)

    if text is None:
        return f"[{key}]"

    if kwargs:
        try:
            return text.format(**kwargs)
        except Exception:
            return text
    return text