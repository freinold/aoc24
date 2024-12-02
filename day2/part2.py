with open("input") as file:
    reports = list(
        map(lambda report: [int(val) for val in report.split()], file.readlines())
    )


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


n_safe_reports = 0

for report in reports:
    is_safe, index = is_report_safe(report)
    if is_safe:
        n_safe_reports += 1
        continue

    report_rm_index = report.copy()
    report_rm_index.pop(index)
    is_safe_rm_index, _ = is_report_safe(report_rm_index)
    if is_safe_rm_index:
        n_safe_reports += 1
        continue

    if index > 0:
        report_rm_before = report.copy()
        report_rm_before.pop(index - 1)
        is_safe_rm_before, _ = is_report_safe(report_rm_before)
        if is_safe_rm_before:
            n_safe_reports += 1
            continue

    report_rm_after = report.copy()
    report_rm_after.pop(index + 1)
    is_safe_rm_after, _ = is_report_safe(report_rm_after)
    if is_safe_rm_after:
        n_safe_reports += 1
    else:
        print(
            f"Deemed still unsafe:\n{report=}\n{report_rm_index=}\n{report_rm_after=}\n\n"
        )


print(f"Number of safe reports with dampener: {n_safe_reports}")
