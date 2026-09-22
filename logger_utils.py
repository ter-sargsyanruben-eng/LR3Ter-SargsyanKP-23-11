from pathlib import Path


def write_log(summary, rows, log_path):
    path = Path(log_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    violations = [row for row in rows if row["Избыточный"] == "Да"]
    with path.open("a", encoding="utf-8") as log:
        log.write(f"[{summary['Время проверки']}] {summary['Результат']}\n")
        log.write(
            f"Запущено: {summary['Всего запущено']}; "
            f"избыточных: {summary['Избыточных']}; "
            f"доля: {summary['Доля избыточных, %']}%\n"
        )
        if violations:
            for item in violations:
                log.write(
                    f"- {item['Контейнер']}: {item['Тип нарушения']}\n"
                )
        else:
            log.write("- Нарушений не обнаружено\n")
        log.write("\n")
