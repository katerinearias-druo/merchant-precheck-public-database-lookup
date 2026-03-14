"""Tests for NIT validator.

El validador siempre retorna el NIT base (sin digito de verificacion)
porque el RUES no acepta el DV.
"""

from app.services.nit_validator import compute_check_digit, validate_nit


class TestValidateNitFormats:
    """Acepta NIT con/sin DV, con/sin guion — siempre retorna solo la base."""

    def test_9_digits_no_dv(self):
        nit, errors = validate_nit("900123456")
        assert nit == "900123456"
        assert errors == []

    def test_with_hyphen_and_dv(self):
        nit, errors = validate_nit("900123456-1")
        assert nit == "900123456"
        assert errors == []

    def test_10_digits_no_hyphen(self):
        nit, errors = validate_nit("9001234561")
        assert nit == "900123456"
        assert errors == []

    def test_with_dots_and_hyphen(self):
        nit, errors = validate_nit("900.123.456-7")
        assert nit == "900123456"
        assert errors == []

    def test_with_dots_no_dv(self):
        nit, errors = validate_nit("900.123.456")
        assert nit == "900123456"
        assert errors == []

    def test_with_spaces(self):
        nit, errors = validate_nit(" 900 123 456 ")
        assert nit == "900123456"
        assert errors == []

    def test_known_nit_with_hyphen(self):
        nit, errors = validate_nit("860002964-8")
        assert nit == "860002964"
        assert errors == []

    def test_known_nit_no_hyphen_with_dv(self):
        nit, errors = validate_nit("8600029648")
        assert nit == "860002964"
        assert errors == []

    def test_known_nit_no_dv(self):
        nit, errors = validate_nit("860002964")
        assert nit == "860002964"
        assert errors == []

    def test_minimum_length(self):
        nit, errors = validate_nit("123456")
        assert nit == "123456"
        assert errors == []


class TestValidateNitErrors:
    def test_empty_nit(self):
        _, errors = validate_nit("")
        assert len(errors) == 1
        assert "vacio" in errors[0].lower()

    def test_non_numeric(self):
        _, errors = validate_nit("900ABC456")
        assert len(errors) == 1
        assert "no numericos" in errors[0].lower()

    def test_too_short(self):
        _, errors = validate_nit("12345")
        assert len(errors) == 1
        assert "longitud" in errors[0].lower()

    def test_too_long_base(self):
        _, errors = validate_nit("12345678901")
        assert len(errors) == 1
        assert "longitud" in errors[0].lower()

    def test_multi_digit_dv(self):
        _, errors = validate_nit("900123456-12")
        assert len(errors) == 1
        assert "digito de verificacion" in errors[0].lower()


class TestComputeCheckDigit:
    def test_known_nit_860002964(self):
        assert compute_check_digit("860002964") == 8

    def test_known_nit_900123456(self):
        result = compute_check_digit("900123456")
        assert 0 <= result <= 9

    def test_short_nit_padded(self):
        result = compute_check_digit("123456")
        assert 0 <= result <= 9

    def test_result_range(self):
        for nit in ["800000000", "900000000", "100000000", "860002964"]:
            dv = compute_check_digit(nit)
            assert 0 <= dv <= 9, f"DV for {nit} out of range: {dv}"
