from spotify_dl.utils import sanitize


def test_sanitize_flename():
    name = sanitize("Dank: Tunes<> $ V The* Dranks |Strike Back/")
    assert name == "Dank Tunes  V The Dranks Strike Back"

    name2 = sanitize('Dank: Tunes<> $ V " The* Dra?nks |Strike Back/', "#")
    assert name2 == "Dank# Tunes## # V # The# Dra#nks #Strike Back#"
