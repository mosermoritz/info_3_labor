import pytest
import shopping

@pytest.fixture()
def setup_warenkorb():
    warenkorb_instance = shopping.Warenkorb()
    yield warenkorb_instance
    del warenkorb_instance

@pytest.fixture()
def setup_article():
    artikel_instance = shopping.Artikel()
    yield artikel_instance
    del artikel_instance

@pytest.fixture()
def setup_discount():
    discount_instance = shopping.Discount()
    yield discount_instance
    del discount_instance

def test_instance(setup_warenkorb):
    assert isinstance(setup_warenkorb, shopping.Warenkorb)

def test_artikel(setup_article):
    artikel = setup_article
    artikel.add("Apfel", 20.0)
    assert artikel.get_price("Apfel") == 20.0

def test_add_warenkorb(setup_warenkorb, setup_article):
    artikel = setup_article
    artikel.add("Apfel", 20.0)
    setup_warenkorb.set_article(artikel)
    setup_warenkorb.add_Artikel("Apfel")
    assert setup_warenkorb.get_Inhalt() == {"Apfel": 1}

def test_get_summe_warenkorb(setup_warenkorb, setup_article):
    artikel = setup_article
    artikel.add("Apfel", 20.0)
    setup_warenkorb.set_article(artikel)
    setup_warenkorb.add_Artikel("Apfel")
    assert setup_warenkorb.get_Summe() == 20.0

def test_get_summe2_warenkorb(setup_warenkorb, setup_article):
    artikel = setup_article
    artikel.add("Apfel", 20.0)
    setup_warenkorb.set_article(artikel)
    setup_warenkorb.add_Artikel("Apfel", 2)
    assert setup_warenkorb.get_Summe() == 40.0

def test_add_discount_rule(setup_discount):
    discount = setup_discount
    discount.add_discountrule("Melanie20", 20)
    assert discount.get_amountofdiscountrule("Melanie20") == 20

def test_use_discount_rule(setup_warenkorb, setup_article, setup_discount):
    artikel = setup_article
    discount = setup_discount
    warenkorb = setup_warenkorb

    artikel.add("Apfel", 20.0)
    warenkorb.set_article(artikel)
    warenkorb.add_Artikel("Apfel", 3)
    discount.add_discountrule("Melanie30", 30)

    assert discount.use_discount("Melanie30", warenkorb) == 42.0

def test_exception_noprice(setup_article):
    artikel = setup_article
    with pytest.raises(ValueError):
        artikel.add("Apfel")
