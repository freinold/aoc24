with open("input") as file:
    reports = list(map(lambda report: [int(val) for val in report.split()], file.readlines()))

n_safe_reports = 0

for report in reports:
    previous_level: int = report[0]
    is_ascending: bool = report[0] < report[1]
    seen_elems = 1
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
        seen_elems += 1

    # Falls previous auf letztem Element => kein break => safe
    if len(report) == seen_elems:
        print(report)
        n_safe_reports += 1

print(f"Number of safe reports: {n_safe_reports}")
