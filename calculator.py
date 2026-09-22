import json
from pathlib import Path
from datetime import datetime


def load_json(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def analyze_containers(config_path="config.json", running_path="running_containers.json"):
    config = load_json(config_path)
    running_data = load_json(running_path)

    allowed = set(config["allowed_containers"])
    outdated = set(config["outdated_containers"])
    running = running_data["running_containers"]

    rows = []
    for name in running:
        if name in outdated:
            status = "Устаревший компонент"
            violation_type = "компонент устаревшей задачи"
            is_redundant = True
        elif name not in allowed:
            status = "Неразрешенный компонент"
            violation_type = "неразрешенный компонент"
            is_redundant = True
        else:
            status = "Разрешенный компонент"
            violation_type = "нет"
            is_redundant = False

        rows.append({
            "Контейнер": name,
            "Статус": status,
            "Тип нарушения": violation_type,
            "Избыточный": "Да" if is_redundant else "Нет",
        })

    redundant_count = sum(1 for row in rows if row["Избыточный"] == "Да")
    total_count = len(rows)
    redundancy_percent = round((redundant_count / total_count * 100), 2) if total_count else 0.0

    summary = {
        "Время проверки": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Всего запущено": total_count,
        "Разрешенных": total_count - redundant_count,
        "Избыточных": redundant_count,
        "Доля избыточных, %": redundancy_percent,
        "Результат": "Обнаружена системная избыточность" if redundant_count else "Нарушений нет",
    }

    return rows, summary, config
