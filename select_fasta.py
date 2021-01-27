#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A script that select the specific sequence of
a given Tx ID in a FASTA file.
"""
from __future__ import absolute_import
import argparse


def create_parser():
    """
    Fuction that creats the arguments used
    """

    parser = argparse.ArgumentParser(add_help=True,
                                     description="A script that select the specific sequence of a given Tx ID in a FASTA file")

    parser.add_argument('-i', '--inputfile',
                        help="Path to the file",
                        type=argparse.FileType("r"),
                        metavar="FASTA",
                        required=True)

    parser.add_argument('-id_seq', '--identifiers',
                        help="Entry sequence identifiers",
                        type=str,
                        required=True)

    return parser


def search_seq_ids(inputfile, identifiers):
    """
    Function returns a dictionary containing in key : chosen identifiers
    and value their sequences.
    @param inputfile : input fasta file
    @param identifiers : search fasta IDs
    """
    dico_fasta = {}
    seq_id = ""
    keep_fasta = True

    for line in inputfile:
        if line.startswith(">"):
            seq_id = line[1:-1]  # select the ID
            if seq_id in identifiers:
                keep_fasta = True
            else:
                keep_fasta = False

        else:  # line doesn't starts with ">"
            if keep_fasta:
                seq = line[0:-1]  # select the sequence
                dico_fasta[seq_id] = seq


def main():
    """
    Function which takes the defined parser arguments and
    use them to return a dictionary containing in key : chosen identifiers
    and value their sequences.
    """
    parser = create_parser()
    args = parser.parse_args()
    print(args)
    search_seq_ids(args.inputfile, args.identifiers)


if __name__ == "__main__":
    main()
