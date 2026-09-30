import json, math
d = json.load(open('/home/claude/japan.geojson'))
# prefecture -> region
REG = {
 'north': ['北海道','青森県','岩手県','宮城県','秋田県','山形県','福島県'],
 'central': ['茨城県','栃木県','群馬県','埼玉県','千葉県','東京都','神奈川県'],
 'south': ['新潟県','富山県','石川県','福井県','山梨県','長野県','岐阜県','静岡県','愛知県','三重県','滋賀県','京都府','大阪府','兵庫県','奈良県','和歌山県'],
 'east': ['鳥取県','島根県','岡山県','広島県','山口県','徳島県','香川県','愛媛県','高知県','福岡県','佐賀県','長崎県','熊本県','大分県','宮崎県','鹿児島県'],
 'island': ['沖縄県'],
}
def dp(pts, eps):
    if len(pts) < 3: return pts
    a, b = pts[0], pts[-1]
    dx, dy = b[0]-a[0], b[1]-a[1]; L = math.hypot(dx, dy)
    best, idx = -1, 0
    for i in range(1, len(pts)-1):
        p = pts[i]
        dist = abs(dy*p[0]-dx*p[1]+b[0]*a[1]-b[1]*a[0])/L if L else math.hypot(p[0]-a[0], p[1]-a[1])
        if dist > best: best, idx = dist, i
    if best > eps:
        return dp(pts[:idx+1], eps)[:-1] + dp(pts[idx:], eps)
    return [a, b]
def area(r):
    return abs(sum(r[i][0]*r[(i+1)%len(r)][1]-r[(i+1)%len(r)][0]*r[i][1] for i in range(len(r))))/2
COS = math.cos(math.radians(37))
def proj(lon, lat): return (lon*COS, -lat)
polys = {}  # name -> list of rings in projected units
for f in d['features']:
    n = f['properties']['nam_ja']; g = f['geometry']
    rings = []
    ps = g['coordinates'] if g['type']=='MultiPolygon' else [g['coordinates']]
    for poly in ps:
        r = [proj(x, y) for x, y in poly[0]]
        rings.append(r)
    polys[n] = rings
# Okinawa is moved to an inset (lower-left); main islands fitted to the frame
def bbox(rs):
    xs=[p[0] for r in rs for p in r]; ys=[p[1] for r in rs for p in r]
    return min(xs),min(ys),max(xs),max(ys)
main = [r for n,rs in polys.items() if n!='沖縄県' for r in rs]
# ignore far outlying islands (Ogasawara etc.) when fitting
core = [r for r in main if -46 < -sum(p[1] for p in r)/len(r) < 46 and 128*COS < sum(p[0] for p in r)/len(r) < 146*COS]
x0,y0,x1,y1 = bbox([r for r in core if area(r) > 0.02])
W, H = 670, 720
PAD = 14
scale = min((W-2*PAD)/(x1-x0), (H-2*PAD-120)/(y1-y0))
ox = PAD + ((W-2*PAD)-(x1-x0)*scale)/2; oy = PAD
def tmain(p): return ((p[0]-x0)*scale+ox, (p[1]-y0)*scale+oy)
# Okinawa inset: same scale, placed in dashed frame bottom-left
ok = polys['沖縄県']
okcore = [r for r in ok if area(r) > 0.0005 and sum(p[0] for p in r)/len(r) < 130.5*COS]
bx0,by0,bx1,by1 = bbox(okcore)
IN_X, IN_Y, IN_W, IN_H = W-252, H-214, 230, 194
ks = min((IN_W-16)/(bx1-bx0), (IN_H-44)/(by1-by0))
iox = IN_X + (IN_W-(bx1-bx0)*ks)/2; ioy = IN_Y + 26
def tok(p): return ((p[0]-bx0)*ks+iox, (p[1]-by0)*ks+ioy)
out = {}
total = 0
for n, rs in polys.items():
    shapes = []
    for r in rs:
        a = area(r)
        if n == '沖縄県':
            if a < 0.0004 or sum(p[0] for p in r)/len(r) > 130.5*COS: continue
            pts = [tok(p) for p in r]; eps = 0.35
        else:
            if a < 0.004: continue   # drop tiny islets
            pts = [tmain(p) for p in r]; eps = 0.45
        pts = dp(pts, eps)
        if len(pts) < 4: continue
        shapes.append(' '.join('%.1f,%.1f' % p for p in pts))
    out[n] = {'shapes': [{'pts': s, 'name': n} for s in shapes]}
    total += sum(len(s) for s in shapes)
json.dump({'map': out, 'reg': REG, 'inset': [IN_X, IN_Y, IN_W, IN_H], 'scale': scale,
           'okscale': ks}, open('map.json', 'w'), ensure_ascii=False)
print('prefs', len(out), 'bytes', total, 'scale', scale, 'ok scale', ks)
# label positions: centroid of region core
for rid, names in REG.items():
    pts = [tuple(map(float, q.split(','))) for n in names if n!='沖縄県' for s in out[n]['shapes'] for q in s['pts'].split()[:400]]
    if pts:
        print(rid, round(sum(p[0] for p in pts)/len(pts)), round(sum(p[1] for p in pts)/len(pts)))
