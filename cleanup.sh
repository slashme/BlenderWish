#!/bin/sh
#Totally clear projects directory and re-initialise empty database.
rm -rf projects/*
rm wishes.db 
python makedb.py
