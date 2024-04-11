from typing import Any, List

from vini_data_api.web.api.vitivinicultura.extractions.base import BaseExtraction
from vini_data_api.web.api.vitivinicultura.schema import Processing, ProcessingResponse
from vini_data_api.web.utils.web_data_extractor import web_data_extractor


class ProcessingExtraction(BaseExtraction):
    def __init__(self) -> None:
        pass

    def extract(self, year: int) -> ProcessingResponse:
        # URLs das páginas para fazer a extração
        urls = [
            f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={year}&subopcao=subopt_01&opcao=opt_03",
            f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={year}&subopcao=subopt_02&opcao=opt_03",
            f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={year}&subopcao=subopt_03&opcao=opt_03",
            f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={year}&subopcao=subopt_04&opcao=opt_03",
        ]
        processings = []

        for url in urls:
            data = web_data_extractor(url)
            data = self.normalize(data, url)
            for row in data:
                product = row["product"]
                quantity = (
                    int(row["quantity"].replace(".", ""))
                    if row["quantity"] not in ["-", "*", "nd"]
                    else 0
                )
                type = row["type"]
                classification = row["classification"]
                processing = Processing(
                    product=product,
                    quantity=quantity,
                    type=type,
                    classification=classification,
                )
                processings.append(processing)

        return ProcessingResponse(processings=processings)

    def normalize(self, data: List[dict[str, str]], *args: Any) -> List[dict[str, str]]:
        url = args[0]
        flat_struct: List[dict[str, str]] = []
        current_principal_product = None

        for item in data:
            product = item["Cultivar"] if "Cultivar" in item else item["Sem definição"]
            if product.isupper():  # É um produto principal
                current_principal_product = product
            else:  # É um subproduto
                novo_item = {
                    "product": product,
                    "quantity": item["Quantidade (Kg)"],
                    "type": current_principal_product,
                    "classification": self.get_classification(url),
                }
                flat_struct.append(novo_item)

        return flat_struct

    def get_classification(self, url: str) -> str:
        sub_option = url.split("subopcao=")[1].split("&")[0]
        classifications = {
            "subopt_01": "Viníferas",
            "subopt_02": "Americanas e Híbridas",
            "subopt_03": "Uvas de mesa",
            "subopt_04": "Sem classificação",
        }
        return classifications[sub_option]
