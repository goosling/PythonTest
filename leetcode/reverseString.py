__author__ = 'joe'
# -*- coding: utf-8 -*-

class Solution(object):
    def reverseWords(self, string):
        begin = 0
        end = 0


        while(end < string.size()):
            if(string[end] == " "):
                swapString(string, begin, end-1):
                    begin = end+1
                    end = begin
        else:



    def swapString(s, begin, end):
        while(end > begin):
            c = s[begin]
            s[begin] = s[end]
            s[end] = c
            begin++
            end--

