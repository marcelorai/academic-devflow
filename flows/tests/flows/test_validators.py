from datetime import timedelta

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone

from flows.validators import validate_date_is_today_or_after


class DateIsTodayOrAfterValidator(TestCase):
    def test_data_anterior_causa_erro(self):
        "O validador não aceita uma data anterior a hoje"
        ontem = (timezone.now() - timedelta(days=1)).date()
        semana_anterior = (timezone.now() - timedelta(days=7)).date()
        mes_anterior = (timezone.now() - timedelta(weeks=4)).date()
        ano_anterior = (timezone.now() - timedelta(weeks=52)).date()

        self.assertRaises(
            ValidationError, validate_date_is_today_or_after, value=ontem)
        self.assertRaises(
            ValidationError, validate_date_is_today_or_after, value=semana_anterior)
        self.assertRaises(
            ValidationError, validate_date_is_today_or_after, value=mes_anterior)
        self.assertRaises(
            ValidationError, validate_date_is_today_or_after, value=ano_anterior)

    def test_data_posterior_nao_causa_erro(self):
        "O validador aceita uma data posterior a hoje"
        amanha = (timezone.now() + timedelta(days=1)).date()
        semana_posteior = (timezone.now() + timedelta(days=7)).date()
        mes_posterior = (timezone.now() + timedelta(weeks=4)).date()
        ano_posterior = (timezone.now() + timedelta(weeks=52)).date()

        self.assertIsNone(validate_date_is_today_or_after(amanha))
        self.assertIsNone(validate_date_is_today_or_after(semana_posteior))
        self.assertIsNone(validate_date_is_today_or_after(mes_posterior))
        self.assertIsNone(validate_date_is_today_or_after(ano_posterior))

    def test_data_atual_nao_causa_erro(self):
        "O validador aceita a data atual"
        hoje = timezone.now().date()

        self.assertIsNone(validate_date_is_today_or_after(hoje))
