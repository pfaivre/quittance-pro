from pathlib import Path
import json
import sys

from py3o.template import Template

from culture import Culture
from datamodel import DataModel


def main():
    RESET = "\x1B[0m"
    CLREOL = "\x1B[K" # Needed to continue background color to the end of the line
    color = "\x1b[{bg};2;{red};{green};{blue}m"

    bg_blue = color.format(bg=48, red=1, green=0, blue=177)
    bg_black = color.format(bg=48, red=0, green=0, blue=0)
    bg_grey = color.format(bg=48, red=163, green=154, blue=162)
    fg_white = color.format(bg=38, red=255, green=255, blue=255)

    print(f"{fg_white}{bg_blue}{CLREOL}")
    print(f"          {bg_grey}╔══════════════════════════╗{bg_blue}{CLREOL}")
    print(f"          {bg_grey}║                          ║{bg_blue}{bg_black} {bg_blue}{CLREOL}")
    print(f"          {bg_grey}║    Quittance Pro 2023    ║{bg_blue}{bg_black} {bg_blue}{CLREOL}")
    print(f"          {bg_grey}║                          ║{bg_blue}{bg_black} {bg_blue}{CLREOL}")
    print(f"          {bg_grey}╚══════════════════════════╝{bg_blue}{bg_black} {bg_blue}{CLREOL}")
    print(f"           {bg_black}                            {bg_blue}{CLREOL}")
    print(f"{CLREOL}")
    print(f"        Copyright (c) 2023 Pierre Faivre{CLREOL}")
    print(f"{CLREOL}")

    try:
        culture = Culture("fr-FR")
        model_path = Path(f"models/tenancy_receipt_model_{culture.culture_code}.odt")
        if not model_path.exists():
            raise ValueError(f"model {model_path} not found")

        with open("data.json") as f:
            data = json.load(f)
    except FileNotFoundError as ex:
        print(f"Please provide the file {ex.filename}{CLREOL}", file=sys.stderr)
        print(f"{CLREOL}")
        print(f"{RESET}{CLREOL}")
        exit(1)
    except json.decoder.JSONDecodeError as ex:
        print(f"The file {f.name} is malformed: {ex}{CLREOL}", file=sys.stderr)
        print(f"{CLREOL}")
        print(f"{RESET}{CLREOL}")
        exit(1)
    except Exception as ex:
        print(f"Error: {ex}{CLREOL}", file=sys.stderr)
        print(f"{CLREOL}")
        print(f"{RESET}{CLREOL}")
        exit(1)

    try:
        d = DataModel(data, culture)
    except ValueError as ex:
        print("The file data.json contains errors:{CLREOL}")
        print(ex, file=sys.stderr)
        print(f"{CLREOL}")
        print(f"{RESET}{CLREOL}")
        exit(1)

    print(f"   Landlord............: {d.landlord.first_name} {d.landlord.last_name}{CLREOL}")
    print(f"   Tenant..............: {d.tenant.first_name} {d.tenant.last_name}{CLREOL}")
    print(f"{CLREOL}")
    print(f"   Tenancy.............: {d.tenancy.address_line1}{CLREOL}")
    if d.tenancy.address_line2:
        print(f"                         {d.tenancy.address_line2}{CLREOL}")
    print(f"{CLREOL}")
    print(f"   Selected culture....: {culture.culture_code} ({culture.culture_name}){CLREOL}")
    print(f"{CLREOL}")
    print(f"   Receipts............: {len(d.receipts)} periods{CLREOL}")
    for r in d.receipts:
        print(f"                         {d.receipt_summary(r)}{CLREOL}")
    print(f"{CLREOL}")

    print(f"   Editing receipts{CLREOL}", end="")

    for r in d.receipts:
        t = Template(
            template=model_path,
            outfile=culture.output_name_pattern.format(
                year=r.year,
                month=r.month) + ".odt"
        )
        data = dict(
            tenancy=d.tenancy,
            landlord=d.landlord,
            tenant=d.tenant,
            receipt=r)
        t.render(data)
        print(f".{CLREOL}", end="")

    print(f"{CLREOL}")
    print(f"   Done.{CLREOL}")
    print(f"{CLREOL}")
    print(f"{RESET}{CLREOL}")


if __name__ == "__main__":
    main()
