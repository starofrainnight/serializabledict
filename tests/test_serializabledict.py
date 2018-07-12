#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `serializabledict` package."""

import pytest
import yaml
import simplejson as json
from click.testing import CliRunner
from serializabledict.storage import YamlFileStorage, JsonFileStorage
from serializabledict.storage.common import FileStorage
from serializabledict import SerializableDict
from typing import List


@pytest.fixture
def dicts() -> List[List]:
    storages = [
        (YamlFileStorage, "./test.yml"),
        (JsonFileStorage, "./test.json"),
    ]

    ret = []
    for item in storages:
        ret.append(SerializableDict(storage=item[0](item[1])))

    return ret


def test_if_wrote_to_file(dicts: List[List]):
    """Test if the data really wrote to file in realtime
    """

    special_value = 0x55aa
    for sdict in dicts:
        sdict["item"] = special_value

        with open(sdict.storage.path) as f:
            if isinstance(sdict.storage, YamlFileStorage):
                other_dict = yaml.safe_load(f)
            elif isinstance(sdict.storage, JsonFileStorage):
                other_dict = json.load(f)

        assert other_dict["item"] == special_value
