# LUIGI

## Problem
Create a map-reduce job to find the max number for the 1st field in a large csv file

## Components

-  1x mapper:
    - input: 0.large-file.txt
    - output: 1.part-00.txt … part-09.txt
- 10x transformer:
    - input: part-xx.txt
    - output: 2.transformed-xx.txt
- 10x reducer:
    - input: transformed-xx.txt
    - output: 3.solved-xx.txt
-  1x collector:
    - input: solved-xx.txt
    - output: 4.solution.txt

## Challenges:
1. All transformers and groupers should run in parallel
2. Transformers and groups should start working before mapper finishes
