import cloudscraper

url = "https://zozo.jp/shop/zozoused/goods-sale/90839041/?did=146716826&rid=1095"

# 忍者の道具(scraper)を準備
scraper = cloudscraper.create_scraper()

def test_ninja():
    print("忍者モードで潜入開始...")
    res = scraper.get(url)
    print(f"ステータスコード: {res.status_code}")
    
    if res.status_code == 200:
        print("✅ 潜入成功！中身を読み取れたよ。")
        if "51,300" in res.text:
            print("価格データも発見できたよ！")
    else:
        print("❌ 忍者モードでも拒否されちゃった...")

if __name__ == "__main__":
    test_ninja()