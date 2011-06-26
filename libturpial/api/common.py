# -*- coding: utf-8 -*-

""" Common variables for Turpial API """
#
# Author: Wil Alvarez (aka Satanas)
# Mar 13, 2011

VERSION = '0.7.0-a1'
STATUSPP = 20

class ProtocolType:
    TWITTER = 'twitter'
    IDENTICA = 'identica'

class UpdateType:
    DM = 'dm'
    STD = 'std'
    PROFILE = 'profile'

class ColumnType:
    TIMELINE = 'timeline'
    REPLIES = 'replies'
    DIRECTS = 'directs'
    SENT = 'sent'
    FAVORITES = 'favorites'