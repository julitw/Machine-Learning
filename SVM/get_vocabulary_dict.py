#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
import numpy as np
from typing import Dict


def get_vocabulary_dict(dict_path) -> Dict[int, str]:
    """Read the fixed vocabulary list from the datafile and return.

    :return: a dictionary of words mapped to their indexes
    """

    # FIXME: Parse data from the 'data/vocab.txt' file.
    # - The file is saved in tab-separated values (TSV) format.
    # - Each line contains a word's ID and the word itself.
    # The output dictionary should map word's ID on the word itself, e.g.:
    #   {1: 'aa', 2: 'ab', ...}

    vocab2array = np.loadtxt(dict_path,dtype="str")
    vocab_keys = list(map(int, vocab2array[:,0].tolist()))
    vocab_values = vocab2array[:,1].tolist()

    res = {}
    for i in range(len(vocab_values)):
         res[vocab_keys[i]] = vocab_values[i]
    return res
