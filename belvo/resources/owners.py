from typing import Dict, List, Union

from belvo.resources.base import Resource


class Owners(Resource):
    endpoint = "/api/owners/"

    def create(
        self,
        link: str,
        *,
        token: str = None,
        save_data: bool = True,
        raise_exception: bool = False,
        **kwargs: Dict,
    ) -> Union[List[Dict], Dict]:
        """Retrieve owners for a Link

        Retrieve owner information for a specific link.

        Example:

            ```python
            # Fetch owners for a Link
            owners = client.Owners.create("b91835f5-6f83-4d9b-a0ad-a5a249f18b7c")

            # Fetch owners for a Link with and timeout after 15 seconds
            owners = client.Owners.create(
                "b91835f5-6f83-4d9b-a0ad-a5a249f18b7c",
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
            Dict: The details of the object. For more information on the response from the API, see our [Owners API documentation](https://developers.belvo.com/reference/retrieveowners).
        """

        data = {"link": link, "save_data": save_data}

        if token:
            data.update(token=token)

        return self.session.post(
            self.endpoint, data=data, raise_exception=raise_exception, **kwargs
        )
