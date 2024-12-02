with open("input") as file:
    reports = list(
        map(lambda report: [int(val) for val in report.split()], file.readlines())
    )

n_safe_reports = 0
bad_reports = list()


def is_report_safe(report: list[int]) -> tuple[bool, int]:
    previous_level: int = report[0]
    is_ascending: bool = report[0] < report[1]
    checked_index = 1
    for level in report[1:]:
        # Check ob Differenz > 3 oder Differenz == 0
        if abs(previous_level - level) > 3 or (level == previous_level):
            break

        # Check ob Differenz falls Werte aufsteigend ist zwischen 1 und 3 ist
        if is_ascending and (previous_level - level) in [1, 2, 3]:
            break

        # Check ob Differenz falls Werte absteigend sind zwischen -3 und -1 ist
        if (not is_ascending) and (previous_level - level) in [-1, -2, -3]:
            break

        # Falls kein Break previous auf aktuelles Element setzen und weiter iterieren
        previous_level = level
        checked_index += 1

    # Falls previous auf letztem Element => kein break => safe
    return len(report) == checked_index, checked_index - 1


for report in reports:
    is_safe, index = is_report_safe(report)
    if is_safe:
        n_safe_reports += 1
        continue

    rm_first_report = report.copy()
    rm_first_report.pop(index)
    is_safe_rm_first, _ = is_report_safe(rm_first_report)
    if is_safe_rm_first:
        n_safe_reports += 1
        continue

    rm_secound_report = report.copy()
    rm_secound_report.pop(index + 1)
    is_safe_rm_second, _ = is_report_safe(rm_secound_report)
    if is_safe_rm_second:
        n_safe_reports += 1


print(f"Number of safe reports with dampener: {n_safe_reports}")
