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

### Verse 1 (Markende Puran 0.2341)
- **Original**: इनके अतिरिक्त और भो हजारों महादँत्य र8, हाथी और घोड़ोंकी सेना साथ लेकर वहाँ देवीके साथ युद्ध करने लगे। स्वयं महिषासुर उस रणभूमिमें कोटि कोटि सहरत रथ, हाथी और घोड़ोंकी सेनासे घिरा हुआ खड़। था। 4 देत्च देवीके स्ताथ तोमर, भिन्दिपाल, शक्ति, मू_्तल, खड़े, परशु और पट्रेश आदि ऊस्त्र-शस्त्रोंका प्रह्मार करते हुए युद्ध कर रहे थे। कुछ दैत्योंने उनपर शक्तिका प्रहार किया, कुछ लोगोंनें चाश फेंके
- **Translation**: 

---

### Verse 2 (Markende Puran 0.2342)
- **Original**: 44--48
- **Translation**: 

---

### Verse 3 (Markende Puran 0.2343)
- **Original**: तश्ना कुछ दूसरे हँत्योंने खज्जग्रहार करके देवोकों मार डालगेका उद्योग किया। देंीने गो क्रोधर्में भरकर खेल-
- **Translation**: 

---

### Verse 4 (Markende Puran 0.2344)
- **Original**: खेलमें ही अपने शस्त्र शस्त्रोंकी वर्षा करके दैत्योंके वे समस्त अस्त्र शस्त्र काट डाले। उनके मुखपर परिश्रम या थकावटका रंजमात्र भी चिह्न नहीं था. देठता और ऋष् उनकी स्तुति करते थे और वे भावतों पसमेश्नरी दैत्योंके शरीरोपर अस्त्र शस्त्रोंकों वर्षा करती रहाँ।
- **Translation**: 

---

### Verse 5 (Markende Puran 0.2345)
- **Original**: “डैयतलाओंके जेजसे देवीकां प्रादुभांव और महिषासुरकी सेनाका बध* धर #%अ4664404 न" हइ 440 0 03.55 0007 46640 0 0 02204446 0 6 शतक 47 002272 6467 *5:1444 757 न/। पा 4447 सो5पि क्रुद्धीं धुतस्तटों देव्या बाहनकेसरी
- **Translation**: 

---

### Verse 6 (Markende Puran 0.2346)
- **Original**: खत्ारासुरसेन्येवु चनेष्खित्ष हुतताशनः। निःश्चासान्‌ पपुचे यांश्र युध्यपाना रणे+प्विका
- **Translation**: 

---

### Verse 7 (Markende Puran 0.2347)
- **Original**: त एव सद्यः सम्भूता गणा; शतसहस्तशः। युवुधुस्ते परशुभिर्िन्दिपालासिपट्डिश:
- **Translation**: 

---

### Verse 8 (Markende Puran 0.2348)
- **Original**: नाशयन्तोड्सुरगणान्‌ देल्ीशकक्‍्त्युपबूंढिता:
- **Translation**: 

---

### Verse 9 (Markende Puran 0.2349)
- **Original**: अवादयन्त पटहान्‌ गणाः शझ्जांस्तथापरे
- **Translation**: 

---

### Verse 10 (Markende Puran 0.2350)
- **Original**: मृदड्रांश्व तथैवान्ये तस्मिन्‌ युद्धमहोत्सवे। कतो देवी ज्रिशूलेन गदया शक्तिवृष्टि्रि:
- **Translation**: 

---

### Verse 11 (Markende Puran 0.2351)
- **Original**: खड्गादिभिश्च श़तशों निजधान महासुरान्‌। 'फातयामास चैवान्यान्‌ घण्टास्वनलियोहितानू
- **Translation**: 

---

### Verse 12 (Markende Puran 0.2352)
- **Original**: असुरान्‌ भुवि पान बरदृध्वा चञान्यानकर्षयत्‌। केचिद्द्विपा कुतास्तीश्णौ: खड्गपातेस्तथापरे
- **Translation**: 

---

### Verse 13 (Markende Puran 0.2353)
- **Original**: विषोधिता लिपातेन गदया भुंथि शेस्ते। बेपुंश् केच्द्रुधिरं मुंसलेन भुर्श हताः
- **Translation**: 

---

### Verse 14 (Markende Puran 0.2354)
- **Original**: केखिप्रिपतिता भूमौ भिन्ना: शूलेन वक्षसि। निरन्‍्तरा! शर्रौघेण कृताः केचित्रणाजिरे
- **Translation**: 

---

### Verse 15 (Markende Puran 0.2355)
- **Original**: श्वेतानुकारिण: प्राणान्‌ पुपुचुस्त्रिदशार्टला:। केषांचिद बाहवशि्छिन्नाशिफरश्नग्रोवास्तश्चापरे
- **Translation**: 

---

### Verse 16 (Markende Puran 0.2356)
- **Original**: शियसि पेतुरन्येपामन्ये पण्ये विदारिता:। विच्छिन्नज्डास्त्वपरे पेतुरुव्याँ महासुरा:
- **Translation**: 

---

### Verse 17 (Markende Puran 0.2357)
- **Original**: एकबाद्भक्षचरणा: केचिहेव्या द्विधा कृताः। छिन्नेषपि चान्वे शिरसि पतिता: एुनरुत्यिला:
- **Translation**: 

---

### Verse 18 (Markende Puran 0.2358)
- **Original**: कबन्धा वुयुधुर्देश्था गृहीतपरमायुथाः। ननृतुझ्लापर तत्र युद्धे तुर्यल्लयाश्रिता:
- **Translation**: 

---

### Verse 19 (Markende Puran 0.2359)
- **Original**: कबन्धाशिछत्रशिरस: खड्गशब्त्यृष्टिगणच; तिप्म तिध्ेति भाषन्तो देवीमन्ये महासुरा:
- **Translation**: 

---

### Verse 20 (Markende Puran 0.2360)
- **Original**: पातिते_ रेथनागाश्वेरसुँकश्. बसुंधरा। अगम्या साभवत्तन्र सत्राभूत्स सहारण:
- **Translation**: 

---

