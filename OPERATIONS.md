# 每月维护和上线说明

## 上线结构

建议将本仓库发布为目标 GitHub Organization 下的公开 `.github` 仓库：

- `profile/README.md`：组织中文公开主页；
- `profile/README_EN.md`：英文主页；
- `COMMUNITY_PROJECTS.md`：人工确认的收录项目清单；
- `PROJECT_STATUS.md`：自动生成的项目公开状态；
- `config/community.json`：每月检查的项目白名单；
- `data/project-status.json`：机器可读的项目状态快照；
- `.github/workflows/monthly-community-maintenance.yml`：每月维护任务。

贡献署名由各项目自行维护，社区仓库专注项目入口、状态、治理与资金透明。

## 首次启用

1. 创建 GitHub Organization 和公开 `.github` 仓库；
2. 将本仓库内容通过功能分支和草稿 PR 发布；
3. 在仓库 Actions 设置中允许工作流读取内容、写入分支和创建 PR；
4. 创建 `project:intake` 标签；
5. 手动运行一次 `Monthly community maintenance`；
6. 核对项目状态草稿 PR 后再合并；
7. 飞书账本完成示例数据清理和匿名只读设置后，再启用正式公开金额入口。

## 每月流程

任务在每月 1 日 09:10（Asia/Shanghai）运行：

1. 读取 `config/community.json` 中的项目；
2. 核对仓库是否公开、是否归档或停用；
3. 核对默认分支、最后推送时间和 GitHub 检测到的许可证；
4. 更新 `data/project-status.json` 和 `PROJECT_STATUS.md`；
5. 创建或刷新 `automation/project-status-YYYY-MM` 草稿 PR；
6. 主理人或管理员核对变化后合并。

GitHub 的计划任务可能延迟；公开仓库长期无活动时，计划任务也可能被平台停用。工作流保留手动运行入口。

## 更换群二维码

1. 将新二维码放入 `assets/`，文件名包含失效日期；
2. 同时更新中英文主页和 `SUPPORT.md` 中的图片路径及有效期；
3. 运行 README 双语校验；
4. 通过 PR 发布，保留旧二维码的 Git 历史，但从当前主页移除。

## 新增或移除项目

同一个 PR 中同时修改：

- `config/community.json`；
- `COMMUNITY_PROJECTS.md`；
- 中英文组织主页项目表；
- 必要时补充项目特有的参与方式。

项目收录范围变化只更新社群项目清单；项目自己的贡献者名单、提交历史和署名文件继续由项目维护者管理。

## 赞助账本

飞书账本由主理人维护，公开主页提供账本入口并说明资金用途。
