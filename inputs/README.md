### Por que os siapes atuais são diferentes da coleta anterior?

Em comparação com coletas passadas houve muita distorção de informação. Novos siapes surgiram, siapes antigos deixaram de existir e por isso decidimos fazer uma pequena análise para saber o que havia ocorrido.

### O que foi feito?


- Contamos a quantidade de Siapes repetidos;
- Transformamos listas de siapes em conjuntos de siapes;
- Realizamos as comparações entre o conjuntos de siapes antigos e siapes novos.

### Posso executar esse código sem o projeto?
Sim. [Aqui](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/7265501908721732/2997771851321793/3630416494522143/latest.html)  há uma versão online no Databricks. Abaixo detalhamos os procedimentos.

## Siapes antigos VS Siapes novos


```python

list_siapes_antigos = [2213705,1975594,1582415,1240255,1714053,2355199,1714245,1621261,2397390,2128227,1751175,1717905,1674151,1278994,1718165,3074016,1495311,1806509,1802971,1670002,1866242,1715037,1017771,1228095,1083055,414695,2077501,2465416,2212758,2091789,2647194,1243118,396307,1321668,1670040,1583297,1923106,1523457,2125184,1163286,1205643,1541567,396310,1714258,2259068,1890095,1806454,1053825,3054099,2353224,2408341,3051962,3051965,2028000,2086207,2453480,1773815,1922730,2213412,1543345,2303561,1806885,1514311,1976866,2857671,1957669,3652543,1545710,1347271,1805741,1181653,1342048,2670029,1733996,1716479,1622468,1806635,1997855,1494364,2969235,1452013,1600131,1166430,1824610,1714333,1932288,1544096,1802981,2053497,2778720,2920879,2999409,1075932,1806473,1521615,1855470,1805780,1714079,1714606,1669481,1673984,1286535,1613523,1566818,1823981,2140339,2073862,1495347,1810758,2778421,1566120,2054349,1586101,1936952,1209630,3046701,1738310,1047432,1461578,2307198,1803028,1157350,2086760,2405039,1141857,2324611,2403558,1114687,2359585,1243629,1135362,2177953,3046725,2082728,2424049,1779124,1919869,2403373,1045370,1414415,1989536,2145538,2145337,2082743,2259009,2082771,1172242,396341,2515320,1333353,1506673,1854626,2585756,2190980,2330828,1446262,1562320,1651506,1606132,1425052,2287311,333743,1497653,1668195,1639993,1054489,2269130,1646054,1714925,1513591,1305260,396348,2626416,2453461,1516953,1314726,1742652,2346474,2449903,396309,2287826,2450151,2358576,3001569,2358560,1677881,1866814,1810852,1671270,1750073,2773653,1956823,2459030,1972281,1868009,1992085,2612800,1048410,1806335,2882034,1509522,2528342,1714158,1846917,1578584,396343,2483376,1998830,1765010,1549816,1849697,396313,1608098,1559161,1849595,1644152,1887789,2778809,1545215,1859784,1612510,1753199,3778301,2465692,2356440,1622769,1354828,2259043,1028844,1767567,1960404,3046771,3043348,1266687,3048570,2392318,1260158,3074337,3043210,2305283,2362447,2269056,1096733,1300112,2220620,1945951,3040143,3035571,1344262,1220588,1850519,1931513,1106764,1603007,2268434,3040015,1445567,1106449,2362263,1674772,1369338,1210042,1242739,3038245,1920159,2362480,1931118,1885864,1639625,1295030,3038201,2268946,1223273,2268962,1931231,1522661,1010218,1548691,1202613,1331638,1280283,3040204,2421279,1008017,2449720,3063651,1926578,1351978,1806558,1809354,1766388,1412720,1545550,1367262,1673887,1714269,1806322,1612618,1714006,1670627,1545427,396361,1347606,1866964,1752076,1806860,1293750,1919410,1550250,1979012,1042177,1805397,1526099,1766085,1669383,1702873,2324639,2605644,1447536,1693060,1806429,1669428,1734818,1817186,1706632,1531432,1506753,3063682,2407318,2420930,3037570,3044724,3074396,3006908,1307256,3057833,2621924,1366262,1633911,1750357,1670421,2055706,1615325,2835021,2213033,2647268,1509560,396406,1780797,1447952,396319,1847005,396345,2275824,2112633,1344385,1669088,2578315,396304,1851841,417480,396317,1854325,2882002,1445181,2093076,2652583,1612008,1544411,1552041,396322,1818437,1546177,1289574,396302,1505717,3287303,1632114,396352,2064979,2055639,1647296,396305,1445570,1221323,1735356,396311,1056334,2585705,1081596,2358462,1806415,2778400,1941853,2799026,1062017,2032774,1866775,1991894,1868167,1669085,1993225,1992355,1801543,1115069,1715546,1866895,1857495,1675646,1582440,2157958,2145222,1531437,1572073,1721067,1161204,1158600,1801529,2070023,1670102,1911587,1848016,2056469,1770896,2031688,1523907,1810697,1451546,1852822,2132096,1714022,1724599,1734120,1996376,1734242,2889730,1069130,2055666,1346487,1992072,1995142,2158134,1847887,1805955,1551469,1982013,1669549,1929798,3043392,3067643,1114898,3046819,3065134,2355166,3046769,3857693,2157654,2118196,1166949,2259454,2355492,1781234,1054265,1992242,1966965,3730657,2178976,2326845,2300979,1070306,1227492,1079363,1998769,1255130,3608635,1695692,1885798,2927342,2303300,1044665,2268933,1071911,2341734,1998194,2884005,1859840,1278513,3036755,1960364,2117051,2213620,1779402,2115806,2425665,3043314,1228751,2426965,2376541,3053081,2996802,1064370,3006937,1225990,1345002,1330146,2132375,1804517,1764968,1565646,1817174,1566547,3825899,1059673,6396274,1857726,1750267,1238040,1816178,2400142,1292448,1055685,1971885,1805847,1507727,1245044,1714448,2031941,1061263,2975474,2093019,2578617,1475444,1789892,2355270,1569443,1792275,1852952,3053116,1228872,2407392,1715025,1086856,2075857,1859693,1984465,2355183,1965894,1763913,1691961,1059009,1674506,1682238,1377937,1998864,1915134,1775593,1919773,1806327,3049235,1432247,1047662,1714573,1224396,1307867,2314006,1046754,1750756,2725571,2321480,1669971,1848243,1058659,2155674,1115061,1953385,1739973,1378429,3044779,2417375,2981983,3073686,2948912,2997052,2389189,1859924,1940164,2035805,3680521,1692519,1991751,1055712,1991874,1991725,2941562,1913549,1992265,2075915,2067096,2993619,2836523,1571613,1969075,1653968,2359211,3049729,2423862,1915790,1649777,3738738,2647223,1872410,2355526,1801817,2778700,1687527,2778371,1992067,2145256,1866823,1887092,1911600,1688422,1693028,1686020,1802639,1894371,1125099,1346264,1992323,1571794,2996746,1900213,1939773,1863139,1743293,1908286,1295986,2061336,199325,3042245,3000538,1308922,2389310,3045573,1811396,1864521,3323686,2044785,2046222,1012116,1016017,2189057,2115859,2045711,2279652,1882965,1991868,1997927,2086657,1998263,1565016,2220519,3005896,2116288,2052419,1141792,1870196,1291659,1989791,1647966,2299718,2203171,2089358,3052057,3005124,3053912,3005098,3048320,3005051,3000518,3027454,1772516,1987186,1434542,1941856,1872793,2639302,1969059,2055681,1771905,2147436,1770056,1982985,1674543,2015250,1055467,1731288,1069297,2031519,1307636,1069806,2080267,1714559,2941614,2028037,2403643,2359408,2884800,1668954,1504300,1577965,1994956,1597112,1570445,1246771,2141506,1633246,2307508,1996830,1634744,2063327,2112919,1991961,1814114,2073429,1316228,2814007,2606987,2359451,2179061,1529267,1840387,1654843,1954343,1197504,2054224,2410397,2981777,2360289,3046693,2995967,2411775,3027651,3065079,2377083,2790064,3052088,2410146,3057831,1882242,2044548,2417870,1212329,2061292,1815470,2269077,1992282,2424075,1859807,1231058,1011243,2300292,2392471,2079946,1885548,1804034,1580369,
3049977]

list_siapes_novos = [2028000,2086207,2453480,1773815,1922730,3110135,2213412,1543345,2303561,1806885,1514311,1976866,2857671,1957669,3652543,1545710,1347271,1805741,1181653,1342048,2670029,1733996,1716479,1622468,1806635,1997855,1494364,2969235,1452013,1600131,1166430,1714333,1932288,1544096,1802981,2053497,2778720,1113176,3124429,2999409,3140939,1915790,1649777,3738738,2647223,1872410,1801817,2778700,3151511,1687527,2778371,1992067,2145256,1866823,1887092,1688422,1693028,1686020,1802639,1894371,1125099,1346264,1992323,1571794,2996746,1900213,1939773,1863139,1743293,1908286,1295986,2061336,2355270,199325,3260145,3153835,3152323,3121368,3045573,3121046,396341,2515320,1506673,1854626,2585756,2190980,2330828,1446262,1562320,1651506,1606132,1425052,2287311,333743,1497653,1668195,1054489,2269130,1646054,1714925,1513591,1305260,2626416,2453461,1516953,1314726,1742652,2346474,3149917,2321480,2449903,396309,2287826,2450151,1333353,3087346,1859924,1940164,2035805,3680521,1692519,1991751,1055712,1991874,1991725,2941562,1913549,1992265,2075915,2067096,2993619,2836523,1571613,1969075,1653968,3125912,3049729,3153220,1078551,2305283,2362447,2269056,1096733,1300112,2220620,1945951,3035571,1344262,1220588,1522462,1931513,1106764,1603007,2268434,3040015,1445567,1100942,1106449,2362263,1674772,1369338,3136031,1220587,1380211,1304596,1210042,1242739,3038245,1920159,1369562,1534454,2362480,1931118,1885864,1639625,1925820,1100187,1295030,3038201,1288187,2268946,1223273,2268962,1931231,1522661,1010218,1548691,1202613,3135955,1525023,1331638,1280283,3040204,2421279,2449720,3063651,1216599,1225990,1345002,1330146,2132375,1804517,1764968,1565646,1817174,1566547,1059673,6396274,1857726,1750267,1238040,1816178,2400142,1292448,1055685,1407016,1200501,1805847,1507727,1245044,1714448,2031941,1061263,2975474,2093019,2578617,1475444,1789892,1569443,1792275,1852952,3125956,3089145,3091508,2213705,1975594,1582415,1413882,1240255,1714053,2355199,1621261,2397390,2128227,1751175,1717905,1674151,1718165,1278994,3074016,1495311,1806509,1802971,1670002,1866242,1715037,1017771,2355526,1228095,1714245,1083055,3825899,2077501,2465416,2212758,2091789,2647194,1243118,396307,1321668,1670040,1583297,1923106,1523457,2125184,1163286,1205643,1541567,1714258,2259068,1890095,1953385,1806454,3105753,3054099,3051962,3051965,1098822,1882242,2044548,2417870,1212329,2061292,1815470,2269077,1992282,2424075,1859807,1231058,1011243,2300292,2392471,1885548,1804034,1580369,3083042,3049977,3153759,1806473,1521615,1855470,1805780,1714079,1714606,1669481,1673984,1286535,1613523,1566818,1823981,2140339,2073862,1495347,1810758,2778421,1566120,2054349,1586101,1936952,3046701,1772516,1987186,1434542,1941856,2639302,1969059,2055681,1771905,2147436,1770056,1982985,1674543,2015250,1055467,1731288,1069297,2031519,1307636,1069806,2080267,1714559,2941614,2028037,2403643,2359408,2884800,1668954,1504300,1577965,1994956,1597112,1570445,1246771,2141506,1633246,2307508,1996830,1634744,2063327,2112919,2079946,1991961,1814114,2073429,1316228,2814007,2606987,2359451,2179061,1529267,1840387,1654843,1954343,1197504,2054224,1172865,3141574,2981777,3046693,3126282,3088671,3027651,3125898,3143336,3124309,3052088,2894656,3136014,1866814,1810852,1671270,1750073,2773653,1956823,2459030,1972281,1868009,1992085,2612800,1048410,1806335,2882034,1509522,2528342,1714158,1846917,1578584,396343,2483376,1998830,1765010,1549816,1849697,396313,1608098,1559161,1849595,1644152,1887789,2778809,1545215,1859784,1612510,1753199,3778301,2465692,2356440,1622769,1354828,1072896,2259043,1028844,1767567,1960404,3046771,3043348,1266687,3154193,3140977,3089637,3124528,3074337,3148074,3043210,1715025,1086856,2075857,1859693,1984465,1355183,1763913,1691961,1059009,1674506,1682238,1377937,1998864,1915134,1775593,1919773,1806327,3049235,1432247,1047662,1714573,1224396,1307867,2314006,1046754,1750756,2725571,1669971,1848243,1058659,2155674,1115061,1739973,1378429,3150512,3044779,3121001,1210836,3073686,3146925,2948912,2997052,3114232,3089052,1864521,3323686,2044785,2046222,1012116,1016017,2189057,2115859,2045711,1005051,2279652,1882965,1991868,1997927,2086657,1998263,1565016,2220519,3005896,2116288,2052419,1141792,1870196,1291659,1989791,1647966,2299718,2203171,2089358,3156385,3048320,3120962,3000518,3129364,3147123,3131404,3122039,3027454,3138573,3151398,3857693,2157654,2118196,1166949,2259454,1781234,1054265,1992242,3730657,2178976,2326845,2300979,1070306,1227492,1079363,1998769,2301915,1255130,3608635,1695692,1885798,2927342,2303300,1044665,2268933,1071911,2341734,1998194,2884005,1859840,1278513,3659516,3036755,1960364,230191,2117051,2213620,1779402,2115806,3121381,3155432,3100022,3131372,2996802,3102969,1064370,3006937,1738310,1047432,1461578,2307198,1803028,1157350,2086760,2405039,1141857,3870514,2324611,2403558,1114687,2359585,1243629,1135362,2177953,3046725,2082728,2424049,1779124,1919869,2403373,1045370,1414415,1989536,2145538,2145337,2082743,2259009,2082771,1172242,3089687,3305285,3131475,1366262,1633911,1750357,1670421,2055706,1615325,2835021,2213033,2647268,1509560,396406,1780797,1447952,396319,1847005,396345,2275824,2112633,1344385,1669088,2578315,396304,1851841,417480,1854325,2882002,1445181,2093076,2652583,1612008,1544411,1552041,396322,1818437,1546177,1289574,396302,1505717,3287303,1632114,396352,2064979,2055639,1789417,1647296,396305,1445570,1221323,1735356,396311,1056334,2585705,3086971,3124459,1926578,1351978,1806558,1809354,1766388,1412720,1545550,1367262,1673887,1714269,1806322,1612618,1714006,1670627,1545427,396361,1347606,1866964,1752076,1806860,1293750,1919410,1550250,1979012,1042177,1805397,1802859,1526099,1669383,1702873,2324639,2605644,1447536,1693060,1806429,1669428,1734818,1817186,1706632,1531432,1506753,3085088,3063682,3037570,3133114,3044724,3074396,3006908,1806415,2778400,1941853,2799026,1062017,2032774,1866775,1991894,1868167,1669085,1993225,1992355,1801543,1115069,1965894,1715546,1866895,1857495,1675646,1582440,2157958,2145222,1531437,1572073,1721067,1161204,1158600,1801529,2070023,1670102,1911587,1848016,2056469,1770896,2031688,1523907,1810697,1451546,1852822,2132096,1714022,1724599,1734120,1996376,1734242,2889730,1069130,2055666,1346487,1992072,1995142,2158134,1847887,3295961,1805955,1551469,1982013,1669549,1929798,3043392,2989611,3067643,3046819,3136382,3131441,1388828,3086918,336632,1181653,1670609,1714179,1545235,2079536,1677881,1806868,1243118,2359110,1547955,1500639,2206331,1574667,2752035,1781560,1802972,1631848,1813593,1991824]
```


<style scoped>
  .ansiout {
    display: block;
    unicode-bidi: embed;
    white-space: pre-wrap;
    word-wrap: break-word;
    word-break: break-all;
    font-family: "Source Code Pro", "Menlo", monospace;;
    font-size: 13px;
    color: #555;
    margin-left: 4px;
    line-height: 19px;
  }
</style>
<div class="ansiout"></div>


### Há siapes repetidos?
Para responder a essa pergunta computou-se a quantidade de elementos antes e depois de transformar uma lista em um conjunto (sem ordem e sem elemento repetido). Nos siapes da última coleta em 2018 não havia nenhuma

### A culpa é da coleta?
Aparentemente não. Professores que estão presentes em cargos nas **Pró-reitorias** e **Direções** não são listados por seus departamentos. Apenas dois deles são listados. Uma solução seria pedir para a SUTIC listar todos eles.


```python
set_siapes_antigos = set(list_siapes_antigos)
set_siapes_novos = set(list_siapes_novos)
print("Quantidade de siapes-2018 no conjunto",len(set_siapes_antigos))
print("Quantidade siapes-2018 na lista:",len(list_siapes_antigos))
print("####")
print("Quantidade de siapes-2019 no conjunto:",len(set_siapes_novos))
print("Quantidade de siapes-2019 na lista:",len(list_siapes_novos))
```


<style scoped>
  .ansiout {
    display: block;
    unicode-bidi: embed;
    white-space: pre-wrap;
    word-wrap: break-word;
    word-break: break-all;
    font-family: "Source Code Pro", "Menlo", monospace;;
    font-size: 13px;
    color: #555;
    margin-left: 4px;
    line-height: 19px;
  }
</style>
<div class="ansiout">Quantidade de siapes-2018 no conjunto 768
Quantidade siapes-2018 na lista: 768
####
Quantidade de siapes-2019 no conjunto 807
Quantidade de siapes-2019 na lista 809
</div>


### Quais são os professores que são listados duas vezes?
 
 * [Jose Domingues Fontenele Neto](https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=1181653)
 - [Jose Erimar Dos Santos](https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=1243118)


```python
from collections import Counter
count = Counter(list_siapes_novos)
print(count.most_common(3))
```


<style scoped>
  .ansiout {
    display: block;
    unicode-bidi: embed;
    white-space: pre-wrap;
    word-wrap: break-word;
    word-break: break-all;
    font-family: "Source Code Pro", "Menlo", monospace;;
    font-size: 13px;
    color: #555;
    margin-left: 4px;
    line-height: 19px;
  }
</style>
<div class="ansiout">[(1181653, 2), (1243118, 2), (2028000, 1)]
</div>


### Quantos e quais são os professores que estavam em 2018 e não aparecem na listagem de 2019?

**72 Professores:**
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=1053825
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=3048570
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=3040143
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=1008017
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=1114898
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=2377083
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=2408341
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=2407318
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=396310
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=1850519
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=3052057
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=1872793
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=3053081
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=396317
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=1209630
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=2410397
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=2358560
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=2410146
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=2355492
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=3057831
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=3057833
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=3005098
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=2359211
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=1971885
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=3065134
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=2920879
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=2790064
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=1911600
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=2358576
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=2995967
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=2423862
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=1639993
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=396348
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=3053116
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=2358462
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=2389310
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=2425665
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=2420930
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=3005124
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=1766085
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=1811396
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=3042245
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=2353224
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=1228872
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=1260158
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=2389189
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=1228751
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=2426965
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=3053912
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=3000538
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=1075932
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=2376541
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=2355166
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=2981983
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=2417375
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=2407392
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=2360289
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=3001569
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=2621924
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=1824610
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=414695
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=2355183
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=3046769
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=3043314
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=1966965
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=3065079
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=1307256
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=1308922
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=3005051
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=1081596
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=2392318
- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=2411775


```python
apenas_antigos = set_siapes_antigos - set_siapes_novos
print(len(apenas_antigos))
print(apenas_antigos)

# To generate the markdown list
#BASE = '- https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape='
#professores_antigos = [BASE+str(siape) for siape in apenas_antigos]
#print('\n'.join(professores_antigos))
```


<style scoped>
  .ansiout {
    display: block;
    unicode-bidi: embed;
    white-space: pre-wrap;
    word-wrap: break-word;
    word-break: break-all;
    font-family: "Source Code Pro", "Menlo", monospace;;
    font-size: 13px;
    color: #555;
    margin-left: 4px;
    line-height: 19px;
  }
</style>
<div class="ansiout">72
{1053825, 3048570, 3040143, 1008017, 1114898, 2377083, 2408341, 2407318, 396310, 1850519, 3052057, 1872793, 3053081, 396317, 1209630, 2410397, 2358560, 2410146, 2355492, 3057831, 3057833, 3005098, 2359211, 1971885, 3065134, 2920879, 2790064, 1911600, 2358576, 2995967, 2423862, 1639993, 396348, 3053116, 2358462, 2389310, 2425665, 2420930, 3005124, 1766085, 1811396, 3042245, 2353224, 1228872, 1260158, 2389189, 1228751, 2426965, 3053912, 3000538, 1075932, 2376541, 2355166, 2981983, 2417375, 2407392, 2360289, 3001569, 2621924, 1824610, 414695, 2355183, 3046769, 3043314, 1966965, 3065079, 1307256, 1308922, 3005051, 1081596, 2392318, 2411775}
</div>


### Quantos e quais são os professores que estão em 2019 e não aparecem na listagem de 2018?

- [CIBELE DOS SANTOS BORGES](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3110135)
- [KLEYTONE ALVES PEREIRA](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=1113176)
- [MADSON ANTONIO BENJAMIN FREITAS](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3124429)
- [ROSUETI DIOGENES DE OLIVEIRA FILHO](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3140939)
- [FELIPE AUGUSTO MARIANO PIRES](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3151511)
- [DAKSON CAMARA DA FE](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3260145)
- [DANIEL LIBERALINO MONTE](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3153835)
- [JONATAS ARIZILANIO DA SILVA](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3152323)
- [POLIANNY AGNE DE FREITAS NEGOCIO](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3121368)
- [WEDSON CARLOS GOMES DE OLIVEIRA](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3121046)
- [RENNAN HERCULANO RUFINO MOREIRA](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3149917)
- [JEFFERSON ALVES DE MORAIS](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3087346)
- [MAGNUS KELLY DE OLIVEIRA PINHEIRO](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3125912)
- [TYCIANNE JANYNNE DE OLIVEIRA CABRAL](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3153220)
- [AGLAGILSON FERNANDES DAS CHAGAS](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=1078551)
- [CLAUDIA LEITE ROLIM MOREIRA](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=1522462)
- [FILIPE CORREIA LIMA RODRIGUES DE MEDEIROS](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=1100942)
- [GERLANE MODESTO DA SILVA](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3136031)
- [GUSTAVO RANDSON SARMENTO VIDAL](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=1220587)
- [HEVILA SUELEN NERI DE LIMA](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=1380211)
- [HUGO SAILLY MOURA BEZERRA](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=1304596)
- [JOSE RODRIGUES PAIVA NETO](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=1369562)
- [LANA LACERDA DE LIMA](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=1534454)
- [MARIA EDUARDA BAIA CORREIA DE OLIVEIRA](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=1925820)
- [MARINA TARGINO BEZERRA ALVES](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=1100187)
- [PAULA ALVES DE FREITAS MENEZES](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=1288187)
- [SAMILA MARISSA PINHEIRO GOMES](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3135955)
- [SHIRLEY KARENINE NOLASCO DA SILVA](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=1525023)
- [TELMA DE SOUSA LIMA](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=1216599)
- [LIDIANE ALVES DE MORAIS](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=1407016)
- [MARCOS ALEXANDRE RABELO DE LIMA](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=1200501)
- [DIEGO PALMIERE FERNANDES](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3125956)
- [JUSCIMARA GOMES AVELINO](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3089145)
- [KAYO LUANN NOGUEIRA PINTO](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3091508)
- [ANA MARIA PEREIRA AIRES](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=1413882)
- [FRANCISCA NATALIA DA SILVA](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3105753)
- [RODRIGO ALBUQUERQUE SERAFIM](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=1098822)
- [JOSE RICARDO MARQUES BRAGA](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3083042)
- [RUI ALEXANDRE RAMOS DUARTE DO ROSARIO](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3153759)
- [ANTONIO EDSON OLIVEIRA HONORATO](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=1172865)
- [CAMILA JESSICA NERES DE OLIVEIRA](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3141574)
- [GERMANNA GABRIELLA AMORIM FERREIRA](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3126282)
- [GUSTAVO HENRIQUE DE SA HONORATO](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3088671)
- [JOCYKLEBER MEIRELES DE SOUZA](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3125898)
- [LIGIA SILVA DE FRANCA BRILHANTE](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3143336)
- [LUIZ CLAUDIO OLIVEIRA RAFAEL](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3124309)
- [TERESA JULIA DE ARAUJO MELO](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=2894656)
- [TULIO DE MEDEIROS JALES](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3136014)
- [TALITA DANTAS PEDROSA](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=1072896)
- [GEOVANNA MARIA ANDRADE DE OLIVEIRA](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3154193)
- [MANOEL LEANDRO ARAUJO E FARIAS](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3140977)
- [MAYARA DE FREITAS MEDEIROS ARAUJO](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3089637)
- [MICHELLE MARIA PEREZ LOTT](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3124528)
- [SILVANETE SEVERINO DA SILVA](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3148074)
- [CIRO JOSE JARDIM DE FIGUEIREDO](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=1355183)
- [ANA ALICE DA SILVA CAMARA](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3150512)
- [DANIEL ALMEIDA BEZERRA](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3121001)
- [JANIELLY KALINE DE OLIVEIRA FERREIRA](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=1210836)
- [MARIA CRISTINA CAVALCANTE BELO](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3146925)
- [RAFAEL DE AZEVEDO PALHARES](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3114232)
- [SARA DE OLIVEIRA MARQUES LUNA](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3089052)
- [FRANCISCO DAS CHAGAS BARBOSA DE SENA](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=1005051)
- [ALDILENE BEZERRA PINHEIRO](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3156385)
- [FRANCISCA IRES VIEIRA DE MELO](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3120962)
- [LOURENA BARBOSA CAVALCANTE PAIVA](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3129364)
- [LUCAS RAMOS DANTAS](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3147123)
- [MAXWELL CARVALHO DO NASCIMENTO](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3131404)
- [NAYANA LETICIA DE MORAIS VIANA](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3122039)
- [THAIS MILLA SIMAO ARAUJO](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3138573)
- [VICTOR DE ANDRADE DANTAS](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3151398)
- [JOSEANE DUNGA DA COSTA](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=2301915)
- [RAFAELY ANGELICA FONSECA BANDEIRA](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3659516)
- [SAMARA MARTINS NASCIMENTO](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=230191)
- [FABIOLA LUANA MAIA ROCHA](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3121381)
- [FRANCISCO LEONÉSIO CARNEIRO DUARTE](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3155432)
- [JOSE HENRIQUE MACIEL DE QUEIROZ](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3100022)
- [LIDIANE ARAUJO VIEIRA DOS SANTOS](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3131372)
- [RENATA JULLY NUNES XAVIER](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3102969)
- [FRANCISCO EBSON GOMES SOUSA](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3870514)
- [BRUNA GABRIELI MORAIS DA SILVA THORPE](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3089687)
- [DANIEL SILVA GUEDES](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3305285)
- [JOSE ERICK DA SILVA FERREIRA](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3131475)
- [RAFAEL RODOLFO DE MELO](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=1789417)
- [FRANCISCO SIDENE OLIVEIRA SILVA](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3086971)
- [MARIA EUGENIA DA COSTA](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3124459)
- [LUCIANA ANGELICA DA SILVA NUNES](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=1802859)
- [ADERSON DE SOUZA MAIA](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3085088)
- [MYLENA MAYLA DE SOUSA](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3133114)
- [SAMANTA MESQUITA DE HOLANDA](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3295961)
- [DANIEL PABLO DANTAS DIOGENES](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=2989611)
- [JONATHA REVOREDO LEITE DA FONSECA](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3136382)
- [MATHEUS EMANUEL TAVARES SOUSA](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3131441)
- [PAULA ROMYNE DE MORAIS CAVALCANTE NEITZKE](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=1388828)
- [PRINCE AZSEMBERGH NOGUEIRA DE CARVALHO](https://sigaa.ufersa.edu.br/sigaa/public/docente/portal.jsf?siape=3086918)
- [JOSE DE ARIMATEA DE MATOS](https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=336632)
- [FELIPE DE AZEVEDO SILVA RIBEIRO](https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=1670609)
- [VANIA CHRISTINA NASCIMENTO PORTO](https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=1714179)
- [RODRIGO SERGIO FERREIRA DE MOURA](https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=1545235)
- [ALMIR MARIANO DE SOUSA JUNIOR](https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=2079536)
- [RODRIGO NOGUEIRA DE CODES](https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=1806868)
- [JEAN BERG ALVES DA SILVA](https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=2359110)
- [VANDER MENDONCA](https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=1547955)
- [ALVARO FABIANO PEREIRA DE MACEDO](https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=1500639)
- [MOACIR FRANCO DE OLIVEIRA](https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=2206331)
- [RODRIGO SILVA DA COSTA](https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=1574667)
- [RAFAEL CASTELO GUEDES MARTINS](https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=2752035)
- [LUDIMILLA CARVALHO SERAFIM DE OLIVEIRA](https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=1781560)
- [ALAN MARTINS DE OLIVEIRA](https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=1802972)
- [ARAKEN DE MEDEIROS SANTOS](https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=1631848)
- [DANIEL FREITAS FREIRE MARTINS](https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=1813593)
- [RICARDO PAULO FONSECA MELO](https://sigaa.ufersa.edu.br/sigaa/public/docente/disciplinas.jsf?siape=1991824)


```python
apenas_novos = set_siapes_novos - set_siapes_antigos
print(len(apenas_novos))
print(apenas_novos)
```


<style scoped>
  .ansiout {
    display: block;
    unicode-bidi: embed;
    white-space: pre-wrap;
    word-wrap: break-word;
    word-break: break-all;
    font-family: "Source Code Pro", "Menlo", monospace;;
    font-size: 13px;
    color: #555;
    margin-left: 4px;
    line-height: 19px;
  }
</style>
<div class="ansiout">111
{1714179, 3126282, 3131404, 3138573, 3136014, 1545235, 3129364, 1304596, 1806868, 3136031, 2752035, 3151398, 1407016, 2989611, 3131441, 3091508, 3086918, 1098822, 3131475, 3124309, 1216599, 1113176, 1813593, 3149917, 1631848, 1802859, 2206331, 3086971, 3125898, 1100942, 1991824, 3151511, 3125912, 3089052, 3143336, 3146925, 3150512, 1547955, 3133114, 1925820, 3125956, 3124429, 3121368, 3295961, 1802972, 3121381, 3089637, 3124459, 3260145, 3110135, 3114232, 3089145, 336632, 3102969, 1413882, 3659516, 1072896, 1574667, 3154193, 1078551, 3089687, 1388828, 1522462, 3088671, 3085088, 1525023, 3083042, 1288187, 3148074, 230191, 2079536, 3124528, 3870514, 1781560, 2894656, 3120962, 3153220, 3305285, 2359110, 3140939, 3153759, 3121001, 3140977, 3147123, 1380211, 1200501, 3100022, 3122039, 3136382, 1172865, 3121046, 1100187, 3156385, 3153835, 1355183, 3152323, 3141574, 1670609, 3135955, 1210836, 3105753, 1369562, 2301915, 1500639, 3155432, 1789417, 1220587, 3131372, 3087346, 1534454, 1005051}
</div>


### Lista de siapes antigos e novos juntos para a coleta de informações


```python
merge_siapes = set_siapes_novos.union(set_siapes_antigos)
print(len(merge_siapes))
for i in merge_siapes:
  print(i)
```


<style scoped>
  .ansiout {
    display: block;
    unicode-bidi: embed;
    white-space: pre-wrap;
    word-wrap: break-word;
    word-break: break-all;
    font-family: "Source Code Pro", "Menlo", monospace;;
    font-size: 13px;
    color: #555;
    margin-left: 4px;
    line-height: 19px;
  }
</style>
<div class="ansiout">879
1998864
2015250
3043348
3129364
1163286
2093076
1347606
2814007
1654843
3608635
3043392
2355270
2031688
1228872
1069130
1806415
1216599
3149917
2035805
1806429
2981983
1671270
1859693
1753199
2359408
1806454
1806473
2359451
1806509
1724599
1044665
2420930
1523907
1859784
2330828
1994956
1016017
3121368
1544411
1806558
1859807
3121381
1868009
3825899
1069297
1773815
1081596
2392318
1716479
1859840
1810697
1495311
3154193
2056469
1388828
3088671
2359585
2355492
1351978
1806635
1495347
2449720
1691961
2326845
2052419
2031941
2355526
1810758
1859924
1565016
1941853
1945951
1941856
1200501
1446262
2515320
1675646
1995142
1286535
1868167
2089358
1802639
1507727
1061263
1008017
1548691
1012116
2392471
1810852
2884005
2920879
3035571
1331638
1634744
3051962
3006908
3051965
1851841
1622468
3006937
2028000
2621924
2220519
2449903
1606132
3027454
2028037
1982985
1806860
1106449
1806868
3052057
1872410
2421279
1806885
1954343
1278513
2118196
3052088
1114687
1929798
1770056
2220620
2835021
2605644
1847887
2064979
1802859
1987186
1307256
2941562
2044548
1979012
3125898
2773653
3125912
3089052
1569443
2941614
2405039
3150512
2790064
1295030
1925820
1647296
3027651
3125956
1766085
1221323
1913549
1848016
1802971
1802972
2417375
1802981
2450151
1721067
1028844
1069806
1622769
336632
3089145
1413882
1135362
1344262
3040015
1172242
1114898
1803028
3085088
230191
1651506
2077501
2425665
1864521
1106764
2073429
2376541
1688422
1692519
2626416
2044785
1475444
1966965
3122039
1045370
3048320
1344385
3040143
2212758
1872793
1815470
1434542
1848243
1586101
1115061
1115069
1811396
3040204
1565646
3105753
2360289
414695
2061292
1577965
1307636
1766388
1545215
1266687
3126282
3138573
1278994
1545235
2061336
1238040
1504300
1991725
1750073
1098822
1991751
2528342
1668195
2585705
2147436
2999409
3048570
2307198
1062017
1053825
2032774
1991824
2647194
2155674
2585756
2213033
3146925
2483376
2647223
1991868
2884800
1991874
2389189
1639625
2397390
2417870
1545427
1991894
2356440
1307867
1070306
2647268
3089637
1823981
3110135
3114232
3065079
1369338
1750267
2778371
1840387
1225990
2073862
1414415
1078551
3089687
1991961
1209630
1525023
2778400
1975594
3065134
2778421
2389310
2086207
2303300
1545550
1582415
1750357
1647966
1693028
1582440
1733996
1885548
3147123
3044724
2053497
2377083
1172865
1992067
1316228
1693060
1086856
1992072
1205643
1291659
1770896
1992085
2459030
1852822
1516953
1566120
3044779
1926578
1529267
2307508
1779124
2799026
1603007
1541567
1197504
2639302
1369562
1615325
1500639
3155432
1734120
1345002
1545710
1549816
1005051
2070023
1852952
3053081
1451546
2213412
3151398
1992242
1246771
1054265
1639993
3053116
1738310
2303561
1992265
2778700
3036755
1578584
1996376
1992282
2778720
1734242
1885798
1631848
1447536
1295986
1242739
1816178
1644152
1992323
1570445
1300112
1717905
1377937
3073686
3151511
2410146
1992355
1885864
3143336
1922730
1971885
1083055
2778809
1210042
2725571
1779402
2287311
1562320
1255130
1750756
2975474
2213620
3659516
3778301
2995967
2189057
1804034
2086657
1042177
1574667
2045711
3049235
1054489
3323686
1890095
1742652
2299718
2213705
1566547
1714006
1668954
1824610
1058659
1714022
2086760
1931118
1632114
1714053
2606987
2578315
1718165
2410397
1714079
2082728
1550250
1017771
333743
2082743
1546177
1521615
1984465
2082771
1181653
1857495
1669085
1931231
3074016
1669088
1894371
1775593
3131372
1452013
1243118
1714158
1161204
1288187
2889730
1714179
3131404
1447952
1304596
1996830
1923106
1407016
2836523
3131441
1972281
2259009
1079363
1714245
2353224
2054224
1714258
3131475
2426965
1714269
1566818
2259043
1333353
1513591
2259068
1378429
2132096
1882242
2324611
1751175
1767567
1509522
1714333
2324639
1292448
1734818
3057831
3057833
2140339
1509560
2578617
1857726
1583297
1059009
3045573
3000518
2054349
2287826
1231058
3000538
2115806
1046754
2279652
1804517
1157350
1612008
1366262
1931513
3102969
1849595
1308922
1915134
3049729
3287303
1669383
3680521
2046222
1714448
1792275
2115859
1280283
3074337
3148074
1669428
1939773
1526099
3053912
3074396
1849697
2128227
1669481
6396274
1870196
1714559
1771905
3037570
2300292
1714573
2132375
1100187
3156385
1608098
2652583
1960364
1669549
1714606
1919410
1202613
1505717
1743293
3152323
2882002
3135955
1960404
1210836
1243629
2275824
2882034
1534454
3049977
2259454
1866242
1686020
1993225
2996746
3136014
3054099
3136031
1976866
1010218
1497653
1677881
2996802
3086918
1763913
1817174
1342048
1817186
1223273
1559161
3086971
2206331
3005051
1260158
1600131
1706632
2067096
199325
1673887
3005098
1305260
1432247
1735356
2116288
1940164
1321668
3005124
2857671
1346264
1731288
3295961
1075932
1612510
1227492
1125099
1055467
1714925
2927342
1673984
2091789
1571613
1522462
1919773
3083042
1911587
1071911
2079536
1911600
2997052
1682238
2894656
1514311
1612618
1715025
1669971
1882965
1059673
1715037
2341734
1670002
1887092
1854325
1919869
3136382
1047432
1915790
2407318
2362263
1670040
1989536
2177953
1969059
1674151
1969075
1346487
3652543
1055685
2145222
3042245
1809354
1571794
1670102
1956823
1702873
1633246
2063327
1055712
2407392
1330146
1772516
1522661
2145256
3087346
3038201
1932288
1752076
396302
396304
396305
396307
396309
396310
396311
1866775
396313
1096733
396317
1997855
1141792
396319
396322
3038245
2403373
2300979
3091508
396341
2423862
396343
2145337
396345
396348
1780797
1866814
396352
1866823
2321480
396361
1354828
2362447
3124309
2157654
1805397
1113176
1813593
1166430
1141857
1997927
1551469
1047662
2362480
1649777
3738738
396406
2112633
1100942
1866895
1850519
1920159
1989791
1854626
1543345
2358462
1240255
1739973
2079946
3124429
1653968
2075857
1866964
1367262
3730657
3001569
2403558
1572073
3124459
2424049
2411775
2145538
2305283
1674506
2075915
2424075
1621261
2268434
1670421
3857693
2358560
3046693
3046701
1674543
3124528
2358576
1801529
2403643
1445181
1228095
2141506
3153220
3046725
1801543
1461578
3140939
1580369
1715546
1494364
1289574
1506673
3140977
3046771
1998194
3046769
3100022
2125184
2157958
2112919
3046819
1805741
1355183
1064370
1293750
1998263
2117051
1506753
3005896
1158600
2670029
1670609
2993619
1805780
2055639
1863139
1670627
1646054
1789417
2346474
1781234
2055666
2055681
2080267
1674772
1805847
2055706
2203171
2752035
1531432
1011243
2989611
1887789
1531437
2158134
1936952
1982013
1908286
2612800
1056334
1801817
1814114
1166949
1764968
1953385
1412720
1633911
1805955
2190980
1846917
2465416
1765010
2969235
1425052
1552041
1547955
1900213
1597112
3133114
1445567
1445570
1347271
417480
1224396
1613523
1847005
3260145
3067643
1072896
1523457
2268933
2268946
2314006
2268962
1957669
2948912
3870514
1781560
3120962
3305285
1818437
1965894
2359110
1048410
3153759
3063651
3121001
1380211
1245044
2355199
2269056
3063682
3043210
2400142
2981777
2269077
3121046
2408341
2465692
2031519
1544096
2178976
1314726
1212329
3153835
2359211
1998769
1789892
3141574
2269130
1695692
1228751
2453461
2093019
2301915
2355166
1687527
2453480
1220587
1220588
1855470
1998830
2355183
1806322
3043314
2179061
1806327
1806335
</div>

