# fqsign

自用的签到脚本

qq推送 请到 https://wx.scjtqs.com/qq/user 里面获取

# 添加github的 actions 方法使用

### 1.先把本项目fork到你自己的账号下去
本项目地址：https://github.com/scjtqs/fqsign

### 2.将参数填到Secrets

在`Secrets`中的`Name`和`Value`格式如下：

Name | Value
-|-
USERS_COVER | config.json中内容

将`config.json`中内容复制下来，按照要求填写添加到`Secrets`中，如若选填内容不想配置，留下空数组即可。应填写如下内容：

```json
{
  "users": {
      "cdpc": [
    {
      "email": "你的账号",
      "passwd": "你的密码"
    },
    {
      "email": "你的账号2",
      "passwd":"你的密码2"
    }
  ],
  "linus": [],
  "pucloud": [],
  "vpork": []
  },
  "qqpush": {
    "qq": "1234567",
    "token": "abcdefg"
  }
}
```

填写之前完后，建议本地保存一份，方便下次填写。

注意`json`格式，最后一个要删掉逗号。建议在填写之前，使用[json校验工具](https://www.bejson.com/)进行校验。

注意：不要将个人信息填写到仓库`config.json`文件中（不要动这个文件就没事），以免泄露。

### 3.开启Actions

默认`Actions`处于禁止状态，在`Actions`选项中开启`Actions`功能，把那个绿色的长按钮点一下。如果看到左侧工作流上有黄色`!`号，还需继续开启。

### 4.进行一次push操作

`push`操作会触发工作流运行。

删除掉`.gitignore`中的`config.json.test`即可。完成后，每天早上`6:30`将自动完成每日任务。

# 同步上游代码

## 将参数填到Secrets

> 注意！为了确保 Push 权限足够，需要 Github Personal access tokens

`token`获取方式如下：

1. [生成新的token](https://github.com/settings/tokens/new)，点击这个链接。
2. 为`token`设置名字，然后把`workflow`勾选上，点击最下方`Generate token`即可生成`token`。

在`Secrets`中的`Name`和`Value`格式如下：

Name | Value
-|-
TOKEN | Github Personal access tokens

在最新的代码中，已经加上自动同步上游代码的`Action`，将会定时在每周五`16`点执行，文件地址在`.github/workflows/auto_merge.yml`。

同时您也可以安装[pull](https://github.com/apps/pull)应用，也可实现自动同步上游代码。

# 安利一下clash
>可以将酸酸乳、v2ray 等订阅转换成clash订阅
>
>我提供一个自用(写)的[转换工具](https://wx.scjtqs.com/utils/user/v2toclash)，做了个建议的qq登录授权。
>
> 得到一个新的url地址当做订阅地址就行了


# 申明

本项目仅用于学习。