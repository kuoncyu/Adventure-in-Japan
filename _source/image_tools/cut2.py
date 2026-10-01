import json, numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage as ndi
files=json.load(open('files.json'))
def disk(r):
    y,x=np.ogrid[-r:r+1,-r:r+1]; return x*x+y*y<=r*r
def cut(path, T=26, close_r=6):
    im=Image.open(path).convert('RGB'); a=np.asarray(im).astype(np.int16)
    h,w,_=a.shape
    # 背景色：以影像四周 8px 邊框取中位數，再以兩側線性漸層近似
    border=np.concatenate([a[:8].reshape(-1,3),a[-8:].reshape(-1,3),a[:,:8].reshape(-1,3),a[:,-8:].reshape(-1,3)])
    bg=np.median(border,axis=0)
    left=np.median(a[:,:12].reshape(-1,3),axis=0); right=np.median(a[:,-12:].reshape(-1,3),axis=0)
    xs=np.linspace(0,1,w)[None,:,None]
    bgmap=(left[None,None,:]*(1-xs)+right[None,None,:]*xs)
    diff=np.abs(a-bgmap).max(axis=2)
    M=diff>T
    M=ndi.binary_closing(M,structure=disk(close_r))
    F=ndi.binary_fill_holes(M)
    # 去掉非常小的雜點（< 60 px），保留墨點裝飾（較大）
    lab,n=ndi.label(F); sizes=ndi.sum(F,lab,range(1,n+1))
    keep=np.isin(lab,[i+1 for i,s in enumerate(sizes) if s>=60])
    F=keep
    alpha=ndi.gaussian_filter(F.astype(np.float32),1.1)
    alpha=np.clip((alpha-0.2)/0.6,0,1)
    rgba=np.dstack([np.asarray(im),(alpha*255).astype(np.uint8)])
    return Image.fromarray(rgba,'RGBA'), F
if __name__=='__main__':
    import os; os.makedirs('cut2',exist_ok=True)
    for k,p in sorted(files.items()):
        out,F=cut(p)
        ys,xs=np.where(F); 
        pad=8; box=(max(0,xs.min()-pad),max(0,ys.min()-pad),min(out.width,xs.max()+pad),min(out.height,ys.max()+pad))
        c=out.crop(box); sc=620/c.height
        c=c.resize((int(round(c.width*sc)),620),Image.LANCZOS); c.save(f'cut2/{k}.png'); print(k,c.size, round(F.mean(),3))
