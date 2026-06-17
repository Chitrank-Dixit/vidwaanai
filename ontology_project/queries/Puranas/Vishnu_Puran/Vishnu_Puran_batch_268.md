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

### Verse 1 (Vishnu Puran 0.5341)
- **Original**: है नप ! चर्मविरुद्ध अर्थ और काम दोनोंका त्याग कर दे तथा ऐसे धर्मका भी आचरण न करे जो उत्तरकारूमें दुःखमय अथवा समाज-विरुद्ध हो
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.5342)
- **Original**: है नरेध्वर ! तदतत्तर ब्राह्ममुहृर्तमें ठठकर प्रथम मूत्रत्याग करे। ग्रामसे नैरऋत्यकोणमें जितनी दूर बाण जा सकता है उससे आगे बढ़कर अथवा अपने निवास स्थानसे दूर जाकर मल-मूत्र त्याग करे। पैर धोया हुआ और जूठा जल अपने घरके आँगनमें न डाले
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.5343)
- **Original**: 8-- 10
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.5344)
- **Original**: अपनी: या व॒क्षकी छायाके ऊपर तथा गौ, सूर्य, अग्नि, वायु, गुरु और द्विजातीय पुरुषके सामने बुद्धिमान्‌ पुरुष कभी घरत-सुत्रल्याग न करें
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.5345)
- **Original**: इसी प्रकार हे पुरुषर्षभ ! जुते हुए सेतमें, सस्यसम्पत्र भूमिमें, गौओंके गोष्ठमें, जन- मार्गके बरीचपें, नदी आदि तीर्थस्थानोंमें, जल अथवा जल्म्नशयके तटपर और दउइमजानमें भी कभी मल-सूत्रक्य्र त्याग न करे
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.5346)
- **Original**: है राजन्‌ ! कोई विशेष आपत्ति न हों तो रात्रिके समय दक्षिण-मुख होकर मूत्रत्याग करे
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.5347)
- **Original**: मल-व्यागके समय पुृथित्रीको तिनकोरॉंसे और सिस्को बस्रसे ढाँप ले तथा ठस स्थानपर अधिक समयतक न रहे आर न कुछ बोले हो
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.5348)
- **Original**: हे राजन्‌ ! बाँबीकी, चूहोंद्वारा बिलसे निकास्मे हुई जलके भीतस्की, शौचकर्मसे बची हुई, घरके ल्लीपनकी चींटो आदि छोटे-छोटे जीबोंद्राग निकात्डी हुई और हलसे उख्लाड़ी हुई--इन सत्र प्रकारकी मृत्तिकाओंका शौच कर्ममें उपयोग न करे
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.5349)
- **Original**: हे नृष ! लिंगमें एक बार, गुदामें तीन आर, बायें हाथमें दस बार और दोनों हाथोंमें सात बार मृत्तिका छगानेसे शौच सम्पन्न होता है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.5350)
- **Original**: तदनन्तर गश्च और फेनरहित स्वच्छ जलसे आचमन करे
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.5351)
- **Original**: तथा फिर सावधानतापूर्वक वहुत-सी मृत्तिका ले
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.5352)
- **Original**: उससे चरण-शुद्धि करनेके अनन्तर फिर पैर घोकर तीन जार कुल्ल्म करे और दो बार मुख धोते
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.5353)
- **Original**: तत्पश्चात्‌ जऊू लेकर शिरोदेद्ामें स्थित
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.5354)
- **Original**: 192 स्वाचान्तस्तु ततः कुर्यात्युमान्केशप्रसाधनम्‌। आदर्शाक्नमाडल्यं दूर्वाद्यालम्भभानि च
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.5355)
- **Original**: 22 सोमसंस्था हविस्संस्था: पाकसंस्थास्तु संस्थिता: । थने यतो मनुष्याणां यतेतातो धनार्जने
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.5356)
- **Original**: 24 नदीनदतटाकेषु च। नित्यक्रियार्थ स्रायीत गिरिप्रस्लवणेषु ल
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.5357)
- **Original**: 25 कृपेषूदधृततोयेन स्त्रानं कुर्वीत वा भुवि। गृहेबृदधूततोयेन ह्ाथवा भुव्यसम्भवे
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.5358)
- **Original**: 26 तेषामेव हि तीर्थेन कुर्वीत सुसमाहित:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.5359)
- **Original**: 27 त्रिरप: प्रीणनार्थाव देवानामपवर्जयेत्‌ । ऋषीणां च यथान्यायं सकृश्ापि प्रजापते:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.5360)
- **Original**: 28 मातामहाय तत्पित्रे तत्पित्रे ले समाहित: । स्घात्पैत्रेण तीथेंन काम्य॑ चान्यच्छृणुष्न मे
- **Translation**: 

---

