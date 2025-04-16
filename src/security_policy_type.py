""" модуль описания типа политики безопасности """

from dataclasses import dataclass
from typing import Any


@dataclass
class SecurityPolicy:
    """ политика безопасности """
    source: str         # отправитель запроса
    destination: str    # получатель
    operation: str      # запрашиваемая операция
    key: Any            # ключ шифрования
