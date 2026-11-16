"""Tests for the chapter numbers that build.py adds. Each test builds its own small HTML."""
import build


def heads(src):
    build.TOC.clear()
    return build.chapter_heads(src)


def test_chapters_get_numbers_in_order():
    out = heads('<h1 class="chapter">Alpha</h1><p>x</p><h1 class="chapter newpage">Beta</h1><h1 class="chapter">Gamma</h1>')
    assert out.index("Chapter 1</div>") < out.index(">Alpha</h1>")
    assert out.index("Chapter 2</div>") < out.index(">Beta</h1>") < out.index("Chapter 3</div>") < out.index(">Gamma</h1>")
    assert "Chapter 4" not in out
    assert [t[1] for t in build.TOC] == ["1. Alpha", "2. Beta", "3. Gamma"]


def test_an_unnumbered_chapter_gets_no_number_and_does_not_count():
    out = heads('<h1 class="chapter">Alpha</h1><h1 class="chapter" data-unnumbered>Sheet</h1><h1 class="chapter">Beta</h1>')
    assert [t[1] for t in build.TOC] == ["1. Alpha", "Sheet", "2. Beta"]
    assert out.count('class="ch-num"') == 2


def test_a_new_page_chapter_keeps_its_new_page():
    out = heads('<h1 class="chapter newpage">Alpha</h1>')
    assert 'class="ch-head newpage"' in out
