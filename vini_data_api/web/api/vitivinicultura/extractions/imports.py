from typing import Any, List

from vini_data_api.web.api.vitivinicultura.extractions.base import BaseExtraction
from vini_data_api.web.api.vitivinicultura.schema import Import, ImportResponse
from vini_data_api.web.utils.web_data_extractor import web_data_extractor


class ImportExtraction(BaseExtraction):
    def __init__(self) -> None:
        pass

    def extract(self, year: int) -> ImportResponse:
        # URLs das páginas para fazer a extração
        urls = [
            f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={year}&subopcao=subopt_01&opcao=opt_05",
            f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={year}&subopcao=subopt_02&opcao=opt_05",
            f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={year}&subopcao=subopt_03&opcao=opt_05",
            f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={year}&subopcao=subopt_04&opcao=opt_05",
            f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={year}&subopcao=subopt_05&opcao=opt_05",
        ]
        imports = []

        for url in urls:
            data = web_data_extractor(url)
            for row in data:
                country = row["Países"]
                quantity = (
                    int(row["Quantidade (Kg)"].replace(".", ""))
                    if row["Quantidade (Kg)"] not in ["-", "*", "nd"]
                    else 0
                )
                value = (
                    float(row["Valor (US$)"].replace(".", "").replace(",", "."))
                    if row["Valor (US$)"] not in ["-", "*", "nd"]
                    else 0.0
                )
                classification = self.get_classification(url)
                importItem = Import(
                    country=country,
                    quantity=quantity,
                    value=value,
                    classification=classification,
                )
                imports.append(importItem)

        return ImportResponse(imports=imports)

    def normalize(self, data: List[dict[str, str]], *args: Any) -> List[dict[str, str]]:
        pass

    def get_classification(self, url: str) -> str:
        sub_option = url.split("subopcao=")[1].split("&")[0]
        classifications = {
            "subopt_01": "Vinhos de mesa",
            "subopt_02": "Espumantes",
            "subopt_03": "Uvas frescas",
            "subopt_04": "Uvas passas",
            "subopt_05": "Suco de uva",
        }
        return classifications[sub_option]
