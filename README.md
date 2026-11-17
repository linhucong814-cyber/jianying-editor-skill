# JianYing Editor Skill 社区版

用 Python 和 AI Agent 为剪映专业版生成可继续编辑的草稿。可以导入本地视频、图片和音频，编排时间轴，添加字幕、配音、转场、滤镜和关键帧。

本仓库基于 [luoluoluo22 的 JianYing Editor Skill](https://github.com/luoluoluo22/jianying-editor-skill) v1.5.0 整理，由 `linhucong814-cyber` 发布。原项目和内嵌依赖的作者及版本见 [来源与许可证](docs/provenance.md)。

## 平台支持

| 环境 | 可用范围 |
| --- | --- |
| Windows + 国内版剪映专业版 | 生成草稿。旧版 UI 自动导出以剪映 5.9 及更早版本为目标，实际可用性取决于已安装版本。 |
| macOS + 国内版剪映专业版 | 实验性支持草稿生成。在剪映中预览和手动导出。 |
| CapCut 国际版、手机剪映 | 当前不在支持范围内。 |

配音使用 Edge TTS，需要联网。云素材表保留名称和 ID，下载取决于剪映服务的可用性，建议先用自有本地素材验证流程。

## 安装和试跑

需要 Git、Python 3.12；建议安装 FFmpeg 并让 `ffmpeg` 和 `ffprobe` 可以从终端调用。剪映专业版请通过其官方渠道安装。

```bash
git clone https://github.com/linhucong814-cyber/jianying-editor-skill.git
cd jianying-editor-skill
python -m venv .venv
```

macOS 使用 `source .venv/bin/activate`，Windows PowerShell 使用 `.\.venv\Scripts\Activate.ps1`，然后安装依赖。

```bash
python -m pip install -r requirements.txt
```

先用内置的合成视频和音频生成测试草稿。示例在独立目录中创建测试项目，已有同名的测试项目会被更新。

```bash
# macOS
JY_PROJECTS_ROOT=./test_run_artifacts python examples/simple_clip_demo.py
```

```powershell
# Windows PowerShell
$env:JY_PROJECTS_ROOT = "./test_run_artifacts"
python examples/simple_clip_demo.py
```

输出在 `test_run_artifacts/Hello_JianYing_V3/`。要在剪映中查看草稿，把 `JY_PROJECTS_ROOT` 指向已确认的剪映草稿目录，再使用新的项目名称生成。只有要用网页动效捕获时才需额外运行 `python -m playwright install chromium`。

## 给 AI Agent 使用

把完整仓库放进 Agent 的技能目录，或在当前项目中让 Agent 读取 [SKILL.md](SKILL.md)。技能文件会引用同目录下的脚本、规则和资源。

> 用 JianYing Editor Skill 把这三个素材剪进一个新草稿，按文件顺序排列，片头加两秒标题，保留原声。

更多用法见 [使用指南](usage.md) 和 [操作手册](docs/agent-playbook.md)。

## 贡献和许可

项目代码沿用 [MIT License](LICENSE)，内嵌的 pyJianYingDraft 适用 [Apache License 2.0](scripts/vendor/pyJianYingDraft/LICENSE)。提交问题或改动前请查看 [贡献指南](CONTRIBUTING.md)。
