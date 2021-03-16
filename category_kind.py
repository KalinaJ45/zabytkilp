# -*- coding: utf-8 -*-
from __future__ import annotations

from enum import Enum
from dataclasses import dataclass


@dataclass(frozen=True)
class CategoryKind:
    kategoria: str
    kod: str
    geometria: list
   

class CategoryKindEnum(Enum):
   
   
    ZABYTEK_NIERUCHOMY = CategoryKind(     
        kategoria = "zabytek nieruchomy",
        kod = "1",
        geometria = ['POLYGON', 'LINE', 'POINT'])
   
    ZABYTEK_ARCHEOLOGICZNY = CategoryKind(
        kategoria = "zabytek archeologiczny",
        kod = "2",
        geometria = ['POLYGON', 'LINE', 'POINT'])
   
    ZABYTEK_RUCHOMY = CategoryKind(
        kategoria = "zabytek ruchomy",
        kod = "3",
        geometria = ['POINT'],)

    OTOCZENIE_ZABYTKU = CategoryKind(
        kategoria = "otoczenie zabytku",
        kod = "4",
        geometria = ['POLYGON'])

    STREFA_OCHRONY_KONSERWATORSKIEJ = CategoryKind(
        kategoria = "strefa ochrony konserwatorskiej",
        kod = "5",
        geometria = ['POLYGON'])

    NAZWA_MIEJSCOWA = CategoryKind(
        kategoria = "nazwa miejscowa",
        kod = "6",
        geometria = ['POINT'],)



