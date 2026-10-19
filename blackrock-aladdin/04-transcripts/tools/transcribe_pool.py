import sys,os,time,subprocess,numpy as np
from faster_whisper import WhisperModel
m=WhisperModel("base.en",device="cpu",compute_type="int8")
files=[l.strip() for l in open(sys.argv[1]) if l.strip()]
for f in files:
    out=os.path.splitext(f)[0]+'.whisper.txt'; lock=out+'.lock'
    if os.path.exists(out): continue
    try: fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY); os.close(fd)
    except FileExistsError: continue
    t=time.time(); a=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',f,'-f','f32le','-ac','1','-ar','16000','-'],capture_output=True).stdout,dtype=np.float32)
    if len(a)<16000: open(out,'w').write(''); print('empty',f,flush=True); continue
    segs,info=m.transcribe(a,beam_size=1,vad_filter=True); text=' '.join(s.text.strip() for s in segs)
    open(out,'w').write(text); print(f"{os.path.basename(f)}: {len(a)/16000:.0f}s audio, {len(text.split())} words, {time.time()-t:.0f}s",flush=True)
print('done')
