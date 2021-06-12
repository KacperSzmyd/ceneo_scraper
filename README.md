# ceneo_scraper
## Etap 1 - Pobranie składowej pojedyńczej opinii o wybranym produkcie z serwisu [Ceneo.pl](https://www.ceneo.pl/)
* pobranie kodu pojedyńczej storny z opiniamy o wskazanym produkcie 
* analiza kodu HTML pojedynczej opinii 

+---------------+------------+--------------+----------+
|Składowa opinii|Selektor CSS|Nazwa zmiennej|Typ danych|
+:==============+:===========+:=============+:=========+
|Opinia|div.js_product-review|opinion|dict| 
+:--------------+:-----------+:-------------+:---------+
|Identyfikator opinii|`["data-entry-id"]`|opinion_id|int| 
+:--------------+:-----------+:-------------+:---------+
|Autor|span.user-post__author-name|author|string|
+:--------------+:-----------+:-------------+:---------+
|Rekomendacja|div.user-post__author-recomendation|recomm|bool|
+:--------------+:-----------+:-------------+:---------+
|Liczba gwiazdek|span.user-post__score-count|stars|float|
+:--------------+:-----------+:-------------+:---------+
|Treść|div.user-post__text|content|string| 
+:--------------+:-----------+:-------------+:---------+
|Lista zalet|review-feature__col:has(> div.review-feature__title--positives) > .review-feature__item\|pros|\[list\]|
||review-feature__col:has(> div[class*="positives") > .review-feature__item\||
||div.review-feature__title--positives ~ review-feature__item||
+:--------------+:-----------+:-------------+:---------+
|Lista wad|review-feature__col:has(> div.review-feature__title--negatives) > .review-feature__item\|cons|\[list\]|
||review-feature__col:has(> div[class*="negatives") > .review-feature__item\||
||div.review-feature__title--negatives ~ review-feature__item||
+:--------------+:-----------+:-------------+:---------+
|Dla ilu osób użyteczna|span`[id^="votes-yes"]`\|useful|int|
||button.vote-yes > span\||
||button.vote-yes`["data-total-vote"]`||
+:--------------+:-----------+:-------------+:---------+
|Dla ilu usób nieużyteczna|span`[id^="votes-no"]`\|useless|int|
||button.vote-no > span\||
||button.vote-not`["data-total-vote"]`||
+:--------------+:-----------+:-------------+:---------+
|Czy opinia jest potwierdzona zakupem|div.review-pz|purchased|bool|
+:--------------+:-----------+:-------------+:---------+
|Data wystawienia opinii|span.user-post__published > time:nth-child(1)`["datetime"]`|publish_date|string|   
+:--------------+:-----------+:-------------+:---------+
|Data zakupu produktu|span.user-post__published > time:nth-child(2)`["datetime"]`|purchase_date|string|
+:--------------+:-----------+:-------------+:---------+

* Pobranie poszczególnych składowych pojedyńczej opinii do indywidualnych zmiennych
* zdefiniowanie funkcji do pobierania elementów struktury HTML z uwzględnieniem obsługi błędów

## Etap 2 - Pobranie wszystkich opinii o pordukcie 
* zdefiniowanie słownika do przechowywania składowych pojedyńczej opinii
* zdefiniowanie listy do przechywowania wszystkich opinii o produkcie
* dodanie pętli przechodzącej po wszystkich opiniach pojedynczej strony
* dodanie pętli przechodzącej po wszystkich stronach z opiniami 
* eksport opinii o produkcie do pliku .json

## Etap 3 - refaktoryzacja kodu
* parametryzacja kodu produktu, o ktorym pobierane są opinie
* użycie słownika składowych opinii oraz wyrażenia słownikowego (dictionary comprehension) do utworzenia słownika z składowymi pojedyńczej opinii

## Etap 4 - analiza opinii dla pojedynczego produktu
* wyliczenie podstawowych statystyk o opiniach
* rysowanie histogramu gęstości poszczególnych ocen(gwiazdki)
* rysowanie histogramu opinii
