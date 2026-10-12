from pathlib import Path
import json,re,html
root=Path(__file__).resolve().parents[1]
def p(text):return ''.join('<p>'+html.escape(t.replace('\n',' '))+'</p>' for t in text.strip().split('\n\n') if t.strip())
history=json.loads((root/'data/history.json').read_text())
f=root/'index.html';text=f.read_text();content=''.join('<p><time>'+html.escape(v['date'])+'</time>　'+html.escape(v['text'])+'</p>' for v in history)
text=re.sub(r'(<div class="history">).*?(</div>)',lambda m:m[1]+content+m[2],text,flags=re.S);f.write_text(text)
entries=json.loads((root/'data/diary.json').read_text());years=sorted({e['date'][:4] for e in entries},reverse=True)
content='<div class="year-links">'+' / '.join('<a href="#year-'+y+'">'+y+'</a>' for y in years)+'</div>';last=None
for e in sorted(entries,key=lambda e:e['date'],reverse=True):
 y=e['date'][:4]
 if y!=last:content+='<h2 id="year-'+y+'">'+y+'年</h2>';last=y
 content+='<article id="entry-'+e['date'].replace('/','-')+'"><h3><time>'+html.escape(e['date'])+'</time>　'+html.escape(e['title'])+'</h3>'+p(e['body'])+'</article>'
f=root/'diary.html';text=f.read_text();text=re.sub(r'(<div class="page-title">DIARY</div>).*?(<p class="back">)',lambda m:m[1]+content+m[2],text,flags=re.S);f.write_text(text)
print('Rebuilt diary and history.')
