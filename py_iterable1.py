#!/usr/bin/env python3
# 01.17.2022 13:04:11 CST
# title = python iterable 1

# test1
songs = ["揺れる想い", "君がいない", "心を開いて", "don\'t you see!", \
    "世界はきっと未来の中", "フォトグラフ", "もう少し あと少し…"
    ]

def song_enumerate(iterable, start=0):
    for song in iterable:
        yield start, song
        start +=1
        
for i, song in song_enumerate(songs, 1):
    print(f"Track {i}: {song}")
    
