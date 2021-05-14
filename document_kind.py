# -*- coding: utf-8 -*-
from __future__ import annotations

from enum import Enum
from dataclasses import dataclass


@dataclass(frozen=True)
class DocumentKind:
    rodzaj: str
   

class DokumentKindEnum(Enum):
   
    BRAK = DocumentKind(     
        rodzaj = "brak")

    BRAK_INFO = DocumentKind(     
        rodzaj = "brak informacji")

    EWIDENCJA_KONSERWATORSKA = DocumentKind(     
        rodzaj = "ewidencja konserwatorska")

    PLAN_ZAGOSPODAROWANIA = DocumentKind(     
        rodzaj = "miejscowy plan zagospodarwania przestrzennego")
        
    INNY = DocumentKind(     
        rodzaj = "inny")



