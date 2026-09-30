# -*- coding: utf-8 -*-
import re, json, random
DECOYS = [
 "因戰國武將行軍經過此地時隨口命名而流傳下來",
 "傳說是某位雲遊高僧隨手一指，就定下了這個名字",
 "因這裡曾發生一場合戰，勝方直接以自己的姓氏重新命名此地",
 "只是古地圖抄寫時的誤植，將錯就錯沿用至今，與地方歷史無關",
 "純粹是地方領主附庸風雅、隨意取的吉祥字，並無實際典故",
 "因地形形似某種動物，先民依外觀直接命名，與語言或墾殖無關",
 "因江戶幕府官員依自己的家鄉地名直接移植而來",
 "因某位藩主的姓氏諧音相近而得名，與土地本身無關",
 "因明治時期官員憑空拼湊漢字命名，與當地原有的稱呼毫無關係",
]
WRONG_FB = ["……不是這個。仔細想想剛剛那段話，答案就藏在裡面。","再猜一次！別被似是而非的說法騙了。","灰霧又濃了一點……再回想一下剛剛聽到的內容吧。"]
SCENES = [("🌾","田|野|原|畑"),("⛰️","山|嶽|岳|嶺|峰"),("🌊","海|灣|港|浦|島|濱"),("💧","川|河|湖|沼|沢|澤|澗"),("🏯","城|館|宿|町|市")]
def scene_for(t):
    for e, pat in SCENES:
        if re.search(pat, t): return e
    return "🌫️"
def split_detail(t, lim=110):
    sents = re.findall(r'[^。]+。?', t)
    out, cur = [], ""
    for s in sents:
        if cur and len(cur)+len(s) > lim: out.append(cur); cur = s
        else: cur += s
    if cur: out.append(cur)
    return out
def quiz_for(pid, p):
    n, pref, short = p['n'], p['c'], p['d']
    rnd = random.Random(pid*7919+13)
    dec = rnd.sample(DECOYS, 3)
    opts = dec + [short]
    rnd.shuffle(opts)
    return dict(q="關於「%s」（%s）這個地名，下列何者才是真正的由來？" % (n, pref),
                opts=opts, correct=opts.index(short),
                rightFb="沒錯！" + short, wrongFb=WRONG_FB[pid % len(WRONG_FB)])
def stop_for(pid, p, guide):
    pages = ["你知道『%s』這個地方，是怎麼來的嗎？%s" % (p['n'], p['d'])] + split_detail(p['detail'] or p['d'])
    return dict(placeId=pid, npcName=guide['name'], npcIcon=guide['icon'], sceneEmoji=scene_for(p['n']+p['d']),
                pages=pages, quiz=quiz_for(pid, p))
def gen_content(places, guides, prefs, flagship_ids):
    # places: list of dict(id,c,n,o,d,detail)
    out = {}
    for pref in prefs:
        mine = [p for p in places if p['c'] == pref and p['id'] not in flagship_ids]
        g = guides.get(pref)
        main, side = [], []
        if g and mine:
            groups = [mine[i:i+4] for i in range(0, len(mine), 4)]
            nmain = (len(groups)+1)//2
            for gi, grp in enumerate(groups):
                kind = "main" if gi < nmain else "side"
                lst = main if kind == "main" else side
                names = "、".join(x['n'] for x in grp)
                out_id = "%s-%s-%d" % (kind, pref, len(lst)+1)
                lst.append(dict(id=out_id, title="%s．%s至%s" % (pref, grp[0]['n'], grp[-1]['n']), kind=kind,
                    opening=g['open'].replace("{names}", names), closing=g['close'],
                    placeIds=[x['id'] for x in grp], stops=[stop_for(x['id'], x, g) for x in grp]))
        out[pref] = dict(mainChains=main, sideQuests=side[:3])
    return out
