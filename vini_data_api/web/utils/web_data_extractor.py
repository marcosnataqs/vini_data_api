from typing import Dict, List

import requests
from bs4 import BeautifulSoup


def web_data_extractor(url: str) -> List[Dict[str, str]]:
    extracted_data: List[Dict[str, str]] = []

    # Faz a requisição para a página
    response = requests.get(url)
    if response.status_code == 200:
        # Parseia o conteúdo HTML da resposta
        soup = BeautifulSoup(response.content, "html.parser")

        # Encontra a tabela na página
        table = soup.find("table", class_="tb_base tb_dados")
        if not table:
            print(f"Nenhuma tabela encontrada em {url}")
            return

        # Extrai os cabeçalhos da tabela
        headers = [header.text.strip() for header in table.find("thead").find_all("th")]

        # Inicializa uma lista para armazenar os dados
        table_data = []

        # Extrai as linhas da tabela
        for row in table.find("tbody").find_all("tr"):
            cols = row.find_all("td")
            if cols:
                cols = [ele.text.strip() for ele in cols]
                table_data.append(dict(zip(headers, cols)))

        extracted_data = table_data
    else:
        print(f"Erro ao acessar {url}")

    return extracted_data
