import os
import re
from urllib import request as urlrequest
from urllib import error as urlerror
from spellchecker import SpellChecker

ADDITIONS_TO_DICTIONARY = [' ', '\n', 'initialize']


def find_misspellings(words):
    spell = SpellChecker()
    spell.word_frequency.load_words(ADDITIONS_TO_DICTIONARY)
    return spell.unknown(words)


def md_file_exists(link):
    PATHS = ['.', '..', os.path.join('..', '..')]
    finds = [os.path.isfile(os.path.join(path, link)) for path in PATHS]
    return True in finds


def http_link_exists(link):
    try:
        urlrequest.urlopen(link)
        return True
    except urlerror.HTTPError as e:
        print(e.code)
    except urlerror.URLError as e:
        print(e.args)
    return False


def link_exists(link):
    if link.startswith('http'):
        return http_link_exists(link)
    elif link.endswith('.md'):
        return md_file_exists(link)
    else:
        print('Unknown link type: ' + link)
    return False


def find_missinglinks(links):
    return [x for x in links if not link_exists(x)]


def remove_nonwords(md_content):
    text_without_links = re.sub(r'\(.*?md\)', '', md_content)
    text_without_links_and_code = re.sub(r'`.*?`', '', text_without_links)
    return text_without_links_and_code


def find_md_files():
    PATHS = ['.', '..']
    IGNORE_PATH = 'node_modules'
    md_filelist = []
    for path in PATHS:
        md_filelist += [os.path.join(location, filename)
                        for location, _, files in os.walk(path) if IGNORE_PATH not in location
                        for filename in files if filename.endswith('.md')]
    return md_filelist


def find_md_links(md):
    INLINE_LINK_RE = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    FOOTNOTE_LINK_URL_RE = re.compile(r'\[(\d+)\]:\s+(\S+)')
    def links_from_pairs(pairs):
        return [item[1] for item in pairs]
    inline_links = links_from_pairs(INLINE_LINK_RE.findall(md))
    footnote_links = links_from_pairs(FOOTNOTE_LINK_URL_RE.findall(md))
    return inline_links + footnote_links


def md_to_links_and_words(md_content):
    extract = {'links': find_md_links(md_content),
               'words': remove_nonwords(md_content)}
    return extract
