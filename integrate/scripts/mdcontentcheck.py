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


def http_link_exists(link):
    try:
        req = urlrequest.Request(link, headers={'User-Agent': 'RaPa/3.0'})
        urlrequest.urlopen(req, timeout=10).read()
        return True
    except urlerror.HTTPError as e:
        print(e.code)
    except urlerror.URLError as e:
        print(e.args)
    return False


def link_exists(link):
    if link.startswith('http'):
        link_does_exist = http_link_exists(link)
    else:
        link_does_exist = os.path.isfile(link)
    return link_does_exist


def find_missinglinks(links):
    return [x for x in links if not link_exists(x)]


def remove_nonwords(md_content):
    text_without_links = re.sub(r'\(.*?md\)', '', md_content)
    text_without_links_and_code = re.sub(r'`.*?`', '', text_without_links)
    return text_without_links_and_code


def find_md_files():
    IGNORE_PATH = 'node_modules'
    md_filelist = [os.path.join(location, filename)
                   for location, _, files in os.walk('.') if IGNORE_PATH not in location
                   for filename in files if filename.endswith('.md')]
    return md_filelist


def find_md_links(md):
    INLINE_LINK_RE = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    FOOTNOTE_LINK_URL_RE = re.compile(r'\[(\d+)\]:\s+(\S+)')
    def links_from_pairs(pairs):
        return [item[1].split()[0] for item in pairs]
    inline_links = links_from_pairs(INLINE_LINK_RE.findall(md))
    footnote_links = links_from_pairs(FOOTNOTE_LINK_URL_RE.findall(md))
    return inline_links + footnote_links
