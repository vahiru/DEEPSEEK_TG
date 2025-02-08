# DEEPSEEK_TG

DEEPSEEKTTG 是一个基于python编写的 Telegram 机器人。本人只在硅基流动平台使用deepseekv3测试其可用性。Demo： t.me/kamikibot

## checklist

- Python 3.9 或以上版本
- Telegram 账号和机器人令牌
- DeepSeek API 密钥

## 安装

1. 克隆仓库：
    ```bash
    git clone https://github.com/yourusername/kamikibot.git
    cd kamikibot
    ```

2. 安装所需的库：
    ```bash
    pip install -r telegram
    pip install -r request
    ```

## 配置

1. 从 [BotFather](https://core.telegram.org/bots#6-botfather) 获取你的 Telegram 机器人令牌。
2. 从 [DeepSeek](https://api.siliconflow.cn) 获取你的 DeepSeek API 密钥。

3. 在项目根目录下创建 `.env` 文件，并添加你的凭证：
    ```env
    TELEGRAM_BOT_TOKEN=your_telegram_bot_token
    DEESEEK_API_KEY=your_deepseek_api_key
    ```

## 使用

1. 运行机器人：
    ```bash
    python kamikibot.py
    ```

2. 在 Telegram 上与机器人开始聊天并进行互动。

## 贡献

如果你有建议或改进，欢迎提出问题或提交拉取请求。

## 许可证

该项目采用 MIT 许可证 - 请参阅 [LICENSE](LICENSE) 文件了解详细信息。

## 联系方式

如果你有任何问题，请通过 [your-email@example.com] 联系我。
