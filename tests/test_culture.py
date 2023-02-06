from unittest import TestCase

from src.culture import Culture, NumberSpelling


class TestNumberSpelling(TestCase):

    def setUp(self):
        pass

    def test_spell_out_en_gb(self):
        pass

    def test_spell_out_en_us(self):
        pass

    def test_spell_out_fr_fr(self):
        self.assertEqual(NumberSpelling.spell_out_fr_fr(
            0),
            "zéro")
        # self.assertEqual(NumberSpelling.spell_out_fr_fr(
        #     0.5),
        #     "zéro-virgule-cinq")
        # self.assertEqual(NumberSpelling.spell_out_fr_fr(
        #     1.3456),
        #     "un-virgule-trois-mille-quatre-cent-cinquante-six")
        # self.assertEqual(NumberSpelling.spell_out_fr_fr(
        #     1.0001),
        #     "un-virgule-zéro-zéro-zéro-un")
        self.assertEqual(NumberSpelling.spell_out_fr_fr(
            16),
            "seize")
        self.assertEqual(NumberSpelling.spell_out_fr_fr(
            17),
            "dix-sept")
        self.assertEqual(NumberSpelling.spell_out_fr_fr(
            21),
            "vingt-et-un")
        self.assertEqual(NumberSpelling.spell_out_fr_fr(
            29),
            "vingt-neuf")
        self.assertEqual(NumberSpelling.spell_out_fr_fr(
            61),
            "soixante-et-un")
        self.assertEqual(NumberSpelling.spell_out_fr_fr(
            71),
            "soixante-et-onze")
        self.assertEqual(NumberSpelling.spell_out_fr_fr(
            75),
            "soixante-quinze")
        self.assertEqual(NumberSpelling.spell_out_fr_fr(
            81),
            "quatre-vingts-un")
        self.assertEqual(NumberSpelling.spell_out_fr_fr(
            100),
            "cent")
        self.assertEqual(NumberSpelling.spell_out_fr_fr(
            105),
            "cent-cinq")
        self.assertEqual(NumberSpelling.spell_out_fr_fr(
            112),
            "cent-douze")
        self.assertEqual(NumberSpelling.spell_out_fr_fr(
            200),
            "deux-cents")
        self.assertEqual(NumberSpelling.spell_out_fr_fr(
            596),
            "cinq-cent-quatre-vingt-seize")
        self.assertEqual(NumberSpelling.spell_out_fr_fr(
            999),
            "neuf-cent-quatre-vingt-dix-neuf")
        self.assertEqual(NumberSpelling.spell_out_fr_fr(
            1000),
            "mille")
        self.assertEqual(NumberSpelling.spell_out_fr_fr(
            1812),
            "mille-huit-cent-douze")
        self.assertEqual(NumberSpelling.spell_out_fr_fr(
            2000),
            "deux-mille")
        self.assertEqual(NumberSpelling.spell_out_fr_fr(
            12000),
            "douze-mille")
        self.assertEqual(NumberSpelling.spell_out_fr_fr(
            12400),
            "douze-mille-quatre-cents")
        self.assertEqual(NumberSpelling.spell_out_fr_fr(
            1000000),
            "un-million")
        self.assertEqual(NumberSpelling.spell_out_fr_fr(
            9999999),
            "neuf-millions-neuf-cent-quatre-vingt-dix-neuf-mille-neuf-cent-quatre-vingt-dix-neuf")
        self.assertEqual(NumberSpelling.spell_out_fr_fr(
            1000000000),
            "un-milliard")
        self.assertEqual(NumberSpelling.spell_out_fr_fr(
            1000000001),
            "un-milliard-un")
        self.assertEqual(NumberSpelling.spell_out_fr_fr(
            1020000000),
            "un-milliard-vingt-millions")
        self.assertEqual(NumberSpelling.spell_out_fr_fr(
            9999999999),
            "neuf-milliards-neuf-cent-quatre-vingt-dix-neuf-millions-neuf-cent-quatre-vingt-dix-neuf-mille-neuf-cent-quatre-vingt-dix-neuf")
        self.assertEqual(NumberSpelling.spell_out_fr_fr(
            1000000000000),
            "un-billion")
        self.assertEqual(NumberSpelling.spell_out_fr_fr(
            1000000000000000),
            "un-billiard")
        self.assertEqual(NumberSpelling.spell_out_fr_fr(
            1000000000000000000),
            "un-trillion")
        self.assertEqual(NumberSpelling.spell_out_fr_fr(
            1000000000000000000000),
            "un-trilliard")


class TestCulture(TestCase):

    def setUp(self):
        pass

    def test___init__(self):
        c = Culture("fr-FR")
        self.assertEqual("fr-FR", c.culture_code)
        self.assertEqual(NumberSpelling.spell_out_fr_fr, c.number_spelling_function)

