# Terra Incognita - Game Design Document

Na tomto repozitári sa nachádza implementácia hry v Pygame. Hra predstavuje semestrálnu prácu z predmetu Objektové technológie.

__Autor__: Marek Repiský

__Vybraná téma__: Jeden level, ale neustále sa mení
___

## 1. Úvod
Terra Incognita je 2D hra, v ktorej hráč ovláda mimozemšťana, ako prechádza rôznymi prostrediami a snaží sa vyhýbať prekážkam. Hra kombinuje rozmanité štýly a nepriateľov aby vybudovala pútavý zážitok.

### 1.1 Inspiration
__<ins>Top 100 3D Renders from the Internet's Largest CG Challenge</ins>__

Hra berie inšpiráciu na meniace sa prostredie od [videa](https://www.youtube.com/watch?v=iKBs9l8jS6Q), ktoré predstavuje 100 rozličných animácií na stanovenú tému a tým poukazuje na kreativitu a úsilie umelcov.
<p align="center">
  <img src="https://github.com/SomeUsername456/Terra-Incognita/blob/main/obr%C3%A1zky/TOP%20100%203D%20Renders.jpg" alt=100 Renderov z Internetovej CG výzvy">
  <br />
  <i>Obrázok 1: 100 Renderov z Internetovej CG výzvy</i>
</p>

__<ins>T-Rex Runner</ins>__

Mechaniku hrateľnosti berie od zabudovanej hry v prehliadači Chrome nazývanú _T-Rex Runner_. _T-Rex Runner_ je jednoduchá hra, v ktorej ovládate malého dinosaura T-Rexa, ktorý skáče cez kaktusy a vyhýba sa vtákom. Rýchlosť hry sa postupne zvyšuje, a čím dlhšie prežijete, tým vyššie skóre dosiahnete.
<p align="center">
  <img src="https://github.com/SomeUsername456/Terra-Incognita/blob/main/obr%C3%A1zky/T-Rex%20Game.jpg" alt=T-Rex Runner">
  <br />
  <i>Obrázok 2: T-Rex Runner</i>
</p>

### 1.2 Herný zážitok
Cieľom hry je prežiť čo najdlhšie, vyhýbaním sa prekážok a dosiahnuť čo najvyššie skóre. Hra sa stále zrýchluje, takže uhnúť sa prekážkam, je čoraz ťažšie. Hráč sa môže pohybovať po mape vertikílne alebo horizontálne.

### 1.3 Vývojový softvér
- __Pygame-CE__: zvolený programovací jazyk
- __PyCharm 2024.3.1.1__: vybrané IDE
- __Itch.io__: zdroj grafických assetov
- __IloveImg__: na úpravu obrázkov
- __Pixabay a Youtube__: zdroj audio assetov
- __123app__: na úpravu zvukov
___

## 2. Koncept
### 2.1 Prehľad hry
Hráč ovláda mimozemšťana, ktorý prechádza po Zemi a snaží sa prežiť v hre čo najdlhšie vyhýbaním sa nepriateľov. Existujú tu 2 typy nepriateľov: 
- __pozemný__
- __lietajúci__

Aby sa hráč úspešne vyhol nepriateľom, musí správne načasovať skok a momentum. Obtiažnosť sa dynamicky prispôsobuje __zväčšovaním__ rýchlosti nepriateľov a sveta o __10%__ každých __100__ bodov skóre.

### 2.2 Interpretácia témy (Jeden level, ale neustále sa mení)
__"Jeden level, ale neustále sa mení"__ - keď hráč dosiahne skóre __500__, čo symbolizuje vzdialenosť, ktorú prešiel; prostredie ako aj nepriatelia sa zmenia, čím sa zmení štýl hry.

### 2.3 Základné mechaniky
- __Pozadie__: na vytvorenie pozadia sú použité paralaxné obrázky, ktoré funguje na princípe kombinavoanie viacerích obrázkov pričom jednotlivé vrstvy majú rôzne rýchlosti, čo vytvára dojem hĺbky.
- __Pozemní nepriatelia__: na zemi mapy sa vytvárajú pozemní nepriatelia, ktorí menia výzor podľa typu pozadia.
- __Lietajúci nepriatelia__: na oblohe mapy sa vytvárajú nepriatelia, ktorý tiež menia výzor podľa typu pozadia. Lietajúci nepriatelia sú oddelení od pozemných čo dáva hráčovi možnosť sa im vyhnúť.
- __Pohyb__: hráč si musí správne načasovať svoj skok a momentum, aby sa mohol vyhýbať nepriateľom.
- __Leaderboard__: rebríček najlepších hráčov podľa ich dosiahnutého skóre.

### 2.4 Návrh tried
- __Game__: riadi celú hru. Stará sa o inicializáciu Pygame, načítanie zdrojov, správu herných objektov, spracovanie hernej logiky, vykresľovanie a obsluhu udalostí.
- __Player__: reprezentuje hráča. Inicializuje hráča, stará sa o jeho animáciu, vykreslenie, resetovanie a aktualizuje jeho pozíciu.
- __Background__: reprezentuje a ovláda pozadie hry, vrátane paralaxného efektu pri prechodoch.
- __Animal__: trieda, ktorá slúži ako základ pre všetky zvieratá.
- __Hyena, Snail, Scorpion, Fly, Vulture, Crow, Pigeon, Mouse__: reprezentujú konkrétne typy zvierat v hre. Odvodené od triedy _Animal_.
___

## 3. Grafika
### 3.1 Vizuálny štýl
Hra používa herný, pixelový alebo kreslený štýl, kde každé pozadie vyniká svojím štýlom. Zvieratá a hráč sú nakreslené v pixelovom štýle.
<p align="center">
  <img src="https://github.com/SomeUsername456/Terra-Incognita/blob/main/obr%C3%A1zky/Parallax.png" alt=Paralexné pozadie">
  <br />
  <i>Obrázok 3: Paralaxné pozadie</i>
</p>

### 3.2 Dizajn
V hre sú rôzne assety z [itch.io](https://itch.io/game-assets). Cieľom bolo dosiahnuť podobný ale odlišný štýl pre každé pozadie. Obrázky zvierat a hráča pochádzajú z _[Street Animal Pixel Art](https://free-game-assets.itch.io/free-street-animal-pixel-art-asset-pack)_ a _[Enemy Sprite Sheets Pixel Art](https://free-game-assets.itch.io/free-enemy-sprite-sheets-pixel-art)_ ako aj z iných zdrojov.
<p align="center">
  <img src="https://github.com/SomeUsername456/Terra-Incognita/blob/main/obr%C3%A1zky/hyena5.png" alt=Hyena">
  <br />
  <i>Obrázok 4: Hyena</i>
</p>

___

## 4. Zvuk
### 4.1 Hudba
Hudba do pozadia bola stiahnutá z [youtube.com](https://www.youtube.com/watch?v=yA41iunMG6A). Hudba obsahuje viacero skladieb z hernej scény a tým vhodne dopĺňa grafický dizajn hry.

### 4.2 Zvuky
Zvukové efekty sú rovnako zamerané na hernú scénu a tým zväčšujú herný zážitok. Všetky efekty pochádzajú z [pixabay.com](https://pixabay.com/sound-effects/).
___

## 5. Herný zážitok
### 5.1 Používateľské rozhranie
Používateľské rozhranie je tiež v pixelovom štýle, takže zapadá do zvyšku hry. Hra sa snaží o pohlcujúci efekt s minimom HUD prvkov. V ľavom hornom rohu sa zobrazuje aktuálne skóre a na konci hry je možnosť reštartu.

### 5.2 Ovládanie
__<ins>Klávesnica</ins>__
- __A, D alebo ľavá a pravá šípka__: horizontálny pohyb hráča.
- __W, horná šípka alebo SPACE__: skok.
- __R__: reštartovanie hry. 
