# -*- coding: utf-8 -*-
import sys, json, re, shutil, os
sys.path.insert(0, '/home/claude/jp'); sys.path.insert(0, '/home/claude/jp/data')
import content as C, gen, hokkaido, stops_north, tohoku, stops_north2, guides_tohoku, kanto, stops_central, guides_kanto, chubu, stops_south, guides_chubu, kinki, stops_kinki, guides_kinki, chushikoku, stops_east, guides_chushikoku, kyushu, stops_kyushu, guides_kyushu, okinawa, stops_island, guides_okinawa

SRC = '/home/claude/src/index.html'
src = open(SRC, encoding='utf-8').read()
L = src.split('\n')
def js(o): return json.dumps(o, ensure_ascii=False, separators=(',', ':'))

def find_decl(name):
    for i, l in enumerate(L):
        if re.match(r'(const|let|var|function)\s+%s\b' % re.escape(name), l): return i
    raise KeyError(name)
def decl_end(i):
    depth = 0; started = False
    quote = None
    for j in range(i, len(L)):
        line = L[j]; k = 0
        while k < len(line):
            ch = line[k]
            if quote:
                if ch == '\\': k += 2; continue
                if ch == quote: quote = None
            else:
                if ch in '"\'`': quote = ch
                elif ch == '/' and line[k+1:k+2] == '/': break
                elif ch in '{[(': depth += 1; started = True
                elif ch in '}])': depth -= 1
            k += 1
        if quote in ('"', "'"): quote = None   # 單行字串不跨行
        if depth <= 0 and line.rstrip().endswith(';') and (started or j == i): return j
        if depth <= 0 and started and line.rstrip().endswith('}') and j > i: return j
    raise ValueError(L[i][:40])
repl = {}   # start index -> (end index, new text)
def replace_decl(name, new):
    i = find_decl(name); j = decl_end(i)
    print('  %-32s lines %d-%d (%d)' % (name, i+1, j+1, j-i+1))
    repl[i] = (j, new)

# ---------- 地圖 ----------
M = json.load(open('/home/claude/jp/map.json'))
prefs_all = []          # 繁中縣名，依區域排序
region_prefs = {}
mapdata = {}
for rid, names in M['reg'].items():
    region_prefs[rid] = [C.kanji(n) for n in names]
    for n in names:
        mapdata[C.kanji(n)] = M['map'][n]
        prefs_all.append(C.kanji(n))
IN = M['inset']
replace_decl('countyMapData', 'const countyMapData = ' + js(mapdata) + ';')

# ---------- 地名資料 ----------
rows = []
for r in hokkaido.PLACES + tohoku.PLACES + kanto.PLACES + chubu.PLACES + kinki.PLACES + chushikoku.PLACES + kyushu.PLACES + okinawa.PLACES:
    rows.append([C.kanji(r[0]), r[1], r[2], r[3], r[4], r[5]])
replace_decl('rawPlacesData', 'const rawPlacesData = ' + js(rows) + ';')
places = [dict(id=i, c=r[0], n=r[1], o=r[2], d=r[3], detail=r[5]) for i, r in enumerate(rows)]

# ---------- 嚮導 ----------
guides_by_pref = {}
COUNTY_GUIDES, GUIDE_MEET, COUNTY_TO_GUIDE, ART = {}, {}, {}, {}
ALL_GUIDES = dict(C.GUIDES); ALL_GUIDES.update(guides_tohoku.GUIDES); ALL_GUIDES.update(guides_kanto.GUIDES); ALL_GUIDES.update(guides_chubu.GUIDES); ALL_GUIDES.update(guides_kinki.GUIDES); ALL_GUIDES.update(guides_chushikoku.GUIDES); ALL_GUIDES.update(guides_kyushu.GUIDES); ALL_GUIDES.update(guides_okinawa.GUIDES)
for gk, g in ALL_GUIDES.items():
    pref = C.kanji(g['county'])
    guides_by_pref[pref] = dict(name=g['name'], icon=g['icon'], open=g['open'], close=g['close'])
    COUNTY_GUIDES[gk] = dict(name=g['name'], county=pref, icon=g['icon'], title=g['title'], desc=g['desc'])
    GUIDE_MEET[gk] = g['meet']; COUNTY_TO_GUIDE[pref] = gk; ART[g['name']] = g['art']
replace_decl('COUNTY_GUIDES', 'const COUNTY_GUIDES = ' + js(COUNTY_GUIDES) + ';')
replace_decl('GUIDE_MEET_DATA', 'const GUIDE_MEET_DATA = ' + js(GUIDE_MEET) + ';')
replace_decl('COUNTY_TO_GUIDE', 'const COUNTY_TO_GUIDE = ' + js(COUNTY_TO_GUIDE) + ';')

# ---------- 立繪名稱對照 ----------
name_art = {"苔野婆婆": "mentor", "岩城源三": "ahai", "結城千夏": "chianma", "藤原文彥": "wenlan", "小野岳": "lahok",
            "與那嶺千代": "phoasoh", "久保田誠": "keshian",
            "山本大翔": "hanlin", "佐藤美咲": "shiaolan", "田中蓮": "poyu", "鈴木陽菜": "sihyu", "高橋悠真": "zihchian",
            "伊藤結衣": "wanjhen", "渡邊颯太": "lali", "小林心春": "kerou", "比嘉海斗": "jianlin", "仲村美海": "jiaen",
            "忘名妖": "wangmingyao", "津輕港的老領航": "chuantou", "荊棘之靈": "chaishan", "海的另一頭來的使者": "chuantou", "鑑真的弟子": "datun", "浮島的船頭": "tubo", "那珂川的渡守": "chuantou", "長崎的通詞": "yanshu", "熊本城的石垣守": "shouyu", "八束水臣津野命": "datun", "太田川的舟守": "chuantou", "愛比売": "wunu", "平城京的舍人": "afu", "洛中的古老": "tubo", "石山的蓮如上人": "shelaogong", "信濃川的潟守": "heichao", "金洗沢的藤五郎": "tubo", "沢彥和尚": "tianhou", "江戶古地圖師": "yanshu", "濱邊的燈台守": "afu", "三ツ石的岩神": "datun", "青葉山的武者魂": "shouyu", "北加伊之魂": "babulu", "宇須岸爺": "shelaogong", "豐平川之魂": "heichao"}
name_art.update(ART)
replace_decl('NAME_TO_ART', 'const NAME_TO_ART = ' + js(name_art) + ';')

# ---------- 角色 ----------
replace_decl('TITLE_BLURB', 'const TITLE_BLURB = ' + js(C.TITLE_BLURB) + ';')
replace_decl('MENTOR', 'const MENTOR = ' + js(C.MENTOR) + ';')
replace_decl('COMPANIONS', 'const COMPANIONS = ' + js(C.COMPANIONS) + ';')
replace_decl('PLAYER_CHARS', 'const PLAYER_CHARS = ' + js(C.PLAYER_CHARS) + ';')
replace_decl('PROTAGONIST_HOME_COUNTY', 'const PROTAGONIST_HOME_COUNTY = ' + js(C.PROTAGONIST_HOME_COUNTY) + ';')
replace_decl('REGION_MEET_NARRATION_VISITOR', 'const REGION_MEET_NARRATION_VISITOR = ' + js(C.REGION_MEET_NARRATION_VISITOR) + ';')
replace_decl('REGION_MEET_NARRATION', 'const REGION_MEET_NARRATION = ' + js(C.REGION_MEET_NARRATION) + ';')
# 台灣專屬的主角群劇本：第 0 批先清空，之後隨各區批次重寫
_i = find_decl('PLAYER_MAIN_SCRIPTS'); _j = find_decl('scriptToSteps') - 1
while L[_j].strip() == '' or L[_j].strip().startswith('//'): _j -= 1
repl[_i] = (_j, 'const PLAYER_MAIN_SCRIPTS = {};')
print('  PLAYER_MAIN_SCRIPTS (extended)     lines %d-%d' % (_i+1, _j+1))
for nm in ('PROTAGONIST_PAIR_INTERACT', 'STOP_COMPANION_LINES', 'PLAYER_STOP_LINES',
           'PROTAGONIST_STOP_BANTER', 'PROTAGONIST_FAREWELL'):
    replace_decl(nm, 'const %s = {};' % nm)
replace_decl('PROTAGONIST_MAIN_INTEGRATED', 'const PROTAGONIST_MAIN_INTEGRATED = {};')

# ---------- 區域 ----------
north_stops = list(stops_north.STOPS)
_byname = {p['n']: p['id'] for p in places}
for st in stops_north2.STOPS:
    st = dict(st); st['placeId'] = _byname[st.pop('placeName')]; north_stops.append(st)
central_stops = []
for st in stops_central.STOPS:
    st = dict(st); st['placeId'] = _byname[st.pop('placeName')]; central_stops.append(st)
south_stops = []
for st in stops_south.STOPS + stops_kinki.STOPS:
    st = dict(st); st['placeId'] = _byname[st.pop('placeName')]; south_stops.append(st)
east_stops = []
for st in stops_east.STOPS + stops_kyushu.STOPS:
    st = dict(st); st['placeId'] = _byname[st.pop('placeName')]; east_stops.append(st)
island_stops = []
for st in stops_island.STOPS:
    st = dict(st); st['placeId'] = _byname[st.pop('placeName')]; island_stops.append(st)
regions = []
for m in C.REGION_META:
    r = dict(m)
    r['counties'] = region_prefs[m['id']]
    r['mapPoly'] = "0,0"
    r['labelPos'] = C.REGION_LABEL_POS[m['id']]
    r['stops'] = north_stops if m['id'] == 'north' else (central_stops if m['id'] == 'central' else (south_stops if m['id'] == 'south' else (east_stops if m['id'] == 'east' else (island_stops if m['id'] == 'island' else []))))
    r['closing'] = C.region_closing(m['id'], False)
    regions.append(r)
replace_decl('REGIONS', 'const REGIONS = ' + js(regions) + ';')
flagship_ids = {s['placeId'] for s in north_stops + central_stops + south_stops + east_stops + island_stops}

# ---------- 縣市內容 ----------
cc = gen.gen_content(places, guides_by_pref, prefs_all, flagship_ids)
replace_decl('COUNTY_CONTENT', 'const COUNTY_CONTENT = ' + js(cc) + ';')

# ---------- 旅程框架 ----------
jr = open('/home/claude/src/index.html', encoding='utf-8').read()
i0 = find_decl('JOURNEY'); j0 = decl_end(i0)
journey_new = '''const JOURNEY = {
  firstOpening: (region) => ([
    "孩子，你手中的羅盤已經甦醒了。看，指針正指向你出發的地方——「"+region.name+"」。",
    "自從人們開始用便利的門牌與合併後的新名字，取代口耳相傳的地名，許多地方的『本名』就漸漸被灰霧籠罩，連當地人都說不清楚自己家鄉名字的由來了。",
    "『忘名妖』最愛藏身在這樣的灰霧裡。牠不會傷人，卻會用似是而非的假故事，把地名真正的記憶一點一點吃掉。",
    "我們的任務，就是從你的家鄉出發，走遍列島，找回被牠吞噬的記憶碎片——那些地名真正的來歷。準備好了嗎，旅人？"
  ]),
  firstClosing: %s,
  lastOpening: [
    "旅人，這是最後一段旅程了。",
    "@mentor@孩子，你的身邊已經聚集了一整支隊伍，還有一位正在學習『把故事聽完』的年輕人。這最後一段路，就讓大家一起，把剩下的拼圖找齊吧。"
  ],
  lastClosing: %s
};''' % (js(C.JOURNEY_FIRST_CLOSING), js(C.JOURNEY_LAST_CLOSING))
repl[i0] = (j0, journey_new)

# ---------- 套用宣告替換 ----------
out = []; i = 0
while i < len(L):
    if i in repl:
        j, new = repl[i]; out.append(new); i = j + 1
    else:
        out.append(L[i]); i += 1
text = '\n'.join(out)

# ---------- 名稱／文字替換（非資料區） ----------
def sub(old, new, count=1):
    global text
    if old not in text: print('!! missing:', old[:50]); return
    text = text.replace(old, new) if count == 0 else text.replace(old, new, count)

sub('<title>台灣地名尋根：拾憶者物語</title>', '<title>日本地名尋根：拾憶者物語</title>')
sub('台 灣 地 名 尋 根 · R P G', '日 本 地 名 尋 根 · R P G')
sub('第一款真正以台灣地名為主軸的冒險遊戲，全台574則地名的記憶等待被拾起', '走遍日本四十七個都道府縣，讓每一則地名的記憶重新被拾起')
sub('🧭 台灣拾憶地圖', '🧭 日本拾憶地圖')
sub('全台574則地名記憶得以化作旅程', '日本各地的地名記憶得以化作旅程')
sub('收集全部 574 則地名記憶', "收集全部 '+placesData.length+' 則地名記憶")
sub('全島 574 則地名記憶已完整收錄', "全國 '+placesData.length+' 則地名記憶已完整收錄")
sub('十位來自全台五個地區的小學生', '十位來自日本五個地區的小學生')
sub('全台共 "+', '全國共 "+', 0)
sub('花蓮的風從太平洋一路灌進縱谷——你聽見了嗎？那是你從小聽到大的浪聲。', '阿蘇的火山風從外輪山一路吹下草原——你聽見了嗎？那是你從小聽到大的風聲。')
sub('青苔婆婆', '苔野婆婆', 0)
sub('我是苔野婆婆，住在這島上最老的榕樹根裡', '我是苔野婆婆，住在這座神社裡最老的一棵大樟樹根裡')
sub('每一個台灣地名，都住著一絲記憶之魂', '每一個日本地名，都住著一絲記憶之魂')
sub('也是先民、原住民族群，還有無數過客留下的印記', '也是先民、阿伊努與琉球等各族群，還有無數過客留下的印記')
sub('在全島的地名裡散布灰霧', '在全國的地名裡散布灰霧')
sub('走遍全島，去問一句最簡單', '走遍列島，去問一句最簡單')
sub('全島的記憶，都被你一一拾起了', '所有的記憶，都被你一一拾起了')
sub('縣市', '都道府縣', 0)
# 舊資料裡與台灣地圖綁定的島嶼方框：改為只有沖繩
sub('const ISLAND_INSETS = {', 'const ISLAND_INSETS_OLD = {')
text = text.replace('const ISLAND_INSETS_OLD = {', 'const ISLAND_INSETS = {};\nconst OKINAWA_INSET = ' + js(dict(x=IN[0], y=IN[1], w=IN[2], h=IN[3])) + ';\nconst _ISLAND_INSETS_UNUSED = {', 1)
sub('const REGION_LABEL_POS = {', 'const REGION_LABEL_POS_OLD = {')
text = text.replace('const REGION_LABEL_POS_OLD = {', 'const REGION_LABEL_POS = ' + js(C.REGION_LABEL_POS) + ';\nconst _REGION_LABEL_POS_UNUSED = {', 1)
sub('    region.counties.forEach(cname=>{\n      if (ISLAND_INSETS[cname])',
    '    if (region.id === "island"){\n'
    '      g.appendChild(svgEl(ns,"rect",{x:OKINAWA_INSET.x, y:OKINAWA_INSET.y, width:OKINAWA_INSET.w, height:OKINAWA_INSET.h, rx:5, fill:"#fdf3da", "fill-opacity":"0.10", stroke:"#fdf3da", "stroke-width":"1.3", "stroke-dasharray":"5 3", "stroke-opacity":"0.9"}));\n'
    '      g.appendChild(svgText(ns, OKINAWA_INSET.x+8, OKINAWA_INSET.y+16, "沖繩縣（放大約 1.5 倍）", 10, "start", {"font-weight":"700"}));\n'
    '    }\n'
    '    region.counties.forEach(cname=>{\n      if (ISLAND_INSETS[cname])')
sub('本圖比例尺：本島、澎湖、綠島、蘭嶼、小琉球、龜山島皆依此繪製', '本州、北海道、四國、九州依同一比例繪製')
sub('金門、馬祖為放大示意，請以各方框內的比例尺為準', '沖繩縣以方框放大顯示（約 1.5 倍），並非實際位置')
sub('drawScaleBar(ns, sc, 16, 698, 50, MAIN_PX_PER_KM);', '/* scale bar omitted */')
# 場景關鍵字補上日本用詞
sub('["temple",   /廟|宮|寺|祠|神社|', '["temple",   /廟|宮|寺|祠|神社|鳥居|御嶽|大社|')
sub('["mountain", /山|嶺|峰|', '["mountain", /山|嶽|岳|火山|嶺|峰|')


NAMEMAP = [("拉利．馬耀","渡邊颯太"),("林承翰","山本大翔"),("蘇曉嵐","佐藤美咲"),("陳柏宇","田中蓮"),("黃思妤","鈴木陽菜"),
  ("郭子謙","高橋悠真"),("葉宛真","伊藤結衣"),("潘可柔","小林心春"),("洪建霖","比嘉海斗"),("許嘉恩","仲村美海"),
  ("柯世安","久保田誠"),("阿翰","小翔"),("小嵐","小咲"),("曉嵐","美咲"),("柏宇","小蓮"),("思妤","小陽"),("子謙","悠真"),
  ("宛真","結衣"),("阿利","小颯"),("可柔","心春"),("阿霖","海斗"),("建霖","海斗"),("嘉恩","美海"),
  ("阿海","岩城源三"),("芊瑪","結城千夏"),("文瀾","藤原文彥"),("拉罕","小野岳"),("潘嫂","與那嶺千代")]
for a, b in NAMEMAP: text = text.replace(a, b)
FIXES = [
 ("怎麼也跑基隆來了！","怎麼也跑函館來了！"),
 ("我可不會讓你一個人在南部稱王。","我可不會讓你一個人在近畿稱王。"),
 ("嘿嘿，畢竟基隆是我的主場啊！走，我帶你去吃廟口甜不辣，順便講幾個你筆記本裡漏掉的地名！","嘿嘿，畢竟函館是我的主場啊！走，我帶你去朝市吃海鮮丼，順便講幾個你筆記本裡漏掉的地名！"),
 ("哈，終於見到本人了，本島仔。","哈，終於見到本人了，內地仔。"),
 ("別叫我本島仔！算了","別叫我內地仔！算了"),
 ("喲，怎麼換妳離開台南跑來我地盤了？","喲，怎麼換妳離開京都跑來我地盤了？"),
 ("妳也來台南了？","妳也來京都了？"),
 ("那個線上一直嘴我的『本島仔』對面本人吧！","那個線上一直嘴我的『內地仔』對面本人吧！"),
 ("你就是基隆那個運動會常常拿冠軍的？","你就是函館那個運動會常常拿冠軍的？"),
 ("你們基隆的地名故事應該也不少吧？","你們函館的地名故事應該也不少吧？"),
 ("你是不是基隆運動會那個很會衝的男生！","你是不是函館運動會那個很會衝的男生！"),
 ("聽說基隆廟口也有很多好吃的，下次換你帶我去吃！","聽說函館朝市也有很多好吃的，下次換你帶我去吃！"),
 ("我有整理各都道府縣小朋友的新聞","我有整理各都道府縣小朋友的新聞"),
 ("妳畫的這個是我們台南的小吃攤耶，畫得好像喔！","妳畫的這個是我們京都的和菓子舖耶，畫得好像喔！"),
]
for a, b in FIXES:
    if a not in text: print('!! fix missing:', a[:30])
    text = text.replace(a, b)

open('/home/claude/jp/index.html', 'w', encoding='utf-8').write(text)
print('built', len(text)//1024, 'KB; places', len(places), '; main chains', sum(len(v['mainChains']) for v in cc.values()),
      '; side', sum(len(v['sideQuests']) for v in cc.values()))
