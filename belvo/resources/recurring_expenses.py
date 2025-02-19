from typing import Dict, List, Union

from belvo.resources.base import Resource


class RecurringExpenses(Resource):
    endpoint = "/api/recurring-expenses/"

    def create(
        self,
        link: str,
        *,
        token: str = None,
        save_data: bool = True,
        raise_exception: bool = False,
        **kwargs: Dict,
    ) -> Union[List[Dict], Dict]:
        """Retrieve recurring expenses for a link

        Retrieve recurring expense insights for checking and savings accounts from a specific link. You can receive insights for a period of up to 365 days, depending on the transaction history available for each bank.

        Example:
            ```python
            # Fetch recurring expenses for a Link
            recurring_expenses = client.RecurringExpenses.create("44d309dc-24c6-4734-99e0-22c595fee2c2")

            # Fetch recurring expenses for a Link with and timeout after 15 seconds
            recurring_expenses = client.RecurringExpenses.create(
                "44d309dc-24c6-4734-99e0-22c595fee2c2",
                timeout=15
            )
            ```

        Args:
            link (str): The `link.id` that you want to get information for (UUID).
            token (str, optional): The MFA token generated by the bank in order to access the institution. Defaults to None.
            encryption_key (str, optional): **Deprecated**.
            save_data (bool, optional): Indicates whether or not to persist the data in Belvo. Defaults to `True`.
            raise_exception (bool, optional): Indicates whether to raise an exception or return the API error. Defaults to `False`.

        Returns:
            Dict: The details of the object. For more information on the response from the API, see our [Recurring expenses API documentation](https://developers.belvo.com/reference/retrieverecurringexpenses).
        """

        data = {"link": link, "save_data": save_data}

        if token:
            data.update(token=token)

        return self.session.post(
            self.endpoint, data=data, raise_exception=raise_exception, **kwargs
        )
