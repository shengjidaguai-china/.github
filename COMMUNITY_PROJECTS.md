# 社区项目收录与治理

## 商业化说明

社群支持和鼓励项目作者探索商业化。商业使用、修改、集成和再分发按照各仓库当时有效的 `LICENSE`、第三方依赖许可和相关服务条款执行。

许可证如有更新，以对应仓库文件为准；本表在下次维护时同步。

## 项目收录方式

升级打怪开源社区提供两种项目收录方式，申请者可以根据自己的情况选择：

| 收录方式 | 适合情况 | 项目管理方式 |
| --- | --- | --- |
| **迁入升级打怪开源社区** | 希望长期作为社区项目开放共建 | 仓库迁移到 `shengjidaguai-china`。原项目作者继续担任项目负责人，可以受邀成为社区正式成员，并默认拥有自己项目的 Admin 权限；该权限仅限相应项目，不代表拥有整个社区的管理权限。 |
| **社区合作收录** | 希望参加社区共建，但暂时不迁移仓库 | 仓库保留在原作者账号下，由作者继续负责管理；社区提供项目展示、共建入口和活动支持。 |

两种方式都可以进入社区项目清单，并按照相同的项目状态规则定期复核。合作收录项目如果长期无人维护，可以从首页重点展示中移除，但保留历史收录记录。

## 后续项目如何收录

项目申请应提供：

1. 可公开访问的 GitHub 仓库；
2. 清楚的 README、项目负责人与问题反馈入口；
3. 明确的许可证和第三方素材边界；
4. 至少一个可以让新成员开始参与的任务；
5. 同意遵守社区行为准则、项目维护与公开更正规则；
6. 如果社区已经收录同类项目，说明新项目在目标人群、解决问题、实现方式或交付成果上的差异。高度相似且没有明确差异的项目，暂不列为同一阶段的重点共建项目。

## 项目状态与定期复核

收录项目使用以下四种状态：

| 状态 | 说明 |
| --- | --- |
| **共建中** | 项目正在推进，项目负责人能够响应问题，并欢迎新成员参与。 |
| **已完成** | 项目已经达到预定目标，成果仍可正常使用或学习，可继续进行必要维护。 |
| **暂停维护** | 项目暂时没有进展，或项目负责人暂时无法持续投入；恢复维护后可以重新调整为“共建中”。 |
| **已归档** | 项目长期无人维护、无法继续使用，或存在无法解决的版权、安全等问题；保留历史记录，但不再作为开放共建项目推荐。 |

社区每三个月人工复核一次项目状态和首页展示位置。复核主要参考项目进展、项目负责人响应、成果可用性、新手参与入口和社区共建情况；仍然适合重点展示的项目可以继续保留，不强制轮换。每月状态任务继续用于核对仓库的公开状态、默认分支、更新时间和许可证等基础信息。

维护状态发生变化时，由项目负责人提出更新，或在定期复核时统一调整。贡献署名、贡献者文件和项目内鸣谢由各项目负责人自行管理。

## 当前共建项目

本表是社群收录项目的范围清单。只有列入 [`config/community.json`](./config/community.json) 的仓库才会被每月任务核对状态；未来收录或移除项目必须通过公开 PR 修改本清单与配置。

| 项目 | 定位 | 项目负责人 | 任期 | 状态 | 默认分支 |
| --- | --- | --- | --- | --- | --- |
| [shengjidaguai-china/BossHunter](https://github.com/shengjidaguai-china/BossHunter) | AI 求职 Agent 与自动化流程 |  |  | [招募中](./README.md#bosshunter-项目维护者招募) | `main` |
| [shengjidaguai-china/personal-homepage-skill](https://github.com/shengjidaguai-china/personal-homepage-skill) | 个人主页与 HTML PPT 生成 Skill |  |  |  | `main` |
| [shengjidaguai-china/goutoujunshi](https://github.com/shengjidaguai-china/goutoujunshi) | AI 恋爱军师与关系支持 Skill |  |  |  | `main` |
| [shengjidaguai-china/xiaoguan](https://github.com/shengjidaguai-china/xiaoguan) | 面向个人与 B 端销售的本地客户军师、成交教练与混合 RAG Skill | [@powerycy](https://github.com/powerycy) |  | 共建中 | `main` |
| [shengjidaguai-china/qiangshou-skill](https://github.com/shengjidaguai-china/qiangshou-skill) | 事实核验与技术内容写作 Skill |  |  |  | `main` |
| [shengjidaguai-china/multi-model-review](https://github.com/shengjidaguai-china/multi-model-review) | 多模型评审与裁判投票 Skill |  |  |  | `main` |
| [shengjidaguai-china/multi-style-image-generator](https://github.com/shengjidaguai-china/multi-style-image-generator) | 多风格图片生成与 360° 空间预览 Skill |  |  |  | `main` |
| [shengjidaguai-china/fitness-tracker](https://github.com/shengjidaguai-china/fitness-tracker) | 健身训练记录、周期计划与 AI 教练辅助 | [@yuppiez99999](https://github.com/yuppiez99999) |  | 共建中 | `master` |
| [xin-yi33/RxyCode](https://github.com/xin-yi33/RxyCode) | 本地 AI 编程工作台，支持桌面端、终端、插件与专家团 | [@xin-yi33](https://github.com/xin-yi33) |  | 共建中 | `master` |
| [xin-yi33/coding-agent-crew](https://github.com/xin-yi33/coding-agent-crew) | 用于开发和改进 coding agent 的工程流程与角色 Skill 包 | [@xin-yi33](https://github.com/xin-yi33) |  | 共建中 | `main` |
| [xin-yi33/-novel-writer-skill](https://github.com/xin-yi33/-novel-writer-skill) | 小说细纲、章节创作、长篇记忆与草稿发布 Skill | [@xin-yi33](https://github.com/xin-yi33) |  | 共建中 | `main` |

### 2026-09-23 收录记录与参与入口

| 项目 | 收录方式 | 许可证 | 新成员参与入口 | 申请与维护确认 |
| --- | --- | --- | --- | --- |
| fitness-tracker | 已迁入社区，原作者继续负责 | [PolyForm Noncommercial 1.0.0](https://github.com/shengjidaguai-china/fitness-tracker/blob/master/LICENSE)，公开源码、非商业使用；商业使用需另行授权 | [补充入门级示例训练计划与说明](https://github.com/shengjidaguai-china/fitness-tracker/issues/12) | [申请 #29](https://github.com/shengjidaguai-china/.github/issues/29) |
| RxyCode | 社区合作收录，保留作者仓库 | [MIT](https://github.com/xin-yi33/RxyCode/blob/master/LICENSE) | [插件与专家团入门任务](https://github.com/shengjidaguai-china/.github/issues/25) · [贡献指南](https://github.com/xin-yi33/RxyCode/blob/master/CONTRIBUTING.md) | [维护确认](https://github.com/shengjidaguai-china/.github/issues/25#issuecomment-5724967521) |
| coding-agent-crew | 社区合作收录，保留作者仓库 | [MIT](https://github.com/xin-yi33/coding-agent-crew/blob/main/LICENSE) | [路径表样例、最小评测夹具与宿主安装任务](https://github.com/shengjidaguai-china/.github/issues/28) | [维护确认](https://github.com/shengjidaguai-china/.github/issues/28#issuecomment-5724968099) |
| Novel Writer | 社区合作收录，保留作者仓库 | [MIT](https://github.com/xin-yi33/-novel-writer-skill/blob/main/LICENSE) | [宿主适配、草稿发布与章节样例任务](https://github.com/shengjidaguai-china/.github/issues/27) | [维护确认与安装记录](https://github.com/shengjidaguai-china/.github/issues/27#issuecomment-5724967831) |

三个合作项目由同一位作者继续维护，作者确认的投入优先级为 RxyCode、coding-agent-crew、Novel Writer；不承诺固定周更，无法继续维护时会说明并协助交接。后续按社区季度复核规则检查维护情况。

使用边界：fitness-tracker 保留原有非商业许可证，训练与 AI 建议仅供辅助参考；RxyCode 在本机运行，但使用云端模型时会发送提示词及进入上下文的代码片段、工具结果等；Novel Writer 的安装验证由作者在 Windows / Claude Code 环境完成，其他宿主仍待适配。收录不代表社区已完成全部功能或安全审计。
