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

### Verse 1 (Vishnu Puran 0.6401)
- **Original**: भक्‍तोठषि पुत्रमित्रकलतमन्त्रिभृत्य- बन्धुबलकोशादयस्समस्ता: काले नैतेनात्यन्त- मतीता:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.6402)
- **Original**: ततः पुनरप्युत्पन्नसाध्वसो राजा अगवन्तं प्रणम्य पप्रच्छ
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.6403)
- **Original**: भगवश्नेव- मवस्थिते मयेयं कस्मे देयेति
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.6404)
- **Original**: ततस्स भगवान्‌ किझिदवनप्रकन्धरः कृताअलिर्भूत्वा सर्वत्त्ेकगुरुरम्भोजयोनिराह
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.6405)
- **Original**: न ह्वादिमध्यान्तमजस्य यस्य विद्यो वय॑ सर्वमयस्य धातु: । न च स्वरूप न परे स्वभायं ने चैव सार॑ परमेश्वरस्थ
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.6406)
- **Original**: 83 कलामुहरत्तादिगययश्ष॒ कालो न यद्विभूते: परिणामहेतुः
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.6407)
- **Original**: अजमन्पनाशस्य हा रनामरूपस्प सनातनस्य
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.6408)
- **Original**: 84 प्रसादादहमच्युतस्य भूत: प्रजासृष्टिकरो5न्तकारी । यस्मान्च मध्ये पुरुषः परस्मात्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.6409)
- **Original**: 85 प्रणाम कर उनसे अपनी कन्याके योग्य बर पूछा
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.6410)
- **Original**: भगवान्‌ ब्रह्मने कहा--'' तुम्हें जो लर अभिमत हों उन्हें बताओ"!
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.6411)
- **Original**: तब उन्होंने भगवान्‌ ब्रह्माजीको पुनः त्रणाम कर अपने समस्त अभिमत वरोंका वर्णन किया और पूछा कि “इनमेंसे आपको कौन वर पसन्द है जिसे मैं यह कन्या दूँ ?'
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.6412)
- **Original**: इसपर भगवान्‌ कमलयोनि कुछ सिर झुकाकर मुसकाते हुए बोले--
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.6413)
- **Original**: “तुमको जो-जो बर अभिप्रत हैं उनमेंसे तो अब पृथिवीपर किसीके पुत्र- पौत्रादिकी सन्‍्तान भी नहीं है
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.6414)
- **Original**: क्योंकि यहाँ 'न्धवॉका गान सुनते हुए तुम्हें कई चतुर्युग जीत चुके है
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.6415)
- **Original**: इस समय पुथिवीतलूपर अट्टाईसवें मन्‌का चतुर्युग प्रायः समाप्त हो चुका है
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.6416)
- **Original**: तथा कलियुगका प्रारम्भ होनेवाल्त्र है।'77
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.6417)
- **Original**: अब तुम ( अपने समान ] अकेले ही रह गये हो, अतः यह कन्या-रत्ष किसी और योग्य बरकों दो। इतने समयमें सुम्हारे पुत्र, सित्र, कल, मन्त्रियर्ग, भुत्यगण, बन्धुगण, सेना और कोशादिका भो सर्वथा अभाव हो चुका है”'
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.6418)
- **Original**: तब तो राजा रैवतने अत्यन्त भयभीत हो भगवान्‌ ब्रह्माजीको पुतः प्रणाम कर पूछ
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.6419)
- **Original**: “भगवन्‌ ! ऐसी बात है, तो अब मैं इसे किसको दूँ ?'
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.6420)
- **Original**: तब सर्वलोकगुरु भगवान्‌ कमलयोनि कुछ सिर झुकाए हाथ जोड़कर बोले
- **Translation**: 

---

