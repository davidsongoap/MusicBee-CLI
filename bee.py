from musicbeeipc.musicbeeipc import MusicBeeIPC
from musicbeeipc.enums import *
from sys import argv
from sys import exit

import os
import random
import colorama
import sys


colorama.init()

mb = MusicBeeIPC()

def colored_print(string, color):
    colors = {"red": 1,
              "green": 2,
              "yellow": 3,
              "blue": 4
              }
    reset = "\033[0m\033[4m"
    try:
        print(f"\033[9{colors[color]}m{string}{reset}")
    except KeyError:
        print("Invalid color")


def current_song():
    # Note: This will pull the information on the file's metadata
    # and not from the file name
    idx = mb.get_current_index()
    artist = mb.now_playing_list_get_file_property(idx, MBMD_Artist)
    song = mb.now_playing_list_get_file_property(idx, MBMD_TrackTitle)
    return artist, song


def skip(amount):
    try:
        mb.set_position(mb.get_position() + (int(amount) * 1000))
    except ValueError:
        colored_print("Invalid Value", "red")


def back_to_library():
    mb.set_shuffle(True)
    mb.now_playing_list_play_library_shuffled()
    colored_print('♫ Playing: Library',"green")


def clear_screen():
    if os.name == 'nt':
        os.system('cls')

def show_current_song():
    artist, song = current_song()
    colored_print(f"♫ Current Song: {artist} - {song}", "green")

def play_song(song):
    # mb.set_shuffle(True)
    results = mb.search_indices(song, fields=["Title"])

    # no results found
    if len(results) == 0:
        colored_print("no results", "yellow")
        return

    # show all option for the query
    if len(results) > 1:
        print("0. cancel")
        for i in range(len(results)):
            s = mb.now_playing_list_get_file_property(results[i], MBFP_Url).split("\\")[-1]
            print(f"{i + 1}. {s[:-4]}")
        pick = input("Pick song: ").strip()

        # invalid input
        if not pick.isnumeric() or not int(pick):
            return
        select_song(results, int(pick)-1)

    # there's only one result 
    else:
        select_song(results, 0)

def select_song(results, index):
    try:
        picked_song_url = mb.now_playing_list_get_file_property(results[index], MBFP_Url)

        # if the song isn't already playing
        if mb.get_file_url() != picked_song_url:
            mb.jump(results[index])
            show_current_song()
        else:
            colored_print(picked_song_url.split("\\")[-1][:-4] + " is already playing!", "yellow")
    except IndexError:
        colored_print("Invalid song!", "red")

def show_song_lyrics():
    lrc = mb.get_lyrics()
    if lrc:
        # fix any weird characters on the lyrics
        lrc = lrc.replace(" ", " ").replace(" ", " ")

        artist, song = current_song()
        colored_print(f"\n{artist} -  {song}", "blue")
        print(f"\n{lrc}\n")
    else:
        colored_print("no lyrics available for this song", "yellow")


def print_help():
    print("""
play song                 - ps <song name>
set volume                - sv <value>
current song              - cs
skip                      - skip <seconds>
show lyrics               - lrc
clear screen              - cls
play the whole library    - lib
""")


def handle_input(inp):
    inp = list(map(str.lower, inp))
    command = inp[0]
    arg = " ".join(inp[1:])

    if command == "sv":
        mb.volume = int(arg)
    elif command == "ps":
        play_song(arg)
    elif command == "h":
        print_help()
    elif command == "cs":
        show_current_song()
    elif command == "skip":
        skip(arg)
    elif command == "lrc":
        show_song_lyrics()
    elif command == "pl":
        play_list(arg)
    elif command == "lib":
        back_to_library()
    elif command in "cls":
        clear_screen()

def main():
    args = list(map(str.lower, argv[1:]))

    # if there are no arguments, open the prompt
    if len(args) == 0:
        arrow_char = "⟩"
        prompt = f"~\033[94m{arrow_char}\033[0m"

        print("use [exit] or [quit] to close")
        print("use [h] for the options")
        print("Music Bee:")
        while 1:
            inp = input(prompt+ " ").lower()
            if inp in ["exit", "quit"]:
                exit(0)
            handle_input(inp.strip().split(" "))
    # else just run the command
    else:
        handle_input(args)

if __name__ == "__main__":
    main()
