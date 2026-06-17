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

### Verse 1 (Vishnu Puran 0.8141)
- **Original**: _प्रद्यप्नोषपि रुक्मिणस्तनयां रूकमयती नामोपयेमे
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.8142)
- **Original**: तस्थामनिरुद्धो जज्ञे
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.8143)
- **Original**: अनिरुद्धोउपि रुक्मिण एज पोत्रीं सुभद्रां नामोपयेसे
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.8144)
- **Original**: तस्थामस्थय वज्रो जज्ञे
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.8145)
- **Original**: वहज्रस्थ श्रतिब्राहुस्तस्पापि सुचारु:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.8146)
- **Original**: . एबमनेकशतसहस्रपुरुषसं ख्यस्य यदुकुलस्थ पुत्रसंख्या वर्षशतैरपि वक्तुं न दइाक्यते
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.8147)
- **Original**: यतो हि इलोकाविमावत्र चरिताथं
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8148)
- **Original**: तिस्र: कोट्यस्सहस्राणापष्टाझ्ीतिशतानि न । कुमाराणां गृहाचार्याश्रापयोगेषु ये रता:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.8149)
- **Original**: 45 संख्यान॑ यादवानां कः करिष्यति महात्मनाम्‌। यत्रायुतानामयुतलक्षेणास्त. सदाहुकः
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.8150)
- **Original**: 46 देवासुरे हता ये तु दैतेयास्सुमहाबलाः । उत्पन्नास्ते मनुष्येषु. जनोपद्रवक्तारिण:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.8151)
- **Original**: 47 तेषामुत्सादनार्थाय भुवि देवा यदोः कुले । अवतीर्णाः कुलझतं यत्रैकाधभ्यधिक द्विज
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.8152)
- **Original**: 48 विष्णुस्तेषां प्रमाणे न प्रभुत्वे च व्यवस्थित: । निदेशस्थायिनस्तस्यथ ववृधुस्सर्वयादवा:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.8153)
- **Original**: 49 इति प्रसूति बृष्णीनां यश्थरणोति नर: सदा । स सं: पातकैर्मुक्तो विष्णुत्त्रेके प्रपद्मयते
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.8154)
- **Original**: 50 ( आ* 157 लाख अस्सी हजार पुत्र उत्पन्न किये
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.8155)
- **Original**: उनमेंसे प्रद्युम्र, चारुदेष्ण और साम्ब आदि तेरह पुत्र प्रधान थे
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.8156)
- **Original**: प्रद्युप्ने भी रुक्मीकी पुत्री रुकक्‍मखतीसे विखाह किया था
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.8157)
- **Original**: उससे अनिरुद्धका जत्म हुआ
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.8158)
- **Original**: अनिरुझते भी रुकमोको पौंत्री सुभद्रासे विवाह किया था
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.8159)
- **Original**: उससे वश्र उत्पन्न हुआ
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.8160)
- **Original**: वज़का पुत्र प्रतिबाहू तथा प्रतिबाहुका सुचारु था
- **Translation**: 

---

