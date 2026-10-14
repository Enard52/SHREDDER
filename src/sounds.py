r"""
sounds.py — управление звуком в программе «ШРЕДДЕР».

Использует встроенный модуль winsound (только Windows).
Если файла со звуком нет — модуль молча ничего не делает.
"""

import os

# winsound встроен в Python, но только на Windows.
try:
    import winsound
    WINSOUND_AVAILABLE = True
except ImportError:
    WINSOUND_AVAILABLE = False


from src.utils import resource_path
SOUNDS_DIR = resource_path("assets/sounds")


def play_looping(filename: str) -> None:
    """
    Запускает звук в цикле (не блокирует программу).

    Звук играет, пока не вызовут stop_all().
    Если файла нет — просто тишина, ничего не падает.
    """
    if not WINSOUND_AVAILABLE:
        return

    path = os.path.join(SOUNDS_DIR, filename)
    if not os.path.isfile(path):
        return

    try:
        # SND_FILENAME — играть из файла.
        # SND_ASYNC    — не блокировать программу (звук в фоне).
        # SND_LOOP     — повторять, пока не остановят.
        winsound.PlaySound(
            path,
            winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP
        )
    except Exception:
        # Не даём звуку уронить программу.
        pass


def stop_all() -> None:
    """Останавливает всё, что сейчас играет."""
    if not WINSOUND_AVAILABLE:
        return
    try:
        # SND_PURGE — «убрать всё, что в данный момент играет».
        winsound.PlaySound(None, winsound.SND_PURGE)
    except Exception:
        pass