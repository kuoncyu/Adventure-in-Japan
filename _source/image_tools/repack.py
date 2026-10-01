import json, io, os, shutil
from PIL import Image
import facecrop
SRC='/home/claude/src/assets'
OUT='/home/claude/jp/assets'
os.makedirs(OUT,exist_ok=True)
m=json.load(open(f'{SRC}/characters.manifest.json')); pack=open(f'{SRC}/characters.pack','rb').read()
G=json.load(open('guess.json'))
def webp(im,q=86):
    b=io.BytesIO(); im.save(b,'WEBP',quality=q,method=6); return b.getvalue()
new={}
for k,(cx,cy,S) in G.items():
    full=Image.open(f'cut2/{k}.png').convert('RGBA')
    new[(k,'full')]=webp(full,86)
    new[(k,'face')]=webp(facecrop.crop_face(k,cx,cy,S),88)
items=[]; buf=bytearray()
for it in m['items']:
    key=(it['key'],it['part'])
    data=new.get(key) or pack[it['offset']:it['offset']+it['length']]
    items.append(dict(key=it['key'],part=it['part'],offset=len(buf),length=len(data),mime='image/webp')); buf+=data
json.dump(dict(version=m['version'],totalBytes=len(buf),items=items),open(f'{OUT}/characters.manifest.json','w'),ensure_ascii=False)
open(f'{OUT}/characters.pack','wb').write(buf)
for f in ('scenes.manifest.json','scenes.pack'): shutil.copy(f'{SRC}/{f}',f'{OUT}/{f}')
print('replaced',len(new),'items; pack',len(buf)//1024,'KB')
for k in G: print(k, len(new[(k,'full')])//1024,'KB full')
