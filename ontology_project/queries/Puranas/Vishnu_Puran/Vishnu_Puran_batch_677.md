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

### Verse 1 (Vishnu Puran 0.13521)
- **Original**: यपाच तेन वै व्याप्त है हक $ सत्तमात्याखिले दूत 5 37... 22
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.13522)
- **Original**: यपावल्कपित॑ सर्वा्‌ 3 डक 74 यह्येतसपता प्रेक्तम्‌ 2-16 --<ड
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.13523)
- **Original**: यपाह्ननिभ पुत्रे य 3-78: जाए यल्ेतर्रगचानाह 2.6 है
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.13524)
- **Original**: या ने ब्राह्मणेध्यः यलेतदगणजह । 2
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.13525)
- **Original**: यथा यभैदम्‌ अल यररेरत्किसनलेसेस्पुक्तम्‌ 1. 18... 18
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.13526)
- **Original**: यथाड़ यसुया सर्वम्‌ । फ्धृष्खति पुवानेल्त्‌ 3 र्ट 3
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.13527)
- **Original**: वर्वाप्रेक उदुध्ा समिष्यतो... » 5 86 7+ 8 *ु5 अत्पूदिब्यो प्रीटिक्वम्‌ 4... 1320 ल्‍्टेंड
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.13528)
- **Original**: यह पयता सुष: । ड़ अत्रगायानि पूठानि 1749 6
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.13529)
- **Original**: यथा सकते जऐ वाता 2 7 0+4है2 अद्ममाणमिर सर्वम्‌ 2 2 3
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.13530)
- **Original**: यथाएँ पूखया तेन 6 .7-2102 युज़तन्न रिधतायवत्‌ 3 13- . -$
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.13531)
- **Original**: यथा सम्ततपूततेषु 5 13 / 8 घर गज कृत कुछे जात 6 1... - 12
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.13532)
- **Original**: यथा च माहिप सॉर्पिः 75 7(957-- ऐेरे यत्र सर्व यतः सर्वम्‌ है. 9... 42
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.13533)
- **Original**: यथायत्र जगरूप्ति 5 17. -. 16 अत ये टेक्टेयस्स है _है2 5
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.13534)
- **Original**: यथा निर्मस्सितस्तेत 5 8 -0> 75 सल बुदमभुरकेण्‌ 5 श्र <
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.13535)
- **Original**: यवेच्यजासमिस्तः है #0-03 रे यत्र यह्र यदी दे 2 23... 742
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.13536)
- **Original**: ययैव फाफन्येकनि 2 76773; देर यत्र केयेकादल« 5... 9... 26
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.13537)
- **Original**: यथैव शृणुगो दूशत्‌ 4 «83 5
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.13538)
- **Original**: अ2207 640 4 /0 40 अत 4: 26 - एप एक 27 लए एज तीर "की री #5 20 -ीप जी #97-णा:,त ल्‍> 9 >0. 0 न # #90 6 & “0 «7 4 +07- # 65 48 /7 7 7 >> हर
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.13539)
- **Original**: सन्न देता न मुनयः अप्रमहेलुदेंले अक्रय॑ भगवान्‌ ब्रह्मा यन्नामकीर्तने भकत्या अत्रः दार्रेयु यदन्यरेहे मय च जगद्झन्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.13540)
- **Original**: सपनिशमविधृत्कल्पषाणामू यपगश्क्रघरः साक्षात्‌ यमस्य विष्ये घोर: ग्रमयेत्य जनशार्ब: यमाराध्य पुएणर्षि- यमुणो यातिगम्भीसम्‌ यमुन्रकर्षणादीनि अपेन प्रह्ित टष्डम्‌ या क्षेश्राइक्तिस्सा सअयाहिश्पाईशेठपम्‌ । लपि >+ 42 याक 20] ही 2अ ह हू हर उक 2 9 09 % 09 20507 0 भा ,ता 6 4 जे भा 40 8625 0: कं 45. / 5 अं 5 6 र. न वा न 6 0 0 >ण: 7 «यु कै सर 44 /क % 6: क््ल्ढ् >> +7 न्‍्ज ल्‍्र _् 3. >> 0. «4. 1.1 0 के ड की 845 अडर 8 86558. जा दर ब * हर रु शक जक 5 &4 <0 4.
- **Translation**: 

---

