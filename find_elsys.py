import subprocess

DIR = '/home/alan/gdrive/AHFC/BMON_FY21_onward/lora/elsys'

def find_elsys_device(dev_eui_substring: str):
    """Displays the key ID values for an Elsys LoRaWAN sensor.
     Assumes the Elsys order CSV files are present in a common directory.
    """
    cmd = [
        "grep",
        "-Rni",        # -R recursive, -n show line numbers, -i case-insensitive (optional)
        "--include=*.csv",
        dev_eui_substring,
        DIR
    ]

    result = subprocess.run(cmd, capture_output=True, text=True).stdout
    rows = []
    for line in result.splitlines():
        # Format from grep: filepath:lineno:line_text
        parts = line.split(":", 2)
        if len(parts) == 3:
            filepath, lineno, raw_line = parts
            filename = filepath.split('/')[-1]
            flds = raw_line.split(';')
            row = {
                'device': flds[0],
                'dev_eui': flds[1],
                'app_eui': flds[2],
                'app_key': flds[3],
                'filename': filename
                }
            if dev_eui_substring.lower() in row['dev_eui'].lower():
                rows.append(row)

    return rows
