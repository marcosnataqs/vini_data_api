import pandas as pd
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
    
    def extract_history(self):
        url = "http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv"
        coll_names = ["col_A", "col_B"]
        list_2 = [str(i) for i in range(1970, 2023)]
        for item in list_2:
            coll_names.append(item)
        df = pd.read_csv(url, sep=";", names=coll_names)
        df.loc[6:8, 'col_A'] = ['vm_Tinto_f', 'vm_Rosado_f', 'vm_Branco_f']
        response = self.normalize_full_load(df)
        return response

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
    
    def normalize_full_load(self, dataframe):
        df = dataframe
        response = []
        sub_item = []
        item = {}

        for index, row in df.iterrows():
            if row['col_A'].isupper():
                if item and sub_item:
                    item["sub_category"] = sub_item
                    sub_item = []#reset sub-item list
                    item={}#reset item dict

                item = {"category": row['col_B'], "total_values": []}  # Create a new item dictionary for each category
                for year in range(1970, 2023):  # Iterate over years from 1970 to 2022
                    item["total_values"].append({year: row[str(year)]})
                response.append(item)
            else:
                sub = {"name": row['col_B'], "values": []}
                for year in range(1970, 2023):  # Iterate over years from 1970 to 2022
                    sub["values"].append({year: row[str(year)]})
                sub_item.append(sub)

        # Add the last item
        if item and sub_item:
            item["sub_category"] = sub_item
            response.append(item)

        return response
    
