from typing import Dict, List, Union

from belvo.resources.base import Resource


class TaxComplianceStatus(Resource):
    endpoint = "/api/tax-compliance-status/"

    def create(
        self,
        link: str,
        *,
        attach_pdf: bool = False,
        save_data: bool = True,
        raise_exception: bool = False,
        **kwargs: Dict,
    ) -> Union[List[Dict], Dict]:
        """Retrieve a tax compliance status for a link

        Example:
        ```python
        # Fetch tax compliance status for a Link
        tax_compliance_status = client.TaxComplianceStatus.create(
            "b91835f5-6f83-4d9b-a0ad-a5a249f18b7c"
        )

        # Fetch tax compliance status for a Link and retrieve its pdf
        tax_compliance_status = client.TaxComplianceStatus.create(
            "b91835f5-6f83-4d9b-a0ad-a5a249f18b7c",
            attach_pdf=True
        )
        ```

        Args:
            link (str): The fiscal `link.id` that you want to get information for (UUID).
            attach_pdf (bool, optional): When set to `True`, you will receive the PDF in binary format in the response. Defaults to `False`.
            save_data (bool, optional): Indicates whether or not to persist the data in Belvo. Defaults to `True`.
            raise_exception (bool, optional): Indicates whether to raise an exception or return the API error. Defaults to `False`.

        Returns:
            Dict: The details of the object. For more information on the response from the API, see our [Tax compliance status API documentation](https://developers.belvo.com/reference/retrievetaxcompliancestatus).
        """

        data = {"link": link, "attach_pdf": attach_pdf, "save_data": save_data}

        return self.session.post(
            self.endpoint, data=data, raise_exception=raise_exception, **kwargs
        )

    def resume(
        self,
        session: str,
        token: str,
        *,
        link: str = None,
        raise_exception: bool = False,
        **kwargs: Dict,
    ) -> Dict:
        raise NotImplementedError()
