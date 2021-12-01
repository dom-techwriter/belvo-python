from unittest.mock import MagicMock

from freezegun import freeze_time

from belvo import resources


@freeze_time("2019-02-28T12:00:00Z")
def test_investments_transactions_create_sets_current_time_if_no_date_given(api_session):
    investments_transactions = resources.InvestmentsTransactions(api_session)
    investments_transactions.session.post = MagicMock()
    investments_transactions.create("fake-link-uuid", "2019-01-01", save_data=False)

    investments_transactions.session.post.assert_called_with(
        "/investments/transactions/",
        data={
            "link": "fake-link-uuid",
            "date_from": "2019-01-01",
            "date_to": "2019-02-28",
            "save_data": False,
        },
        raise_exception=False,
    )


def test_investments_transactions_create_sends_token_if_given(api_session):
    investments_transactions = resources.InvestmentsTransactions(api_session)
    investments_transactions.session.post = MagicMock()
    investments_transactions.create(
        "fake-link-uuid", "2019-01-01", date_to="2019-02-28", token="fake-token"
    )

    investments_transactions.session.post.assert_called_with(
        "/investments/transactions/",
        data={
            "link": "fake-link-uuid",
            "date_from": "2019-01-01",
            "date_to": "2019-02-28",
            "save_data": True,
            "token": "fake-token",
        },
        raise_exception=False,
    )
