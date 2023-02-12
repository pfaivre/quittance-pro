# Quittance Pro -**next**-

Specifications for the next version.

Highlighted features:
- Manages owners, buildings, properties, tenants and leases
- Supports multiple owners for a property
- All database in a single human-readable Json file
- Simple command line interface to manage everything
- Generates rent receipts

## Database format

The database is in a Json file:

<details>

<summary>data.json</summary>

```json
{
    "format_name": "quittance-pro",
    "format_version": "2023.0",

    "landlords": [
        {
            "id": 1,
            "first_name": "Alice",
            "last_name": "Shaone",
            "address_line1": "288 Campus Drive",
            "address_line2": "Stanford, CA 94305, United States",
        }
    ],
    "buildings": [
        {
            "id": 1,
            "name": "Opéra Garnier"
        }
    ],
    "properties": [
        {
            "id": 1,
            "building": 1,
            "address_line1": "1 Place de l'Opéra",
            "address_line2": "75009 Paris",
            "surface": 456.5,
            "rooms": 42,
            "number": 1,
            "owners": [1]
        }
    ],
    "tenants": [
        {
            "id": 1,
            "first_name": "Bob",
            "last_name": "Skein",
            "title": "M.",
            "address_line1": "41 Brattle St",
            "address_line2": "Cambridge, MA 02138, United States"
        }
    ],
    "leases": [
        {
            "tenant": 1,
            "property": 1,
            "periodicity": "monthly",
            "entry_date": "2022-12-15",
            "leaving_date": null,
            "rent_periods": [
                {
                    "start_date": "2022-12-15",
                    "end_date": "2022-12-31",
                    "rent_amount": 285,
                    "expanses": 50,
                    "payment_received": true,
                    "payment_date": "2022-12-06"
                },
                {
                    "start_date": "2023-01-01",
                    "end_date": "2023-01-31",
                    "rent_amount": 570,
                    "expanses": 100,
                    "payment_received": true,
                    "payment_date": "2023-01-03"
                },
                {
                    "start_date": "2023-02-01",
                    "end_date": "2023-02-28",
                    "rent_amount": 570,
                    "expanses": 100,
                    "payment_received": true,
                    "payment_date": "2023-02-02"
                }
            ]
        }
    ]
}

```

</details>

## Command line interface:

```
$ qpro summary

Properties:
╭────────────────────┬─────────────────────┐
│ Opéra Garnier      ┊ M. Bob Skein        │
│ 1 Place de l'Opéra ┊ Payments up to date │
│ 75009 Paris        ┊                     │
│ n° 1               ┊                     │
└────────────────────┴─────────────────────╯

```

```
$ qpro add property

Buildings: 1: "Opéra Garnier", 2: "Another one"
Building> 1

Property number within the building> 1

Address (line 1)> 1 Place de l'Opéra
Address (line 2)> 75009 Paris

Surface> 456.5

Rooms> 42

Landlords: 1: "Alice Shaone"
Owners> 1

New property:
    address:  1 Place de l'Opéra
              75009 Paris
    building: Opéra Garnier
    number:   1
    surface:  456.5 m²
    rooms:    42
    owners:   Alice Shaone

Is that correct? [yes, no] > yes
Property added!
```

```
$ qpro remove landlord

Landlords: 1: "Alice Shaone"
> 1

Warning, landlord "Alice Shaone" has 1 property, they will be removed from them.
continue? [yes, no] > yes

Alice Shaone has been removed.
```
