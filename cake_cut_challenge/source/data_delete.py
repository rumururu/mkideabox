#!/usr/bin/env python3
"""케이크 판정단 데이터 삭제 안내 페이지 (Play 데이터 보안 '데이터 삭제 URL'). 사용: python3 data_delete.py → ../data-delete.html"""
import html
from pathlib import Path
from render import CSS, APP_NAME, PACKAGE, EMAIL

T = {
 'ko': ('한국어', '데이터 삭제 안내', ['앱에서 오늘의 케이크 → 순위 보기를 엽니다.', "아래쪽 '내 순위 기록 지우기'를 누릅니다.", '서버의 순위 기록이 바로 삭제되고 순위 참여 동의도 취소됩니다.'],
   '삭제되는 데이터: 무작위 설치 ID, 그림 별명, 날짜별 점수와 케이크 종류. 요청 횟수 제한용 기록은 원래 1분 뒤 자동 삭제됩니다. 따로 보관하는 데이터는 없습니다. 사진은 처음부터 서버로 보내지 않습니다.',
   '앱을 이미 삭제했다면 그림 별명(예: 🍰 #4821)과 순위에 올린 날짜를 적어 {e} 로 메일을 보내 주세요. 확인 후 7일 안에 삭제합니다.'),
 'en': ('English', 'How to delete your data', ["In the app, open Today's cake → Rankings.", 'Tap "Delete my ranking data" at the bottom.', 'Your ranking records are deleted from the server right away, and your consent to join the rankings is withdrawn.'],
   'Data deleted: the random install ID, picture name, and daily scores with cake type. Rate-limit records are already deleted automatically after one minute. No data is kept afterwards. Photos are never sent to the server in the first place.',
   'If you already deleted the app, email {e} with your picture name (for example 🍰 #4821) and the dates you posted. We delete the records within 7 days after checking.'),
 'ja': ('日本語', 'データ削除の方法', ['アプリで「今日のケーキ」→「ランキング」を開きます。', '下の「ランキング記録を削除」を押します。', 'サーバーのランキング記録がすぐに削除され、参加の同意も取り消されます。'],
   '削除されるデータ: ランダムなインストールID、絵の名前、日付ごとのスコアとケーキの種類。回数制限用の記録はもともと1分後に自動削除されます。削除後に保管するデータはありません。写真はそもそもサーバーに送りません。',
   'すでにアプリを削除した場合は、絵の名前（例: 🍰 #4821）と登録した日付を書いて {e} までメールしてください。確認後7日以内に削除します。'),
 'zh': ('简体中文', '如何删除数据', ['在应用中打开“今日蛋糕”→“排行榜”。', '点击底部的“删除我的排行记录”。', '服务器上的排行记录会立即删除，参加排行榜的同意也会撤销。'],
   '删除的数据：随机安装ID、图案名字、每天的分数和蛋糕种类。限制请求次数的记录本来就会在1分钟后自动删除。删除后不保留任何数据。照片从一开始就不会发送到服务器。',
   '如果已经删除了应用，请把图案名字（例如 🍰 #4821）和上传日期发送到 {e}。我们核实后7天内删除。'),
 'zh_Hant': ('繁體中文', '如何刪除資料', ['在應用程式中開啟「今日蛋糕」→「排行榜」。', '點選下方的「刪除我的排行紀錄」。', '伺服器上的排行紀錄會立即刪除，參加排行榜的同意也會撤銷。'],
   '刪除的資料：隨機安裝ID、圖案名字、每天的分數和蛋糕種類。限制請求次數的紀錄原本就會在1分鐘後自動刪除。刪除後不保留任何資料。照片從一開始就不會傳送到伺服器。',
   '如果已經刪除應用程式，請把圖案名字（例如 🍰 #4821）和上傳日期寄到 {e}。我們確認後7天內刪除。'),
 'es': ('Español', 'Cómo borrar tus datos', ['En la app, abre Pastel del día → Ranking.', 'Toca "Borrar mis datos del ranking" abajo.', 'Tus registros del ranking se borran del servidor al instante y se retira tu consentimiento.'],
   'Datos que se borran: el ID de instalación aleatorio, el nombre con dibujo y las puntuaciones diarias con el tipo de pastel. Los registros del límite de solicitudes ya se borran solos al minuto. No se conserva ningún dato. Las fotos nunca se envían al servidor.',
   'Si ya borraste la app, escribe a {e} con tu nombre con dibujo (por ejemplo 🍰 #4821) y las fechas en que subiste puntuaciones. Lo borraremos en un plazo de 7 días tras comprobarlo.'),
 'fr': ('Français', 'Supprimer tes données', ["Dans l'app, ouvre Gâteau du jour → Classement.", 'Touche « Supprimer mes données de classement » en bas.', 'Tes données de classement sont supprimées du serveur immédiatement et ton accord est retiré.'],
   "Données supprimées : l'identifiant d'installation aléatoire, le nom illustré et les scores quotidiens avec le type de gâteau. Les traces de limitation des requêtes sont déjà supprimées automatiquement au bout d'une minute. Aucune donnée n'est conservée. Les photos ne sont jamais envoyées au serveur.",
   "Si tu as déjà supprimé l'app, écris à {e} avec ton nom illustré (par exemple 🍰 #4821) et les dates de publication. Nous supprimons les données sous 7 jours après vérification."),
 'de': ('Deutsch', 'Daten löschen', ['Öffne in der App Kuchen des Tages → Rangliste.', 'Tippe unten auf „Meine Ranglistendaten löschen“.', 'Deine Ranglisteneinträge werden sofort vom Server gelöscht und deine Zustimmung widerrufen.'],
   'Gelöschte Daten: die zufällige Installations-ID, der Bildname und die täglichen Punktzahlen mit Kuchensorte. Einträge der Anfragebegrenzung werden ohnehin nach einer Minute automatisch gelöscht. Es werden keine Daten aufbewahrt. Fotos werden nie an den Server gesendet.',
   'Hast du die App bereits gelöscht, schreib an {e} mit deinem Bildnamen (z. B. 🍰 #4821) und den Tagen deiner Einträge. Wir löschen sie nach Prüfung innerhalb von 7 Tagen.'),
 'pt': ('Português', 'Como apagar seus dados', ['No app, abra Bolo do dia → Ranking.', 'Toque em "Apagar meus dados do ranking" embaixo.', 'Seus registros do ranking são apagados do servidor na hora e seu consentimento é retirado.'],
   'Dados apagados: o ID de instalação aleatório, o nome com desenho e as pontuações diárias com o tipo de bolo. Os registros do limite de solicitações já são apagados sozinhos após um minuto. Nenhum dado é mantido. As fotos nunca são enviadas ao servidor.',
   'Se você já apagou o app, escreva para {e} com seu nome com desenho (por exemplo 🍰 #4821) e as datas em que enviou pontuações. Apagamos em até 7 dias após conferir.'),
 'id': ('Bahasa Indonesia', 'Cara menghapus data', ['Di aplikasi, buka Kue hari ini → Peringkat.', 'Ketuk "Hapus data peringkatku" di bagian bawah.', 'Catatan peringkat Anda langsung dihapus dari server dan persetujuan Anda dicabut.'],
   'Data yang dihapus: ID instalasi acak, nama bergambar, serta skor harian dengan jenis kue. Catatan pembatasan permintaan memang terhapus otomatis setelah satu menit. Tidak ada data yang disimpan. Foto tidak pernah dikirim ke server.',
   'Jika Anda sudah menghapus aplikasi, kirim email ke {e} berisi nama bergambar (misalnya 🍰 #4821) dan tanggal Anda mengirim skor. Kami menghapusnya dalam 7 hari setelah memeriksa.'),
}
HL = {'zh': 'zh-Hans', 'zh_Hant': 'zh-Hant'}
nav = ''.join(f'<a href="#{c}">{html.escape(v[0])}</a>' for c, v in T.items())
out = ['<!DOCTYPE html>', '<html lang="ko">', '<head>', '<meta charset="UTF-8">',
       '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
       f'<title>데이터 삭제 / Delete your data - {APP_NAME}</title>', '<style>', CSS, '</style>', '</head>', '<body>',
       '<h1>데이터 삭제 &middot; Delete your data</h1>',
       f'<p class="meta">{APP_NAME} &middot; <code>{PACKAGE}</code><br>개발자 mkideabox &middot; <a href="mailto:{EMAIL}">{EMAIL}</a></p>',
       f'<nav>{nav}</nav>']
for c, (name, title, steps, what, mail) in T.items():
    out.append(f'<section id="{c}" lang="{HL.get(c, c)}">')
    out.append(f'<h1>{html.escape(title)} &middot; {html.escape(name)}</h1>')
    out.append('<ol>' + ''.join(f'<li>{html.escape(s)}</li>' for s in steps) + '</ol>')
    out.append(f'<p>{html.escape(what)}</p>')
    out.append('<p>' + html.escape(mail).replace('{e}', f'<a href="mailto:{EMAIL}">{EMAIL}</a>') + '</p>')
    out.append('</section>')
out += ['</body>', '</html>']
(Path(__file__).resolve().parent.parent / 'data-delete.html').write_text('\n'.join(out) + '\n', encoding='utf-8')
