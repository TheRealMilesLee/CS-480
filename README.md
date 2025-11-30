# CS-480

> EN: Algorithms and heuristic search playground (BFS / DFS / A* / state-space puzzles) with modular Python implementations and test harness.
> 中文: 搜索与启发式算法练习平台（BFS / DFS / A* / 经典状态空间谜题），包含模块化 Python 实现与可扩展测试框架。

## 🔍 Scope / 范围
| Component | EN | 中文 |
|-----------|----|------|
| `search.py` | Generic uninformed search framework | 通用无信息搜索框架 |
| `informedSearch.py` | Heuristic guided (A*, Best‑First) | 启发式搜索实现（A* / 最佳优先） |
| `eightPuzzle.py` | 8-puzzle solver | 八数码求解器 |
| `RiverCross.py` | River crossing puzzle | 过河问题（状态合法性检测） |
| `pq.py` | Priority queue | 优先队列封装（基于 heapq） |
| `Mover.py` | Move abstraction | 动作抽象层（生成后继） |
| `Test.py` | Simple test harness | 轻量测试驱动 |

## 🗂 Structure / 目录
```
1/            # 主实现集 (核心脚本集中于此目录)
2/            # 扩展/实验性代码 (如需分类可重命名)
LICENSE
README.md
```

## 🚀 Quick Start / 快速开始
```bash
git clone <repo-url>
cd CS-480
python 1/informedSearch.py      # 运行启发式搜索示例
python 1/eightPuzzle.py         # 解决八数码并打印步数
python 1/RiverCross.py          # 运行过河问题状态扩展
```

Optional (Notebook):
```bash
pip install notebook
jupyter notebook
```

## 🧠 Heuristics / 启发式示例 (8-Puzzle)
| Heuristic | 描述 | Notes |
|-----------|------|-------|
| Misplaced tiles | 统计错误位置数 | Admissible, 易实现 |
| Manhattan distance | 累积曼哈顿距离 | 更精确，仍可接受 |
| Linear conflict (扩展) | 行/列冲突加罚值 | 可扩展提高估计质量 |

在 `informedSearch.py` 中可添加：
```python
def linear_conflict(state) -> int:
   # TODO: 实现行列冲突启发式
   return manhattan(state) + conflict_penalty(state)
```

## 🧪 Testing / 测试
轻量测试：
```bash
python 1/Test.py
```
建议新增 `tests/` + `pytest`：
```python
def test_goal_reached():
   from eightPuzzle import solve
   assert solve("12345678_") == []  # 已是目标状态
```

## 🧩 Extending / 拓展
添加新谜题：
1. 建立新文件 `myPuzzle.py`
2. 实现：`initial_state()`, `is_goal(state)`, `expand(state)`
3. 使用 `search.py` 中通用搜索例程：
```python
from search import bfs
solution = bfs(initial_state())
```

## 📈 Performance / 性能提示
- 启发式越贴近真实距离，Open 集合越小
- 避免重复展开：使用 `visited` hash 存储已处理状态
- 优先队列中可存 `(f, counter, node)` 解决同分值比较问题

## 🧬 Architecture / 架构概述
State → Heuristic → Frontier (PQ/Queue) → Expansion (Mover) → Goal Test → Path Reconstruction

## 🛠 Code Style / 代码建议
- 使用 `dataclass` 表达 Node（可选）
- 添加类型标注：`def expand(state: str) -> list[str]: ...`
- 复杂函数写开头注释：时间复杂度 / 空间复杂度

## 🌐 Bilingual Notes / 双语补充
| EN | 中文 |
|----|------|
| frontier | 前沿 / 待探索集合 |
| explored | 已探索集合 |
| heuristic | 启发函数 |

## 🤝 Contributing / 贡献
1. 提交前运行脚本确保无异常
2. 新增启发式请在 README 的 Heuristics 表中添加条目
3. 大型重构请开 issue 讨论方向

## 📄 License / 许可证
详见 `LICENSE`。

## Roadmap / 后续规划
- [ ] 添加 IDA* 示例
- [ ] 引入 Bidirectional Search
- [ ] 提供可视化 (Notebook 展示搜索树)
- [ ] Benchmark 脚本输出节点展开数量

---
### 中文速览
运行脚本 → 查看启发式差异 → 添加新谜题 → 扩展测试与性能分析。

