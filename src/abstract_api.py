from abc import ABC, abstractmethod
import requests
from typing import Dict, Any


class AbstractAPI(ABC):
    """Абстрактный класс для работы с API сервисов с вакансиями."""

    @abstractmethod
    def get_vacancies(self, search_query: str) -> list[Dict[str, Any]]:
        pass

    def _connect_to_api(self, url: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Приватный метод для подключения к API."""
        response = requests.get(url, params=params)
        if response.status_code != 200:
            raise Exception(f"Ошибка подключения к API: {response.status_code}")
        return response.json()
