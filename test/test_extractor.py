import sys
import unittest
from io import StringIO

from WikiExtractor import Extractor, dropNested

lines_str = """
{{存命人物の出典明記|date=2012年3月}}
{{Infobox 漫画家|
| 名前 = 羽海野 チカ
| 画像 =
| 画像サイズ =
| 脚注 =
| 生地 = {{JPN}}・[[東京都]][[足立区]]&lt;ref name=&quot;Profile&quot; /&gt;
| 国籍 = {{JPN}}
| 生年 =
| 生月 = 8
| 生日 = 30
| 没年 =
| 職業 = [[漫画家]]
| ジャンル = 少女・青年漫画
| 活動期間 = 1995年-
| 代表作 = 『[[ハチミツとクローバー]]』&lt;br /&gt;『[[3月のライオン]]』
| 受賞 = 第27回[[講談社漫画賞]]少女部門(2003年)&lt;br /&gt;[[このマンガがすごい!]]オンナ編第1位(2006年、2007年)&lt;br /&gt;第1回[[ブクログ]]大賞マンガ部門大賞(2010年)&lt;br /&gt;第35回講談社漫画賞一般部門(2011年)&lt;br /&gt;第18回手塚治虫文化賞マンガ大賞(2014年)
| 公式サイト = [http://www13.plala.or.jp/umino/ 羽海野チカ_umino*chika]
}}
{{漫画}}
'''羽海野 チカ'''（うみの ちか、8月30日&lt;ref name=&quot;Profile&quot;&gt;[http://natalie.mu/comic/artist/1800 コミックナタリー羽海野チカ]（2011年7月29日閲覧）&lt;/ref&gt; - ）は、[[日本]]の[[漫画家]]。[[東京都]][[足立区]]出身&lt;ref name=&quot;Profile&quot; /&gt;。[[東京都立工芸高等学校]]デザイン科卒業{{要出典|date=2011年12月}}。[[女性]]。

== 略歴 ==
小学生の頃から[[キャラクターデザイナー]]や漫画家になる夢を抱いており&lt;ref name=&quot;Profile1&quot;&gt;[http://www.s-woman.net/umino/1.shtml 『ハチミツとク
ローバー』スペシャルインタビュー 羽海野チカ]（2011年12月5日閲覧）&lt;/ref&gt;、美術系の高校の時、「[[ぶ〜け]]」に一度だけ作品投稿し掲載されたが&lt;ref name=&quot;萩尾対談&quot;&gt;『マンガのあなた、SFのわたし 萩尾望都対談集1970年代編』所収「萩尾望都×羽海野チカ」河出書房新社 2012年&lt;/ref&gt;、卒業と同時に株式会社[[サンリオ]]へ就職&lt;ref name=&quot;Profile2&quot;&gt;2003年 フリーマガジン「Sai+」no.6 「ハチミツとクローバー」マンガ家 羽海野チカ・インタビューより（2011年12月5日閲覧）&lt;/ref&gt;、勤務外に同人誌活動をする&lt;ref name=&quot;萩尾対談&quot; /&gt;。
就職してからの3年後、独立しフリーへと転進&lt;ref name=&quot;Profile2&quot; /&gt;し、キャラクターイラスト（[[イラストレーター]]）やグッズデザイナー等を手掛ける。

しかし、同人誌活動は継続し&lt;ref name=&quot;萩尾対談&quot; /&gt;、漫画家への夢をあきらめず、[[コミックマーケット]]参加時代には同人誌を発行しサークルを1人で回し、見かねた読者が度々手伝うこともあったが、コミケ帰りには友達がいなく一人で泣いて帰ったと雑誌CONTINUE SPECIAL 48-49P で回答している。

[[ペンネーム]]は自身の[[読み切り]]作品、「海の近くの遊園地」からとったものである&lt;ref name=&quot;Profile1&quot; /&gt;。

偶然『[[CUTiE Comic]]』へのカット絵の仕事を依頼された際に、[[ネーム (漫画)|ネーム]]を見せたことから『[[ハチミツとクローバー]]』でデビュー、初連載となった&lt;ref name=&quot;Profile2&quot; /&gt;。しかし『CUTiE Comic』休刊が決定したことで、連載が終了する。
それでもこの作品を描き続けたいと、自ら出版社へ持ち込みをし、[[集英社]]の『[[ヤングユー|YOUNG YOU]]』での再連載が決定した&lt;ref&gt;BSマンガ夜話「ハチミツとク
ローバー」2008年6月20日　いしかわじゅん発言。『３月のライオン』第10巻にて、作者のあとがきに掲載。&lt;/ref&gt;。（後に『[[Cocohana|コーラス]]』へ移籍。）

『ハチミツとクローバー』は[[2005年]]に[[アニメ]]化、[[2006年]]に実写[[映画]]化、[[2008年]]にはTV[[ドラマ]]化され大ヒットし、自身の代表作となる。[[2003年]]には同作で第27回[[講談社漫画賞]]少女部門を受賞している。

[[2007年]]からは、『[[3月のライオン]]』を連載開始。[[2010年]]、第1回[[ブクログ]]大賞マンガ部門、[[2011年]]にはマンガ大賞と第35回講談社漫画賞一般部門、[[2014年]]に第18回手塚治虫文化賞マンガ大賞をそれぞれ受賞している。

[[2013年]]入院、手術、療養のため一時休載された。

== 人物 ==
* 心から敬愛する漫画家は「[[くらもちふさこ]]」「[[萩尾望都]]」&lt;ref&gt;[http://ameblo.jp/chica-umino/entry-10170465474.html 公式ブログ「海の近くの遊園地」2008年11月28日エントリ「2007/3/26 まんがキッチン☆」（2013年3月17日確認）]&lt;/ref&gt;。萩尾望都の作品から技法を学びとり独習した。『ハチミツとクローバー』はぐち
ゃんは、萩尾望都『[[ポーの一族]]』シリーズ短編第2作『[[ポーの村]]』に登場した[[メリーベル]]をイメージして、巻き毛の髪の長いおでこを出した少女にしたという&lt;ref name=&quot;萩尾対談&quot; /&gt;。
* 『ハチミツとクローバー』に出てきた「折れたシソの茎」のエピソードは作者である羽海野チカの失恋、いじめられっ子をかばった姪の話はそれぞれ実話と、[[ニコ・ニコルソン]]の漫画道場破りで収録されている。
* 『ハチミツとクローバー』は、ファミリーレストラン[[ロイヤルホスト]]でネーム作業をしていたと「[http://www.amazon.co.jp/dp/4872339568/ CONTINUE SPECIAL 特集 ハチミツとクローバー]」で回答している。
* デビュー第2作目の『3月のライオン』は編集者の、[[将棋]]か[[ボクシング]]漫画との提案で、将棋を全く知らなかったが興味があって、対局シーンは作ってもらいつつ描いている。『ハチミツとクローバー』成功後の「一発屋」との風評に抗して、手堅い作品をと前作7巻目から準備を始めた。萩尾望都『[[海のアリア]]』に倣い実在の場所でキャ
ラクターの存在感を出すため[[鎌倉]]を舞台にと考えたが、重ねての写真取材が必要で、川べりで橋が多くあり、川で画面が広くなり絵になる場所ということで都内の[[月島]]を舞台にした&lt;ref name=&quot;萩尾対談&quot; /&gt;。
* 2010年12月8日に公式ブログで、「東京都青少年健全育成条例改正案」の表現への規制に、反対を表明している&lt;ref&gt;[http://ameblo.jp/chica-umino/entry-10730298673.html 公式ブログ「海の近くの遊園地」2010年12月8日エントリ「東京都青少年健全育成条例改正案」について]&lt;/ref&gt;。
* 『ハチミツとクローバー』のあとがきにもあるように、『[[ハリー・ポッターシリーズ|ハリー・ポッター]]』と[[宮崎駿|宮崎アニメ]]が好きらしく、自らを[[オタク]]と称する。
* 『[[3月のライオン]]』3巻あとがきによれば自身を「巨大なネガティブエンジンを4基搭載した巨大生物のようなもので、そのエネルギーの強大さといったら空も飛べるはず☆」と語っている。
* 新刊発売日には書店に新刊が本当に並んでいるか・買ってくれる読者がいるか不安になり、書店では売れ行きを見て「不安とアンドの急激な温度差に動揺し思考が停止」すると収録されている。
* 愛猫家であり、スコティッシュフォールド種の「ブンちゃん」と一緒に暮らしており３月のライオン単行本２巻以降の著者（のネコ）近影にて収録されている。
* 2013年9月28日の公式Twitterによると、好物は[[雪見だいふく]]である。

== 作品リスト ==
=== 連載作品 ===
; [[ハチミツとクローバー]]
: 詳細については同項目を参照。
: 同作品の[[アニメ]]では本人のイメージ・キャラクターである、“ウミノクマ”が時々出現していた（声優はない）。
: 第27回[[講談社漫画賞]]少女部門受賞作。
; [[3月のライオン]]
: 詳細については同項目を参照。
: 白泉社『[[ヤングアニマル]]』2007年14号（7月13日発売）より連載中。第1回[[ブクログ]]大賞マンガ部門、[[マンガ大賞]]2011大賞、第35回講談社漫画賞一般部門受賞作品、[[2014年]]第18回手塚治虫文化賞マンガ大賞。

=== 読み切り作品 ===
; 冬のキリン
: 全6ページのカラーで掲載された。作中に登場した公園の[[観覧車]]は、『ハチミツとクローバー』2巻で登場する観覧車と同じ場所のものである、と同作品が収録された『スピカ〜羽海野チカ初期短編集〜』にて述べている。
: [[マガジン・マガジン]]『小説JUNE』118号、2000年4月掲載。
; 夕陽キャンディー
: 全6ページの作品で、『スピカ〜羽海野チカ初期短編集〜』に収録された。
: [[JUNK!BOY]]（[[ビブロス]]）2000年夏号掲載。
; ミドリの仔犬
: [[探偵]]に夢を抱いている、少年“キオ”の短編作品第1作目。羽海野が小さい頃に読んだ、「探偵シリーズ」のような物語が描きたくて作った作品である、と同作品が収録さ
れた『スピカ〜羽海野チカ初期短編集〜』にて述べている。
: [[ソニーマガジンズ]] Be Street Vol.2 2000年8月29日掲載。
; 空の小鳥
: 『ハチミツとクローバー』10巻に収録された。『[[YOUNG YOU]]』（現在は休刊）2001年8月号掲載。
; はなのゆりかご
: 「ミドリの仔犬」のその後の続編の短編作品第2作目。『スピカ〜羽海野チカ初期短編集〜』に収録された。
: [[幻冬舎コミックス]] Be Street Vol.7 2001年12月24日掲載。
; スピカ
: [[バレエ]]と勉強の両立に悩む女の子のストーリー。雑誌掲載時の予告カットで、「学校ジャージにチュチュ」を描きたくて作った作品である、と同作品が収録された『スピカ〜羽海野チカ初期短編集〜』にて述べている。
: [[flowers]]（[[小学館]]）2002年10月号掲載の28ページ作品。
; タイトル不明
: [[装苑]]（[[文化出版局]]）2002年10月号掲載の4コマ作品。
; [[星のオペラ]]
: 『ハチミツとクローバー』10巻に収録された。各漫画家による『[[ドラえもん]]』のひみつ道具を[[リスペクト]]したオムニバス企画作品のひとつ。COMIC CUE Vol.300!（2003年）掲載。
; イノセンスを待ちながら
: [[パトレイバー]]劇場版1・2に登場する背景や登場人物南雲警部、[[攻殻機動隊]]に登場するバトーへの悲しみを描いた6ページ作品。[[スタジオジブリ]]小冊子 熱風 2004
年2月掲載（[[太田出版]]・コンティニュースペシャル）。

=== 挿絵・イラスト ===
* 冒険者たち GLASS HEART（[[若木未生]]）
* LOVE WAY GLASS HEART（同）
* 熱の城 GLASS HEART（同）
* まんがキッチン（[[福田里香]]）
* [[連れてって 連れてって]]（[[DREAMS COME TRUE]]）
* さざなみLP（[[スピッツ (バンド)|Spitz]]）
* ワルツ（[[スネオヘアー]]）
* [[ドラマチック (YUKIの曲)|ドラマチック]]（[[YUKI (歌手)|YUKI]]）
* 松本隆WORKSコンピレーション「風街少年」「風街少女」（[[松本隆]]）
* 神菜、頭をよくしてあげよう（[[大槻ケンヂ]]）
* 扉を開けて（[[新井素子]]）
* 妄想炸裂（[[三浦しをん]]）
* [[夜は短し歩けよ乙女]]（[[森見登美彦]]）解説
* [[ふしぎの国のアリス]]（[[ルイス・キャロル]]）- 2006年ナツイチスペシャルカバー版
* MORI LOG ACADMEY（[[森博嗣]]）
* 新訳 [[赤毛のアン]]シリーズ（[[ルーシー・モード・モンゴメリ]]）集英社みらい文庫 [[おのともえ]]絵共作
*# 赤毛のアン 2011年
*# アンの青春 2012年
*# アンの愛情 2013年
* 広告特集「嵐とマンガ」にて[[櫻井翔]]の肖像イラスト - 2011年2月3日 [[朝日新聞]]朝刊
* [[集英社みらい文庫]]イメージキャラクター
* [[マコちゃんのリップクリーム]] 第7巻表紙
: 羽海野が「[[杉田智和のアニゲラ!ディドゥーーン]]」に出演した際、この作品が好きだと発言し、それが作者の[[尾玉なみえ]]の耳に入り実現した企画&lt;ref&gt;[[月刊少年シリウス]] 2012年5月号「なみえの懺悔」より&lt;/ref&gt;。『ハチミツとクローバー』第6巻の表紙のセルフパロディである。

=== アニメーション ===
* ハチミツとクローバー
* ハチミツとクローバーII
* [[〈物語〉シリーズ セカンドシーズン|囮物語]]（第4話エンドカード）
* 3月のライオン（第22話（最終回）エンディング原画）
以下キャラクター原案:羽海野チカ
* [[東のエデン]]（2009年4月開始、[[フジテレビジョン|フジテレビ]]「[[ノイタミナ]]」枠）
* 東のエデン 総集編 Air Communication
* 東のエデン 劇場版I The King of Eden
* 東のエデン 劇場版II Paradise Lost
* [[Xi AVANT]] （2011年）

== 書籍 ==
=== 漫画 ===
* ハチミツとクローバー（宝島社版/全1巻）
* ハチミツとクローバー（全10巻）
* ハチミツとクローバー Vol.0 オフィシャル・ファンブック
* 3月のライオン（既刊13巻、連載中）
* 3月のライオン おさらい読本 初級編
* スピカ 〜羽海野チカ初期短編集〜

=== 対談 ===
* 雑誌「オトメコンティニュー」 Vol.4「[[木皿泉]]×羽海野チカ2万字対談」&lt;ref&gt;[http://www.ohtabooks.com/otome/backnumber/vol04/2011/01/07172302.html 「オトメコンティニュー」HP Vol.4紹介]&lt;/ref&gt;2011年 [[太田出版]]
* マンガのあなた SFのわたし 萩尾望都・対談集 1970年代編「特別対談 羽海野チカ」2012年 [[河出書房新社]]
* MOE (モエ) 2015年 01月号 1万字ロングインタビュー 羽海野チカをつくったもの ―絵本と雑貨と手づくりと― http://www.moe-web.jp/moe/20151.html [[白泉社]]

=== 関連書籍 ===
* ハチミツとクローバー イラストレーションズ
* ハチミツとクローバー 手づくり絵本BOX
* [[spoon.]]（[[角川書店]]） 〜『ハチミツとクローバー』のすべて〜 2005年4月号
* コンティニュースペシャル（太田出版、2005年6月号）
* spoon. （角川書店）〜ハロー＆グッバイ!ハチミツとクローバー〜 2006年8月号
* 別冊spoon 〜ハチミツとクローバー特集〜 2009年3月号
* Otome continue Vol.4 2011年 （太田出版）
* [[よしながふみ]]対談集 あのひととここだけのおしゃべり

== CD・DVD ==
* ハチミツとクローバー（全9巻）
* ハチミツとクローバーII（全4巻）
* ハチミツとクローバー オリジナルサウンドトラック
* ハチミツとクローバー COMPLETE BEST
* 東のエデン Vol.1〜5
* 東のエデン 劇場版I The King of Eden
* 東のエデン 劇場版II Paradise Lost

== 交友 ==
* 『[[デトロイト・メタル・シティ]]』や『[[ササメケ]]』、『[[リストランテ・パラディーゾ]]』、『[[監督不行届]]』など多数の他作家の作品の帯にイラストやコメントを寄せている。逆に『ハチミツとクローバー』の公式ファンブックからは[[高橋しん]]など親交が深い多数の作家からトリビュートされている事が分かる。
* [[島本和彦]]の漫画『[[吼えろペン|新・吼えろペン]]』第29話に、羽海野チカをもじった「'''陸野地下'''」（りくのちか）という漫画家が登場する。またその回が収録さ
れている第8巻の帯に羽海野が応援コメントを寄せており、「『[[吼えろペン|燃えよペン]]』から大好きでした」とそれ以前から島本のファンだった事を明かしている。
* [[戸田泰成]]の漫画『[[スクライド (漫画)|スクライド]]』の読み切り漫画「スクライド・ビギンズ」に、「チカ」を「千力」と読んだ'''羽海野チカ'''（うみの“せんりき”）というキャラクターが登場している。ちなみに漫画『スクライド』の脚本を担当した[[黒田洋介]]は、アニメ『ハチミツとクローバー』の脚本も担当している。
* 声優の[[神谷浩史]]、[[杉田智和]]、[[高橋美佳子]]とはアニメ『ハチミツとクローバー』終了後も交流を続けており、現在でも食事に行ったりお互いの家に遊びに行く仲である。[[神谷浩史]]がパーソナリティーの『[[さよなら絶望放送]]』をよく聞いているらしく、[[高橋美佳子]]がパーソナリティを務める『[[美佳子@ぱよぱよ]]』や、[[杉田
智和]]がパーソナリティを務めるラジオ『[[杉田智和のアニゲラ!ディドゥーーン]]』にもゲスト出演したことがある。また、神谷が出演した「[[Kiramune#Kiramune Music Festival|Kiramune Music Festival]] 2009」では羽海野と杉田から贈られた花が会場に飾られていた（実際は羽海野、杉田、[[マフィア梶田]]の3人からである）。
* 神谷、杉田を通じてか同じく声優の[[中村悠一]]とも交流がある。
* [[よしながふみ]]とも親しい。
* マンガ大賞2014を受賞した[[森薫]]は羽海野チカからの祝辞に感謝した上で[http://news.livedoor.com/article/detail/8693105/ 「同じ高校の先輩」]と会場内を驚かせた
。

== アシスタント ==
; 鳥野しの
: 羽海野には「はれちゃん」と呼ばれている。単行本のあとがき漫画では耳の長いネコのキャラクターとしてよく登場している。
: 『[[フィールヤング]]』にて「[[オハナホロホロ]]」を連載。
; 塾長
: 苗字に“魁”という一文字が入っていたばかりに塾長という連想から命名された。ハチミツとクローバー2巻あとがき漫画でたれ耳キャラクターとして登場している。
; ベッチー
; チヨ
; ワキタ
; エミリー
; まっちゅん
; オノ
; Ｒ

== 脚注 ==
{{脚注ヘルプ}}
{{Reflist}}

== 関連項目 ==
* [[神山健治]]

== 外部リンク ==
* {{Twitter|CHICAUMINO}}
* [http://ameblo.jp/chica-umino/ 海の近くの遊園地] - Amebaでのブログ
* [http://www13.plala.or.jp/umino/ 羽海野チカ_umino*chika] - 本人サイト
* {{Official|http://3lion.younganimal.com/|name=『3月のライオン』羽海野チカ}}
* [http://miraibunko.jp/ 集英社みらい文庫]
* [http://www.1101.com/umino_chika/index.html ほぼ日刊イトイ新聞 恋、みたいなもの。]
* [http://www.1101.com/umino_chika_2012/index.html ほぼ日刊イトイ新聞 ウミコせんせいにきく 書き文字＆マーク入門]

{{Manga-artist-stub}}
{{Normdaten}}
{{DEFAULTSORT:うみの ちか}}
[[Category:日本の漫画家]]
[[Category:東京都区部出身の人物]]
[[Category:存命人物]]"""

lines = lines_str.splitlines()


class TestExtractor(unittest.TestCase):
    def setUp(self) -> None:
        self.extractor = Extractor(123, 77, 'Extractor.title', lines)

    def test_extract(self):
        out = StringIO()
        self.extractor.extract(out)
        print(out.getvalue())

    def test_transform(self):
        input_text = 'AAA {{BBB}} CCC <nowiki>DDD {{EEE}} FFF</nowiki>'
        expected = 'AAA  CCC <nowiki>DDD {{EEE}} FFF</nowiki>'
        result = self.extractor.transform(input_text)
        self.assertEqual(result, expected)

    def test_transform_in_double_nowiki(self):
        input_text = '<nowiki>{{AAA}}</nowiki>{{BBB}}<nowiki>{{CCC}}</nowiki>'
        expected = '<nowiki>{{AAA}}</nowiki><nowiki>{{CCC}}</nowiki>'
        result = self.extractor.transform(input_text)
        self.assertEqual(result, expected)

    def test_wiki2text(self):
        input_text = 'AAA  CCC [[aiee]]<nowiki>DDD {{EEE}} FFF</nowiki>'
        result = self.extractor.wiki2text(input_text)
        expected = 'AAA  CCC aiee<nowiki>DDD  FFF</nowiki>'
        self.assertEqual(result, expected)

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


class TestFunctions(unittest.TestCase):
    def test_dropNested(self):
        input_text = 'AAA {{BBB {{CCC}}}} DDD {{EEE}}'
        result = dropNested(input_text, r"{{", r"}}")
        self.assertEqual(result, 'AAA  DDD ')

    def test_dropNested_in_invalid_case(self):
        input_text = 'AAA {{BBB {{CCC}}}}}} DDD {{EEE}}'
        result = dropNested(input_text, r"{{", r"}}")
        self.assertEqual(result, 'AAA }} DDD ')


if __name__ == '__main__':
    unittest.main()


