# -*- coding: utf-8 -*-
from __future__ import annotations

from enum import Enum
from dataclasses import dataclass


@dataclass(frozen=True)
class DocumentKind:
    """Examines the class DokumentKindEnum to find fields. 
    """
    code: str
    type: str


class DokumentKindEnum(Enum):
    """Enum Class consist of kind of momument protecion documents as members.
    """
    EWIDENCJA_KONSERWATORSKA = DocumentKind(
        code='1',
        type="ewidencja konserwatorska")

    REJESTR_ZABYTKÓW = DocumentKind(
        code='2',
        type="rejestr zabytków")

    PLAN_ZAGOSPODAROWANIA = DocumentKind(
        code='3',
        type="miejscowy plan zagospodarwania przestrzennego")

    BRAK_INFO = DocumentKind(
        code='4',
        type="brak informacji")

    BRAK = DocumentKind(
        code='5',
        type="brak")

    INNY = DocumentKind(
        code='6',
        type="inny")
