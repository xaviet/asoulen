#! /usr/bin/python3
# coding=utf-8
'''
  name = textview.py
'''


import os


def main():
  colnums, lines=os.get_terminal_size()
  print(colnums, lines)


if(__name__ == '__main__'):
  main();
