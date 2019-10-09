import os
import re
from spellchecker import SpellChecker

ADDITIONS_TO_DICTIONARY = ['initialize']


def find_misspellings(words):
    spell = SpellChecker()
    spell.word_frequency.load_words(ADDITIONS_TO_DICTIONARY)
    return spell.unknown(words)


def link_exists(link):
    paths = ['.', '..', os.path.join('..', '..')]
    finds = [os.path.isfile(os.path.join(path, link)) for path in paths]
    return True in finds


def find_missinglinks(links):
    return [x for x in links if not link_exists(x)]


def remove_nonwords(md_content):
    text_without_links = re.sub(r'\(.*?\)', '', md_content)
    text_without_links_and_code = re.sub(r'`.*?`', '', text_without_links)
    return text_without_links_and_code


def md_to_links_and_words(md_content):
    extracted = {}
    extracted.links = re.findall(r'\(.*?\)', md_content)
    extracted.words = remove_nonwords(md_content)
