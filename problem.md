# LUIGI

## Problem
Create a map-reduce job to find the average number for the 1st field in a large csv file

## Components

- mapper:
    - input: large-file.txt
    - output: part-00.txt … part-09.txt
- 10x transformer:
    - input: part-xx.txt
    - output: part-xx-transformed.txt
- 10x grouper:
    - input: part-xx-transformed.txt
    - output: part-xx-solution.txt
- reduce:
    - input: part-xx-solution.txt
    - output: large-file-solution.txt

## Challenges:
1. All transformers and groupers should run in parallel
2. Transformers and groups should start working before mapper finishes
