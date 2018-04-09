# -*- coding: utf-8 -*-
from sphinx.search import SearchLanguage
# from smallseg import SEG
import jieba


class SearchChinese(SearchLanguage):
    lang = 'zh'

    def init(self, options):
        # print "reading Chiniese dictionary"
        print ("reading Chiniese dictionary")
        self.seg = jieba

    def split(self, input):
        return self.seg.cut_for_search(input.encode("utf8"))

    def word_filter(self, stemmed_word):
        return len(stemmed_word) > 1
