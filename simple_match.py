# + a
# + ab
# - b
# - ba
REGEXP_1 = '^a\\.*'

# + aab
# + abb
# + acb
# - ab
# - aabc
REGEXP_2 = '^\w{3}$'

# + sofia.mp3
# + sofia.mp4
# - sofia.mp7
# - sofia.mp34
REGEXP_3 = '^\w+[.]mp[34]$'

# + taverna
# + versus
# + vera
# + zveri
# - zver
REGEXP_4 = '^\w+[^r]$'

# - a
# - aa
# + aaa
# - aaaa
# - b
# - bb
# + bbb
# - bbbb
# - ccc
REGEXP_5 = '^[ab]{3}$'

# - Ok
# - OkOk
# + OkOkOk
# - OkOkOkOk
# - ab
# - abab
# + ababab
# - abababab
REGEXP_6 = '^[Okab]{6}$'

# - aaa
# - aaa aaa
# + aaa Aaa aaa
# + aaa aaa Aaa
# + Aaa aaa aaa
# - A
# - aaa A aaa
REGEXP_7 = '^[Aa ]{11}$'

# + abc
# + abc03
# + a-b-c-3
# + a.b.c.0
# - Aabc
# - abc1
# - #abc
REGEXP_8 = '^a.*[^1]$'
