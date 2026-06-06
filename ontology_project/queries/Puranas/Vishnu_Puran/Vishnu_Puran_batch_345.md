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

### Verse 1 (Vishnu Puran 0.6881)
- **Original**: अपने पितापहकी यज्ञश्ञाामें आया
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.6882)
- **Original**: राजा सगरने भी चोड़ेके मिल जानेपर अपना यज्ञ समाप्त किया और ([ अपने पुत्रोके खोदे हुए
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.6883)
- **Original**: सागरकों ही अपत्य-स्रेहसे अपना पुत्र माना
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.6884)
- **Original**: उस अँशुमान्‌के दिल्मप नामक पुत्र हुआ और दिलीपके भगीरथ हुआ जिसने गल्लाजीको स्वर्गसे पृथिवोपर व्वकर उनका नाम भागीरथी कर दिया
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.6885)
- **Original**: भगीरथसे सुन्ोत्र, सु्तो्से श्रुति, श्रुतिसे नाभाग, नाभागसे अम्बरीष, अस्बरीपसे सिन्धुद्वीप, सिन्स॒ुद्बिपसे अयुतायु और अतुतायुसे ऋतुपर्ण नामक पुत्र हुआ जो राजा नलका सहायक और चद्यूतक्रीडाका पारदर्शों था
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.6886)
- **Original**: ऋतुपर्णका पुत्र सर्वकाम था, उसका सुदास और सुदासका पुत्र सौदास मित्रसह हुआ
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.6887)
- **Original**: 38--40
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.6888)
- **Original**: एक दिन मृगयाके लिये बनमें घूमते-घूमते उसने दो व्याघ्र देखे
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.6889)
- **Original**: इन्होंने सम्पूर्ण बनको मृगहीन कर दिया है--ऐसा समझकर उसने उनमेंसे एकको बाणसे मार ड्यछा
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.6890)
- **Original**: मरते समय यह अति भयद्भररूप क़्र- वदन राक्षस हो गया
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.6891)
- **Original**: तथा दूसरा भी “मैं इसका बदला रूुगा' ऐसा कहकर अन्तर्धात हो गया
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.6892)
- **Original**: काल्म्रन्तरमें सौदासने एक यज्ञ किया
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.6893)
- **Original**: यज्ञ समाप्त हो जानेपर जब आचार्य वसिश्न बाहर चले गये तब वह राक्षस वसिष्ठजीका रूप बनाकर बोल्का, 'यज्ञके पूर्ण होनेपर मुझे नर-मौसयुक्त भोजन कराना चाहिये; अतः तुम ऐसा अन्न तैयार कणओ, मैं अभी आता हूँ" ऐसा कहकर सह जाहर चला गया
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.6894)
- **Original**: फिर रसोइयेका वेष खनाकर राजाकी आज्ञासे उसने मनुष्यका मौस पकाकर उसे नियेदन किया
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.6895)
- **Original**: राजा भी उसे सुवर्णपात्रमें रखकर वसिष्ठजीके आनेकी प्रतीक्षा करने लगा और उनके आते ही बह मांस निवेदन कर दिया
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.6896)
- **Original**: वसिष्ठजीने सोचा, 'अहो ! इस साजाकी कुटिलता तो देखो जो यह जान-बूझकर भी मुझे खानेके लिये यह मांस देता है।' फिर यह जाननेके लिये कि यह किसका है वे ध्यानस्थ हो गये
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.6897)
- **Original**: ध्यानायस्थामें उन्होंने देखा कि वह तो नरमास है
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.6898)
- **Original**: तब तो क्रोधके कारण क्षुव्धचित्त होकर उन्होंने राजाको यह शाप दिया
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.6899)
- **Original**: “क्योंकि तूने जान-बूझकर भी हमारे जैसे तपस्वियोकि लिये अत्यत्त अभक्ष्य यह नरमांस मुझे सानेको दिया है इसलिये तेरी इसीमें ह्मेछुपता होगी [ अर्थात्‌ तू राक्षस हो जायगा ]
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.6900)
- **Original**: 248 श्रीविष्णुपुराण [ आ0 4 अनन्तरं च तेनापि भगवतैवाभिहितो 5स्मीत्युक्ते कि कि मयाभिहितमिति मुनिः पुनरपि समाधो तस्थो
- **Translation**: 

---

