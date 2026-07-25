---
title: "SV Freya"
permalink: /freya/
date: 2024-02-16T18:39:14+00:00
---

Freya är en Malö 116 från 1984, en klassisk orustbåt från den tiden med allt vad det betyder, semilång ingjuten köl, skedda framför rodret och självklart lite för mycket plast i skrovet som sig bör. Då hennes första ägare önskade en hydraulisk rullmast från Reckman, som är lite tyngre och "stadigare" än Seldens dito, har hon även fått lite extra vikt på kölen och sticker därmed lite djupare än vanligt, vi räknar med 185cm.

Lastad väger hon runt 10ton i kranen och av det är ca 1500kg diverse utrustning som kan vara bra att ha på en segelbåt som inte vill vara beroende av behöva gå in i marinor eller få extern hjälp. Vi skulle såklart behöva fler reservdelar och verktyg ombord men då hon bara är 12m räcker platsen inte riktigt till. Man kan tydligen inte få allt.

På tal om utrustning i skrivandets stund är Freya utrustad med följande: (har säkert missat en hel massa)

## Segel
* 130% Genua 49m2 , Crosscut, Hydranet på rulle. (2022)
* 105% Storsegel 33m2, Crosscut Hydranet med stående lattor. (2024)
* 115m2 Gennaker (2022)
* 7m2 stormfock i dacron till löstagbart innre förstag (Äldre men aldrig använd)

## Motor

För att ta oss fram när det inte går att segla eller i lite trängre utrymmen som hamnar etc har vi en motor från Volvo. Något år innan vi tog över Freya fick hon en ny Volvo Penta D2-75 av sina tidigare ägare, för dig som inte är expert på Volvos båtmotorer så är det en turbodiesel som levererar 75hk. Personligen hade jag inte valt en så stor motor och inte heller en med turbo till en segelbåt av Freyas storlek men ibland får man spela de kort man får.

Motorn driver ett VP S150-drev som vi satt en 20/13" trebladig <a href="2025/07/17/propeller.html">Flexofold</a> propeller på.

## Ankring
När man ligger still eller lämnar båten är det bra om den sitter fast, det har Freya alltid gjort utan några som helst problem. 
* Lofrans X2 ankarspel med trumma
* 80m Rostfri kätting (8mm)
* 20kg Viking primärankare
* Vetus (Fortress FX-23) aluminiumankare
* 2 x 40-50 meter förtöjningslinor
* 24kg Ankarvikt, om vi behöver extra vikt på kättingen har vi en kettlebell som även extraknäcker som träningsredskap när andan faller på.
* 2st 5m långa kättingar (6mm) när vi behöver binda mot land runt vassa stenar
* Ankarboj och diverse andra "bra att ha"-prylar

## Navigering, nätverk och kommunikation

Primärt använder vi en Raymarine MFD med sjökort för relevant område för att se vart vi är på väg. För att vi ska vara lättare att se har vi även en sändande AIS (Raymarine AIS700), den visar såklart även andra båtar med sändare på vår MFD. Vår AIS och VHF (Raymarine RAY90 Blackbox) är kopplade på två olika antenner som sitter monterade på olika ställen för att kunna användas som backup till varandra om olyckan skulle vara framme. Skulle vår fasta RAY90 VHF av någon anledning slås ut har vi även en fast Simrad med både AIS och extern handkontroll monterad fast inte inkopplad som backup, och skulle även den gå sönder har vi 2 handhållna VHF'er varav en med DSC och GPS inbyggt. Hängslen och livrem....

På tal om hängslen och livrem, vi har även en separat MFD som vi primärt använder som display till vårt ekolod men displayen går även att använda till navigation om det skulle behövas.

Skulle det vara dimma, mörkt eller nedsatt sikt av andra skäl har vi vår trofasta digitala radar (Raymarine) med doppler funktion, den visar allt från andra båtar utan AIS sändare, land som sticker upp ur vattnet till regnväder. Den är toppen att använda vid ankring i mörker både för att se andra båtar och land.

Utöver det har vi såklart en autopilot som hjälper oss att styra, den är hydraulisk och hänger direkt på roderkvadranten om något skulle hända med övrig styrning då det är lite svårt att komma åt med nödstyrning direkt på roderstocken på en Malö 116. Hydrauliken styrs av en ACU-400 som är kopplad på båtens NMEA-nätverk tillsammans med en digital 9-axlad EV-1 kompass. Autopiloten kan såklart styras både från rorsmans plats via en P70 display och från MFD'n i skyddet av rutor och sprayhood. Vi har även en fjärrkontroll som gör att vi kan styra skutan trådlöst från fördäck eller vart vi nu håller hus om andan skulle falla på.

I toppen av masten har vi förutom en analog klassisk vindex även en vindsensor som skickar data till övriga system på båten så att vi både kan se hur mycket det blåser och från vilken riktning via en Raymarine mn100 display, vindinformationen kan såklart användas av autopiloten för att styra som ett vanligt "analogt" vindroder.

På tal om analoga vindroder så har vi även ett Sailomat 700 på akterspegeln om vi inte vill använda autopiloten eller om den skulle kasta in handsken. Vi har även en rorkultsautopilot som vi kan koppla till vårt vindroder och använda den istället för vindflöjeln om det skulle behövas.

För att allt ska hänga ihop har vi även en YDEG-04 för att få in motorinformation på NMEA-nätet och en Raymarine Micro-Talk gateway för att få tillgång till all information trådlöst.

För den som är lite nördig så finns det även en SignalK server med Grafana på en Raspberry Pi med PICAN-M NMEA och numera även en IoT [Sailserver](/ais/) så att vi kan se vad som händer ombord när vi lämnat Freya ensam på en ankring. Men mer om allt det där vid ett annat tillfälle.

## Elektronik

Freya drivs av 2 LiFePO4 [batterier](/2025/06/10/batteri.html) bestående av 8st 280Ah celler som styrs av två BMS'r som klarar av att leverera nästan 4kW tillsammans vilket är mer än tillräckligt för oss i skrivandets stund. Båten är för tillfället konfigurerad som en enbankslösning vilket betyder att vi använder vår förbrukningsbank (våra lithiumbatterier) även som startbatteri. Det gör allt betydligt mindre komplext då vi bara behöver fundera på hur en sorts batterityp ska laddas och övervakas.

Vår batteribank laddas via 3st 215W 24V Victron solpaneler som är kopplade till en Victron MPPT 100/30. Den som är skarpsynt och snabb på att räkna ser förmodligen att vår MPPT är lite i underkant men då max laddning från solpanelerna är så pass sällsynt har vi valt att låta MPPT'n gå på max under lite längre tid än att lägga pengar på en uppgradering för att krama ut några extra watt lite då och då (runt 3%). Då vi har en temperaturstyrd generator är den kopplad direkt på batteribanken utan massa extra teknik mellan. Som kall laddar generatorn runt 80A, med grövre kablar och extra kylning bör det kunna höjas med 25% utan större bekymmer.

Vårt gamla bly/syra-startbatteri står kvar som reserv och ska få en micro-droppladdare byggd till sig vid tillfälle men fram tills dess fungerar en 4mm2 kabel utmärkt att ladda upp det med lite då och då direkt från husbanken. 

> Om du som läser det här är av den oroliga sorten så har vi såklart testat att starta motorn bara med ett LiFePO4 batteri om utifall ett batteri skulle kasta in handsken. Skulle en BMS gå sönder har vi en extra i reserv med oss och batteribanken går såklart fint att köra utan BMS om det skulle behövas.

För att kunna använda övrig elektronik ombord har vi även 2 inverters ombord, en Victron Phoenix 1200VA som klarar av att leverera stadiga 1000W och som knappt drar 1,5W på standby. Skulle den ge upp eller om vi skulle behöva mer kraft så har vi även en Renegy 3000W inverter som klarar även klarar av toppar på upp till 6kW vilket är betydligt mer än vad våra batterier är sugna på att leverera för tillfället. Vår Renegy är perfekt att använda tillsammans med induktionshällen om gasen skulle ta slut.

De två systemen är kopplade i serie så att båten primärt hämtar 220V från Victron och skulle den stängas av eller om vi behöver mer effekt än vad den klarar av att leverera kommer den större Renergy inverten vakna och ta över.

Vi har tillräckligt med solpaneler och batterier för att kunna driva allt relevant ombord utan att behöva koppla oss till det fasta elnätet. De få gånger vi faktiskt kopplar oss mot det vanliga elnätet så är det 100% galvaniskt avskilt från båtens 12 och 24 volts nät, inte via en isolationstransformator utan helt enkelt genom att det inte finns någon koppling alls mellan de två näten. Vår förbrukning är så pass låg när vi kopplar in oss på elnätet och driver induktionshällen (som vi även använder sommartid via inverter) och värme (elvärme) via landel så solpanelerna klarar av att hålla batterierna fulla utan några som helst problem.

Det finns såklart massor mer att säga om elen ombord men något måste ju sparas till diverse framtida inlägg.

Dubbeuttag för 230V i stuvfack, toalett, navbord, akterkoj, pentry och i förpik.

## Komfort

* Watermaker av märket [MAB](https://watermaker.se). Vår är lite speciell med annan pump och motor än övriga då Ulf har använt Freya som testpilot, vi har även två osmosmembran vilket gör att vi kan producera en bra bit över 100liter färskvatten i timmen.
* Uttag i sittbrunnen för däckspolning med både färsk och saltvatten. 60 liter/min både färskvatten och saltvatten med möjlighet att koppla på högtryckstvätt med 15m spolslang. Perfekt vid rengörning av däck efter smutsigt regn eller seglatser med mycket saltvatten över däck.
* Vattenmantlad dieselvärmare, fungerar som en vanlig luftvärmare som även kan värma upp vår 20 liters varmvattenberedare. På vattenslingan sitter även en kopparledning på toaletten som element och handdukstork.
* Vår dieselvärmare är kopplad till en Afterburner som ger oss lite extra funktioner.

Malö 116 har en djup och rymlig sittbrunn som skyddar väl mot väder och vågor som vill kommma på besök. Vi har även ett "doghouse" som gör att vi kan stänga halva sittbrunnen när vi seglar i dåligt eller kallt väder, det gör att vi sitter både tryggt och varmt i lä bakom rutorna i sittbrunnen samtidigt som vi kan styra Freya via vår Raymarine MFD. 

## Säkerhet

* 3 brandsläckare ombord
* Installerade brandportar till motorn
* Brandvarnare
* Temperatursensorer på batteribanken
* Kolmonoxidvarnare
* Timer till gasolen
* Viking Offshore livflotte för 6 personer
* En hisklig massa fyrverkerier
* 1 PLB1
* 2 MOB1
* Livlinor
* Flytvästar
* 2 Manuella länspumpar, en vid styrplatsen samt en i salongen
* 2 Elektriska länsppumpar. En mindre automatisk om ca 1000 liter/timme som även är kopplad till siren samt en på ca 5000 liter/timmme som aktiveras manuellt