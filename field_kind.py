# -*- coding: utf-8 -*-
from __future__ import annotations

from enum import Enum
from dataclasses import dataclass


@dataclass(frozen=False)
class FieldKind:
    """Examines the class FieldKindEnum to find fields. 
    """
    index: int
    field_name: str
    alias_field: str
    long_field: int
    widget_type: str
    not_null: bool


class FieldKindEnum(Enum):
    """Enum Class consist of created layer fields  as members.
    """
    IN_ID = FieldKind(
        index=0,
        field_name='IN_ID',
        alias_field="INSPIRE_ID",
        long_field=100,
        widget_type='String',
        not_null=True,
    )

    NAZWA = FieldKind(
        index=1,
        field_name='NAZWA',
        alias_field="Nazwa obiektu",
        long_field=100,
        widget_type='String',
        not_null=True,
    )
    KATEG = FieldKind(
        index=2,
        field_name='KATEG',
        alias_field="kategoria obiektu",
        long_field=50,
        widget_type='ValueMap',
        not_null=True,
    )
    FUNKCJA = FieldKind(
        index=3,
        field_name='FUNKCJA',
        alias_field="funkcja obiektu",
        long_field=50,
        widget_type='ValueRelation',
        not_null=True,

    )
    CZY_ZESP = FieldKind(
        index=4,
        field_name='CZY_ZESP',
        alias_field="Czy obiekt stanowi część zespołu?",
        long_field=3,
        widget_type='CheckBox',
        not_null=True,
    )
    DATOW = FieldKind(
        index=5,
        field_name='DATOW',
        alias_field="Datowanie obiektu",
        long_field=50,
        widget_type='String',
        not_null=True,
    )
    RODZ_DOKUM = FieldKind(
        index=6,
        field_name='RODZ_DOKUM',
        alias_field="Rodzaj dokumentów dotyczących ewentualnej ochrony",
        long_field=50,
        widget_type='ValueMap',
        not_null=True,
    )

    DOK = FieldKind(
        index=7,
        field_name='DOK',
        alias_field="Dokumenty dotyczące ewentualnej ochrony",
        long_field=254,
        widget_type='Srting',
        not_null=False,
    )
    CZY_DZIER = FieldKind(
        index=8,
        field_name='CZY_WYDZ',
        alias_field="Czy obiekt jest wydzierżawiony?",
        long_field=3,
        widget_type='CheckBox',
        not_null=True,
    )
    CZY_DOST = FieldKind(
        index=9,
        field_name='CZY_DOST',
        alias_field="Czy obiekt jest dostępny do zwiedzania?",
        long_field=3,
        widget_type='CheckBox',
        not_null=True,
    )
    UWAGI = FieldKind(
        index=10,
        field_name='UWAGI',
        alias_field="Uwagi",
        long_field=254,
        widget_type='String',
        not_null=False,
    )
