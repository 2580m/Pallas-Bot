<div align="center">

<img alt="LOGO" src="https://user-images.githubusercontent.com/18511905/195892994-c1a231ec-147a-4f98-ba75-137d89578247.png" width=360 height=270/>

# Pallas-Bot

# ***So-Vits-SVC 4.1、DDSP-SVC 6.1的支持来自@一只沙貂***

<br>

我是来自米诺斯的祭司帕拉斯，会在罗德岛休息一段时间......

虽然这么说，我渴望以美酒和戏剧被招待，更渴望走向战场。

<br>

<div align="left">

# **注意事项：**

**1.关于依赖：笨蛋仓库所有者不会处理依赖，请分别进入 src/plugins/sing/so_vits_svc_41 和 src/plugins/sing/DDSP-SVC 文件夹，借助文件夹内的 requirements.txt 安装依赖**  <br>
**2.下载预训练模型：由于 Github 不允许上传超过 100MiB 的文件，所以 so_vits_svc41 和 DDSP-SVC 运行时所需的预训练模型需要另外下载:** <br>
  **2.1.对于 so_vits_svc_41 : 前往 https://huggingface.co/BG4JEC/DDSP61_SVC41_Pretrain_Models/tree/main 进入 so_vits_svc_41/pretrain ，下载模型并将模型放入本仓库的对应目录** <br>
  **2.2.对于 DDSP-SVC : 前往 https://huggingface.co/BG4JEC/DDSP61_SVC41_Pretrain_Models/tree/main 进入 DDSP-SVC/ ，下载其中的文件并按照 huggingface 上的目录结构将文件放入本仓库的对应目录** <br>
  **2.3.若您无法访问 HuggingFace 请使用以下镜像： https://www.modelscope.cn/models/BG4JEC/DDSP61_SVC41_Pretrain_Models 使用方法与 2.1 与 2.2 中所述相同**

<br>

**其他改动：** <br>
1.新增了本地歌曲库功能，路径在 resource/local_music <br>
2.唱歌时可以传入 -t 参数用来控制输出时长，该参数的优先级高于 .env 文件中配置的时长 <br>
2.1.传入 -t 参数时为避免直接发送缓存，会将 svc mix splices 这三个文件夹内的对应 speaker 和 song_id 的缓存删掉 <br>
3.为 key= 参数增加 -k 别名 <br>
4.手动清除特定 speaker song_id 的缓存 <br>
5.牛牛点歌：发送 resource/sing/ncm 中的原曲 <br>
6.发送歌曲文件：以群文件的方式上传 resource/sing/splices 中推理好的成曲 <br>
7.自动化回收切片和人声分离文件 <br>
7.1.人声分离文件可以考虑不自动回收，但若这样则需在传入 -t 参数的代码块内新增删除 hdemucs_mmi 中的对应 song_id 的缓存文件的机制

Todo:支持RVC

<div align="left">

</div>
<br>

## 什么都，守护不了啊！

由于 QQ 官方针对协议库的围追堵截，不断更新加密方案，我们已无力继续维护此项目。  
在 [go-cqhttp](https://github.com/Mrs4s/go-cqhttp) 有完美的平替前，Pallas-Bot 将无限期停止维护，感谢大家一直以来的支持！

## 牛牛有什么功能？

牛牛的功能就是废话和复读。牛牛几乎所有的发言都是从群聊记录中学习而来的，并非作者硬编码写入的。群友们平时怎么聊，牛牛就会怎么回，可以认为是高级版的复读机

## 那为什么牛牛说了一些群里从来没说过的话？

牛牛有跨群功能，若超过 N 个群都有类似的发言，就会作为全局发言，在任何群都生效

## 你说牛牛没有功能，为什么有时候查询信息、或者一些其它指令，牛牛会回复？

从别的机器人（可能是其他群）那里学来的

~~你这机器人功能不错呀，现在牛牛也会了！~~

## 有时候没人说话，牛牛自己突然蹦出来几句话

哈，是主动发言功能！内容同样从群聊里学来的！

## 怎么教牛牛说话呢？

正常聊天即可，牛牛会自动学。

如果想强行教的话，可以这样：

```text
—— 牛牛你好
—— 你好呀
—— 牛牛你好
—— 你好呀
—— 牛牛你好
—— 你好呀
```

如此重复 3 次以上，下一次再发送 “牛牛你好”，牛牛即会回复 “你好呀”

## 牛牛说了一些不合适的话，要怎么删除？

群管理员 **回复** 牛牛说的那句话 “不可以” 即可，同样的若超过 N 个群都禁止了这句话，就会作为全局禁止，在任何群都不发

## 牛牛的一些其他小功能

- `牛牛喝酒`：切换至 ChatRWKV 模型，由 AI 回复（只回复 at 及 `牛牛` 开头的内容）
- `牛牛唱歌 <网易云歌曲 ID>`：AI 牛牛翻唱！（人声提取 + 音色转换）
- `牛牛轮盘` & `牛牛开枪`：需要给牛牛管理员才能使用，试试你就知道是啥功能了.jpg
- 随机修改自己的群名片为近期发言的人，夺舍！期望时间 8 小时一次

## 题外话

牛牛的说什么完全依赖于大家聊什么，希望大家不要故意教牛牛一些不好的东西。发现牛牛学了一些不合适的话及时帮忙删除。

大家一起教出更棒更聪明的牛牛！✿✿ヽ(°▽°)ノ✿

## 如何拥有一只自己的牛牛？

### 直接拉作者部署的牛牛进群

~~官方牛~~

请加 [QQ群](#QQ群)，在群公告的表格里挑一只你喜欢的牵走~  

但请留意，我这里只加明日方舟相关的群聊；且如果发现群里有人故意教牛牛一些不好的话，我会全局拉黑这个群 + 邀请人！
  
### 自行部署

请参考 [基础部署教程](docs/Deployment.md) & [AI 功能部署教程](docs/AIDeployment.md)

## 致谢

### 开源库

[nonebot2](https://github.com/nonebot/nonebot2): 跨平台 Python 异步聊天机器人框架  
~~[go-cqhttp](https://github.com/Mrs4s/go-cqhttp): cqhttp的golang实现，轻量、原生跨平台.~~  
[nonebot-plugin-gocqhttp](https://github.com/mnixry/nonebot-plugin-gocqhttp): 一款在NoneBot2中直接运行go-cqhttp的插件, 无需额外下载安装  
[jieba_fast](https://github.com/deepcs233/jieba_fast): 高效的中文分词库  
[demucs](https://github.com/facebookresearch/demucs): Code for the paper Hybrid Spectrogram and Waveform Source Separation  
[so-vits-svc](https://github.com/innnky/so-vits-svc): 基于vits与softvc的歌声音色转换模型  
[ChatRWKV](https://github.com/BlinkDL/ChatRWKV): ChatRWKV is like ChatGPT but powered by RWKV (100% RNN) language model, and open source.  
[PaddleSpeech](https://github.com/PaddlePaddle/PaddleSpeech): Easy-to-use Speech Toolkit including Self-Supervised Learning model, SOTA/Streaming ASR with punctuation, Streaming TTS with text frontend, Speaker Verification System, End-to-End Speech Translation and Keyword Spotting. Won NAACL2022 Best Demo Award.  
[NapCat](https://github.com/NapNeko/NapCatQQ): 现代化的基于 NTQQ 的 Bot 协议端实现  

### 贡献者

感谢各位大佬！

[![Contributors](https://contributors-img.web.app/image?repo=MistEO/Pallas-Bot)](https://github.com/MistEO/Pallas-Bot/graphs/contributors)

## QQ群

~~牛牛调教一群: 831322617 被腾讯封了 orz~~  
~~牛牛调教一群: 765213099 又被封了（恼~~  
~~牛牛调教四群: 717508273 。。。~~  
~~牛牛调教五群：228620837~~  
牛牛调教六群：865638357  
开发者群: 716692626

## 打赏

请作者喝杯咖啡吧~ （请备注牛牛项目，感谢你的资瓷 ✿✿ヽ(°▽°)ノ✿）

<a href="https://afdian.com/a/misteo">
  <img width="200" src="https://pic1.afdiancdn.com/static/img/welcome/button-sponsorme.png">
</a>
