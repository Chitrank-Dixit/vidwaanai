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

### Verse 1 (Vishnu Puran 0.8841)
- **Original**: करें; मैं इसके गर्भसे उत्पन्न हुए सभी बालक आपको सौंप श्रीपय्शर उकाच तथेत्याह तत: कंसो बसुदेत द्विजोत्तम । न घातयामास च ता देवकीं सत्यगौरवात्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.8842)
- **Original**: 11 एतस्मिन्नेच काले तु भूरिभारावपीडिता । जगाम धरणी मेरौ समाजं त्रिदिवोकसाम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.8843)
- **Original**: 12 सब्रह्मकान्सुरान्सबा्रणिपत्याथ मेदिनी । कथयामास तत्सर्व स्वेदात्ककरणभाषिणी
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.8844)
- **Original**: 13 भूमित्वाच अग्निस्सुवर्णस्थ गुरुर्गवां सूर्य: परो गुरु: । ममाप्यखिलस्णेकानां गुरुनारायणों गुरु:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.8845)
- **Original**: 14 अ्जापतिपतिग्रह्ा पूर्वेधामपि पूर्वज: । कलाकाष्ठरानिमेषात्मा कालश्चाव्यक्तपूत्तिपानू
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.8846)
- **Original**: 15 तदंझभूतस्सरेधां सपूहो वस्सुरोत्तमा:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.8847)
- **Original**: 16 आदित्या मसुतस्साध्या रुद्रा वस्वश्चिवह्य: । पघितरो ये च लोकारनां स्रष्टारोउत्रिपुरोगमा:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8848)
- **Original**: 17 एते तस्थाप्रमेयस्य विष्णो रूप महात्मनः
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.8849)
- **Original**: 18 यक्षराक्षसदैतेयपिशाचो रगदानवा:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.8850)
- **Original**: गन्धर्वाप्सरसशैव रूप विष्णोर्महात्मम:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.8851)
- **Original**: 19 अहर्क्षतारकाचित्रगगनाभिजलानिला:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.8852)
- **Original**: अहं चर विषयाओव सर्व विष्णुमय जगत्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.8853)
- **Original**: 20 तथाप्यनेकरूपस्थ तस्य रूपाण्यहर्निशम्‌ । बाध्यवाधकता यान्ति कल्लोला इब सागरे
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.8854)
- **Original**: 21 तत्साम्प्रतममी दैत्या: कालनेमिपुरोगमा: । मर्त्यछोक॑ समाक्रम्य बाधन्ते5हर्निश प्रजा:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.8855)
- **Original**: 22 कालनेमिर्तो योउसौ विष्णुना प्रभविष्णुना । उग्रसेनसुतः कंसस्सम्भूतस्स महासुरः
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.8856)
- **Original**: 23 अएिष्टो धेनुकः केशी प्रलृम्यो नरकस्तथा । सुन्दो5सुरस्तथात्युग्रे बाणश्लापि बलेस्सुत:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.8857)
- **Original**: 24 तथान्ये च महावीर्या नृपाणां भवनेषु ये । सपुत्यत्ञा दुरात्मानस्तान्न संख्यातुमुत्सहे
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.8858)
- **Original**: 25 दूँगा!
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.8859)
- **Original**: शआरीपराद्ारजी बोल्छे--हे द्विजोत्तम ! तब सत्यके गौरवसे कंसने यसुदेवजोसे 'यहुत अच्छा' कह देवकीका खघ नहीं कियां। 1515
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.8860)
- **Original**: इसी समय अत्पन्त भारसे पोडित होकर पूथियों [ गौका रूप धारणकर ] सुपेरु- पर्बृतपर देवताओंके दल्में गयीं
- **Translation**: 

---

