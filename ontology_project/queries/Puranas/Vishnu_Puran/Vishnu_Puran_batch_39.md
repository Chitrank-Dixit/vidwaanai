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

### Verse 1 (Vishnu Puran 0.761)
- **Original**: 22 शाद्स्‍रों भगवाज्छौरिगौरी लक्ष्मीहिजोत्तम । भैत्रेय केशव: सूर्यस्तत्रभा कमत्लालया
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.762)
- **Original**: 23 विष्णु: पितृगण: पद्मा स्वधा शाश्तपुष्टिदा । चौ: श्री: सर्वात्यको विष्णु रवकाशो उतिविस्तर:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.763)
- **Original**: 24 झशाडु: श्रीधर: कान्ति: श्रीस्तथैवानपायिनी । धृतिर्लक्ष्मी्जगच्चेष्टा वायु: सर्वत्रगों हरि:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.764)
- **Original**: 25 जलधिद्विज गोविन्दस्तद्वेला श्रीर्महामुने । लक्ष्मीस्वरूपमिन्द्राणी देवेन््रे मधुसूदन:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.765)
- **Original**: 26 यपश्चक्रधर: साक्षादयूमोर्णा कमलालया
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.766)
- **Original**: ऋद्धि; श्री: श्रीधरो देव: स्वयमेत्र धनेश्रर:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.767)
- **Original**: 27 गौरी लक्ष्मीम॑हाभागा केशावों वरुण: स्वयम्‌ । श्री्िबसेना विप्रेष्न॒ देवसेनापतिहीरिं:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.768)
- **Original**: 28 अवष्टश्मो गदापाणि: शक्तिरलक्ष्मीद्विजोत्तम । काछठ लक्ष्मीनिमिषो सो मुहूत्तोंससौ कला त्वियम्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.769)
- **Original**: 29 लताभूता जगन्याता श्रीविष्णुईमसंज्ञितः
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.770)
- **Original**: 30 विभावरी श्रीर्दिवसों देवश्नक्रगदाधरः । बरप्रदो बरो विष्णुर्वधू: पद्मवनालया
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.771)
- **Original**: 31 नदस्वरूपी . भगवाड्छीर्नदीरूपसंस्थिता । ध्वजश्न पुण्डरीकाक्ष: पताका कमलालया
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.772)
- **Original**: 32 तृष्णा लक्ष्मीर्जगन्नाथो लोभो नारायण: पर: । रती रागश्च मैत्रेय लक्ष्मीगोबिन्द एव थे
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.773)
- **Original**: 33 कि चातिबहुनोक्तेन सल्लेपेणेदमुच्यते
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.774)
- **Original**: 34 देवतिर्यड्मनुष्यादो पुन्नामा भगवान्हरि: सख््रीनाप्ती श्रीक्ष बिज्ञेया नानयोविद्यते परम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.775)
- **Original**: 35 लक्ष्मीजी आज्याहुति (घृतकी आहुति) हैं
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.776)
- **Original**: है मुने
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.777)
- **Original**: मधुसूदन बजमानगृह हैं और लक्ष्मोजी पत्रोशाला हैं, श्रीहरि यूप हैं और लक्ष्मोजी चिति हैं तथा भगवान्‌ कुशा हैं और लक्ष्मीजी इध्सा हैं
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.778)
- **Original**: भगवान्‌ सामा्वरूप हैं और श्रीकमलादेज्ी उद्बीति हैं, जगत्पति भगवान्‌ वासुदेव हुताझन हैं और लक्ष्मीजी स्वाहा हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.779)
- **Original**: हे द्विजोत्तम ! अगवान्‌ विष्णु शंकर हैं और श्रीलक्ष्मीजी गौरी हैं तथा हे मैत्रेय ! औकेशव सूर्य हैं और कमलवासिनी श्रीलक्ष्मीजी उनकी प्रभा हैं
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.780)
- **Original**: श्रीविष्णु पितृगण हैं और श्रीकमल्ला नित्य पुष्टिदायिनी स्वधा हैं, विष्णु अति विस्तीर्ण सर्वात्पक अबकादा हैं और लक्ष्यीजी स्वर्गस्त्रेक हैं
- **Translation**: 

---

