from typing import Any, List

from vini_data_api.web.api.vitivinicultura.extractions.base import BaseExtraction
from vini_data_api.web.api.vitivinicultura.schema import Production, ProductionResponse
from vini_data_api.web.utils.web_data_extractor import web_data_extractor


class ProductionExtraction(BaseExtraction):
    def __init__(self) -> None:
        pass

    def extract(self, year: int) -> ProductionResponse:
        # URLs das páginas para fazer a extração
        urls = [
            f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={year}&opcao=opt_02",
        ]
        productions = []

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
                production = Production(product=product, quantity=quantity, type=type)
                productions.append(production)

        return ProductionResponse(productions=productions)

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
