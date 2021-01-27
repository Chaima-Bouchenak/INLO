#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A script that computes the length of genomic transcript.
"""
import re

transcript_start = dict()
transcript_end = dict()


def get_tx_genomic_length(input_file=None):
    """
    Function that computes the length of genomic transcript of a putted GTF file
    by saving 2 dictionnaries the smallest length value 'start current element'
    and the biggest 'end current element'
    then calculating their subtraction
    """

    file_handler = open(input_file)
    for line in file_handler:
        token = line.split("\t")
        start = int(token[3])  # start current element
        end = int(token[4])  # end current element
        # The transcript identifier

        tx_id = re.search('transcript_id "([^"]+)"', token[8]).group(1)

        if tx_id not in transcript_start:
            transcript_start[tx_id] = start
            transcript_end[tx_id] = end

        else:
            if start < transcript_start[tx_id]:
                transcript_start[tx_id] = start
                if end > transcript_end[tx_id]:
                    transcript_end[tx_id] = end

    for tx_id in transcript_start:
        print(tx_id + "\t" + str(transcript_end[tx_id] - transcript_start[tx_id] + 1))


if __name__ == '__main__':
    get_tx_genomic_length(input_file='../pymetacline/data/gtf/simple.gtf')
