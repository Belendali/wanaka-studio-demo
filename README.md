# Wanaka Studio · Create（对话式生成）— 开发交接

**在线 demo**：https://belendali.github.io/wanaka-studio-demo/
**Figma**：[Wanaka Studio · 0909/0910 分区](https://www.figma.com/design/PWtgAaGdl6znpuQykrnIbb/Wanaka-Studio?node-id=47617-12192)

这是一个可交互的原型，用来说明**交互和状态规则**，不是生产代码。视觉以 Figma 为准，行为以本文档和 demo 为准。两者不一致时，请找设计确认。

---

## 1. 整体结构

| 区域 | 内容 |
|---|---|
| 左侧 Create 面板 | 类别（Character / 3D Model / 2D & UI / …）、**Generate now** 按钮、资产库（搜索 + 卡片） |
| 中间 | 场景视口，资产 Add to scene 后以编辑态（选中框 + 移动 gizmo）出现 |
| 右侧 Chat 面板 | 顶部：对话名 ▾（切换器）+ **「+」**；中间：对话内容；底部：输入框 |

右侧有两种对话：

- **Chat**：和 Wana 一起规划、制作游戏的对话（原型里的 “Jump Jump game”）。
- **Asset chat**：生成资产的对话，按类别区分：**3D Model / 2D & UI / Character**。同一个对话里连续生成，风格保持一致。

## 2. 生成流程

### 3D Model / 2D & UI
1. 左侧选类别 → **Generate now** → 进入该类别的 asset chat（规则见 §3.1）。
2. 输入描述并发送 → Thinking → 结果卡片（预览、文件名、**Add Animation**（仅 3D）/ **Add to scene**）。
3. 结果同时出现在左侧资产库顶部。
4. 一次要多个（如 “Create 4 puppy models”）→ **多变体卡片**：左边大图，右边缩略图点击切换；下方 **Add all N to scene** / **Keep selected only**。
5. 2D 结果可以 **Create 3D model**，在同一个对话里继续。

### Character
1. 先生成**概念图** → 用户确认；**10 秒无操作自动继续**（可重新生成）。
2. 生成模型 + 绑定骨骼（进度卡片）→ 结果卡片标记 Rigged。
3. 点开 → **动作弹窗**：左侧动作列表（纯文字标签），中间实时预览；**Show Rig 默认关闭**，无网格背景。
4. 弹窗内 **Edit Rig** → Orient Model 对话框（调整朝向）；另有 **Download**、**Add to scene**。

## 3. 对话管理规则

### 3.1 Generate now = 默认复用
- 跳到**该类别最近打开的那个 asset chat**（不含已归档的），比较的是 `max(最后打开时间, 最后活跃时间)`。
- 对话顶部弹出卡片 **“Continue in this chat?”**，副标题如 “Latest 3D chat · 4 assets · 2 h ago”，按钮：**Start a new chat** / **Continue here**。
- 直接发消息也算继续，卡片消失。已经在该对话里时，不弹卡片。
- 该类别还没有对话时，直接新建。

### 3.2 顶部「+」：直接新建，不弹选择
- 在 Chat 里点 → 新建一个 Chat。
- 在 asset chat 里点 → 新建一个**同类别**的 asset chat。

### 3.3 草稿与命名
- 新对话显示 **Draft** 标签；发送第一条消息前离开，就丢弃，不进列表。
- 用第一条 prompt 自动命名（如 “Puppy models”），可重命名。

### 3.4 切换器（点对话名 ▾）
- 两个分组：**Chat / Assets**，带数量；默认打开当前对话所属的分组。
- 每个分组都有搜索框；底部是 **+ New chat**。
- **Assets**：先 **PINNED**，再 **RECENT**（按最后活跃时间），**不做类别筛选**。每行显示首个结果缩略图、类别标签（3D/2D）、资产数量、最后活跃时间。底部右侧是 **Archived (n) ›**。
- **Chat**：列出做游戏的对话，按最后活跃时间排序。
- 当前对话打 ✓。Esc 关闭。

### 3.5 行菜单（hover 出现 ···）
- **Rename**（行内编辑，Enter 保存，Esc 取消，F2 快捷键）
- **Pin to top / Unpin**（toast 带 Undo）
- **Archive**（toast 带 Undo）
- **Delete chat** → 二次确认。**只删对话，资产保留在资产库和场景里。**

### 3.6 归档
- 30 天无活动的对话自动归档（原型里用种子数据演示）。
- Archived 视图可 Restore；在归档对话里发消息，自动恢复。

### 3.7 资产库卡片菜单
- **Add to scene** · **Continue in chat** · **Download**
- Continue in chat：打开生成该资产的对话（hover 提示对话名）。对话已删除时置灰，显示 “Chat deleted”。

## 4. 数据模型（原型里的实现，供参考）

```js
AssetChat = { id, name, cat: '3D Model' | '2D & UI' | 'Character',
              thread: Message[], pinned, archived, last /*最后活跃*/, opened /*最后打开*/ }
GameChat  = { id, name, prompt, last }
Asset     = { id, name, kind: '2D' | '3D', cat, img, large, chatId, rigged? }
Message   = { role: 'user' | 'thinking' | 'result' | 'gallery' | 'concept' | 'rig', ... }
```

关键点：**Asset 记录 `chatId`**，所以资产库能找回生成它的对话；删除对话不删资产。

## 5. 对照 Figma 查看各状态

直接打开下面的链接，就能看到对应状态（在线 demo 地址后面加参数）：

| 链接参数 | 状态 | Figma 帧 |
|---|---|---|
| `?step=1` | 默认（Chat） | default |
| `?step=2` | 选中 3D Model | default create 3D |
| `?step=3` | Generate now → 新 asset chat | default create 3D generate new chat |
| `?step=4` | 生成中 Thinking | default create 3D |
| `?step=5` / `6` | 结果 / 第二个结果 | default created 3D / 02 |
| `?step=7` | Add to scene 编辑态 | default created 3D add |
| `?step=8` | 多变体卡片 | 2D & UI created |
| `?step=9` → `14` | Character：概念图 → 绑骨 → 结果 → 动作弹窗 → Edit Rig | Character 1 / 3 / 5 |
| `&cat=2D%20%26%20UI` 或 `&cat=Character` | 与 step 组合，切换类别 | 2D & UI / Character 行 |
| `?chats=menu` | 切换器 · Assets | Chats 1 |
| `?chats=games` | 切换器 · Chat | Chats 1b |
| `?chats=rowmenu` | 行菜单 | Chats 2 |
| `?chats=rename` | 行内重命名 | Chats 3 |
| `?chats=delete` | 删除确认 | Chats 4 |
| `?chats=archived` | 归档列表 | Chats 6 |
| `?chats=lib` | 资产库卡片菜单 | Chats 7 |
| `?chats=resume` | Generate now 复用 + 继续卡片 | Chats 8 |
| `?chats=draft` | 新对话草稿 | Chats 9 |

完整规则卡（中英）：Figma 帧 **Chat management · rules**。

## 6. 文件

| 路径 | 说明 |
|---|---|
| `index.html` | 原型（HTML + CSS + JS 单文件，无依赖、无构建）。1920×1080 画布，按窗口缩放 |
| `wanaka-create-single-file.html` | 同上，图片全部内联，可以离线打开或直接发给别人 |
| `assets/` | 从 Figma 导出的图标和图片 |
| `tools/build-single.py` | 生成单文件版：`python3 tools/build-single.py index.html wanaka-create-single-file.html` |
| `plan-b.html` | 旧链接，自动跳转到 `index.html` |
| `archive/` | 已放弃的方案（Plan A 表单式、Plan C 每类一个对话），仅存档，页面上没有入口 |

代码导读（`index.html`）：`bState()` 是初始数据；`panel()` / `chat()` / `chatMenu()` 负责渲染；`openChat` / `newChat` / `newGame` / `sendB` 是对话逻辑；`startCharacter` / `renderAnim` 是 Character 流程；所有点击都通过 `data-act` 统一分发。文件里还留着 Plan A 表单面板的代码，当前入口不会用到。

**原型里是模拟的部分**：生成（固定延时 + 示例图）、自动命名、30 天归档、下载，都没有接后端。
