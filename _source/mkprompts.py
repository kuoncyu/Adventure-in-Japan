# -*- coding: utf-8 -*-
STYLE = ("hand-painted watercolor and fine ink line illustration, storybook style for a children's educational adventure game, "
         "warm textured paper grain, soft pastel washes with delicate ink outlines, gentle rim light, rich but harmonious colors")
COMP = ("wide landscape composition (16:9), character shown from the waist up or three-quarter view and centered, "
        "face large, clearly visible and unobstructed in the upper-middle of the frame, "
        "surrounded by 3 to 5 small themed props and scenery elements that fit inside one irregular torn-paper and ink-splatter cloud-shaped vignette, "
        "everything outside the vignette is plain pure white background, no text, no letters, no logos, no watermark, no frame, "
        "correct anatomy, natural hands")
NEG = "Avoid: text, captions, signatures, watermark, extra fingers, distorted hands, photorealism, 3D render, heavy black background."

groups = []
def G(title, note, items): groups.append((title, note, items))

# key, 名稱, 中文簡述, 英文角色描述
G("一、主角群（10 位・小學六年級）",
  "年齡約 12 歲的日本小學生，服裝要素簡單、乾淨、適合兒童，表情與姿勢要符合各自個性。檔名請沿用括號內的代號。",
  [
   ("hanlin","山本大翔","函館港町長大、活潑外放的棒球少年",
    "a cheerful 12-year-old Japanese boy, spiky short black hair, tanned skin, huge laughing grin with one arm raised waving, wearing a navy hooded jacket with a small anchor emblem over a baseball undershirt and shorts, carrying a baseball glove and a bat over the shoulder. Scenery: Hakodate harbor with red-brick warehouses, harbor cranes, seagulls, Mount Hakodate in the distance, a few scattered baseball cards"),
   ("shiaolan","佐藤美咲","害羞內向、愛畫速寫的女孩",
    "a shy 12-year-old Japanese girl, black bob haircut with a small hairclip, gentle timid smile, hugging a sketchbook to her chest, wearing a cream cardigan over a white blouse and a plaid skirt, a pencil behind the ear. Scenery: a slope street in Hakodate with old Western-style wooden houses, an old streetcar (tram) on a hill, pencil sketches and tram tickets floating around"),
   ("poyu","田中蓮","嘴利、腦筋快的手遊少年",
    "a sarcastic clever 12-year-old Japanese boy, slightly messy dark hair, half-lidded smirking eyes, wearing a loose gray hoodie, holding a handheld game console in one hand and a small mecha model kit in the other. Scenery: Tokyo downtown (shitamachi) rooftops, Tokyo Skytree in the distance, a vending machine, arcade-style glowing signs (no readable text)"),
   ("sihyu","鈴木陽菜","愛跳街舞的班長",
    "an energetic 12-year-old Japanese girl, high ponytail with a colorful scrunchie, bright confident smile, striking a street-dance pose, wearing a cropped jacket, T-shirt, shorts and sneakers, a smartphone on a mini tripod nearby. Scenery: a Tokyo shopping street with paper lanterns, cherry blossom petals, colorful stickers floating around"),
   ("zihchian","高橋悠真","一板一眼的歷史迷男孩",
    "a serious studious 12-year-old Japanese boy, neat black hair, round glasses, white short-sleeve shirt and navy shorts, backpack straps, a magnifying glass hanging from a cord, raising one index finger as if explaining, an old bound book under the other arm. Scenery: Kyoto Nishijin old machiya wooden townhouses, a stone shrine monument, shogi pieces and old maps"),
   ("wanjhen","伊藤結衣","溫和、愛做和菓子的女孩",
    "a gentle 12-year-old Japanese girl, long hair in a loose low braid tied with a ribbon, warm smile, wearing a simple casual dress with a cute apron, holding a small wooden tray of colorful wagashi sweets, a small notebook in her apron pocket. Scenery: a Kyoto shopping arcade with noren curtains, a traditional sweets shop, cherry blossoms"),
   ("lali","渡邊颯太","沉默寡言的長跑少年",
    "a quiet athletic 12-year-old Japanese boy, short dark hair with a sports headband, calm steady gaze, wearing a running shirt, shorts and trail shoes, a small worn backpack. Scenery: the vast grassland of Aso caldera in Kumamoto, Mount Aso smoking gently in the distance, grazing red-brown cattle, wind-swept grass"),
   ("kerou","小林心春","開朗愛唱歌的女孩",
    "a cheerful 12-year-old Japanese girl, short twin pigtails, mouth open singing happily, wearing a light padded hanten jacket over a simple dress, carrying a small basket of wild mountain vegetables, musical notes floating around. Scenery: Aso grassland with wildflowers, a small roadside shrine, gentle mountains"),
   ("jianlin","比嘉海斗","古靈精怪的沖繩海邊男孩",
    "a mischievous 12-year-old Okinawan boy, tanned skin, messy hair, cheeky grin, a skateboard under one arm, holding a small bucket with a crab, wearing a bright short-sleeve shirt and shorts, barefoot or in sandals. Scenery: a low-tide reef flat in Okinawa, a shisa lion-dog statue, red-tile roofs, a coral stone wall, hibiscus flowers"),
   ("jiaen","仲村美海","冷靜早熟的貝殼收集女孩",
    "a calm mature-for-her-age 12-year-old Okinawan girl, long straight black hair, quiet thoughtful expression, holding a conch shell in one hand and a small notebook in the other, wearing a light blue sleeveless dress. Scenery: Naha harbor at dusk with a starry sky, seashells, hibiscus, a stone lantern"),
  ])

G("二、導師與夥伴（7 位）","成年角色，畫風同上，要有各自的職業感與親切感。",
  [
   ("mentor","苔野婆婆","羅盤的守護者，住在神社大樟樹根裡",
    "an ancient tiny grandmother spirit with long silvery hair naturally intertwined with green moss and small leaves, kind wrinkled smiling eyes, wearing a moss-green kimono-like robe, holding a small glowing compass. Scenery: the roots of a giant camphor tree at a shrine, a shimenawa rope, a stone lantern, fireflies"),
   ("ahai","岩城源三","函館討海五十年的老漁夫",
    "an elderly Japanese fisherman, weathered tanned face, short white stubble, white cloth headband (hachimaki), navy padded fisherman's coat, laughing loudly with a hearty expression, holding a glass fishing float. Scenery: Hakodate harbor, squid-fishing boats with lanterns, Mount Hakodate, seagulls"),
   ("chianma","結城千夏","跑遍關東的民俗調查員",
    "a young Japanese woman ethnographer around 24 years old, short ponytail, curious bright eyes, wearing a field vest over a plain shirt, holding a notebook and a small voice recorder, a camera bag on her shoulder. Scenery: a Kanto plain river levee, a thatched old farmhouse, rice fields, a village elder's silhouette"),
   ("wenlan","藤原文彥","京都出身的古文書考據生",
    "a refined young Japanese scholar around 22 years old, round glasses, neat black hair, wearing a high-collared white shirt and vest with a light haori jacket, holding a bundle of old bound manuscripts and a brush, thoughtful serious expression. Scenery: an old Kyoto library with scrolls, wooden shelves, a stone garden lantern"),
   ("lahok","小野岳","阿蘇山麓的山林嚮導",
    "a lean calm young Japanese mountain guide around 23 years old, tanned skin, a headband, wearing a simple outdoor jacket and pants, a large backpack, a wooden walking staff, binoculars around the neck, steady quiet expression. Scenery: Aso and Kuju mountains, forest trail, morning mist"),
   ("phoasoh","與那嶺千代","久高島出身的漁婦兼祭祀助手",
    "a warm friendly Okinawan woman around 50 years old, wearing a light Ryukyu-style bingata-patterned apron and a headscarf, holding a woven fishing basket, smiling kindly. Scenery: an Okinawan sacred grove (utaki) with sea behind, a shisa statue, red-tile roofs, hibiscus"),
   ("keshian","久保田誠","帶著祖父土地台帳的土地家屋調查士",
    "a serious young Japanese land surveyor around 24 years old, glasses, tidy short hair, beige field jacket, a leather satchel, holding an old Meiji-era bound land ledger, a surveying tripod beside him, skeptical but sincere expression. Scenery: old cadastral maps, survey boundary markers, a rural road"),
   ("wangmingyao","忘名妖（反派）","吞噬地名記憶的灰霧精怪（可沿用現有圖）",
    "a mysterious swirling gray fog spirit whose smoke forms a faint eerie face with hollow eyes, drifting wisps and fading kanji-like brush strokes (illegible), silvery gray and sepia tones, slightly menacing but not scary for children. Scenery: withering leaves, faded old paper, mist"),
  ])

G("三、故事旗艦站 NPC（12 位・目前已用到）","每個地名旗艦站的說書人。多為精怪、傳說人物或老者。",
  [
   ("npc_kitakai","北加伊之魂","北海道旗艦站：北海道名稱的由來",
    "a dignified elderly Ainu elder spirit rendered respectfully and with cultural accuracy (traditional Ainu embroidered robe and headband with authentic-style patterns, please consult references), semi-transparent, swirling snow around him, calm wise expression. Scenery: snowy Hokkaido plains, a river, a wooden ritual stick (inau), a flying salmon"),
   ("npc_usukeshi","宇須岸爺","函館旗艦站：宇須岸→箱館→函館",
    "an old harbor sage spirit with a friendly weathered face, wearing a sailor's happi coat, holding a small square wooden box, a paper lantern hanging beside him. Scenery: Hakodate bay at dusk, an old wooden sailing ship, box-shaped fortress silhouette on the shore"),
   ("npc_toyohira","豐平川之魂","札幌旗艦站：乾涸的大河",
    "a graceful river spirit woman made of flowing translucent water and reeds, long hair like streams, half of her form dry riverbed pebbles, half flowing water, gentle expression. Scenery: Sapporo river with reeds, autumn leaves, a faint city grid in the distance"),
   ("npc_tsugaru","津輕港的老領航","青森旗艦站：青き森",
    "a gruff kind old harbor pilot with a peaked cap, binoculars and a pipe, sea-weathered face. Scenery: Aomori harbor with a small lighthouse, a green forest landmark on the shore, red apples, seagulls"),
   ("npc_mitsuishi","三ツ石的岩神","岩手旗艦站：岩手的鬼手印傳說",
    "a stone deity spirit formed from three huge moss-covered boulders with a calm carved face emerging from the rock, a giant oni handprint pressed into the stone, gentle stern expression. Scenery: a shrine rope (shimenawa) around the rocks, misty forest, an oni's horn silhouette in the fog"),
   ("npc_aoba","青葉山的武者魂","仙台旗艦站：千代→仙台",
    "a noble samurai spirit in black-and-gold armor with a crescent moon ornament on the helmet, translucent glowing edges, a calm proud expression. Scenery: Aoba mountain, Sendai castle stone walls, bamboo, a bright crescent moon, tanabata-style streamers"),
   ("npc_ibara","荊棘之靈","茨城旗艦站：以荊棘築城",
    "a forest thorn spirit woven from brambles and wild roses, with a mysterious face in the vines, small white wild rose blossoms and thorns forming a small castle wall around it. Scenery: an ancient Kanto plain, cave openings, misty hills"),
   ("npc_edo","江戶古地圖師","東京旗艦站：江戶＝入江的入口",
    "an old Edo-period cartographer with round glasses and a topknot, holding a large old map scroll and an ink brush, kind wise expression. Scenery: the old Edo Bay coastline, Edo castle, sailing boats, waves drawn like an old woodblock map"),
   ("npc_hama","濱邊的燈台守","橫濱旗艦站：橫向的濱",
    "a friendly lighthouse keeper in a dark uniform and cap, holding a glowing lantern, bearded smiling face. Scenery: Yokohama bay at dusk, a small lighthouse, red-brick warehouses, an old black steamship on the water"),
   ("npc_shinano","信濃川的潟守","新潟旗艦站：新的潟",
    "a lagoon keeper spirit wearing a straw raincoat (mino) and a straw hat, calm watery expression, reeds growing from his sleeves. Scenery: the Shinano river mouth with sandbars, wetlands, swans, a sunset"),
   ("npc_fujigoro","金洗沢的藤五郎","金沢旗艦站：金洗沢",
    "a poor but cheerful potato-digger named Togoro, patched work clothes, a woven basket of wild yams, kneeling by a clear spring with gold flakes glittering in the water. Scenery: a mountain spring, old Kanazawa castle in the distance, gold leaf sparkles"),
   ("npc_sawahiko","沢彥和尚","岐阜旗艦站：井ノ口→岐阜",
    "a wise Zen monk with a shaved head, black robe, wooden prayer beads, holding a calligraphy brush (no legible writing, just brush strokes), calm smiling eyes. Scenery: Gifu mountain castle on a hill, a Zen temple gate, cherry blossoms, morning mist"),
  ])

G("四、縣嚮導（目前 23 位；其餘縣於後續批次補上）","每縣一位在地嚮導，多為 10～14 歲孩子或長者，並帶有該縣特色小物件。",
  [
   ("guide_hokkaido","貝澤凜","北海道：阿伊努族說書少女",
    "an Ainu girl around 12 years old, depicted respectfully and with cultural accuracy (please consult references for authentic Ainu embroidery patterns on the headband and clothing), soft gentle smile. Scenery: a snowy riverbank in Hokkaido, a leaping salmon, a wooden hut (chise) roof, falling snow"),
   ("guide_aomori","工藤湊","青森：蘋果與港口少年",
    "a sunburned boy around 12 years old with short dark hair, holding a red apple in one hand and a rope in the other, wearing a yellow windbreaker. Scenery: Aomori harbor, apple orchard, Mount Iwaki in the distance"),
   ("guide_iwate","小岩茜","岩手：南部鐵壺少女",
    "a warm shy girl around 12 years old with a hair bun, wearing a kimono-style casual top, holding a small black cast-iron kettle with steam. Scenery: Morioka old street, Tono valley hills, a tiny kappa silhouette in the reeds"),
   ("guide_miyagi","佐佐木七夏","宮城：七夕祭文史少女",
    "a poised girl around 13 years old with shoulder-length hair, neat blazer-style jacket, warm smile, colorful tanabata paper streamers hanging around her. Scenery: Sendai Aoba castle silhouette, a crescent moon, ginkgo trees"),
   ("guide_akita","小玉大地","秋田：雪國野孩子",
    "a blunt spirited boy around 12 years old with a worn knit hat, red cheeks, thick winter coat, snow on the shoulders. Scenery: snowy Akita village with kamakura snow huts, an Akita dog, a hint of a Namahage demon mask in the background (friendly, not scary)"),
   ("guide_yamagata","最上光","山形：花笠祭的和藹阿婆",
    "a kind elderly grandmother around 70 years old with a floral embroidered headscarf, gentle smile, holding safflower flowers. Scenery: Yamagata safflower fields, Zao snow monster trees in the distance, a hanagasa festival hat"),
   ("guide_fukushima","白川文哉","福島：會津史學少年",
    "a quiet bookish boy around 13 years old with glasses, wearing a school-style jacket, holding a stack of old books. Scenery: Aizu Tsuruga castle, a red ox (akabeko) toy, fluffy clouds"),
   ("guide_ibaraki","水野隼人","茨城：納豆之鄉的少年",
    "a straightforward loud-voiced boy around 12 years old with short hair, a farm work apron, holding a bundle of rice-straw natto. Scenery: rice fields, Mount Tsukuba, plum blossoms of Kairakuen"),
   ("guide_tochigi","日向いろは","栃木：日光傘下少女",
    "a graceful polite girl around 12 years old with long black hair, holding a hand-painted oil-paper umbrella, bowing slightly. Scenery: Nikko shrine gate and stone lanterns, a waterfall, autumn maple leaves"),
   ("guide_gunma","湯川ゆの","群馬：溫泉鄉的女孩",
    "a cheerful girl around 12 years old with a straw hat, a towel around her neck, holding a wooden bath bucket, laughing while pinching her nose. Scenery: Kusatsu onsen wooden yubatake channels with steam, mountain ridges"),
   ("guide_saitama","氷川さくら","埼玉：櫻花髮飾少女",
    "a gentle tidy girl around 12 years old with a cherry blossom hairpin, holding handwritten index cards. Scenery: a long shrine approach with a torii, Kawagoe old storehouse street, cherry blossoms"),
   ("guide_chiba","安房真凜","千葉：房總海邊女孩",
    "a lively adventurous girl around 12 years old with a flower-decorated sun hat, tanned skin, a cheerful wave. Scenery: Boso peninsula coast, flower fields, a lighthouse, sea breeze"),
   ("guide_tokyo","千代田進","東京：江戶前少年",
    "a calm observant boy around 12 years old with a navy cap, wearing a school-style jacket, looking down at an old stone monument. Scenery: Tokyo Station red brick building, Tokyo Skytree, an old wooden bridge"),
   ("guide_kanagawa","港南海人","神奈川：橫濱港少年",
    "a cheerful talkative boy around 13 years old wearing a baseball cap backwards, a windbreaker, gesturing excitedly with both hands. Scenery: Yokohama bay, red-brick warehouses, a Ferris wheel, seagulls"),
   ("guide_niigata","笹川雪乃","新潟：越後雪國少女",
    "a calm gentle girl around 12 years old wearing a thick red scarf and a padded coat, snowflakes on her hair. Scenery: a snowy rice field with straw racks, a distant mountain, footprints in the snow"),
   ("guide_toyama","立野陽介","富山：賣藥人的後代",
    "a friendly talkative boy around 12 years old carrying a small old wooden medicine box on his back, a warm salesman-like smile. Scenery: Tateyama mountain range with snow, a traditional old street, medicine packets"),
   ("guide_ishikawa","金森紗月","石川：金箔工房少女",
    "an elegant quiet girl around 13 years old with hair pinned up, fingertips dusted with gold leaf, gentle smile. Scenery: Kanazawa old teahouse street, Kenrokuen garden, floating gold leaf sparkles"),
   ("guide_fukui","朝倉和真","福井：恐龍化石少年",
    "an enthusiastic curious boy around 12 years old with a backpack covered in dinosaur badges, holding a small fossil and a mini pickaxe. Scenery: Fukui cliffs by the sea (Tojinbo), a dinosaur skeleton silhouette, a crab"),
   ("guide_yamanashi","甲斐峻","山梨：富士山下的少年登山者",
    "a calm sturdy boy around 13 years old with a headlamp strapped to his forehead, hiking clothes and a backpack, steady eyes. Scenery: Mount Fuji at dawn, Lake Kawaguchi, vineyards"),
   ("guide_nagano","諏訪信也","長野：信州山林少年",
    "a bookish earnest boy around 13 years old with a big backpack, holding a small notebook full of notes. Scenery: the Japanese Alps, Matsumoto castle, Zenko-ji temple, a soba field in bloom"),
   ("guide_gifu","飛騨花乃","岐阜：合掌造村的女孩",
    "a cheerful nimble girl around 12 years old with an embroidered headband, wearing a simple traditional-inspired top, laughing brightly. Scenery: Shirakawa-go thatched gassho-style houses, cormorant fishing boats on a river, misty mountains"),
   ("guide_shizuoka","牧野茶々","靜岡：茶園少女",
    "a gentle slow-speaking girl around 12 years old wearing a tea-picking straw hat and apron, holding a small basket of fresh tea leaves. Scenery: rows of green tea fields with Mount Fuji behind, morning mist"),
   ("guide_aichi","尾張拓海","愛知：工業之都少年",
    "a practical handy boy around 12 years old with a screwdriver in his pocket, holding a small gear, a work-cap on his head, confident grin. Scenery: Nagoya castle with golden shachihoko, machinery parts, gears"),
  ])


groups[2][2].extend([
   ("npc_heijo","平城京的舍人","奈良旗艦站：奈良語源多說並存",
    "an old Nara-period court attendant spirit (toneri) in a pale green Nara-era court robe with a black cap, holding a wooden tablet (mokkan) and a scroll, gentle wise smile, semi-transparent edges. Scenery: Heijo-kyo Suzaku avenue, a vermilion gate, a friendly deer, cedar trees"),
   ("npc_rakuchu","洛中的古老","京都旗艦站：京＝都",
    "a dignified old Kyoto elder in a dark kimono and haori, holding a folding fan and a paper lantern, calm refined expression. Scenery: a Kyoto machiya alley at dusk, a stone lantern, cherry blossoms, the grid pattern of the old capital faintly drawn like a map"),
   ("npc_rennyo","石山的蓮如上人","大阪旗艦站：大坂→大阪",
    "a kind elderly Buddhist monk in a plain dark robe and a purple stole, prayer beads in hand, gentle compassionate smile, semi-transparent edges. Scenery: a hilltop temple on the Uemachi plateau, a big slope leading down to the sea, an old castle wall, fluttering banners without text"),
])
groups[3][2].extend([
   ("guide_mie","磯部波留","三重：伊勢志摩的見習海女",
    "an energetic straightforward girl around 13 years old with a white diver's headscarf, tanned skin, holding a fishing net and a small basket of abalone, hearty laugh. Scenery: Shima rocky coast, Ise-Shima sea, a wedded-rock (Meoto Iwa) style pair of sea rocks, waves"),
   ("guide_shiga","浅井湖太","滋賀：琵琶湖的少年漁夫",
    "a gentle quiet boy around 12 years old with a straw hat, holding a wooden oar in a small boat, calm smile. Scenery: Lake Biwa calm surface like a mirror, a floating torii gate on the water, Hikone castle in the distance, reeds"),
   ("guide_kyoto","北野千早","京都：古都的小舞妓見習生",
    "a refined polite girl around 13 years old in a light pastel yukata, hair with a small kanzashi ornament, holding a folding fan, giving a slight bow (modest, child-appropriate, not a real geisha makeup). Scenery: Kyoto stone-paved alley, a vermilion torii tunnel, cherry blossom petals, a small tea house"),
   ("guide_osaka","難波笑太","大阪：相聲少年",
    "a chatty comedic boy around 12 years old with a big open grin, holding a boat of takoyaki (octopus balls) and gesturing with a skewer, wearing a casual jacket. Scenery: Dotonbori canal with big glowing mechanical crab and running-man style signs (no legible text), Osaka castle in the distance"),
   ("guide_hyogo","生田ひなた","兵庫：神戶爵士少女",
    "a lively musical girl around 13 years old with a short bob, holding a small trumpet under her arm, stylish vintage-inspired outfit, cheerful. Scenery: Kobe harbor tower silhouette, foreign-style hillside mansions (ijinkan), a jazz record, sea breeze"),
   ("guide_nara","春日鹿之介","奈良：鹿少年",
    "a laid-back slow-moving boy around 12 years old gently petting a small deer, wearing casual clothes, holding a few deer crackers, sleepy warm smile. Scenery: Nara Park lawn, a five-story pagoda, stone lanterns, morning mist"),
   ("guide_wakayama","紀伊茂吉","和歌山：蜜柑園的老爺爺",
    "a gentle elderly grandfather around 75 years old with a worn straw hat and a warm wrinkled smile, holding a couple of mandarin oranges, work clothes. Scenery: terraced mikan orchards on a hillside, the Kumano pilgrimage trail with cedar trees, the sea in the distance"),
])
groups[2] = ("三、故事旗艦站 NPC（15 位・目前已用到）", groups[2][1], groups[2][2])
groups[3] = ("四、縣嚮導（目前 30 位；其餘縣於後續批次補上）", groups[3][1], groups[3][2])

groups[2][2].extend([
   ("npc_yatsuka","八束水臣津野命","出雲旗艦站：八雲立つ出雲",
    "a giant benevolent Shinto deity of the sky and land, majestic robed figure with long hair tied in ancient mizura style, wearing ancient Japanese Kofun-period-inspired robes, a long rope in his hands (referring to the land-pulling myth), calm noble expression, semi-transparent edges blending into clouds. Scenery: layered towering clouds (yakumo), Izumo coast, a large shimenawa rope, a shrine roof"),
   ("npc_funamori","太田川的舟守","廣島旗艦站：廣島名稱的兩種說法",
    "a gentle old boatman in a dark work jacket and towel headband, holding a long bamboo pole on a small flat boat, kind wise eyes. Scenery: the delta of the Ota River splitting into several branches, calm water, a distant castle keep, a white dove flying"),
   ("npc_ehime","愛比売","愛媛旗艦站：愛比売（古事記國生神話）",
    "a graceful young goddess spirit in an ancient Japanese white-and-pink robe with flowing scarf (hire), long black hair decorated with citrus blossoms, warm smile, semi-transparent glowing edges. Scenery: Shikoku island shaped like a body with four faces drawn softly in the clouds, mandarin orange trees, the Seto Inland Sea"),
])
groups[3][2].extend([
   ("guide_tottori","砂川陸","鳥取：砂丘少年",
    "an adventurous cheerful boy around 12 years old with sandy dusty trousers and sandals, drawing a map in the sand with a stick, wearing a light cotton hat. Scenery: Tottori Sand Dunes with wind ripples, a camel silhouette, the Sea of Japan, a ripe nashi pear"),
   ("guide_shimane","八雲縁","島根：見習巫女少女",
    "a quiet gentle girl around 12 years old dressed in a simple child-sized white and vermilion shrine maiden (miko) outfit, a red string tied around her wrist, calm firm eyes. Scenery: Izumo Taisha giant shimenawa rope, layered clouds (yakumo), a stone lantern, Lake Shinji at dusk"),
   ("guide_okayama","吉備桃真","岡山：桃太郎的故鄉少年",
    "a brave cheerful boy around 12 years old with a small peach charm on his backpack, holding a peach, a Shiba Inu dog at his feet (Momotaro-inspired but modern child clothing). Scenery: peach orchard, Okayama castle black walls, Korakuen garden, rice fields"),
   ("guide_hiroshima","厳島楓","廣島：宮島的楓葉少女",
    "a kind earnest girl around 12 years old with a red maple leaf hairpin, gentle expression showing quiet care for peace, plain modest clothing. Scenery: Itsukushima Shrine floating torii at high tide, red maple leaves, deer at Miyajima, a small paper crane (subtle, respectful, no violent imagery)"),
   ("guide_yamaguchi","長門龍","山口：關門海峽少年",
    "a calm stubborn boy around 13 years old with short hair, windbreaker, looking out toward the sea with a steady gaze. Scenery: Kanmon Strait with the Kanmon Bridge, passing ships, a pufferfish lantern, Kintai Bridge arches in the distance"),
   ("guide_tokushima","阿波いつき","德島：阿波舞少女",
    "a lively rhythmic girl around 12 years old wearing a traditional Awa Odori dance outfit (yukata-style with a woven amigasa hat), mid-dance pose, big smile. Scenery: Naruto whirlpools, a summer festival street with lanterns (no text), indigo-dyed cloth"),
   ("guide_kagawa","讃岐大吾","香川：烏龍麵店的少年",
    "an enthusiastic talkative boy around 12 years old wearing a white apron and headband, holding a steaming bowl of udon noodles, flour on his cheek. Scenery: Kotohira-gu long stone steps, small green hills of Sanuki, an udon shop with noren curtain (no legible writing), the Seto Inland Sea"),
   ("guide_ehime","伊予柑奈","愛媛：蜜柑園少女",
    "a sweet cheerful girl around 12 years old with an orange headscarf, holding a basket of mandarin oranges, sunny smile. Scenery: terraced citrus orchards on a hillside by the Seto Inland Sea, Matsuyama castle in the distance, orange blossoms, Dogo Onsen tower"),
   ("guide_kochi","桂竜介","高知：鰹魚漁師少年",
    "a hearty bold boy around 13 years old with deeply tanned skin, wearing a fisherman's happi coat and holding a fishing pole and a bonito fish, roaring laugh. Scenery: Katsurahama beach with big Pacific waves, a crescent moon over the sea, a tall rocky cape, straw-grilled bonito flames in the corner"),
])
groups[2] = ("三、故事旗艦站 NPC（18 位・目前已用到）", groups[2][1], groups[2][2])
groups[3] = ("四、縣嚮導（目前 39 位；其餘縣於後續批次補上）", groups[3][1], groups[3][2])

groups[2][2].extend([
   ("npc_nakagawa","那珂川的渡守","福岡旗艦站：福岡與博多",
    "a cheerful old ferryman in a short work jacket and towel headband, holding a long bamboo pole, standing on a small flat boat, friendly weathered face, semi-transparent edges. Scenery: the Naka River between two townscapes (one old merchant port, one castle town), yatai food stall lanterns (no text), Hakata Bay"),
   ("npc_tsuji","長崎的通詞","長崎旗艦站：長い崎",
    "an Edo-period interpreter (tsuji) in a formal haori and hakama, holding a Dutch-style book and a quill, thoughtful smart expression, subtle mix of Japanese and Dutch fashion, semi-transparent edges. Scenery: Nagasaki harbor with a Dutch trading ship, Dejima fan-shaped island silhouette, slope streets, lanterns"),
   ("npc_kumamoto","熊本城的石垣守","熊本旗艦站：隈本→熊本",
    "a stern but kind old stonemason spirit in a dark work jacket, holding a wooden mallet and a stone chisel, strong arms, gentle eyes, semi-transparent edges blending into stone. Scenery: the curved fan-shaped stone walls of Kumamoto Castle (musha-gaeshi), the castle keep at sunset, camphor trees"),
])
groups[3][2].extend([
   ("guide_fukuoka","那珂ももか","福岡：博多屋台的少女",
    "a frank cheerful girl around 12 years old wearing an apron and a headband, holding a bowl of steaming tonkotsu ramen, big bright laugh. Scenery: a Hakata yatai food-stall street at night with warm lanterns (no readable text), Fukuoka Tower in the distance"),
   ("guide_saga","有田陶太","佐賀：陶瓷工房少年",
    "a focused quiet boy around 12 years old with clay on his fingers and apron, holding a blue-and-white porcelain bowl. Scenery: Arita pottery kilns with rising smoke, blue-and-white porcelain plates on shelves, misty valley, Yoshinogari-style thatched hut in the background"),
   ("guide_nagasaki","中島ほのか","長崎：燈籠節的少女",
    "a gentle curious girl around 12 years old holding a glowing red paper lantern, wearing a light modern outfit with a subtle Chinese-style embroidered collar, soft smile. Scenery: Nagasaki slope streets at dusk, lantern festival lights, a tram, the harbor in the distance"),
   ("guide_kumamoto","石垣大樹","熊本：石垣師傅的孫子",
    "a sturdy honest boy around 12 years old with a small backpack and work gloves, holding a small stone, sun-tanned. Scenery: Kumamoto Castle curved stone walls at sunset, a stonemason's wooden tools, camellia flowers"),
   ("guide_oita","由布かなで","大分：溫泉鄉的少女",
    "an elegant gentle girl around 13 years old wearing a light purple scarf, with steam rising around her, soft calm smile. Scenery: Yufuin onsen town with Mt. Yufu behind, morning mist over a small lake, bamboo, rising onsen steam from hot spring vents (Beppu)"),
   ("guide_miyazaki","日向陽太","宮崎：神樂舞少年",
    "a sunny enthusiastic boy around 12 years old carrying a small traditional kagura wooden mask on his back, wearing a light happi jacket. Scenery: Takachiho gorge with waterfalls, sunlit ocean coast with palm trees (Aoshima), rising sun in the sky"),
   ("guide_kagoshima","錦江大和","鹿兒島：櫻島腳下的少年",
    "a broad-minded patient boy around 13 years old holding a small umbrella to block volcanic ash, tanned, calm grin. Scenery: Sakurajima volcano with a plume of ash across Kagoshima Bay, palm trees, a steam-rising sand-bath beach (Ibusuki), a ferry"),
])
groups[2] = ("三、故事旗艦站 NPC（21 位・目前已用到）", groups[2][1], groups[2][2])
groups[3] = ("四、縣嚮導（目前 46 位；沖繩於最後一批補上）", groups[3][1], groups[3][2])

groups[2][2].extend([
   ("npc_shisha","海的另一頭來的使者","沖繩旗艦站：琉球（中國史書的稱呼）",
    "a dignified Ming-dynasty-style envoy in a formal blue official robe and winged hat, holding a scroll, standing on the deck of a large wooden ship, calm serious expression, semi-transparent edges. Scenery: a Ryukyu Kingdom harbor with vermilion Shuri-style architecture on a hill, tropical blue sea, sails, hibiscus"),
   ("npc_ganjin","鑑真的弟子","沖繩旗艦站：沖縄（阿兒奈波）",
    "a serene young Buddhist monk in a plain Tang-dynasty-style robe, shaved head, holding prayer beads and a scroll of sutras, gentle smile, semi-transparent edges. Scenery: a wooden sailing ship on a stormy-to-calm sea, a small tropical island with coral beach, palm trees, dawn light"),
   ("npc_ukishima","浮島的船頭","沖繩旗艦站：那覇（浮島）",
    "a cheerful old Ryukyuan boatman in traditional Okinawan work clothes and a cloth headband (headwrap), tanned skin, holding an oar, big warm smile, semi-transparent edges. Scenery: the harbor of old Naha with a long stone causeway leading toward a hilltop castle, wooden Ryukyuan sailing boats, turquoise water"),
])
groups[3][2].extend([
   ("guide_okinawa","玉城なぎさ","沖繩：三線與獅子的少女",
    "a warm steady girl around 12 years old with a small sanshin (Okinawan three-string instrument) on her back, wearing a light bingata-patterned dress or vest, hibiscus in her hair, gentle smile. Scenery: Shuri Castle vermilion gate, shisa lion-dog statue on a red-tile roof, coral stone wall, turquoise sea and hibiscus"),
])
groups[2] = ("三、故事旗艦站 NPC（24 位）", groups[2][1], groups[2][2])
groups[3] = ("四、縣嚮導（共 47 位，已全部涵蓋）", groups[3][1], groups[3][2])

BG_STYLE = ("hand-painted watercolor and fine ink line illustration for a children's educational adventure game, "
            "warm textured paper grain, soft pastel washes, delicate ink outlines, gentle atmospheric lighting")
BG_COMP = ("full-bleed wide landscape scene (16:9, at least 1920x1080), NO characters in the foreground (only tiny distant silhouettes are allowed), "
           "horizon or main subject in the upper-middle of the frame, the lower third calm and uncluttered (a dark dialogue box is placed over it in the game), "
           "no text, no readable signs, no kanji or letters, no logos, no watermark, no frame or border")
BACKGROUNDS = [
 ("bg_city","city","城市街景","a busy Tokyo downtown street at dusk after light rain, wet asphalt reflecting glowing neon lights (abstract non-readable signs), tall buildings with Tokyo Tower or Skytree faintly visible in the sky, taxis and pedestrians with umbrellas as tiny distant figures, purple-orange twilight sky"),
 ("bg_oldstreet","oldstreet","老街","a quiet old Kyoto street lined with wooden machiya townhouses with latticed fronts and hanging noren curtains, paper lanterns lit at golden hour, stone-paved road, a small pagoda roof in the distance, a few tiny distant figures"),
 ("bg_school","school","學校","a Japanese public elementary school building with a clock tower, a big schoolyard with sand ground and a small gym, cherry blossom trees in bloom, white clouds and blue sky, bicycles parked, a few tiny distant children"),
 ("bg_home","home","住家房間","a cozy Japanese child's room at night, a wooden study desk with a desk lamp, an open notebook and colored pencils, a window showing city lights, a low bookshelf with picture books, tatami and futon partly visible, a cat sleeping on a cushion, warm lamp light"),
 ("bg_mountain","mountain","山岳","a sea of clouds between the Japanese Alps ridges at dawn, jagged snow-dusted peaks rising above misty layers, alpine pines on the ridge in the foreground, soft pink and blue morning light"),
 ("bg_forest","forest","森林","an ancient Japanese cedar forest with tall straight trunks, moss-covered stones and a narrow mossy trail, dappled sunlight rays through the leaves, ferns, a small stone lantern half hidden"),
 ("bg_ocean","ocean","海岸","a wide sandy beach at sunset on the Pacific coast, gentle waves with white foam, orange and pink sky reflected on wet sand, small islands on the horizon, a few footprints in the sand, tiny distant walkers"),
 ("bg_harbor","harbor","漁港","a small Japanese fishing harbor at dusk with several wooden and FRP fishing boats moored, red paper lanterns and lit windows of fish market buildings, calm water reflecting the twilight, ropes and buoys on the pier, seagulls"),
 ("bg_river","river","溪流","a clear mountain stream flowing over rocks in a green gorge, ferns and maple trees on the banks, mist rising, sunlight streaming, a small wooden bridge in the distance, a lively but peaceful mood"),
 ("bg_field","field","田野","golden rice paddies ready for harvest under a clear autumn sky, a winding farm path, a thatched-roof farmhouse and drying rice racks (hasagake), mountains in the distance, a few tiny distant farmers"),
 ("bg_temple","temple","神社","a Shinto shrine at golden hour with a vermilion torii gate, stone-paved approach lined with stone lanterns, a wooden main hall with a thatched or copper roof, a sacred rope (shimenawa), old camphor trees, incense smoke and drifting cherry petals, a few tiny distant worshippers"),
 ("bg_wetland","wetland","濕地／潮間帶","a vast wetland and tidal flat at sunset with reeds and shallow channels reflecting the golden sky, cranes and herons standing in the water, distant low hills, flocks of birds flying, misty warm atmosphere"),
]

out = ["# 拾憶者物語・日本篇｜角色生圖指令（全部批次）\n"]
out.append("## 使用方式\n")
out.append("1. 每個角色生成 **1 張圖**，檔名請用括號內的**代號**（例如 `hanlin.png`）。\n2. 我會自動把大圖縮成遊戲用的大圖（約 1085×620）與 128×128 臉部縮圖，並去背、打包。\n3. 每個角色的完整指令 = **共同風格（A）+ 角色描述 + 共同構圖（B）+ 避免項目（C）**。下方每個區塊已幫你組好，可直接複製。\n4. 建議尺寸：**16:9 橫幅，至少 1920×1080**。臉一定要在畫面上中部、不被手或道具擋住（臉部會被裁成小圖）。\n5. 如果你的工具沒有「負向提示詞」欄，就把 C 那一行接在最後面。\n")
out.append("## 共同片段\n")
out.append("**A. 共同風格**\n```\n%s\n```\n" % STYLE)
out.append("**B. 共同構圖**\n```\n%s\n```\n" % COMP)
out.append("**C. 避免項目**\n```\n%s\n```\n" % NEG)
out.append("**小提醒**\n- 阿伊努族角色（北加伊之魂、貝澤凜）請務必參考真實的阿伊努刺繡與服飾資料，避免刻板印象或混用其他民族的服飾。\n- 主角與嚮導請不要畫成成人化、性感化或暴露的樣子；同一位角色的髮型、服裝盡量固定，方便遊戲中一眼辨識。\n- 想要 Midjourney 用的話，可以在結尾加上 `--ar 16:9 --style raw`。\n- 之後每批（近畿、中四九、沖繩）我會補上該批新角色的指令；舊角色不需要重畫。\n")
n = 0
for title, note, items in groups:
    out.append("\n## %s\n" % title)
    out.append("> %s\n" % note)
    for key, name, zh, desc in items:
        n += 1
        out.append("### %s（`%s`）— %s\n" % (name, key, zh))
        out.append("```\n%s. %s. %s\n%s\n```\n" % (STYLE, desc[0].upper()+desc[1:], COMP, NEG))
out.append("\n## 五、背景圖（12 張）\n")
out.append("> 對話畫面的背景。原本的 12 張背景都帶有台灣元素（中文招牌、台灣校旗、廟宇、紅燈籠等），日本版需要全部替換。**這 12 張與角色不同：整張滿版、不去背、沒有白底。**\n> 檔名請用括號內代號（例如 `bg_city.png`）。建議 16:9、至少 1920×1080；畫面下方三分之一請保持簡潔，因為遊戲會在那裡蓋上對話框與暗色漸層。\n")
out.append("**背景共同風格**\n```\n%s\n```\n" % BG_STYLE)
out.append("**背景共同構圖**\n```\n%s\n```\n" % BG_COMP)
for key, sk, zh, desc in BACKGROUNDS:
    n += 1
    out.append("### %s（`%s`）— %s\n" % (zh, key, zh))
    out.append("```\n%s. %s. %s\n%s\n```\n" % (BG_STYLE, desc[0].upper()+desc[1:], BG_COMP, NEG))

out.append("\n---\n共 %d 張圖（角色 + 背景）。\n" % n)
open('/mnt/user-data/outputs/角色生圖指令_日本篇.md','w',encoding='utf-8').write('\n'.join(out))
print(n)
