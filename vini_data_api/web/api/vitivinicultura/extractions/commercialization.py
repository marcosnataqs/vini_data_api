from typing import Any, List

from vini_data_api.web.api.vitivinicultura.extractions.base import BaseExtraction
from vini_data_api.web.api.vitivinicultura.schema import (
    Commercialization,
    CommercializationResponse,
)
from vini_data_api.web.utils.web_data_extractor import web_data_extractor


class CommercializationExtraction(BaseExtraction):
    def __init__(self) -> None:
        pass

    def extract(self, year: int) -> CommercializationResponse:
        # URLs das páginas para fazer a extração
        urls = [f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={year}&opcao=opt_04"]
        commercializations = []

        for url in urls:
            data = web_data_extractor(url)
            data = self.normalize(data)
            for row in data:
                product = row["product"]
                quantity = (
                    int(row["quantity"].replace(".", ""))
                    if row["quantity"] not in ["-", "*"]
                    else 0
                )
                type = row["type"]
                commercialization = Commercialization(
                    product=product,
                    quantity=quantity,
                    type=type,
                )
                commercializations.append(commercialization)

        return CommercializationResponse(commercializations=commercializations)

    def normalize(self, data: List[dict[str, str]], *args: Any) -> List[dict[str, str]]:
        flat_struct: List[dict[str, str]] = []
        current_principal_product = None

        for item in data:
            if item["Produto"].isupper():  # É um produto principal
                current_principal_product = item["Produto"]
            else:  # É um subproduto
                novo_item = {
                    "product": item["Produto"],
                    "quantity": item["Quantidade (L.)"],
                    "type": current_principal_product,
                }
                flat_struct.append(novo_item)

        return flat_struct
