# -*- coding: utf-8 -*-
# 依「玩家 × 區域」組裝的主角專屬劇本：greet（進入該區的相遇）／farewell（道別＋帶話）／errand（在後面的區域傳達帶話）
import content as C, protagonist as PR

CH = {c["key"]: c for c in C.PLAYER_CHARS}
ORDER = ["north", "central", "south", "east", "island"]
LOCAL = {"north": ["hanlin","shiaolan"], "central": ["poyu","sihyu"], "south": ["zihchian","wanjhen"], "east": ["lali","kerou"], "island": ["jianlin","jiaen"]}
REGION_OF = {k: r for r, ks in LOCAL.items() for k in ks}

def rel(a, b):
    A, B = CH[a], CH[b]
    if A["friend"].find(B["name"]) >= 0 or B["friend"].find(A["name"]) >= 0: return "friend"
    if A["rival"].find(B["name"]) >= 0 or B["rival"].find(A["name"]) >= 0: return "rival"
    return "stranger"

def pron(text, listener):            # 依聽話者性別統一你／妳（「你們／妳們」不動）
    import re
    g = CH[listener]["gender"]
    if g == "f": return re.sub(r"你(?!們)", "妳", text)
    return re.sub(r"妳(?!們)", "你", text)

OPEN = {  # 本區同伴對玩家說的第一句（依關係）
 "hanlin":  {"friend":"欸！你怎麼也跑來啦！我在函館等你好久了！","rival":"（瞪大眼睛）……你怎麼會出現在我的地盤！下次運動會，我一定贏你！","stranger":"嗨！我是山本大翔，大家都叫我小翔！函館港是我的地盤，你要不要我帶你逛逛？"},
 "shiaolan":{"friend":"……你來了。我在筆記本裡，幫你留了一頁。","rival":"……你也來了。我的觀察日記，這次不會輸。","stranger":"……你好，我是佐藤美咲。喜歡畫速寫，還有記筆記。"},
 "poyu":    {"friend":"喂，你怎麼來東京了？我還以為你被攻略卡住了。","rival":"哼，你也來了？線上打過，現實裡，還是頭一次見面。","stranger":"喔，你好。我是田中蓮，玩遊戲的。地名這種事，就當作現實世界的支線任務吧。"},
 "sihyu":   {"friend":"哇！你終於來了！我等你好久，正好缺一位攝影師！","rival":"（雙手抱胸）……哼，你也來東京了？才藝比賽，我不會讓的！","stranger":"嗨！我是鈴木陽菜，大家都叫我小陽！要不要一起跳一段？"},
 "zihchian":{"friend":"你來了。這一區的碑文，我抄了一半，剛好缺你的眼睛。","rival":"……你也來查這件事？資料有沒有出處，我可是會核對的。","stranger":"你好，我是高橋悠真。地名這種事，就該一字一句查清楚。"},
 "wanjhen": {"friend":"咦，你來了！我剛做好和菓子，正好給你試吃！","rival":"呵呵，你也來京都了？點心跟才藝，我都不會輸的喔。","stranger":"你好，我是伊藤結衣，愛做點心的人。要不要吃一個？"},
 "lali":    {"friend":"……你來了。阿蘇的風，一直在等你。","rival":"……你也來了。長跑，這次不會輸。","stranger":"……你好。渡邊颯太。阿蘇的路，我熟。"},
 "kerou":   {"friend":"哇！你來了！我在唱一首新歌，正好缺一位聽眾！","rival":"咦？你也來阿蘇了？鄉土語文，我不會輸的喔！","stranger":"你好！我是小林心春，大家都叫我心春！你聽過阿蘇的童謠嗎？"},
 "jianlin": {"friend":"欸欸，你來啦！退潮了，快，我們去抓螃蟹！","rival":"（賊笑）喔，你就是那個線上一直嘴我的？終於見到本人了！","stranger":"嘿！我是比嘉海斗，大家都叫我海斗！這一帶的礁石，我全都認得！"},
 "jiaen":   {"friend":"……你來了。我的地名冊，寫到第三本了。","rival":"……你來了。縣賽的作文，我會拿第一。","stranger":"……你好。我是仲村美海，收集貝殼，也收集地名。"},
}
REPLY = {  # 玩家的回應（依玩家個性 × 關係）
 "hanlin":  {"friend":"哈，我也是！一起把這一區的地名都找回來吧！","rival":"別緊張，我不是來比賽的。不過有機會的話，我也不會輸！","stranger":"你好，我是山本大翔！請多指教，一起找地名吧！"},
 "shiaolan":{"friend":"……嗯，我來了。這次，我也想記很多。","rival":"……我也不會輸。","stranger":"……你好，我是佐藤美咲。請多指教。"},
 "poyu":    {"friend":"被攻略卡住？我是來刷支線的。","rival":"……哼，那就現實裡，再比一場。","stranger":"田中蓮。地名任務，我接了。"},
 "sihyu":   {"friend":"來啦來啦！攝影師的位子，我幫你留著了！","rival":"哼，我才不會輸呢！走著瞧！","stranger":"你好！我是鈴木陽菜，請多指教！"},
 "zihchian":{"friend":"好。抄到一半的，我來核對。","rival":"資料我有，出處我也有。請別急著下結論。","stranger":"高橋悠真。請多指教，資料我會核對。"},
 "wanjhen": {"friend":"太好了，我正好肚子餓！","rival":"呵呵，我也不會輸的喔。","stranger":"你好，我是伊藤結衣，請多指教。"},
 "lali":    {"friend":"……嗯。我來了。","rival":"……不會輸。","stranger":"……渡邊颯太。請多指教。"},
 "kerou":   {"friend":"好啊好啊！我最愛聽新歌了！","rival":"我才不會輸呢！走著瞧！","stranger":"你好！我是小林心春，請多指教！"},
 "jianlin": {"friend":"好耶！螃蟹我來抓，桶子你拿！","rival":"哈！終於見到本人了！比一場吧！","stranger":"我是比嘉海斗，請多指教！這一帶我可以當嚮導喔！"},
 "jiaen":   {"friend":"……嗯。我也帶了新的剪報。","rival":"……我也不會輸。","stranger":"……仲村美海。請多指教。"},
}
VISIT = {
 "north": "津輕海峽的海風迎面吹來，你才剛踏進函館，港邊就有兩道身影朝你這裡靠近。",
 "central": "東京下町的巷口，一陣手遊的按鍵聲和一段熱舞的節奏，同時朝你這裡靠近。",
 "south": "京都的石板路上，一位捧著舊書、一位端著和菓子的身影，同時注意到了你。",
 "east": "阿蘇的火山風迎面吹來，兩道身影已經出現在你面前——一個安靜寡言，一個笑聲清亮。",
 "island": "退潮的潮間帶上，兩個蹲在礁石邊嘻嘻鬧鬧的身影，被你的腳步聲吸引，回過頭來。"}

# 跨區「帶話」：只發生在彼此是競爭對手、且住在不同區的兩人之間。(說話者, 對象): (託付內容, 對象的回應)
MSG = {
 ("hanlin","lali"):   ("下次運動會，一千五百公尺，我一定贏你！","……來啊。我在阿蘇等。"),
 ("lali","hanlin"):   ("……跟他說，我不會輸。","哈！叫他放馬過來！我天天在練！"),
 ("shiaolan","jiaen"):("……我的地名冊，寫得比妳的久。","……作文比賽見。我的，更厚。"),
 ("jiaen","shiaolan"):("……我的地名冊，這次多了三十頁。","……我也是。三十一頁。"),
 ("shiaolan","kerou"):("……鄉土語文，這次我會寫得更好。","我會唱得更好聽！跟她說，走著瞧！"),
 ("kerou","shiaolan"):("跟她說：這次我唱得更好聽！","……我把文章，寫得更好。"),
 ("poyu","jianlin"):  ("線上遊戲，今晚再打一場，輸的請客。","哈！我這次一定贏！叫他別遲到！"),
 ("jianlin","poyu"):  ("叫那個東京來的洗好脖子等我！這次我一定贏！","……哼，來啊。我又不怕。"),
 ("sihyu","wanjhen"): ("熱舞社今年一定搶到社辦！","呵呵，烹飪社，也不會讓的喔。"),
 ("wanjhen","sihyu"): ("新的點心，我做好了，等她來認輸。","哈！我才不認輸，我跳給她看！"),
}

def steps_of(pairs): return [[a, b] for a, b in pairs]

def build_for(P):
    me = CH[P]; route = ORDER[ORDER.index(me["region"]):] + ORDER[:ORDER.index(me["region"])]
    out = {}
    delivered = set()
    for ri, rid in enumerate(route):
        last = (ri == len(route) - 1)
        locals_ = [k for k in LOCAL[rid] if k != P]
        if not locals_: continue
        sc = {}
        # ---- greet ----
        g = []
        g.append(["n", VISIT[rid] if len(locals_) == 2 else C.REGION_MEET_NARRATION[rid]])
        for j, k in enumerate(locals_):
            r = rel(P, k)
            g.append([k, pron(OPEN[k][r], P)])
            if j == 1 and r == "stranger" and rel(P, locals_[0]) == "stranger":
                g.append(["me", "（也向另一位點了點頭）請多指教。"])
            else:
                g.append(["me", pron(REPLY[P][r], k)])
        if len(locals_) == 2:
            for ln in PR.PAIR_INTERACT.get("_".join(locals_) if "_".join(locals_) in PR.PAIR_INTERACT else "_".join(reversed(locals_)), []):
                g.append([ln["spk"], ln["text"]])
        names = "、".join(CH[k]["name"] for k in locals_)
        g.append(["mentor", "既然有緣同路，%s，就讓%s陪%s，一起把這段地名記憶找回來吧。" % (names, "你" if len(locals_) == 1 else "你們", me["name"])])
        sc["greet"] = g
        # ---- farewell（含帶話）----
        f = []
        for k in locals_:
            r = rel(P, k)
            v = PR.FAREWELL[k][r]["last" if last else "mid"]
            for ln in v:
                if ln["spk"] == "me": f.append(["me", pron(ln["text"], k)])
                else: f.append([k, pron(ln["text"], P)])
            # 帶話：k 對某位「競爭對手、住在之後的區域」的託付
            if not last:
                for (a, b), (msg, _) in MSG.items():
                    if a == k and b != P and b in REGION_OF and route.index(REGION_OF[b]) > ri and (a, b) not in delivered:
                        f.append([k, pron("對了，幫我轉告%s：「%s」" % (CH[b]["name"], msg), P)])
                        f.append(["me", pron("……好，我幫你帶到。", k)])
                        delivered.add((a, b))
        sc["farewell"] = f
        out[rid] = sc
    # ---- errand：在收件人所在的區域，傳達之前收到的託付 ----
    for (a, b) in delivered:
        rid = REGION_OF[b]
        msg, reply = MSG[(a, b)]
        e = out[rid].setdefault("errand", [])
        e.append(["me", pron("（想起來）對了，%s要我轉告你：「%s」" % (CH[a]["name"], msg), b)])
        e.append([b, pron(reply, P)])
    return out

PLAYER_MAIN_SCRIPTS = {k: build_for(k) for k in CH}


# ---- 每一站測驗後，玩家依個性說的一句反應（站序需與 REGIONS 的 stops 順序一致）----
HOOKS = {
 "north":   ["「カイ」——生於此地的人","箱館與函館","乾涸的大河","青色的森林","岩石上的手印","千代與仙台"],
 "central": ["荊棘築成的城","入江的入口","橫向的沙洲"],
 "south":   ["新的潟","洗出金砂的泉水","岐山與曲阜","多說並存的奈良","都都相疊的京都","坂與阪"],
 "east":    ["八雲立つ","廣島的兩種說法","愛比売","搬了家的福岡","長長的岬","隈與熊"],
 "island":  ["外面取的琉球","阿兒奈波","漂在海上的浮島"],
}
TPL = {
 "hanlin":  ["「{h}」啊！這個我要記住，回去講給大家聽！","「{h}」！好熱血的故事，我一口氣就記住了！","聽完「{h}」，我又想衝去下一站了！"],
 "shiaolan":["……「{h}」，我寫在筆記本上了。","……「{h}」，我想畫成一頁。","……「{h}」，我會慢慢記住。"],
 "poyu":    ["「{h}」……這條資料，我存檔了。","「{h}」，比攻略本寫的還精彩，算你們厲害。","行，「{h}」這條支線，我記下了。"],
 "sihyu":   ["「{h}」唸起來好有節奏！我要編進舞步裡！","「{h}」！這個故事我要拍成短影片！","哇，「{h}」，我要說給熱舞社的大家聽！"],
 "zihchian":["「{h}」，出處已記錄，回去我再核對一次。","「{h}」……說法不只一種，我要並列記錄。","「{h}」，有憑有據，可以收進筆記。"],
 "wanjhen": ["「{h}」……這個故事，我想說給點心舖的老闆聽。","「{h}」，聽完好像肚子都餓了呢。","「{h}」，我要把它寫進我的食記裡。"],
 "lali":    ["……「{h}」。土地記得的事，比我們想的還多。","……「{h}」。爺爺說得對，名字就是地圖。","……「{h}」。我記住了。"],
 "kerou":   ["「{h}」！這個我要編成歌！","「{h}」，唱起來一定很好聽！","哇，「{h}」，我要唱給奶奶聽！"],
 "jianlin": ["「{h}」？哈，這個故事比我想的還酷！","「{h}」……我回去一定要跟大家吹噓。","「{h}」！下次退潮，我們去找找看有沒有更多故事！"],
 "jiaen":   ["……「{h}」，我收進地名冊了。","……「{h}」，跟我蒐集的資料對得上。","……「{h}」，比課本教的有意思多了。"],
}
PLAYER_STOP_LINES = {}
for P in CH:
    PLAYER_STOP_LINES[P] = {r: [TPL[P][i % 3].format(h=h) for i, h in enumerate(hs)] for r, hs in HOOKS.items()}
