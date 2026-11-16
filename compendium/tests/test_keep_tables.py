"""Tests for keep_tables. Each test builds its own HTML."""
from keep_tables import body_rows, keep_small_tables


def table(rows, cls=' class="compact"'):
    body = "".join(f"<tr><td>{i}</td></tr>" for i in range(rows))
    return f"<table{cls}><thead><tr><th>H</th></tr></thead><tbody>{body}</tbody></table>"


def test_body_rows_does_not_count_the_head():
    assert body_rows(table(3)) == 3


def test_a_small_table_gets_the_class_and_keeps_its_old_class():
    out = keep_small_tables(table(4))
    assert out.startswith('<table class="compact keep">')


def test_a_large_table_does_not_change():
    t = table(11)
    assert keep_small_tables(t, max_rows=10) == t


def test_a_table_with_no_class_gets_one():
    assert keep_small_tables(table(2, cls="")).startswith('<table class="keep">')


def test_each_table_in_the_text_is_handled_alone():
    out = keep_small_tables("<p>a</p>" + table(2) + "<p>b</p>" + table(20), max_rows=10)
    assert out.count("keep") == 1


def test_a_bold_label_before_a_small_table_goes_into_one_kept_block():
    out = keep_small_tables("<p>Text.</p>\n<p><strong>Ranks</strong></p>\n" + table(3))
    assert out.startswith('<p>Text.</p>\n<div class="keep"><p><strong>Ranks</strong></p>')
    assert out.endswith("</table></div>")


def test_a_label_before_a_large_table_does_not_change():
    t = "<p><strong>Ranks</strong></p>" + table(20)
    assert keep_small_tables(t, max_rows=10) == t
