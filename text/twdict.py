""" from https://github.com/keithito/tacotron """

import re


valid_symbols = [
"a", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "ah", "ah2", "ah3", "ah4", "ah5", "ah6", "ah7", "ah8", "ai", "ai2", "ai3", "ai4", "ai5", "ai6", "ai7", "ai8", "ainn", "ainn2", "ainn3", "ainn4", "ainn5", "ainn6", "ainn7", "ainn8", "ak", "ak2", "ak3", "ak4", "ak5", "ak6", "ak7", "ak8", "am", "am2", "am3", "am4", "am5", "am6", "am7", "am8", "an", "an2", "an3", "an4", "an5", "an6", "an7", "an8", "ang", "ang2", "ang3", "ang4", "ang5", "ang6", "ang7", "ang8", "ann", "ann2", "ann3", "ann4", "ann5", "ann6", "ann7", "ann8", "annh", "annh2", "annh3", "annh4", "annh5", "annh6", "annh7", "annh8", "ap", "ap2", "ap3", "ap4", "ap5", "ap6", "ap7", "ap8", "at", "at2", "at3", "at4", "at5", "at6", "at7", "at8", "au", "au2", "au3", "au4", "au5", "au6", "au7", "au8", "auh", "auh2", "auh3", "auh4", "auh5", "auh6", "auh7", "auh8", "b",  "b2",  "b3",  "b4",  "b5",  "b6",  "b7",  "b8",  "e", "e2", "e3", "e4", "e5", "e6", "e7", "e8", "eh", "eh2", "eh3", "eh4", "eh5", "eh6", "eh7", "eh8", "enn", "enn2", "enn3", "enn4", "enn5", "enn6", "enn7", "enn8", "ennh", "ennh2", "ennh3", "ennh4", "ennh5", "ennh6", "ennh7", "ennh8", "g",  "g2",  "g3",  "g4",  "g5",  "g6",  "g7",  "g8",  "h",  "h2",  "h3",  "h4",  "h5",  "h6",  "h7",  "h8",  "i", "i2", "i3", "i4", "i5", "i6", "i7", "i8", "iNULL",  "iNULL2",  "iNULL3",  "iNULL4",  "iNULL5",  "iNULL6",  "iNULL7",  "iNULL8",  "ia", "ia2", "ia3", "ia4", "ia5", "ia6", "ia7", "ia8", "iah", "iah2", "iah3", "iah4", "iah5", "iah6", "iah7", "iah8", "iak", "iak2", "iak3", "iak4", "iak5", "iak6", "iak7", "iak8", "iam", "iam2", "iam3", "iam4", "iam5", "iam6", "iam7", "iam8", "ian", "ian2", "ian3", "ian4", "ian5", "ian6", "ian7", "ian8", "iang", "iang2", "iang3", "iang4", "iang5", "iang6", "iang7", "iang8", "iann", "iann2", "iann3", "iann4", "iann5", "iann6", "iann7", "iann8", "iannh", "iannh2", "iannh3", "iannh4", "iannh5", "iannh6", "iannh7", "iannh8", "iap", "iap2", "iap3", "iap4", "iap5", "iap6", "iap7", "iap8", "iat", "iat2", "iat3", "iat4", "iat5", "iat6", "iat7", "iat8", "iau", "iau2", "iau3", "iau4", "iau5", "iau6", "iau7", "iau8", "iauh", "iauh2", "iauh3", "iauh4", "iauh5", "iauh6", "iauh7", "iauh8", "iaunn", "iaunn2", "iaunn3", "iaunn4", "iaunn5", "iaunn6", "iaunn7", "iaunn8", "ih", "ih2", "ih3", "ih4", "ih5", "ih6", "ih7", "ih8", "ik", "ik2", "ik3", "ik4", "ik5", "ik6", "ik7", "ik8", "im", "im2", "im3", "im4", "im5", "im6", "im7", "im8", "in", "in2", "in3", "in4", "in5", "in6", "in7", "in8", "ing", "ing2", "ing3", "ing4", "ing5", "ing6", "ing7", "ing8", "inn", "inn2", "inn3", "inn4", "inn5", "inn6", "inn7", "inn8", "innh", "innh2", "innh3", "innh4", "innh5", "innh6", "innh7", "innh8", "io", "io2", "io3", "io4", "io5", "io6", "io7", "io8", "ioh", "ioh2", "ioh3", "ioh4", "ioh5", "ioh6", "ioh7", "ioh8", "iok", "iok2", "iok3", "iok4", "iok5", "iok6", "iok7", "iok8", "iong", "iong2", "iong3", "iong4", "iong5", "iong6", "iong7", "iong8", "ip", "ip2", "ip3", "ip4", "ip5", "ip6", "ip7", "ip8", "it", "it2", "it3", "it4", "it5", "it6", "it7", "it8", "iu", "iu2", "iu3", "iu4", "iu5", "iu6", "iu7", "iu8", "iuh", "iuh2", "iuh3", "iuh4", "iuh5", "iuh6", "iuh7", "iuh8", "iunn", "iunn2", "iunn3", "iunn4", "iunn5", "iunn6", "iunn7", "iunn8", "j",  "j2",  "j3",  "j4",  "j5",  "j6",  "j7",  "j8",  "k",  "k2",  "k3",  "k4",  "k5",  "k6",  "k7",  "k8",  "kh",  "kh2",  "kh3",  "kh4",  "kh5",  "kh6",  "kh7",  "kh8",  "l",  "l2",  "l3",  "l4",  "l5",  "l6",  "l7",  "l8",  "m", "m",  "m2", "m2",  "m3", "m3",  "m4", "m4",  "m5", "m5",  "m6", "m6",  "m7", "m7",  "m8", "m8",  "mh", "mh2", "mh3", "mh4", "mh5", "mh6", "mh7", "mh8", "n",  "n2",  "n3",  "n4",  "n5",  "n6",  "n7",  "n8",  "ng", "ng",  "ng2", "ng2",  "ng3", "ng3",  "ng4", "ng4",  "ng5", "ng5",  "ng6", "ng6",  "ng7", "ng7",  "ng8", "ng8",  "ngh", "ngh2", "ngh3", "ngh4", "ngh5", "ngh6", "ngh7", "ngh8", "o", "o2", "o3", "o4", "o5", "o6", "o7", "o8", "oh", "oh2", "oh3", "oh4", "oh5", "oh6", "oh7", "oh8", "ok", "ok2", "ok3", "ok4", "ok5", "ok6", "ok7", "ok8", "om", "om2", "om3", "om4", "om5", "om6", "om7", "om8", "ong", "ong2", "ong3", "ong4", "ong5", "ong6", "ong7", "ong8", "onn", "onn2", "onn3", "onn4", "onn5", "onn6", "onn7", "onn8", "oo", "oo2", "oo3", "oo4", "oo5", "oo6", "oo7", "oo8", "ooh", "ooh2", "ooh3", "ooh4", "ooh5", "ooh6", "ooh7", "ooh8", "op", "op2", "op3", "op4", "op5", "op6", "op7", "op8", "p",  "p2",  "p3",  "p4",  "p5",  "p6",  "p7",  "p8",  "ph",  "ph2",  "ph3",  "ph4",  "ph5",  "ph6",  "ph7",  "ph8",  "s",  "s2",  "s3",  "s4",  "s5",  "s6",  "s7",  "s8",  "t",  "t2",  "t3",  "t4",  "t5",  "t6",  "t7",  "t8",  "th",  "th2",  "th3",  "th4",  "th5",  "th6",  "th7",  "th8",  "ts",  "ts2",  "ts3",  "ts4",  "ts5",  "ts6",  "ts7",  "ts8",  "tsh",  "tsh2",  "tsh3",  "tsh4",  "tsh5",  "tsh6",  "tsh7",  "tsh8",  "u", "u2", "u3", "u4", "u5", "u6", "u7", "u8", "ua", "ua2", "ua3", "ua4", "ua5", "ua6", "ua7", "ua8", "uah", "uah2", "uah3", "uah4", "uah5", "uah6", "uah7", "uah8", "uai", "uai2", "uai3", "uai4", "uai5", "uai6", "uai7", "uai8", "uainn", "uainn2", "uainn3", "uainn4", "uainn5", "uainn6", "uainn7", "uainn8", "uan", "uan2", "uan3", "uan4", "uan5", "uan6", "uan7", "uan8", "uann", "uann2", "uann3", "uann4", "uann5", "uann6", "uann7", "uann8", "uat", "uat2", "uat3", "uat4", "uat5", "uat6", "uat7", "uat8", "ue", "ue2", "ue3", "ue4", "ue5", "ue6", "ue7", "ue8", "ueh", "ueh2", "ueh3", "ueh4", "ueh5", "ueh6", "ueh7", "ueh8", "uh", "uh2", "uh3", "uh4", "uh5", "uh6", "uh7", "uh8", "ui", "ui2", "ui3", "ui4", "ui5", "ui6", "ui7", "ui8", "un", "un2", "un3", "un4", "un5", "un6", "un7", "un8", "ut", "ut2", "ut3", "ut4", "ut5", "ut6", "ut7", "ut8"
]

_valid_symbol_set = set(valid_symbols)


class TWDict:
  '''Thin wrapper around CMUDict data. http://www.speech.cs.cmu.edu/cgi-bin/cmudict'''
  def __init__(self, file_or_path, keep_ambiguous=True):
    if isinstance(file_or_path, str):
      with open(file_or_path, encoding='latin-1') as f:
        entries = _parse_twdict(f)
    else:
      entries = _parse_twdict(file_or_path)
    if not keep_ambiguous:
      entries = {word: pron for word, pron in entries.items() if len(pron) == 1}
    self._entries = entries


  def __len__(self):
    return len(self._entries)


  def lookup(self, word):
    '''Returns list of ARPAbet pronunciations of the given word.'''
    return self._entries.get(word.upper())



_alt_re = re.compile(r'\([0-9]+\)')


def _parse_twdict(file):
  twdict = {}
  for line in file:
#    if len(line) and (line[0] >= 'A' and line[0] <= 'Z' or line[0] == "'"):
    if len(line):
#      parts = line.split('  ')
      parts = line.split(' ')
#      word = re.sub(_alt_re, '', parts[0])
      word = parts[0]
      pronunciation = _get_tw_pronunciation(parts[1])
      if pronunciation:
        if word in twdict:
          twdict[word].append(pronunciation)
        else:
          twdict[word] = [pronunciation]
  return twdict


def _get_tw_pronunciation(s):
  parts = s.strip().split(' ')
  for part in parts:
    if part not in _valid_symbol_set:
      return None
  return ' '.join(parts)
