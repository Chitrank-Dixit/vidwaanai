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

### Verse 1 (Vishnu Puran 0.13261)
- **Original**: ततश्सब्दगुणे तस्प 6 25 ए्रइकमं 027 ऋष्योडश गकाः हे 8 ए4- 72-
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.13262)
- **Original**: ठतस्स मन्िभिस्सार्टम्‌ 6 कब त्॑ं+26: सतक्षा्टी ययना 4 7:94 प3.
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.13263)
- **Original**: ठवा्तमभ्युपेत्याए 6 फ्जनाकैः 40783 खत एकाददा भूस्तव+ अं र4- 94
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.13264)
- **Original**: ततस्स्व यथाकतर्‌ (2:52: <. हतस्तेत्फासधोंदरा 48 एृ4 (74:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.13265)
- **Original**: ततस्तौ जातदरपी तु 5700 64े है ततम्न कोपाव्मख तु 4 रंड 59 .
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.13266)
- **Original**: ततस्त्वान्दोलिकाभिश्ष कलए कृपा दे 4 7 एड 768...
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.13267)
- **Original**: कारापरतिरूफेशपि एक 6714:126 खतश्वार्थ प्वामिजनहेतु: 48 23: 4: बतलदोकु सर्वमू 8 7136: रे ततश्न खमित्रः &575 “17 5230
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.13268)
- **Original**: ऋशन: 4 छणहै:र4:म366 च्तश्ानिभिभृति: कै 7-38 428-
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.13269)
- **Original**: जलक्ष कुशप्नो नाग - उ4 कार): एके 5 वतश्च नए ह. $ 2:3
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.13270)
- **Original**: 33.1 उतभ रथीता: है / 525 40752 ततंश्व ठृगविन्दु: 4 714 'डढे।.
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.13271)
- **Original**: ततआ कुशाश्रः इ+67%रफनजड6 काशछालाबुसानाम्‌ है: है? छोडट/..
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.13272)
- **Original**: छाल सुमनास्तस्मापि 4 छाश ग्रे चतरशद्बमुपाणपसीत्‌ 7»... 6 7 इते 7 3:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.13273)
- **Original**: ततभिषेकमड्लम, इ/#44544 68 /एाछुइकत 453...
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.13274)
- **Original**: सात दृश्फेतु: '.. 4श्कीदल/पर6
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.13275)
- **Original**: ततस्तों चिबुके शौरि: तत्श्तूदकु् नेगेन ततन्टीपनि व्यक््यय्‌ सत्ता: सुक्चनप्‌ सतस्ख्रातत्य वै कत्तिः तक पीण्ड्रकफ्श्रीमान्‌ उहस्तत्याः पिता गान्दिनी उततोजुनो धुर्दिव्यम्‌ जो ग़जा हा खुल्वा अचा: अध्या* इलो« '* 4 खऋाछात्रर हे. है9. 37 छड 5; 1960) 4ंद डे. 20 द्द 4 मरणट्मश्र 407 3 शव 5 हू 82 प्‌ दि रण 7: श्4ड 3 9 ऊंडछुर
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.13276)
- **Original**: हद 5 1319. 216 एल्क्ारठ कु 8 20 डर 5 श्नडेट श्र 5 पर्व 50 205 श्5 5 रहे डे हुई हर 5. बे8 श्र 68 दछ श्ड 6 ] केश द्च £] 6 "। र्के है?ए8 ! व 15 ए-. स्ेट 19 श्‌ रे 6. ] 5. सेंट 18 5. शै8 श्3 5. सेट 5 5 ऋशइाजएब्रूद्‌ 5- 36 99 5 हेद् 5 5- हेए ब्5 5 हे 21 छू हेड इझ 5 देंड 58 5. दे 58 5 रेहे. (52 5 करी 35 5. 13 20 के रै3 डेट 5 श्र 59 40 »# 4:00 55
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.13277)
- **Original**: 75 इ040705 77 के राज्य प्राप्य को मनुष्याः पश्चव: तवों विवल्ानास्याते तवो व्यास भरदाज: ततोष्ज मब्युतो व्यासः तवोश्नत्तरमैस्कार* ततोऊल॑ स्थाप्तों संत्रमू ततोडय स तदा दष्यौ ततोरर्वाक्लोतसा सर्ग, तत्ो देवामुरपिगृर्‌ को दुर्गाणिच यथा क्जे वरह्मत्मसम्भूतम्‌ सही घन्दन्मर्रिवः दक्ेदेया मुद्दा युक्ताः अँज्ा: अध्यार एलो0 रे0 पु ड्0 ह्े0 28 28 28 26 28 र्3 र्ट श्ष 5 ृ शर्ट श्षड 27 /इ9 5573 5 5 हैंड 57-19 डे 26 42 150 इ्‌ दर 4187 55 18 डेदे रैट- 5 के श्8 रे श्ए 29 5 घट हर 50 32072 कि हरे यू श3
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.13278)
- **Original**: :7 40 हु7 7; 44 59 54. 545 54%] श्र धर छः हे? 2010 33 श्र प्र र व 3] श्द्द 04 37 1:59 10 नजर 4 ड्ड ध् .48 7. * रे3 8 37 8:50 16 60117 46 #एहुतल 12 हे मेड सन संत 30 4] 20 +
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.13279)
- **Original**: बह 20 धए 27 /2 हक ला 290 2रु हब 20 6 रच 22 4ए कु या खा जरा वा खा आए *
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.13280)
- **Original**: 6 4 कर हब 6 अा 23 हा & 4 €
- **Translation**: 

---

