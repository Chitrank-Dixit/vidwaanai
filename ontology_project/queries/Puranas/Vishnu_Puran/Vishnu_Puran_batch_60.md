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

### Verse 1 (Vishnu Puran 0.1181)
- **Original**: 19 भार्येति प्रोच्यते चान्या मद्ठिधा पुण्यवर्जिता
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.1182)
- **Original**: 20 पुण्योपचयसम्पन्नस्तस्या: पुत्रस्तथोत्तम: । मम पुत्रस्तथा जात: स्वल्पपुण्यो ध्रुवो भवान्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.1183)
- **Original**: 21 तथापि दुःखं न भवान्‌ कर्त्ुमहति पुत्रक । यस्य यावत्स तेनैव स्वेन तुष्यति मानव:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.1184)
- **Original**: 22 यदि ते दुःखमत्यर्थ सुरुव्या वचसाभवत्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.1185)
- **Original**: तत्पुण्योप्चये यत्र॑ कुरु सर्वफलप्रदे
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.1186)
- **Original**: 23 सुशीत्त्षे भव धर्मात्मा मैत्र: प्राणिहिते रत: । निम्न॑ यथाप: ग्रतणा: पात्रमायान्ति सम्पद:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.1187)
- **Original**: 24 घ्र॒व उवाव अम्ब यक्तवमिदं प्रात्थ प्रशमाय वचो मम । नैतहुर्बबसा भिन्ने हदये मम तिप्ठति
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.1188)
- **Original**: 25 सो5हं तथा यतिष्यामि यथा सर्वोत्तमोत्तमम्‌ । स्थान॑ प्राप्स्याम्यशेषाणां जगतामभिपूजितम्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.1189)
- **Original**: 26 सुरुचिर्दयिता राज्ञस्तस्पा जातो5स्मि नोदरात्‌ । अभाव पहय मे>म्ब त्वं बृद्धस्यापि तवोदरे
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.1190)
- **Original**: 27 उत्तम: स पम भ्राता यो गर्भेण धृतस्तया । स राजासनमाप्रोतु पित्रा दत्त तथास्तु तत्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.1191)
- **Original**: 28 नान्यदतमभीणष्सामि स्थानमम्ब स्वकर्मणा । इच्छामि तदहं स्थान यज्न प्राप पिता मम
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.1192)
- **Original**: 29 श्रीपराशर उवाच निर्जगाम गृहान्मातुरित्युक्त्वा मातरं ध्रुव: । पुराक्च निर्गम्य ततस्तद्वाह्योपव्न॑ ययौ
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.1193)
- **Original**: 30 स ददर्श मु्नीस्तत्र सप्त पूर्वागतान्थुव: । कृष्णाजिनोत्तरीयेषु विष्टरेषु समास्थितान्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.1194)
- **Original**: 31 स॒ राजपुत्रस्तान्सर्वान्ग्मणिपत्याभ्यभाषत । प्रश्रयावनत:.. सम्यगभिवादनपूर्वकम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.1195)
- **Original**: 32 घुव उतानत उत्तानपादतनयं मां निवोधत सत्तमा: । जात॑ सुनीत्यां निर्वेदाधुष्पाकं प्राप्तमन्तिकम्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.1196)
- **Original**: 33 श्रीचिच्णुप्राण [ अ₹13 नहीं करना चाहिये
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.1197)
- **Original**: हे वत्स ! जिसका पुण्य होता है टसीको राजासन, राजच्छप तथा उत्तम-उत्तम घोड़े और हाथी आदि मिलते हैं--ऐसा जानकर तू झान्त हो जा
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.1198)
- **Original**: अन्य जन्मोमें किये हुए पुण्य-कर्मोके कारण ही सुरूचिमें राजाक्ी सुरुचि (प्रीति) है और पुण्यहीना होनेसे ही मुझ-जैसी स्त्री केबल भार्या (भरण करने योग्य) ही कही जाती है
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.1199)
- **Original**: उसी प्रकार उसका पुत्र उत्तम भी बड़ा पुण्य-पुझ्लसग्गन्न है और मेरा पुत्र तू घुज मेरे समान ही अल्प पुण्यवान्‌ है
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.1200)
- **Original**: तथापि बेटा ! तुझे दुःखी नहीं होना चाहिये, क्योकि जिस मनुष्यको जितना मिलता है वह अपनी ही पुँजीमें मप्न रहता है
- **Translation**: 

---

