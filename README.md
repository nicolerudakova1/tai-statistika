**Kasutatud andmestik**

Projektis kasutati Tervise Arengu Instituudi (TAI) andmebaasi andmestikku:

ETU41 – Depressiooni sümptomite esinemine soo, vanuserühma ja taustatunnuste järgi

Link andmestikule:
https://statistika.tai.ee/pxweb/et/Andmebaas/Andmebaas__05Uuringud__01ETeU__04VaimneTervis/ETU41.px/table/tableViewLayout2/

### **A) Andmete puhastamine + salvestamine (transform.py)**

Andmed laaditi alla CSV-formaadis TAI andmebaasist.
Andmed loeti Pythonisse kasutades csv moodulit.

Puhastamise käigus tehti järgmised sammud:
1. Puuduvate väärtuste töötlemine
Algandmetes olid puuduvad väärtused märgitud sümboliga "..".
Need asendati väärtusega None.

2. Andmetüüpide korrigeerimine
Numbrilised väärtused teisendati float-tüübiks, et võimaldada arvutusi ja analüüsi.
3. Puuduvate väärtuste taastamine loogilise reegli alusel
Andmestikus kehtib järgmine loogika:
Olulise depressioonita + Olulise depressiooniga = 100%
Kui üks väärtus puudus, arvutati see valemiga: 100 − olemasolev väärtus

Selle tulemusel eemaldati kõik puuduvad protsentväärtused.

Pärast puhastamist:
loodi uus CSV-fail depression_cleaned_data.csv
andmed on ilma puuduvate väärtusteta
andmestik sobib edasiseks analüüsiks ja SQL kasutamiseks

### **B) SQL päringud + andmemudel**

Kasutati lihtsat ühe tabeliga mudelit:

Tabel: depression_stats

Tabel sisaldab järgmisi veerge:
1. Aasta
2. Taustatunnus
3. Depressioon
4. Sugu
5. Vanuserühmade protsendid

Andmed salvestati SQLite andmebaasi (depression.db).

Teostati kolm SQL-päringut:

1. Päring tagastab iga haridustaseme kohta protsentväärtuse vanuserühmas 25–34.
Tulemused järjestatakse kahanevas järjekorras, et näha, millise haridustasemega rühmas on depressiooni osakaal kõige kõrgem.

2. Päring tagastab protsentväärtuse vanuserühmas 25–34 nende inimeste kohta, kellel esineb oluline depressioon aastal 2019.
Analüüs hõlmab ainult rühma „Mehed ja naised” ning võrdleb kahte rahvusrühma: „Eestlane” ja „Mitte-eestlane”.
Tulemused järjestatakse kahanevas järjekorras, et näha, millises rahvusrühmas on olulise depressiooni osakaal kõrgem.


### **C) Visualiseering + uuendusloogika kirjeldus**

Loodi joonis, mis näitab: olulise depressiooniga inimeste osakaalu kolme haridustaseme lõikes erinevates 
vanuserühmades aastal 2019.
Graafik võimaldab visuaalselt hinnata, kuidas haridustase on seotud depressiooni esinemissagedusega ning kuidas see muutub vanuse kasvades.


**Andmevoo igapäevane uuendamine**

Andmevoog võiks toimida järgmiselt:

1. Uued andmed laaditakse automaatselt alla TAI andmebaasist.

2. Puhastamise skript käivitatakse automaatselt.

3. Töödeldud andmed salvestatakse CSV- ja andmebaasifaili.

4. SQL-päringud ja visualiseeringud uuenevad automaatselt.

5. Graafikud salvestatakse pildifailidena või uuendatakse aruandes.

6. Protsessi saab automatiseerida ajastatud ülesandena (cron job või Windows Task Scheduler).

**Projekti failid ja nende roll**

1. **transform.py**
Vastutab andmete puhastamise ja salvestamise eest.

2. **database.py**
Loob SQLite andmebaasi ja teostab SQL-päringuid.

3. **visualization.py**
Loob graafiku töödeldud andmete põhjal.

4. **depression_cleaned_data.csv**
Puhastatud andmestik.

**Kuidas koodi jooksutada**

1. Paigalda vajalikud teegid: `pip install pandas matplotlib`

2. Käivita andmete puhastamine: `python transform.py`

3. Käivita SQL analüüs: `python database.py`

4. Loo visualiseering: `python visualization.py`







