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

### Verse 1 (Rig Ved 0.11341)
- **Original**: धिये पूषन्नयुज्महि
- **Translation**: 

---

### Verse 2 (Rig Ved 0.11342)
- **Original**: हे पूषनूदेव ! आप हमें मार्ग में सुरक्षित करें । जैसे अन्न के लिए रथ नियोजित करते हैं, वैसे ही हम बुद्धि- पूर्वक कर्म करने के लिए आपके सम्मुख उपस्थित होते हैं
- **Translation**: 

---

### Verse 3 (Rig Ved 0.11343)
- **Original**: 4936. अभि नो नय॑ बसु बीरं प्रयतदक्षिणम्‌ । बा गृहपतिं नय
- **Translation**: 

---

### Verse 4 (Rig Ved 0.11344)
- **Original**: 8 ऋप्वेद संहिता भाग - 2 हे पृषन्देव ! आप हमें मनुष्यों के हितैषी, पर्याप्त धन दान करने वाले दानवीर और प्रशंसनीय गृहस्थ के समीप ले चलें
- **Translation**: 

---

### Verse 5 (Rig Ved 0.11345)
- **Original**: 4937, अदित्सन्तं चिदाघृणे पूषन्दानाय चोदय। पणेश्निद्वि प्रदा मन:
- **Translation**: 

---

### Verse 6 (Rig Ved 0.11346)
- **Original**: है प्रकाशमान पूषनदेव ! आप कंजूस को दान देने की प्रेरणा दें । (कृपण) व्यापारी के कठोर हृदय को कोमल बनाएँ
- **Translation**: 

---

### Verse 7 (Rig Ved 0.11347)
- **Original**: 4938. वि पथो बाजसातये चिनुहि वि मृथो जहि। साधन्तामुग्र नो धिय:
- **Translation**: 

---

### Verse 8 (Rig Ved 0.11348)
- **Original**: हे पूषनूदेव ! आप हमारे घातक शत्रुओं का नाश करें । हमें धन प्राप्त करने का मार्ग बताएँ
- **Translation**: 

---

### Verse 9 (Rig Ved 0.11349)
- **Original**: 4939, परि तृन्थि पणीनामारया हृदया कवे
- **Translation**: 

---

### Verse 10 (Rig Ved 0.11350)
- **Original**: अथेमस्मभ्यं रन्‍्यय
- **Translation**: 

---

### Verse 11 (Rig Ved 0.11351)
- **Original**: हे पूषन्देव ! आप ज्ञानी हैं। आप (ज्ञानरूपी) शस्त्र से इन प्राणियों के कठोर हृदयों को चीर कर (परिवर्तित कर) हमारे अनुकूल कर दें
- **Translation**: 

---

### Verse 12 (Rig Ved 0.11352)
- **Original**: 4940, वि पृषन्नारया तुद पणेरिच्छ हृदि प्रियम्‌। अधेपस्मभ्यं रन्‍्धय
- **Translation**: 

---

### Verse 13 (Rig Ved 0.11353)
- **Original**: हे पृषन्देव ! आप आरे से प्राणियों के हृदय को चीरकर (परिवर्तित कर) उनके हृदय में प्रिय भाव भरें और हमारे वशीभूत कर दें
- **Translation**: 

---

### Verse 14 (Rig Ved 0.11354)
- **Original**: 4941, आ रिख किकिरा कृणु पणीनां हृदया कवे। अथेमस्मभ्यं रन्‍्धय
- **Translation**: 

---

### Verse 15 (Rig Ved 0.11355)
- **Original**: हे पूषनूदेव ! आप प्राणियों के हृदयों की कठोरता को खाली करें और उन्हें हमारे अधीन करें
- **Translation**: 

---

### Verse 16 (Rig Ved 0.11356)
- **Original**: 4942. यां पृषन्ब्रह्मचोदनीमारां विभर्ष्याघृणे। तया समस्य हृदयमा रिख किकिरा कृणु
- **Translation**: 

---

### Verse 17 (Rig Ved 0.11357)
- **Original**: हे पृषनदेव ! आप ज्ञान से प्रेरित आरे से कृपणों के हृदयों को अच्छी तरह खाली कर समभाव से भरें
- **Translation**: 

---

### Verse 18 (Rig Ved 0.11358)
- **Original**: 4943. या ते अष्टा गोओपशाघृणे पशुसाधनी । तस्यास्ते सुम्नमीमहे
- **Translation**: 

---

### Verse 19 (Rig Ved 0.11359)
- **Original**: हे तेजस्वी वीर पूषन्‌देव ! आप अपने जिस अख्त्र से पशुओं को प्रेरित कर सही मार्ग में चलाते हैं; उसी से हम भी अपने कल्याण की कामना करते हैं
- **Translation**: 

---

### Verse 20 (Rig Ved 0.11360)
- **Original**: 4944. उत नो गोषणिं धियमश्चसां वाजसामुत । नृवत्‌ कृणुहि बीतये
- **Translation**: 

---

