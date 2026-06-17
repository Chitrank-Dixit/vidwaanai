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

### Verse 1 (Vishnu Puran 0.6321)
- **Original**: 32 अमाद्यदिद्धस्सोमेन दक्षिणाभिद्विजातय: । मरुत: परिवेष्टारस्सदस्याश्न दिवोकसः
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.6322)
- **Original**: 33 स॒ मरुत्तश्नक्रवर्ती नरिष्यन्तनामानं पुत्रमबाप
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.6323)
- **Original**: तस्मान्च दम:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.6324)
- **Original**: दमस्य पुत्रो राजवर्द्धनो जज्ञे
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.6325)
- **Original**: . राजवर्द्धनात्सुवृद्धि:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.6326)
- **Original**: युधने अनुरक्त होकर उस ख्तीसे पुरूरता नामक पुत्र उत्पन्न किया
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.6327)
- **Original**: पुरूरवाके जन्मके अनन्तर भी ऋरतुमय ऋग्यजुःसामायर्यमय, सर्ववेदमय, मनोमय, ज्ञानमय, अन्नमय और पसरमार्थतः अकिश्चिग्मय भगवान्‌ यज्ञपुरुषक्य यथाबत्‌ यजन किया । तन उनकी कृपासे इल्त्र फिर भी सुधुम्न हो गयी
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.6328)
- **Original**: उस (सुधुम्र) के भी उत्कछ, गय और खिनत नामक तौन पुत्र हुए
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.6329)
- **Original**: पहले स्त्री होनेके कारण सुध्ुम्रको राज्याधिकार प्राप्त नहीं हुआ
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.6330)
- **Original**: वसिष्ठजीके कहनेसे उनके पिताने उन्हें प्रतिष्ठान नामक नगर दें दिया था, तहीं उन्होंने पुरूरवाको दिया
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.6331)
- **Original**: पुरूरवाकी सन्‍्तान सम्पूर्ण दिज्ञाओँमें फैले हुए क्षन्नियगण हुए । मनुका पृषध नामक पुत्र गुर्की गौका वध करनेके कारण शूद्र हो गया
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.6332)
- **Original**: मनुका पुत्र करूप था। करूषसे कारूष नामक महाबल्ते और पणक्तमी क्षत्रियगण उत्पन्न हूए
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.6333)
- **Original**: दिष्टका पुत्र नाभाग लैक्य हो गया था; उससे बल्थन नामक पुत्र हुआ
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.6334)
- **Original**: बअल्ल्धनसे महान्‌ कीर्तिमान्‌ अत्सप्रीति, वत्सप्रीतिसे प्रौशु और आंशुसे प्रजापति नामक इकल्लैता पुत्र हुआ
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.6335)
- **Original**: 20--22
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.6336)
- **Original**: प्रजापतिसे खनित्र, खनित्रसे चाक्षुष तथा चाक्षुषसे अति खल-पराक्रम-सम्पन्न विश हुआ
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.6337)
- **Original**: 23--25
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.6338)
- **Original**: विज्लसे विविश्ञक, विविशकसे खनिनेत्र, सनिनेत्से अतिविभूति और अतिविभूतिसे अति बलवान्‌ और शूरवीर कर्धम नामक : पुत्र हुआ
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.6339)
- **Original**: 26--29
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.6340)
- **Original**: करन्धमसे अविक्षित्‌ हुआ और अविक्षित॒के मरुत नामक अति बल-पराक्रमयुक्त पूत्र हुआ, जिसके विषयमें आजकल भी ये दो इलोक गाये जाते हैं
- **Translation**: 

---

