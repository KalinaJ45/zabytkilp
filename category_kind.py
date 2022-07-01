# -*- coding: utf-8 -*-
from __future__ import annotations
import code

from enum import Enum
from dataclasses import dataclass


@dataclass(frozen=True)
class CategoryKind:
    """Examines the class CategoryKindEnum to find fields. 
    """
    category: str
    code: str
    geometry: list


class CategoryKindEnum(Enum):
    """Enum Class consist of kind of monuments categories as members.
    """
    ZABYTEK_NIERUCHOMY = CategoryKind(
        category="zabytek nieruchomy",
        code='1',
        geometry=['POLYGON', 'LINE', 'POINT'])

    ZABYTEK_ARCHEOLOGICZNY = CategoryKind(
        category="zabytek archeologiczny",
        code='2',
        geometry=['POLYGON', 'LINE', 'POINT'])

    ZABYTEK_RUCHOMY = CategoryKind(
        category="zabytek ruchomy",
        code='3',
        geometry=['POINT'],)

    OTOCZENIE_ZABYTKU = CategoryKind(
        category="otoczenie zabytku",
        code='4',
        geometry=['POLYGON'])

    STREFA_OCHRONY_KONSERWATORSKIEJ = CategoryKind(
        category="strefa ochrony konserwatorskiej",
        code='5',
        geometry=['POLYGON'])

    NAZWA_MIEJSCOWA = CategoryKind(
        category="nazwa miejscowa",
        code='6',
        geometry=['POINT'],)
