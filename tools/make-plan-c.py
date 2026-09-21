import sys
p=sys.argv[1]; t=open(p).read()
def rep(a,b):
    global t
    assert a in t, 'MISSING '+a[:100]; t=t.replace(a,b,1)
def cut(start_marker, end_marker, new):
    global t
    s=t.index(start_marker); e=t.index(end_marker, s)
    t=t[:s]+new+t[e:]
rep("<title>Wanaka Studio · Plan B</title>", "<title>Wanaka Studio · Plan C</title>")
rep('<span class="lbl">Wanaka Studio · Plan B · chat generation</span>', '<span class="lbl">Wanaka Studio · Plan C · one chat per category</span>')
rep('''<a href="index.html" style="font:500 12px/1 var(--font);color:#ccc;background:#2a2a2a;border:1px solid #3a3a3a;border-radius:6px;padding:7px 10px;text-decoration:none;margin-left:8px">Plan A ↗</a>''',
    '''<a href="index.html" style="font:500 12px/1 var(--font);color:#ccc;background:#2a2a2a;border:1px solid #3a3a3a;border-radius:6px;padding:7px 10px;text-decoration:none;margin-left:8px">Plan A ↗</a>
  <a href="plan-b.html" style="font:500 12px/1 var(--font);color:#ccc;background:#2a2a2a;border:1px solid #3a3a3a;border-radius:6px;padding:7px 10px;text-decoration:none;margin-left:6px">Plan B ↗</a>''')
s=t.index("  seed('c-puppy'"); e=t.index("  const games = [", s)
t=t[:s]+r'''  const mkChat = (id, cat) => { const c = { id, cat, name: cat, last: 0, thread: [], pinned: false, archived: false }; chats.push(c); return c; };
  const add = (c, at, prompt, items, opts = {}) => {
    items.forEach(it => { it.chatId = c.id; lib.push(it); });
    if (opts.topic) c.thread.push({ role: 'topic', at });
    c.thread.push({ role: 'user', text: prompt, at });
    c.thread.push(items.length > 1 ? { role: 'gallery', gallery: { id: uid++, items, sel: 0 }, at } : { role: 'result', item: items[0], at });
    c.last = Math.max(c.last, at);
  };
  const c3 = mkChat('k-3d', '3D Model'), c2 = mkChat('k-2d', '2D & UI'), cc = mkChat('k-char', 'Character');
  add(c3, now - 9 * DAY, 'Create a cat model', [{ id: uid++, name: 'Cat model_3D.glb', short: 'Cat model', img: 'cat3d-a.png', large: 'cat3d-a.png', kind: '3D', cat: '3D Model' }]);
  add(c3, now - 6 * DAY, 'Create platform tiles', [{ id: uid++, name: 'Platform tile_3D.glb', short: 'Platform tile', img: 'dog.png', large: 'dog-large.png', kind: '3D', cat: '3D Model' }], { topic: true });
  add(c3, now - 2 * HOUR, 'Create 4 puppy models', [1, 2, 3, 4].map(i => ({ id: uid++, name: `Puppy model 0${i}_3D.glb`, short: 'Puppy model', img: 'dog.png', large: 'dog-large.png', kind: '3D', cat: '3D Model' })), { topic: true });
  add(c2, now - 45 * DAY, 'Create coin icons', [{ id: uid++, name: 'Coin icon_2D.png', short: 'Coin icon', img: 'coin.png', large: 'coin.png', kind: '2D', cat: '2D & UI' }]);
  add(c2, now - 4 * DAY, 'Create 2 puppy stickers', [1, 2].map(i => ({ id: uid++, name: `Puppy sticker 0${i}_2D.png`, short: 'Puppy sticker', img: `puppy${i}.png`, large: `puppy${i}.png`, kind: '2D', cat: '2D & UI' })), { topic: true });
  add(cc, now - 26 * HOUR, 'Create a cat student character', [{ id: uid++, name: 'Cat student_3D.glb', short: 'Cat student', img: 'cat.png', large: 'cat-turn.webp', kind: '3D', cat: 'Character', rigged: true }]);
'''+t[e:]
rep("    chats, activeChat: null,", "    chats, activeChat: null, openSess: {}, flashItem: null,")
cut("function syncActive() {", "function discardDraft(", r'''function catChat(cat) { cat = cat && GEN_TITLE[cat] ? cat : '3D Model'; let c = S.chats.find(x => x.cat === cat); if (!c) { c = { id: 'k-' + (uid++), cat, name: cat, last: Date.now(), thread: [], pinned: false, archived: false }; S.chats.push(c); } return c; }
function syncActive() {
  if (S.chat !== 'assets') return null;
  let c = chatById(S.activeChat); if (!c) { c = catChat(S.cat); S.activeChat = c.id; }
  c.thread = S.thread; return c;
}
''')
rep("function discardDraft(keepId) { const c = chatById(S.activeChat); if (c && c.id !== keepId && !hasUser(c)) S.chats = S.chats.filter(x => x !== c); }", "function discardDraft() {}")
cut("const CAT_FILTERS = ", "function renderDel() {", r'''const CAT_ICON = { '3D Model': 'cat-asset.svg', '2D & UI': 'cat-image.svg', 'Character': 'cat-character.svg' };
const destRow = (c) => { const n = chatItems(c).filter(i => !i.deleted).length; const on = S.chat === 'assets' && S.activeChat === c.id;
  return `<div class="crow${on ? ' on' : ''}" data-act="copen" data-v="${c.id}"><div class="cthumb ci"><img src="${U(CAT_ICON[c.cat])}" alt=""></div><div class="ctext"><div class="ctitle"><span class="nm">${esc(c.cat)}</span></div><div class="cmeta">${hasUser(c) ? `${n} asset${n === 1 ? '' : 's'} · ${rel(c.last)}` : 'Nothing yet'}</div></div>${on ? '<span class="ccheck">✓</span>' : ''}</div>`; };
const chatMenu = () => {
  const g = curGame(); const gon = S.chat === 'game';
  return `<div class="chat-menu sw2 simple" id="chatmenu">
    <div class="crow${gon ? ' on' : ''}" data-act="cgame" data-v="${S.gameChat}"><div class="cthumb">${I('mascot.png',28,30)}</div><div class="ctext"><div class="ctitle"><span class="nm">${esc(g.name)}</span><span class="badge game">Game</span></div><div class="cmeta">Plan &amp; build with Wana · ${rel(g.last)}</div></div>${gon ? '<span class="ccheck">✓</span>' : ''}</div>
    <div class="csec">CREATE</div>
    ${['3D Model', '2D & UI', 'Character'].map(cat => destRow(catChat(cat))).join('')}
  </div>`;
};
''')
cut("const assetsThread = () =>", "/* ---------------- chat management ---------------- */", r'''const dayKey = (ms) => { const d = new Date(ms); return `${d.getFullYear()}-${d.getMonth()}-${d.getDate()}`; };
const dayLabel = (ms) => { const d = new Date(ms), n = new Date(); const hm = `${pad(d.getHours())}:${pad(d.getMinutes())}`; if (dayKey(ms) === dayKey(n.getTime())) return `Today ${hm}`; if (dayKey(ms) === dayKey(n.getTime() - DAY)) return 'Yesterday'; return d.toLocaleString('en-US', { month: 'short' }) + ' ' + pad(d.getDate()); };
const msgItems = (m) => m.gallery ? m.gallery.items : m.item ? [m.item] : m.concept ? [m.concept.item] : m.rig ? [m.rig.item] : [];
const msgHtml = (m, i) => { const inner = m.role === 'user' ? userB(m) : m.role === 'thinking' ? thinkingB() : m.role === 'gallery' ? galleryB(m.gallery) : m.role === 'concept' ? conceptB(m.concept) : m.role === 'rig' ? rigB(m.rig) : resultB(m.item);
  const its = msgItems(m); const gone = its.length && its.every(x => x.deleted); const flash = S.flashItem && its.some(x => x.id === S.flashItem);
  return `<div class="msgw${gone ? ' gone' : ''}${flash ? ' flash' : ''}" data-mi="${i}">${gone ? '<span class="gonetag">Removed from library</span>' : ''}${inner}</div>`; };
function sessionsOf(thread) {
  const out = []; let cur = null;
  thread.forEach((m, i) => { const at = m.at || Date.now();
    if (!cur || m.role === 'topic' || (m.role === 'user' && dayKey(at) !== cur.day && cur.msgs.length)) { cur = { start: i, day: dayKey(at), at, topic: m.role === 'topic', msgs: [] }; out.push(cur); }
    if (m.role !== 'topic') cur.msgs.push([m, i]); });
  return out;
}
const assetsThread = () => {
  if (!S.thread.length) return `<div class="cb-empty">${I(S.cat === 'Character' ? 'empty-char.webp' : S.cat === '2D & UI' ? 'empty-2d.webp' : 'empty-3d.webp',180,180)}<p class="t">${S.cat === 'Character' ? 'Character' : S.cat === '2D & UI' ? '2D & UI' : '3D Model'}</p><p class="s">Create with images and context.</p></div>`;
  const ss = sessionsOf(S.thread); const cid = S.activeChat;
  const html = ss.map((s, k) => {
    const last = k === ss.length - 1; const key = `${cid}:${s.start}`; const open = last || S.openSess[key];
    const items = s.msgs.flatMap(([m]) => msgItems(m)).filter(x => !x.deleted); const first = s.msgs.find(([m]) => m.role === 'user');
    const title = first ? assetName(first[0].text) : 'New topic';
    const div = `<div class="topicdiv"><span>${s.topic ? 'New topic · ' : ''}${dayLabel(s.at)}</span></div>`;
    if (!open) return `${div}<div class="sess" data-act="sexp" data-v="${key}">${items[0] ? `<div class="sth">${I(items[0].img, 24, 24)}</div>` : ''}<div class="stx"><span class="sn">${esc(title)}</span><span class="sm">${items.length} asset${items.length === 1 ? '' : 's'}</span></div><span class="stg">Show</span></div>`;
    const hide = !last ? `<div class="sesshide" data-act="sexp" data-v="${key}">Hide</div>` : '';
    const body = s.msgs.length ? s.msgs.map(([m, i]) => msgHtml(m, i)).join('') : `<p class="topichint">Start describing something new. Earlier results in this chat won't be used as a style reference.</p>`;
    return `${div}${hide}${body}`;
  }).join('');
  return `<div class="thread" id="thread">${html}</div>`;
};
''')
rep("""  const name = assets ? `<span class="nmh">${esc(ac && ac.name ? ac.name : 'New chat')}</span>${ac && !hasUser(ac) ? '<span class="draft">Draft</span>' : ''}` : `<span class="nmh">${esc(curGame().name)}</span>`;""",
"""  const name = assets ? `<span class="hic"><img src="${U(CAT_ICON[ac.cat])}" alt=""></span><span class="nmh">${esc(ac.cat)}</span>` : `<span class="nmh">${esc(curGame().name)}</span>`;""")
rep("""<div class="chat-plus" data-act="newchat" title="New chat">${I('plus.svg',12,12)}</div>""",
    """${assets ? `<div class="topic-btn" data-act="topic" title="Start a new topic in this chat">${I('plus.svg',12,12)}<span>New topic</span></div>` : ''}""")
rep("""    ${assets && ac && !hasUser(ac) ? '<p class="draftnote">Not saved until you send the first message</p>' : ''}
""", "")
s=t.index("    ${assets && ac && S.resumed === ac.id ? (() => {"); e=t.index("    <div class=\"composer-area\">", s); t=t[:s]+t[e:]
rep("""  if (S.chat !== 'assets') { S.chat = 'assets'; S.activeChat = null; S.thread = []; }
  if (ta) ta.value = '';
  S.thread.push({ role: 'user', text }); S.thread.push({ role: 'thinking' }); S.busy = true;""",
"""  if (S.chat !== 'assets') { const c = catChat(S.cat); S.chat = 'assets'; S.activeChat = c.id; S.thread = c.thread; }
  if (ta) ta.value = '';
  S.thread.push({ role: 'user', text, at: Date.now() }); S.thread.push({ role: 'thinking' }); S.busy = true;""")
rep("that matches the style of your other assets.</p>", "${(() => { const i = S.thread.length - 3; const prev = S.thread[i]; return !prev || prev.role === 'topic' ? 'in a fresh style for this new topic.' : 'that matches the earlier results in this chat.'; })()}</p>")
s=t.index("    case 'gennow': {"); e=t.index("    case 'rkeep':", s)
t=t[:s]+r'''    case 'gennow': {
      const c = catChat(S.cat); S.cat = c.cat;
      if (S.chat === 'assets' && S.activeChat === c.id) { S.menu = false; renderChat(); } else openChat(c.id);
      { const ta = document.getElementById('cbInput'); if (ta) ta.focus(); } break; }
    case 'topic': {
      const lastM = S.thread[S.thread.length - 1];
      if (!S.thread.length || (lastM && lastM.role === 'topic')) { toast('Already on a new topic · describe what you need'); const ta = document.getElementById('cbInput'); if (ta) ta.focus(); break; }
      S.thread.push({ role: 'topic', at: Date.now() }); renderChat(); { const ta = document.getElementById('cbInput'); if (ta) ta.focus(); }
      toast('New topic · earlier results won’t shape the style', () => { if (S.thread[S.thread.length - 1]?.role === 'topic') { S.thread.pop(); renderChat(); } }); break; }
    case 'sexp': { S.openSess[v] = !S.openSess[v]; const th = document.getElementById('thread'); const top = th ? th.scrollTop : 0; renderChat(); const th2 = document.getElementById('thread'); if (th2) th2.scrollTop = top; break; }
    case 'lmdel': { const it = S.lib.find(i => i.id === +v); S.libMenu = null; renderLibMenu(); if (!it) break; const pos = S.lib.indexOf(it); S.lib.splice(pos, 1); it.deleted = true; renderPanel(); renderChat();
      toast(`Deleted ${it.name}`, () => { it.deleted = false; S.lib.splice(pos, 0, it); renderPanel(); renderChat(); }); break; }
'''+t[e:]
rep("""    case 'lmchat': { const it = S.lib.find(i => i.id === +v); S.libMenu = null; renderLibMenu(); const c = it && chatById(it.chatId); if (c) { c.archived = false; openChat(c.id); toast(`Opened “${c.name}” · describe what else you need in this style`); } break; }""",
"""    case 'lmchat': { const it = S.lib.find(i => i.id === +v); S.libMenu = null; renderLibMenu(); const c = it && chatById(it.chatId); if (!c) break;
      const ss = sessionsOf(c.thread); const s = ss.find(x => x.msgs.some(([m]) => msgItems(m).includes(it))); if (s) S.openSess[`${c.id}:${s.start}`] = true;
      S.flashItem = it.id; openChat(c.id);
      const el = [...document.querySelectorAll('#thread .msgw.flash')].pop(); const th = document.getElementById('thread'); if (el && th) th.scrollTop = Math.max(0, el.offsetTop - th.offsetTop - 60);
      setTimeout(() => { S.flashItem = null; document.querySelectorAll('.msgw.flash').forEach(n => n.classList.remove('flash')); }, 1800); break; }""")
rep("    case 'newchat': newChat(S.cat && GEN_TITLE[S.cat] ? S.cat : null); break;", "    case 'newchat': break;")
rep("""    <div class="mi${ok ? '' : ' off'}" data-act="lmchat" data-v="${it.id}">Continue in chat<small>${ok ? `Opens “${esc(c.name)}”${c.archived ? ' · restores it from Archived' : ''} · makes more in this style` : 'The chat that made this was deleted'}</small></div>
    <div class="mi" data-act="lmdl" data-v="${it.id}">Download</div></div>`);""",
"""    <div class="mi${ok ? '' : ' off'}" data-act="lmchat" data-v="${it.id}">Show in chat<small>Jumps to where it was made in the ${esc(c ? c.cat : '')} chat</small></div>
    <div class="mi" data-act="lmdl" data-v="${it.id}">Download</div>
    <div class="mi danger" data-act="lmdel" data-v="${it.id}">Delete</div></div>`);""")
rep("  const v = new URLSearchParams(location.search).get('chats'); if (!v) return;", "  const v = null; if (!v) return;")
idx = t.rindex("\nrenderShell(); fit();\n")
t = t[:idx] + r'''
renderShell(); fit();
/* ---------- Plan C review states: ?c=menu|history|topic|lib|show ---------- */
(function () {
  const v = new URLSearchParams(location.search).get('c'); if (!v) return;
  S.cat = '3D Model'; renderPanel(); openChat('k-3d');
  if (v === 'menu') { S.menu = true; renderChat(); }
  if (v === 'history') { const ss = sessionsOf(chatById('k-3d').thread); S.openSess[`k-3d:${ss[0].start}`] = true; renderChat(); document.getElementById('thread').scrollTop = 0; }
  if (v === 'topic') { S.thread.push({ role: 'topic', at: Date.now() }); renderChat(); }
  if (v === 'lib') { S.cat = null; renderPanel(); S.libMenu = S.lib.find(i => /Cat model/.test(i.name)).id; setTimeout(renderLibMenu, 60); }
  if (v === 'show') { S.cat = null; renderPanel(); S.libMenu = S.lib.find(i => /Cat model/.test(i.name)).id; renderLibMenu(); document.querySelector('[data-act="lmchat"]').click(); }
})();
''' + t[idx+len("\nrenderShell(); fit();\n"):]
rep("</style>", r'''
  /* ============================ Plan C ============================ */
  .chat-menu.sw2.simple { padding: 8px; }
  .cthumb.ci img { width: 22px; height: 22px; object-fit: contain; }
  .chat-name .hic { width: 18px; height: 18px; flex: none; display: flex; align-items: center; justify-content: center; } .chat-name .hic img { width: 16px; height: 16px; }
  .chat-name span.hic { flex: none; }
  .topic-btn { height: 28px; padding: 0 10px; border-radius: 10px; background: var(--w08); display: flex; align-items: center; gap: 6px; font: 500 12px/16px var(--font); color: rgba(255,255,255,.85); cursor: pointer; white-space: nowrap; flex: none; }
  .topic-btn:hover { background: var(--w14); color: #fff; }
  .msgw { width: 100%; display: flex; flex-direction: column; align-items: flex-end; gap: 16px; border-radius: 22px; transition: box-shadow .3s, background .3s; position: relative; }
  .msgw.flash { box-shadow: 0 0 0 2px var(--brand); background: rgba(192,240,0,.06); }
  .msgw.gone { opacity: .45; } .gonetag { align-self: flex-start; padding: 2px 8px; border-radius: 6px; background: var(--w08); font: 500 11px/15px var(--font); color: rgba(255,255,255,.7); }
  .topicdiv { width: 100%; display: flex; align-items: center; gap: 10px; font: 500 11px/14px var(--font); color: rgba(255,255,255,.4); letter-spacing: .02em; }
  .topicdiv::before, .topicdiv::after { content: ''; flex: 1 0 0; height: 1px; background: var(--w08); }
  .sess { width: 100%; display: flex; align-items: center; gap: 10px; padding: 8px 10px; border-radius: 10px; background: var(--w05); cursor: pointer; }
  .sess:hover { background: var(--w08); }
  .sth { width: 32px; height: 32px; flex: none; border-radius: 8px; background: #191718; display: flex; align-items: center; justify-content: center; } .sth img { width: 24px; height: 24px; object-fit: contain; }
  .stx { flex: 1 0 0; min-width: 0; display: flex; flex-direction: column; } .sn { font: 500 13px/17px var(--font); color: rgba(255,255,255,.85); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; } .sm { font: 400 11px/15px var(--font); color: rgba(255,255,255,.45); }
  .stg { font: 500 12px/16px var(--font); color: var(--brand); }
  .sesshide { align-self: center; font: 500 11px/14px var(--font); color: rgba(255,255,255,.5); cursor: pointer; padding: 2px 8px; border-radius: 6px; } .sesshide:hover { color: #fff; background: var(--w08); }
  .topichint { width: 100%; text-align: center; font: 400 12px/18px var(--font); color: rgba(255,255,255,.45); padding: 4px 24px; }
  .libmenu .mi.danger { color: #ff6b6b; }
</style>''')
open(p,'w').write(t); print('plan-c written', len(t))
