import sys,os,time,subprocess,numpy as np
from faster_whisper import WhisperModel
m=WhisperModel("base.en",device="cpu",compute_type="int8")
outdir=sys.argv[1]
for f in sys.argv[2:]:
    out=os.path.join(outdir,os.path.basename(f)+'.ts.txt')
    if os.path.exists(out): continue
    t=time.time()
    a=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',f,'-f','f32le','-ac','1','-ar','16000','-'],capture_output=True).stdout,dtype=np.float32)
    segs,info=m.transcribe(a,beam_size=1,vad_filter=True)
    with open(out+'.part','w') as w:
        for s in segs:
            w.write(f"[{int(s.start)//60:02d}:{int(s.start)%60:02d}] {s.text.strip()}\n")
    os.rename(out+'.part',out)
    print(f"{os.path.basename(f)}: {len(a)/16000:.0f}s audio, {time.time()-t:.0f}s",flush=True)
print('done')
