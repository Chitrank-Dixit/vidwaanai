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

### Verse 1 (Vishnu Puran 0.3181)
- **Original**: देवगण भी निरन्‍्तर यही गान करते हैं कि जिन्होंने स्वर्ग और अपवर्गके सार्गभूत भारतवर्षमे जन्म टिया है वे पुरुष हम देबताओंकी अपेक्षा भी अधिक धन्य (बड़भागी) हैं
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3182)
- **Original**: जो लोग इस कर्मभूमिमें जन्म लेकर अपने फल्म्रकाद्भसे रहित कर्मोंकों परमात्म- स्वरूप श्रीतिष्णुभगवानक्नी अर्पेण करनेसे निर्मल (पापपुण्यसे रहित) होकर उन अनन्तमें ही लीन हो जाते हैं [वे धन्य हैं !]
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3183)
- **Original**: “पता नहीं, अपने स्वर्गप्रदकर्मोका क्षय होनेपर हम कहाँ जम ग्रहण करेंगे ! धन्य तो ले ही मनुष्य हैं जो भारतभूमिमें उत्पन्न होकर इन्द्रियॉकी झक्तिसे हीन नहीं हुए हैं!
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3184)
- **Original**: 194 श्रीकिष्णुप्राण ( अ* 4 नववर्ष तु मैत्रेय जम्बूद्वीपमिंदं मया। लक्षयोजनविस्तारं॑ सद्लेपात्कथितं तब
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3185)
- **Original**: 27 जम्बूद्वीप॑ समावृत्य लक्षयोजनबिस्तरः । हे मैत्रेय ! इस प्रकार ल्मख योजनके विस्तारवाले नकक्‍वर्ष-विशिष्ट इस जम्बूद्रोफका मैंने तुमसे संक्षेपसे बर्णन किया
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3186)
- **Original**: है मैत्रेय ! इस जम्बूद्वीपकों खाहर चारों ओरसे ल्वख योजनके विस्तारवाले वलयाकार स्कारे मैत्रेय बलयाकारः स्थित: क्षारोद्घिबहिः
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3187)
- **Original**: पानीके समुद्रने घेरा हुआ है
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3188)
- **Original**: अर है. अप्कण8-0 इति श्रीविष्णुपुराणे द्वितीयेंडशे तुतोयोउध्याय:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3189)
- **Original**: _ब_-_- नह जौ अकमननः-ः+--, चोथा अध्याय प्रक्ष तथा शाल्मछ आदि टद्वीपोंका विज्ेष वर्णन अऔपराज्मर उवाच क्षारोदेन यथा द्वीपो जम्बूसंज्ञोउभिवेष्टित: । संबेष्टय क्षारमुद्धि प्लक्षद्वीपस्तथा स्थित:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3190)
- **Original**: 9 जम्बूद्वीपस्थ विस्तार: शतसाहस्लसम्मित: । स एब द्विगुणो ब्रह्मन प्नक्षद्वीप उदाहत:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3191)
- **Original**: 2 सप्त मेधातिथेः पुत्रा: प्रक्षद्वीपेश्वरस्थ जै । ज्येष्ट: शान्तहयो नाम शिशिरस्तदनन्तर:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3192)
- **Original**: हे सुखोदयस्तथानन्द: शिव: क्षेमक एवं च। घुवश्न सप्रमस्तेषां प्रक्षद्वीपेश्रा हि ते
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3193)
- **Original**: 4 पूर्व ज्ञात्तहयं वर्ष शिशिरं च सुख तथा । आनन्द च शिव चैव क्षेपकं धुवमेव च
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3194)
- **Original**: 5 मर्यादाकारकास्तेषां तथान्ये वर्षपर्वता: । सप्तैव तेषां नामानि श्रुणुप्त मुनिसत्तम
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3195)
- **Original**: 6 गोमेदशरैव चद्धश्व॒ नारदो दुन्दुभिस्तथा। सोमकः सुमनाश्षैत्र वैश्राजश्लैव सप्तम:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3196)
- **Original**: 7 वर्षाचलेपु रम्येषु चानघा: । बसन्ति देबगन्धर्वसहिता: सतत प्रजा:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3197)
- **Original**: 8 तेबु पुण्या जनपदाश्चिराञ्च प्रियते जनः। नाथयो व्याधयो वापि सर्वकालसुखं हि तत्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3198)
- **Original**: 9 त्े्षा नद्मस्तु सप्तैव वर्षाणां च समुद्रगाः । नामतस्ता: प्रवक्ष्यामि श्रुता: पाप॑ हरन्ति या:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3199)
- **Original**: 10 अनुतप्ता झिखी चैब विपाशा त्रिदिबाक़ुमा । अमृता सुकृता चैब सप्लैतास्तत्र निम्नगाः
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3200)
- **Original**: 11 श्रीपराज्रजी बोले--जिस प्रकार जम्बूद्वीप क्षारसमुद्रसे खिशा हुआ है उसी प्रकार क्षारसमुद्रक्ते घेरे हुए प्नक्षद्वीप स्थित है
- **Translation**: 

---

