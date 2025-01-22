# Terra Incognita - Game Design Document

Na tomto repozitári sa nachádza implementácia hry v Pygame. Hra predstavuje semestrálny projekt pre predmet Objektové technológie.

__Autor__: Ľubomír Benko

__Vybraná téma__: Jeden level, ale neustále sa mení
___

## 1. Úvod
Terra Incognita je 2D hra, v ktorej hráč ovláda mimozemšťana, ako prechádzaja rôznymi prostrediami a snaží sa vyhýbať prekážkam. Hra kombinuje rozmanité štýly a nepriateľov aby vybudovala pútavý zážitok.

### 1.1 Inspiration
<ins>Top 100 3D Renders from the Internet's Largest CG Challenge</ins>

Hra berie inšipiárciu na meniace sa prostredie od [videa](https://www.youtube.com/watch?v=iKBs9l8jS6Q), ktoré prestavuje 100 rozličných animácií na stanovenú tému a tým poukazuje na kreativitu a úsilie umelcov.
<p align="center">
  <img src="https://github.com/SomeUsername456/MovieLens-ETL/blob/main/MovieLens_ERD.png" alt=100 Renderov z Internetovej CG výzvy">
  <br />
  <i>Obrázok 1: 100 Renderov z Internetovej CG výzvy</i>
</p>

<ins>T-Rex Runner</ins>

Mechaniku hrateľnosti berie od zabudovanej hry v prehliadači Chrome nazývanú T-Rex Runner. T-Rex Runner je jednoduchú a zábavnú hru, v ktorej ovládate malého dinosaura T-Rexa, ktorý skáče cez kaktusy a vyhýba sa vtákom. Hra sa postupne zvyšuje na rýchlosti, a čím dlhšie prežijete, tým vyššie skóre dosiahnete.
<p align="center">
  <img src="https://github.com/SomeUsername456/MovieLens-ETL/blob/main/MovieLens_ERD.png" alt=T-Rex Runner">
  <br />
  <i>Obrázok 2: T-Rex Runner</i>
</p>

### 1.2 Herný zážitok
Cieľom hry je prežiť čo najdlhšie, vyhýbaním sa prekážok a dosiahnuť čo najvyššie skóre. Hra sa stále zrýchluje, takže uhnúť sa prekážkam, je čoraz ťažšie. Hráč sa môže pohybovať po mape vertikílne alebo horizontálne.

### 1.3 Development Software

1.3 Vývojový softvér
- __Pygame-CE__: zvolený programovací jazyk
- __PyCharm 2024.3.1.1__: vybrané IDE
- __Itch.io__: zdroj grafických assetov
- __IloveImg__: na úpravu obrázkov
- __Pixabay a Youtube__: zdroj audio assetov
- __123app__: na úpravu zvukov
___
## 2. Koncept
