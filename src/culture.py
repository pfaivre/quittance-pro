
class NumberSpelling:
    @staticmethod
    def spell_out_en_gb(number: float) -> str:
        # TODO implement spell_out_en_gb
        return str(number)

    @staticmethod
    def spell_out_en_us(number: float) -> str:
        # TODO implement spell_out_en_us
        return str(number)

    @staticmethod
    def spell_out_fr_fr(number: float) -> str:
        result = []

        # 0 -> 99
        # Yes, it is ugly and can be factorised, but France's french is messy.
        dizaines_unites = [
            "", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf",
            "dix", "onze", "douze", "treize", "quatorze", "quinze", "seize", "dix-sept", "dix-huit", "dix-neuf",
            "vingt", "vingt-et-un", "vingt-deux", "vingt-trois", "vingt-quatre",
                "vingt-cinq", "vingt-six", "vingt-sept", "vingt-huit", "vingt-neuf",
            "trente", "trente-et-un", "trente-deux", "trente-trois", "trente-quatre",
                "trente-cinq", "trente-six", "trente-sept", "trente-huit", "trente-neuf",
            "quarante", "quarante-et-un", "quarante-deux", "quarante-trois", "quarante-quatre",
                "quarante-cinq", "quarante-six", "quarante-sept", "quarante-huit", "quarante-neuf",
            "cinquante", "cinquante-et-un", "cinquante-deux", "cinquante-trois", "cinquante-quatre",
                "cinquante-cinq", "cinquante-six", "cinquante-sept", "cinquante-huit", "cinquante-neuf",
            "soixante", "soixante-et-un", "soixante-deux", "soixante-trois", "soixante-quatre",
                "soixante-cinq", "soixante-six", "soixante-sept", "soixante-huit", "soixante-neuf",
            "soixante-dix", "soixante-et-onze", "soixante-douze", "soixante-treize", "soixante-quatorze",
                "soixante-quinze", "soixante-seize", "soixante-dix-sept", "soixante-dix-huit", "soixante-dix-neuf",
            "quatre-vingts", "quatre-vingts-un", "quatre-vingts-deux", "quatre-vingts-trois", "quatre-vingts-quatre",
                "quatre-vingts-cinq", "quatre-vingts-six", "quatre-vingts-sept", "quatre-vingts-huit", "quatre-vingts-neuf",
            "quatre-vingt-dix", "quatre-vingt-onze", "quatre-vingt-douze", "quatre-vingt-treize", "quatre-vingt-quatorze",
                "quatre-vingt-quinze", "quatre-vingt-seize", "quatre-vingt-dix-sept", "quatre-vingt-dix-huit", "quatre-vingt-dix-neuf",
        ]

        # 1, 1'000, 1'000'000, 1'000'000'000, 1'000'000'000'000, etc.
        magnitudes = ["", "mille", "million", "milliard", "billion", "billiard", "trillion", "trilliard"]
        current_magnitude = 0

        int_part = str(int(number))

        # Special case, "zéro" is used alone only
        if int_part == "0":
            return "zéro"

        # Loop in each group of 3 digits from right to left
        while int_part:
            digits_1_2 = int(int_part[-2:])
            int_part = int_part[:-2]
            magnitude = magnitudes.pop(0)

            if digits_1_2:
                plural_letter = "s" if digits_1_2 > 1 and current_magnitude >= 2 else ""
                result = [magnitude + plural_letter] + result

            # Special case, we do not say "un-mille", but just "mille"
            if not (digits_1_2 == 1 and magnitude == "mille"):
                result = [dizaines_unites[digits_1_2]] + result

            if int_part:
                hundred = int(int_part[-1:])
                int_part = int_part[:-1]

                # Special case, we do not say "un-cent", but just "cent"
                if hundred == 1:
                    result = ["cent"] + result
                elif hundred > 1:
                    # Special case, cent varies only when it is not followed by a cardinal adjective
                    plural_letter = "s" if digits_1_2 == 0 else ""
                    result = [dizaines_unites[hundred], "cent" + plural_letter] + result

            current_magnitude += 1

        # TODO: add fractional part

        # Join everything with dashes according to the 1990 reform
        return "-".join(filter(None, result))


class Culture:
    """This class allows to adapt language elements for a given culture

    Example::

        culture = Culture("fr-FR")
        culture.month_names[2]  # "février"
        culture.spell_out(18)  # "dix-huit"

        culture = Culture("en-GB")
        culture.month_names[2]  # "February"
        culture.spell_out(18)  # "eighteen"
    """

    C_MONTH_NAMES = {
        "en-GB": [None, "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ],
        "en-US": [None, "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ],
        "fr-FR": [None, "janvier", "février", "mars", "avril", "mai", "juin",
            "juillet", "août", "septembre", "octobre", "novembre", "décembre"
        ],
    }

    C_CULTURE_NAMES = {
        "en-GB": "British English",
        "en-US": "American English",
        "fr-FR": "Français France",
    }

    C_OUTPUT_NAME_PATTERNS = {
        "en-GB": "{year}-{month:02d} Tenancy receipt",
        "en-US": "{year}-{month:02d} Tenancy receipt",
        "fr-FR": "{year}-{month:02d} Quittance de loyer",
    }

    C_PERIOD_STRINGS = {
        "en-GB": "from {start} to {end}",
        "en-US": "from {start} to {end}",
        "fr-FR": "du {start} au {end}",
    }

    C_DATE_FORMATS = {
        "en-GB": "{day} {month} {year}",
        "en-US": "{month} {day} {year}",
        "fr-FR": "{day} {month} {year}",
    }

    C_NUMBER_SPELLING_FUNCTIONS = {
        "en-GB": NumberSpelling.spell_out_en_gb,
        "en-US": NumberSpelling.spell_out_en_us,
        "fr-FR": NumberSpelling.spell_out_fr_fr,
    }

    CURRENCIES = {
        "EUR": ("euros",    "€", 1),
        "GBP": ("pounds",   "£", 0),
        "USD": ("dollars",  "$", 0),
    }
    """(full_name, symbol, symbol_after_amount)
    """

    def __init__(self, culture_code: str):
        self.culture_code = culture_code
        self.culture_name = Culture.C_CULTURE_NAMES[culture_code]

        self.month_names = Culture.C_MONTH_NAMES[culture_code]
        self.output_name_pattern = Culture.C_OUTPUT_NAME_PATTERNS[culture_code]
        self.period_string = Culture.C_PERIOD_STRINGS[culture_code]
        self.date_format = Culture.C_DATE_FORMATS[culture_code]
        self.number_spelling_function = Culture.C_NUMBER_SPELLING_FUNCTIONS[culture_code]

    def spell_out(self, number: float) -> str:
        """Spells out the number in words, depending on the current culture

        For instance in culture fr-FR, 180.5 will return
        cent-quatre-vingts-virgule-cinq

        Args:
            number: number to write down in letters
        """

        return self.number_spelling_function(number)

