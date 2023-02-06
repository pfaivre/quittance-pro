import json
import sys

from py3o.template import Template

from culture import Culture
from datamodel import DataModel


def main():
    print()
    print("          ╔══════════════════════════╗")
    print("          ║                          ║")
    print("          ║    Quittance Pro 2023    ║")
    print("          ║                          ║")
    print("          ╚══════════════════════════╝")
    print()
    print("        Copyright (c) 2023 Pierre Faivre")
    print()

    culture = Culture("fr-FR")
    model_path = f"models/tenancy_receipt_model_{culture.culture_code}.odt"

    try:
        with open("data.json") as f:
            data = json.load(f)
    except FileNotFoundError as ex:
        print(f"Please provide the file {ex.filename}", file=sys.stderr)
        print()
        exit(1)
    except json.decoder.JSONDecodeError as ex:
        print(f"The file {f.name} is malformed: {ex}", file=sys.stderr)
        print()
        exit(1)

    try:
        d = DataModel(data, culture)
    except ValueError as ex:
        print("The file data.json contains errors:")
        print(ex, file=sys.stderr)
        print()
        exit(1)

    print(f"   Landlord............: {d.landlord.first_name} {d.landlord.last_name}")
    print(f"   Tenant..............: {d.tenant.first_name} {d.tenant.last_name}")
    print()
    print(f"   Tenancy.............: {d.tenancy.address_line1}")
    if d.tenancy.address_line2:
        print(f"                         {d.tenancy.address_line2}")
    print()
    print(f"   Selected culture....: {culture.culture_code} ({culture.culture_name})")
    print()
    print(f"   Receipts............: {len(d.receipts)} terms")
    for r in d.receipts:
        print(f"                         {d.receipt_summary(r)}")
    print()

    print("   Editing receipts", end="")

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
        print(".", end="")

    print()
    print("   Done.")
    print()


if __name__ == "__main__":
    main()
