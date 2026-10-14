r"""
fix_popular_locales.py — добавляет человеческие переводы 4 новых ключей
для избранных (популярных) языков.

Запуск:
    python tools/fix_popular_locales.py
"""

import json
import os


LOCALES_DIR = os.path.join("assets", "locales")


TRANSLATIONS = {
    "de": {
        "confirm_lnk_title": "⚠ VERKNÜPFUNG (.lnk)",
        "confirm_lnk_text": "Dies ist eine Verknüpfung (.lnk). Nur die Verknüpfung selbst wird vernichtet.\n\nDie Zieldatei, auf die sie zeigt, bleibt unversehrt.\n\nFortfahren?",
        "drive_remote_warning": "Dies ist ein Netzlaufwerk (\\\\server\\share).\nDas Überschreiben von Sektoren garantiert keine Vernichtung — der Server kann Snapshots, Deduplizierung oder CoW haben.\n\nFortfahren?",
        "drive_removable_warning": "Dies ist ein Wechseldatenträger (USB-Stick / externe Festplatte).\nDer Controller kann alte Blöcke in Reserve behalten.\n\nFortfahren?",
        "ft_lnk": "Verknüpfung (.lnk) — Bestätigung erforderlich",
        "dont_ask_again": "Nicht mehr fragen",
        "dont_show_again": "Nicht mehr anzeigen",
        "search_placeholder": "Suchen...",
    },
    "fr": {
        "confirm_lnk_title": "⚠ RACCOURCI (.lnk)",
        "confirm_lnk_text": "Ceci est un raccourci (.lnk). Seul le raccourci lui-même sera détruit.\n\nLe fichier cible vers lequel il pointe restera intact.\n\nContinuer ?",
        "drive_remote_warning": "Ceci est un lecteur réseau (\\\\serveur\\partage).\nL'écrasement des secteurs ne garantit pas la destruction — le serveur peut avoir des instantanés, de la déduplication ou du CoW.\n\nContinuer ?",
        "drive_removable_warning": "Ceci est un lecteur amovible (clé USB / disque externe).\nLe contrôleur peut conserver d'anciens blocs en réserve.\n\nContinuer ?",
        "ft_lnk": "Raccourci (.lnk) — confirmation requise",
        "dont_ask_again": "Ne plus demander",
        "dont_show_again": "Ne plus afficher",
        "search_placeholder": "Rechercher...",
    },
    "it": {
        "confirm_lnk_title": "⚠ COLLEGAMENTO (.lnk)",
        "confirm_lnk_text": "Questo è un collegamento (.lnk). Solo il collegamento stesso sarà distrutto.\n\nIl file di destinazione a cui punta rimarrà intatto.\n\nContinuare?",
        "drive_remote_warning": "Questa è un'unità di rete (\\\\server\\condivisione).\nLa sovrascrittura dei settori non garantisce la distruzione — il server potrebbe avere snapshot, deduplicazione o CoW.\n\nContinuare?",
        "drive_removable_warning": "Questa è un'unità rimovibile (chiavetta USB / HDD esterno).\nIl controller potrebbe conservare vecchi blocchi di riserva.\n\nContinuare?",
        "ft_lnk": "Collegamento (.lnk) — richiede conferma",
        "dont_ask_again": "Non chiedere più",
        "dont_show_again": "Non mostrare più",
        "search_placeholder": "Cerca...",
    },
    "es": {
        "confirm_lnk_title": "⚠ ACCESO DIRECTO (.lnk)",
        "confirm_lnk_text": "Este es un acceso directo (.lnk). Solo el acceso directo será destruido.\n\nEl archivo de destino al que apunta permanecerá intacto.\n\n¿Continuar?",
        "drive_remote_warning": "Esta es una unidad de red (\\\\servidor\\recurso).\nLa sobrescritura de sectores no garantiza la destrucción — el servidor puede tener instantáneas, deduplicación o CoW.\n\n¿Continuar?",
        "drive_removable_warning": "Esta es una unidad extraíble (memoria USB / HDD externo).\nEl controlador puede conservar bloques antiguos en reserva.\n\n¿Continuar?",
        "ft_lnk": "Acceso directo (.lnk) — requiere confirmación",
        "dont_ask_again": "No volver a preguntar",
        "dont_show_again": "No volver a mostrar",
        "search_placeholder": "Buscar...",
    },
    "es-419": {
        "confirm_lnk_title": "⚠ ACCESO DIRECTO (.lnk)",
        "confirm_lnk_text": "Este es un acceso directo (.lnk). Solo el acceso directo será destruido.\n\nEl archivo de destino al que apunta permanecerá intacto.\n\n¿Continuar?",
        "drive_remote_warning": "Esta es una unidad de red (\\\\servidor\\recurso).\nLa sobrescritura de sectores no garantiza la destrucción — el servidor puede tener instantáneas, deduplicación o CoW.\n\n¿Continuar?",
        "drive_removable_warning": "Esta es una unidad extraíble (memoria USB / HDD externo).\nEl controlador puede conservar bloques antiguos en reserva.\n\n¿Continuar?",
        "ft_lnk": "Acceso directo (.lnk) — requiere confirmación",
        "dont_ask_again": "No volver a preguntar",
        "dont_show_again": "No volver a mostrar",
        "search_placeholder": "Buscar...",
    },
    "pt-PT": {
        "confirm_lnk_title": "⚠ ATALHO (.lnk)",
        "confirm_lnk_text": "Este é um atalho (.lnk). Apenas o próprio atalho será destruído.\n\nO ficheiro de destino para o qual aponta permanecerá intacto.\n\nContinuar?",
        "drive_remote_warning": "Esta é uma unidade de rede (\\\\servidor\\partilha).\nA sobrescrita de setores não garante a destruição — o servidor pode ter snapshots, desduplicação ou CoW.\n\nContinuar?",
        "drive_removable_warning": "Esta é uma unidade removível (pen USB / HDD externo).\nO controlador pode manter blocos antigos em reserva.\n\nContinuar?",
        "ft_lnk": "Atalho (.lnk) — requer confirmação",
        "dont_ask_again": "Não perguntar novamente",
        "dont_show_again": "Não mostrar novamente",
        "search_placeholder": "Pesquisar...",
    },
    "pt-BR": {
        "confirm_lnk_title": "⚠ ATALHO (.lnk)",
        "confirm_lnk_text": "Este é um atalho (.lnk). Apenas o próprio atalho será destruído.\n\nO arquivo de destino para o qual aponta permanecerá intacto.\n\nContinuar?",
        "drive_remote_warning": "Esta é uma unidade de rede (\\\\servidor\\compartilhamento).\nA sobrescrita de setores não garante a destruição — o servidor pode ter snapshots, desduplicação ou CoW.\n\nContinuar?",
        "drive_removable_warning": "Esta é uma unidade removível (pen drive / HDD externo).\nO controlador pode manter blocos antigos em reserva.\n\nContinuar?",
        "ft_lnk": "Atalho (.lnk) — requer confirmação",
        "dont_ask_again": "Não perguntar novamente",
        "dont_show_again": "Não mostrar novamente",
        "search_placeholder": "Pesquisar...",
    },
    "uk": {
        "confirm_lnk_title": "⚠ ЯРЛИК (.lnk)",
        "confirm_lnk_text": "Це ярлик (.lnk). Буде знищено лише сам ярлик.\n\nФайл, на який він вказує, залишиться цілим.\n\nПродовжити?",
        "drive_remote_warning": "Це мережевий диск (\\\\server\\share).\nПерезапис секторів не гарантує знищення — на сервері можуть бути снепшоти, дедуплікація або CoW.\n\nПродовжити?",
        "drive_removable_warning": "Це знімний диск (флешка / зовнішній USB).\nКонтролер може залишити старі блоки в резерві.\n\nПродовжити?",
        "ft_lnk": "Ярлик (.lnk) — потребує підтвердження",
        "dont_ask_again": "Більше не питати",
        "dont_show_again": "Більше не показувати",
        "search_placeholder": "Пошук...",
    },
    "pl": {
        "confirm_lnk_title": "⚠ SKRÓT (.lnk)",
        "confirm_lnk_text": "To jest skrót (.lnk). Zniszczony zostanie tylko sam skrót.\n\nPlik docelowy, na który wskazuje, pozostanie nienaruszony.\n\nKontynuować?",
        "drive_remote_warning": "To jest dysk sieciowy (\\\\serwer\\udział).\nNadpisanie sektorów nie gwarantuje zniszczenia — serwer może mieć migawki, deduplikację lub CoW.\n\nKontynuować?",
        "drive_removable_warning": "To jest dysk wymienny (pendrive / zewnętrzny HDD).\nKontroler może zachować stare bloki w rezerwie.\n\nKontynuować?",
        "ft_lnk": "Skrót (.lnk) — wymaga potwierdzenia",
        "dont_ask_again": "Nie pytaj ponownie",
        "dont_show_again": "Nie pokazuj ponownie",
        "search_placeholder": "Szukaj...",
    },
    "tr": {
        "confirm_lnk_title": "⚠ KISAYOL (.lnk)",
        "confirm_lnk_text": "Bu bir kısayoldur (.lnk). Yalnızca kısayolun kendisi yok edilecek.\n\nİşaret ettiği hedef dosya bozulmadan kalacaktır.\n\nDevam edilsin mi?",
        "drive_remote_warning": "Bu bir ağ sürücüsüdür (\\\\sunucu\\paylaşım).\nSektör üzerine yazma yok etmeyi garanti etmez — sunucuda anlık görüntüler, tekilleştirme veya CoW olabilir.\n\nDevam edilsin mi?",
        "drive_removable_warning": "Bu bir çıkarılabilir sürücüdür (USB bellek / harici HDD).\nDenetleyici eski blokları yedekte tutabilir.\n\nDevam edilsin mi?",
        "ft_lnk": "Kısayol (.lnk) — onay gerektirir",
        "dont_ask_again": "Bir daha sorma",
        "dont_show_again": "Bir daha gösterme",
        "search_placeholder": "Ara...",
    },
    "ar": {
        "confirm_lnk_title": "⚠ اختصار (.lnk)",
        "confirm_lnk_text": "هذا اختصار (.lnk). سيتم تدمير الاختصار نفسه فقط.\n\nالملف الهدف الذي يشير إليه سيبقى سليمًا.\n\nمتابعة؟",
        "drive_remote_warning": "هذا قرص شبكة (\\\\خادم\\مشاركة).\nالكتابة فوق القطاعات لا تضمن التدمير — قد يحتوي الخادم على لقطات أو إلغاء تكرار أو CoW.\n\nمتابعة؟",
        "drive_removable_warning": "هذا قرص قابل للإزالة (ذاكرة USB / قرص خارجي).\nقد يحتفظ المتحكم بكتل قديمة في الاحتياط.\n\nمتابعة؟",
        "ft_lnk": "اختصار (.lnk) — يتطلب تأكيدًا",
        "dont_ask_again": "لا تسأل مرة أخرى",
        "dont_show_again": "لا تعرض مرة أخرى",
        "search_placeholder": "بحث...",
    },
    "ko": {
        "confirm_lnk_title": "⚠ 바로 가기 (.lnk)",
        "confirm_lnk_text": "이것은 바로 가기(.lnk)입니다. 바로 가기 자체만 파괴됩니다.\n\n가리키는 대상 파일은 그대로 남습니다.\n\n계속하시겠습니까?",
        "drive_remote_warning": "이것은 네트워크 드라이브입니다(\\\\서버\\공유).\n섹터 덮어쓰기는 파괴를 보장하지 않습니다 — 서버에 스냅샷, 중복 제거 또는 CoW가 있을 수 있습니다.\n\n계속하시겠습니까?",
        "drive_removable_warning": "이것은 이동식 드라이브입니다(USB 메모리 / 외장 HDD).\n컨트롤러가 이전 블록을 예비로 보관할 수 있습니다.\n\n계속하시겠습니까?",
        "ft_lnk": "바로 가기 (.lnk) — 확인 필요",
        "dont_ask_again": "다시 묻지 않기",
        "dont_show_again": "다시 표시하지 않기",
        "search_placeholder": "검색...",
    },
    "zh-Hans": {
        "confirm_lnk_title": "⚠ 快捷方式 (.lnk)",
        "confirm_lnk_text": "这是快捷方式 (.lnk)。只有快捷方式本身会被销毁。\n\n它所指向的目标文件将保持不变。\n\n继续？",
        "drive_remote_warning": "这是网络驱动器 (\\\\服务器\\共享)。\n扇区覆盖不保证销毁 — 服务器可能有快照、去重或 CoW。\n\n继续？",
        "drive_removable_warning": "这是可移动驱动器 (U 盘 / 外置硬盘)。\n控制器可能会保留旧块作为备用。\n\n继续？",
        "ft_lnk": "快捷方式 (.lnk) — 需要确认",
        "dont_ask_again": "不再询问",
        "dont_show_again": "不再显示",
        "search_placeholder": "搜索...",
    },
    "ja": {
        "confirm_lnk_title": "⚠ ショートカット (.lnk)",
        "confirm_lnk_text": "これはショートカット (.lnk) です。ショートカット自体のみが破壊されます。\n\nそれが指す対象ファイルはそのまま残ります。\n\n続行しますか？",
        "drive_remote_warning": "これはネットワークドライブです (\\\\サーバー\\共有)。\nセクターの上書きは破壊を保証しません — サーバーにスナップショット、重複排除、CoW がある可能性があります。\n\n続行しますか？",
        "drive_removable_warning": "これはリムーバブルドライブです (USB メモリ / 外付け HDD)。\nコントローラが古いブロックを予備として保持する場合があります。\n\n続行しますか？",
        "ft_lnk": "ショートカット (.lnk) — 確認が必要",
        "dont_ask_again": "今後確認しない",
        "dont_show_again": "今後表示しない",
        "search_placeholder": "検索...",
    },
    "hi": {
        "confirm_lnk_title": "⚠ शॉर्टकट (.lnk)",
        "confirm_lnk_text": "यह एक शॉर्टकट (.lnk) है। केवल शॉर्टकट ही नष्ट किया जाएगा।\n\nजिस लक्ष्य फ़ाइल की ओर यह इंगित करता है वह अक्षुण्ण रहेगी।\n\nजारी रखें?",
        "drive_remote_warning": "यह एक नेटवर्क ड्राइव है (\\\\सर्वर\\शेयर)।\nसेक्टर ओवरराइट विनाश की गारंटी नहीं देता — सर्वर पर स्नैपशॉट, डिडुप्लीकेशन या CoW हो सकते हैं।\n\nजारी रखें?",
        "drive_removable_warning": "यह एक हटाने योग्य ड्राइव है (USB स्टिक / बाहरी HDD)।\nनियंत्रक पुराने ब्लॉक आरक्षित रख सकता है।\n\nजारी रखें?",
        "ft_lnk": "शॉर्टकट (.lnk) — पुष्टि आवश्यक",
        "dont_ask_again": "दोबारा न पूछें",
        "dont_show_again": "दोबारा न दिखाएँ",
        "search_placeholder": "खोजें...",
    },
}


def main():
    updated = 0
    missing = 0

    for code, trans in TRANSLATIONS.items():
        path = os.path.join(LOCALES_DIR, f"{code}.json")
        if not os.path.isfile(path):
            print(f"  пропуск {code}.json — файла нет")
            missing += 1
            continue

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        strings = data.setdefault("strings", {})
        for key, value in trans.items():
            strings[key] = value

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        updated += 1

    print(f"✅ Обновлено языков: {updated}")
    if missing:
        print(f"⚠️  Пропущено: {missing}")


if __name__ == "__main__":
    main()