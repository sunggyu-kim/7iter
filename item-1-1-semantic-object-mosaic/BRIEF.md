# Item 1-1 — Semantic Object Mosaic Lab

## Fork origin
Forked from Item 1 — Mosaic Year App.

## Problem
Color-grid mosaic alone does not preserve target object readability when the target has large background areas.

## Goal
Create object-first mosaics where:
- target object is segmented,
- object cells use semantically/color-relevant image tiles,
- NULL/background cells are also filled with real image tiles,
- no cell is a blank color block,
- original tile images are not heavily recolored.

## Success bar
A viewer should recognize the target object from distance and discover real image tiles when zoomed in.
