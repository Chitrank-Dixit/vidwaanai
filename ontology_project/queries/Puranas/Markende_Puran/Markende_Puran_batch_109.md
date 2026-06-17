# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Markende Puran 0.2161)
- **Original**: क्तपिरुवाच
- **Translation**: 

---

### Verse 2 (Markende Puran 0.2162)
- **Original**: दर 4 नित्यैव सा जगस्पूर्तिस्तया सर्वमिर्द ततम्‌
- **Translation**: 

---

### Verse 3 (Markende Puran 0.2163)
- **Original**: 5 तथाधि सत्समुत्पत्ति्वहुधा श्रूयतां मम।
- **Translation**: 

---

### Verse 4 (Markende Puran 0.2164)
- **Original**: ्ः देयानां कार्यसिद्धयर्भमाविर्भवति स्रा यदा
- **Translation**: 

---

### Verse 5 (Markende Puran 0.2165)
- **Original**: ह उत्पन्नेतिं तदा लोके सा नित्याप्यभिधीयते। बोगनिद्रों बदा विष्णुर्जगत्येकार्णवीकृते
- **Translation**: 

---

### Verse 6 (Markende Puran 0.2166)
- **Original**: ! 4, आसतीर्य शेषमभजत्कल्पात्ते भगवान्‌ प्रभु:। तदा द्वावसुरो घोशे विख्यातौं मशुकैटभौ
- **Translation**: 

---

### Verse 7 (Markende Puran 0.2167)
- **Original**: । बिष्णुकए्णमलोद्धूता हन्तुं प्रह्माणमुद्यती। सर नाध्यिकिमले विध्णो: स्थितों ज़ह्या प्रजापति:
- **Translation**: 

---

### Verse 8 (Markende Puran 0.2168)
- **Original**: दृष्ठा त्रावसुरै चोग्री प्रसुप्तं घ जवार्टनम्‌। ! तुष्ठात्ष ययोगनिद्रों तामेकाग्राहदयस्थितः
- **Translation**: 

---

### Verse 9 (Markende Puran 0.2169)
- **Original**: 6, पाौ0-कर्म चास्याक। 2. पा0- यश््वभावा। 3. किसी फिसी प्रतिसें इसे बाद हो 'भ्र्मोवाचर' है तथा 'निद्ठों भगवर्ताय्‌' इस श्लोकार्थके स्थानमें-'स्लौपि निद्रां धावतों विष्थोस्टुलतेजस:
- **Translation**: 

---

### Verse 10 (Markende Puran 0.2170)
- **Original**: ' ऐसा पाठ है।
- **Translation**: 

---

### Verse 11 (Markende Puran 0.2171)
- **Original**: +मेथा ऋषिक़ा राज्य सुरक्ष और सप्ताधिकों भगनतोीक्ी पहिमा सुनाना* 183 अ353:4:8ऋ---+ + *0 + 5 2034 फकत# ह-807 + > 24 3 + ऊतक #+000
- **Translation**: 

---

### Verse 12 (Markende Puran 0.2172)
- **Original**: ज506,6&6/%7 0 7 जे 3.52.22 0 +0+ 05-37 2::::566% ब्रह्माजीने जब तन दोनों भयानक्र असुरोको अपने
- **Translation**: 

---

### Verse 13 (Markende Puran 0.2173)
- **Original**: स्रोडुपि निद्रावर्श भीतः कस्त्ां स्तोतुमिहेशाः। पास आया और भ्रगवानकों सोया हुआ देखा तो शकाग्रचित होकर उन्होंने भगवान्‌ विष्णुको जगानेके लिये उनके नेन्नॉमें निवास करनेबाली योगनिद्ठाका स्तवन आरम्भ क्िया। जो इस विश्वको आधी करी, जगहूकों धारण करनेवालों, संसार्का पालय और संहार करनेत्रालों तथा तेज:स्वकृप भगवान्‌ बिण्णुकों अनुष्म शक्ति हैं, उन्हों भगवती निद्गादेवीकी भगवार्‌ ब्रह्मा स्तुति करने लगे
- **Translation**: 

---

### Verse 14 (Markende Puran 0.2174)
- **Original**: ब्रह्मोग्त्च
- **Translation**: 

---

### Verse 15 (Markende Puran 0.2175)
- **Original**: 72 4 त्व॑ स्वाह्म त्व॑ स्वथा त्वं हि वषद्क्मार; स्व॒रात्मिकां
- **Translation**: 

---

### Verse 16 (Markende Puran 0.2176)
- **Original**: सुधा त्वपक्षरे नित्य त्रिया मात्रात्मिका स्थिता। अर्क्षमान्नास्थिता निल्या यानुच्चार्सा विशेषतः
- **Translation**: 

---

### Verse 17 (Markende Puran 0.2177)
- **Original**: त्वमेव संध्या साथित्री त्वे देवि जननी परा। त्वयैतद्धार्यते विश्व त्वयैतत्पुम्यते जगतू।
- **Translation**: 

---

### Verse 18 (Markende Puran 0.2178)
- **Original**: ज्थयैतत्पात्यते देवि त्तमत्स्यन्ते च्॒ सर्वद्ा। विसुष्टी सृष्टिकृपा त्व॑ स्थितिरृपा च पालने
- **Translation**: 

---

### Verse 19 (Markende Puran 0.2179)
- **Original**: तथा संहतिरूपाने जगतो5स्थ जगन्मये। महाबिधा महामाया महाग्रेथा महास्मृत्रि:
- **Translation**: 

---

### Verse 20 (Markende Puran 0.2180)
- **Original**: मड्ठामोहा च भवतों महादेवी महासुरी। प्रकृतिस्त्त॑ च सर्वेस्थ गुणत्रयविभाविनी 478 7 कालराज्िमहारात्रिपोहरात्रिक्ष॒ दारूणा। स्॑॑ भ्रीस्त्वमी भ्ररी त्वे हस्त्न॑ चुद्धिर्बोधलक्षणा
- **Translation**: 

---

