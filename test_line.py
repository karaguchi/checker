import os
from dotenv import load_dotenv
from linebot import LineBotApi
from linebot.models import TextSendMessage

# 1. .envファイルから設定を読み込む
load_dotenv()

# 2. 環境変数からトークンとIDを取得
TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
USER_ID = os.getenv('LINE_USER_ID')

# 3. LINE APIの準備
line_bot_api = LineBotApi(TOKEN)

def main():
    print("LINE送信を開始...")
    try:
        # 4. 実際にメッセージを送る（push通知）
        line_bot_api.push_message(
            USER_ID, 
            TextSendMessage(text='テスト成功！')
        )
        print("✅ LINEにメッセージを送信しました")
    except Exception as e:
        print(f"❌ エラー発生:\n{e}")

if __name__ == "__main__":
    main()