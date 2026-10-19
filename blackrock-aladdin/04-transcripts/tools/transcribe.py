import sys,os,glob,time,subprocess
import numpy as np
from faster_whisper import WhisperModel
m=WhisperModel("base.en",device="cpu",compute_type="int8")
def load(f):
    r=subprocess.run(['ffmpeg','-v','error','-i',f,'-f','f32le','-ac','1','-ar','16000','-'],capture_output=True); return np.frombuffer(r.stdout,dtype=np.float32)
files=sorted(glob.glob('media/*.mp4')+glob.glob('media/*.m4a')+glob.glob('media/*.webm')+glob.glob('media/*.mp3'))
for f in files:
    out=os.path.splitext(f)[0]+'.whisper.txt'
    if os.path.exists(out) or f.endswith('.part'): continue
    t=time.time(); a=load(f)
    if len(a)<16000: print('skip empty',f,flush=True); continue
    segs,info=m.transcribe(a,beam_size=1,vad_filter=True)
    text=' '.join(s.text.strip() for s in segs)
    open(out,'w').write(text)
    print(f"{os.path.basename(f)}: {len(a)/16000:.0f}s audio, {len(text.split())} words, {time.time()-t:.0f}s elapsed",flush=True)
print('done')
