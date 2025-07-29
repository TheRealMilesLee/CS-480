# CS-480 Project README
## Project Overview
The CS-480 project implements algorithms for problem-solving and search optimization, with a focus on puzzle-solving and pathfinding scenarios. Core functionality includes:
- Search algorithm implementations (BFS, DFS, A*, etc.)
- Puzzle-solving logic for sliding puzzles and river crossing problems
- Heuristic evaluation and state management systems
- Test frameworks for algorithm validation
The project combines Python implementations with Jupyter notebook experiments to demonstrate algorithm behavior and performance characteristics.
## Installation
1. Clone the repository
2. Ensure Python 3.x is installed
3. Install dependencies (if applicable):
```bash
pip install -r requirements.txt
## Usage
### Entry Points
- Run specific algorithms via script:
```bash
python informedSearch.py
python RiverCross.py
- Execute Jupyter notebooks for interactive analysis:
```bash
jupyter notebook
### Core Components
- `search.py`: Base search algorithm framework
- `informedSearch.py`: Implements A* and best-first search
- `eightPuzzle.py`: Sliding puzzle solver
- `pq.py`: Priority queue implementation
- `Test.py`: Unit testing framework
## File Structure
.
├── .vscode/
├── 1/
│   ├── .gitignore
│   ├── LICENSE
│   ├── eightPuzzle.py
│   ├── eightPuzzles.py
│   ├── informedSearch.py
│   ├── Mover.py
│   ├── pitcher.py
│   ├── pq.py
│   ├── RiverCross.py
│   ├── search.py
│   ├── Test.py
│   ├── .sample
│   ├── .json
│   ├── .index
│   ├── .idx
│   └── (other Git metadata files)
└── (additional files)
## Dependencies
- Python 3.x
- Standard library modules
- Jupyter Notebook (for interactive analysis)
## Contribution Guidelines
- Review open issues for feature requests or bug fixes
- Propose changes via pull requests
- Ensure code adheres to PEP8 standards
- Update documentation for new features
## License
This project is licensed under the terms specified in the `LICENSE` file.

---

## 中文版本

# CS-480 项目文档
## 项目简介
CS-480 是一个基于 Python 的算法实现项目，主要聚焦于搜索算法、问题求解框架及经典谜题的实现。项目包含启发式搜索、八数码问题、河流过河问题等核心模块，提供可复用的算法框架与测试用例。
## 安装方式
1. 克隆仓库：`git clone <repository-url>`
2. 安装 Python 依赖（如需）：`pip install -r requirements.txt`
3. 确保已安装 Jupyter Notebook（用于 .ipynb 文件）
## 使用方法
1. 运行 Python 脚本：`python <filename>.py`
2. 执行 Jupyter Notebook：`jupyter notebook <filename>.ipynb`
3. 通过 `Test.py` 文件运行单元测试用例
## 项目结构说明
CS-480/
├── .vscode/                # VS Code 配置文件
├── 1/                     # 未明确分类的代码文件
├── 2/                     # 未明确分类的代码文件
├── eightPuzzle.py         # 八数码问题实现
├── eightPuzzles.py        # 八数码问题扩展实现
├── informedSearch.py      # 启发式搜索算法实现
├── Mover.py               # 移动逻辑抽象类
├── pitcher.py             # 特定移动逻辑实现
├── pq.py                  # 优先队列实现
├── RiverCross.py          # 河流过河问题实现
├── search.py              # 基础搜索算法实现
├── Test.py                # 单元测试框架
├── LICENSE                # 开源协议文件
└── .gitignore             # 版本控制忽略配置
## 依赖项
- Python 3.x
- Jupyter Notebook（可选）
- 标准库（无需额外安装）
## 开发与贡献指南
1. 通过 `git clone` 获取源码
2. 在 `1/` 和 `2/` 目录中添加新功能模块
3. 使用 `Test.py` 验证代码正确性
4. 提交 Pull Request 时请遵循以下规范：
   - 保持代码风格统一（缩进/命名/注释）
   - 新增功能需配套单元测试
   - 重大变更需更新项目简介
