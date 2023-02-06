import datetime
from calendar import monthrange

from culture import Culture


class Item(object):
    pass


class DataModel:
    def __init__(self, model_dict: dict, culture: Culture):
        self.culture = culture

        try:
            self._extract_dict(model_dict, culture)
        except KeyError as ex:
            raise ValueError(f"Missing {ex} from input data")

    def _extract_dict(self, model_dict: dict, culture: Culture):
        # TODO: revamp how the validation is made:
        # * use Json schema
        # * first extract fields (allowing for missing values), then assert their presence

        t = model_dict["tenancy"]
        self.tenancy = Item()
        self.tenancy.address_line1 = t["address_line1"]
        self.tenancy.address_line2 = t["address_line2"]
        currency_info = Culture.CURRENCIES[t["currency"]]
        self.tenancy.currency = currency_info[0]
        self.tenancy.currency_symbol = currency_info[1]
        # TODO: put the symbol before or after depending on the currency

        l = model_dict["landlord"]
        self.landlord = Item()
        self.landlord.first_name = l["first_name"]
        self.landlord.last_name = l["last_name"]
        self.landlord.address_line1 = l["address_line1"]
        self.landlord.address_line2 = l["address_line2"]
        self.landlord.editing_city = l["editing_city"]

        t = model_dict["tenant"]
        self.tenant = Item()
        self.tenant.first_name = t["first_name"]
        self.tenant.last_name = t["last_name"]
        self.tenant.title = t["title"]
        self.tenant.address_line1 = t["address_line1"]
        self.tenant.address_line2 = t["address_line2"]

        self.receipts = list()
        for r in model_dict["receipts"]:
            self._validate_receipt(r)

            receipt = Item()
            receipt.year = r["year"]
            receipt.month = r["month"]
            receipt.month_name = culture.month_names[r["month"]]
            receipt.start_day = r["start_day"]
            receipt.end_day = r["end_day"]
            receipt.period = culture.period_string.format(
                start=receipt.start_day,
                end=receipt.end_day) + f" {receipt.month_name}"
            receipt.rent = r["rent"]
            receipt.expanses = r["expanses"]
            receipt.total = receipt.rent + receipt.expanses
            receipt.totalspelledout = culture.number_spelling_function(receipt.total)
            payment_date = datetime.date.fromisoformat(r["payment_date"])
            receipt.payment_date = culture.date_format.format(
                day=payment_date.day,
                month=culture.month_names[payment_date.month],
                year=payment_date.year
            )
            today = datetime.date.today()
            receipt.editing_date = culture.date_format.format(
                day=today.day,
                month=culture.month_names[today.month],
                year=today.year
            )
            self.receipts.append(receipt)

    def _validate_receipt(self, receipt: dict):
        if not 1 <= receipt["month"] <= 12:
            raise ValueError(f"Invalid month number '{receipt['month']}'")

        if receipt["start_day"] < 0:
            raise ValueError(f"Start day must be positive")

        if receipt["start_day"] > receipt["end_day"]:
            raise ValueError(f"Start day must be lower than end day")

        last_day = monthrange(receipt["year"], receipt["month"])[1]
        if receipt["end_day"] > last_day:
            raise ValueError(f"Last day of {receipt['year']}-{receipt['month']} is {last_day}")

        if receipt["rent"] < 0:
            raise ValueError(f"Rent amount must be positive or null")

        if receipt["expanses"] < 0:
            raise ValueError(f"Expanses amount must be positive or null")

    def receipt_summary(self, r: Item):
        c = self.culture

        # Example: "1-31 décembre 2022: 620 €"
        return f"{r.start_day}-{r.end_day} {c.month_names[r.month]} {r.year}: {r.rent+r.expanses} {self.tenancy.currency_symbol}"
