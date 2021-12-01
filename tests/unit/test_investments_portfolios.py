from unittest.mock import MagicMock

from belvo import resources


def test_investments_portfolios_create_token_if_given(api_session):
    investments_portfolios = resources.InvestmentsPortfolios(api_session)
    investments_portfolios.session.post = MagicMock()
    investments_portfolios.create("fake-link-uuid", token="fake-token")

    investments_portfolios.session.post.assert_called_with(
        "/investments/portfolios/",
        data={"link": "fake-link-uuid", "save_data": True, "token": "fake-token"},
        raise_exception=False,
    )


def test_investments_portfolios_resume(api_session):
    investments_portfolios = resources.InvestmentsPortfolios(api_session)
    investments_portfolios.session.patch = MagicMock()
    investments_portfolios.resume("fake-session", "fake-token")

    investments_portfolios.session.patch.assert_called_with(
        "/investments/portfolios/",
        data={"session": "fake-session", "token": "fake-token"},
        raise_exception=False,
    )
