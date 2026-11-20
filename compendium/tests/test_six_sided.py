from six_sided import convert, add_brackets, check_dice

def test_convert():
    assert convert("1d8 + 3") == "d6 + 4"
    assert convert("2d8+3") == "2d6 + 5"
    assert convert("4d8 − 4") == "4d6"
    assert convert("1d4") == "d6 − 1"
    assert convert("2d10") == "2d6 + 4"
    assert convert("1d12 + 1") == "d6 + 4"
    assert convert("1d8 + 1d6 + 2") == "2d6 + 3"
    assert convert("1d20") == "3d6"
    assert convert("2d6 + 1") is None

def test_add_brackets():
    assert add_brackets("<p>Hit: 7 (1d8 + 3) Slashing</p>") == "<p>Hit: 7 (1d8 + 3) [d6 + 4] Slashing</p>"
    once = add_brackets("<p>2 (1d4) Cold</p>")
    assert add_brackets(once) == once
    assert add_brackets("<p>(2d6) Fire</p>") == "<p>(2d6) Fire</p>"
    assert add_brackets('<p title="(1d8)">Recharge 5–6</p>') == '<p title="(1d8)">Recharge 5–6</p>'

def test_check_dice():
    assert check_dice("| d66 | Event |") == []
    assert len(check_dice("| d20 | Event |")) == 1
    assert len(check_dice("Roll a d100.")) == 1
