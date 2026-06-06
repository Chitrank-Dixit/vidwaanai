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

### Verse 1 (Vishnu Puran 0.11381)
- **Original**: 41 शरीरग्रहणात्मिका । लीलेयं सर्वभूतस्य॒ तब चेष्टोपलक्षणा
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11382)
- **Original**: 42 तत्मसीदाभयं दत्त बाणस्थास्य मया प्रभो। तक्त्कया नानृतं कार्य यन्मया व्याहत॑ वच:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11383)
- **Original**: 43 अस्मस्संश्रयदृप्तोठयय नापराधी तवाव्यय । मया कद़्तबरो दैत्यस्ततस्त्वां क्षयाम्यहम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11384)
- **Original**: डड॑ अ्रीपयशर उवाच इत्पुक्त: प्राह गोविन्द: झूलपाणिमुमापतिम्‌ । प्रसन्ननदनों भूत्वा गतामषों5सुरं प्रति
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11385)
- **Original**: 45 औभगवानुवाच युष्पदत्ततरों वाणो जीवतामेष झज्जर । ल्द्वाक्यगौरवादेतन्पया चक्र निवर्तितम्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11386)
- **Original**: 46 त्वया यदभय॑ दतं तहत्तमखिलं मया। म्त्तोजविभिन्नमात्मान द्रह्ममहीसि शद्भूर
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11387)
- **Original**: 47 योडहं स॒त्व॑ जगधेेद॑ सदेवासुरमानुषम्‌। अत्तो नान्यदशेष यत्तत्त्व ज्ञातुभिहाहसि
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11388)
- **Original**: 48 अविद्यामोहितात्मानः पुरुषा भिन्नदर्शिनः । बदन्ति भेद पश्यन्ति चावयोरन्तर हर
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11389)
- **Original**: 49 प्रसन्नोडह गमिष्यामि त्व॑ गच्छ वृषभध्वज
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11390)
- **Original**: 50 अ्रीपराशर उवाच इत्युक्त्वा प्रययौ कृष्ण: प्राद्युप्नियत्र तिष्ठति । तहन्धफणिनो. नेशुर्गरुडानिल्तपोथिता:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11391)
- **Original**: 51 ततो5निरुद्धमारोप्प सपत्रीक॑ गरुत्मति । आजम्मुर्हरकां रामका््णिदामोदरा: पुरीम्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11392)
- **Original**: 52 पुत्रपोत्र: परिवृतस्तत्र रेमे जनार्दन: । देवीभिस्सतत॑ विप्र भूभारतरणेच्छया
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11393)
- **Original**: 53 श्रीठमापतिने गोविन्दके पास आकर सामपूर्वक कहा--
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11394)
- **Original**: बोले--हे कृष्ण ! है कृष्ण !! हे जगन्नाथ !! मैं यह जानता हूँ कि आप पुरुषोत्तम परमेश्वर, परमात्मा और आदि-अन्तसे रहित श्रीहरि हैं
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11395)
- **Original**: आप सर्वभूतमय हैं । आप जो देव, तिर्यक्‌ और मनुष्यादि योनियोंमें शरीर धारण करते हैं यह आफ्की स्वाधीन चेष्टाकी उपलक्षिका लीला ही है
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11396)
- **Original**: है प्रभो ! आप प्रसन्न होइये। मैंने इस बाणासुरको अभयदान दिया है । हे नाथ
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11397)
- **Original**: मैंने जो वचन दिया है उसे आप मिथ्या न करें
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11398)
- **Original**: है अव्यय ! यह आपका अपराधी नहीं है; यह तो गेरा आश्रय पानेसे ही इतना गर्वीला हो गया है। इस दैत्यकों मैंने ही वर दिया था इसलिये मैं ही आपसे इसके लिये क्षमा करता हूँ
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11399)
- **Original**: श्रीपराह्यरजी खोछे--विशूलपाणि भगवान्‌ उमापतिके इस प्रकार कहनेपर श्रीगोचिन्दने बाणासुरके प्रति क्रोधभाव त्याग दिया और प्रसन्ननदन होकर उनसे कहा--
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11400)
- **Original**: श्रीभगबान्‌ बोले--हे शद्भूर ! यदि आपने इसे वर दिया है तो यह बाणासुर जीवित रहे । आपके वचनका मान रखनेके लिये मैं इस चक्रको रोके लेता हूँ
- **Translation**: 

---

