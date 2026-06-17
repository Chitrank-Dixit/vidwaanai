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

### Verse 1 (Vishnu Puran 0.10281)
- **Original**: जब ठन घिकसितमुखकमल बालकोंने उससे पुष्प माँगे तो उसने अपने दोनों हाथ पृथिवापर टेककर सिरसे भूमिकों स्पर्श क्रिया
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.10282)
- **Original**: फिर उस मालीने कहा--''हे नाथ ! आपस्मेग छड़े ही कृपालु हैं जो मेरे घर पधारे
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.10283)
- **Original**: मैं धन्य हैं, क्योंकि आज मैं आपका पूजन कर सकूँगा'
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.10284)
- **Original**: तदनन्त! उसने “देखिये, ये बहूत सुन्दर हैं, ये बहुत सुन्दर हैं --इस प्रकार प्रसन्नमुखसे लुभा-लुभाकर उन्‍हें इच्छानुसार पुष्प दिये
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.10285)
- **Original**: उसने उन दोनों पुरुषश्रेष्ठोंकी पुतः- पून. प्रणामकर अत्ति निर्मक और सुगन्धित मनोहर पुष्प दिये
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.10286)
- **Original**: तब कृष्णचन्द्रने भी प्रसन्न होकर उस मालीको यह यर दिया कि “हे भद्र ! मेरे आश्रित रहनेखाली लक्ष्मी तझे
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.10287)
- **Original**: 362 बलहानिर्न ते सौम्य धनहानिरथापि या। याबद्दिनानि तावच्च न नश्िष्यति सनन्‍्ततिः
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.10288)
- **Original**: 25 भुकक्‍्त्वा च विपुलानभोगांस्त्वमन्ते मद्नसादत: । ममानुस्मरणं प्राप्य दिव्य छोकमवाप्स्यसि
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.10289)
- **Original**: 26 धर्में मनश्न ते भद्र सर्वकालं भविष्यति। युष्यत्सन्ततिजातानां दीर्घमायुर्भविष्यति
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.10290)
- **Original**: 27 नोपसर्गादिक दोष युध्मत्सन्ततिसम्भवः । अवाप्सय्ति महाभाग यावत्सूर्यों भविष्यति
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.10291)
- **Original**: 28 अपराशर उकाच उत्युवत्वा बलदेवसहायवान्‌ । श्रीविष्णुपुराण [ अब 20 कभी न ख्ोड़ेगी
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.10292)
- **Original**: हे सौम्य ! तेरे बकू और श्रनका हास कभी न होगा और जबतक दिन (सूर्य) की सत्ता रहेगी तबतक तेरी सनन्‍्तानका उच्छेद न होगा
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.10293)
- **Original**: तू भी यावज्जीबन नाता प्रकारके भोग भोगता हुआ अच्तमें मेरी कपासे मेरा स्मरण करनेके कारण दिव्य त्लेकको प्राप्त होगा
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.10294)
- **Original**: हे भद्र ! तेरा मन सर्वदा घर्मपरायण रहेगा तथा तेरे वंदामें जन्म लेनेवालॉकी आयु दीर्घ -होगी
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.10295)
- **Original**: हे महाभाग ! जबतक सूर्य रहेगा तबठक तेरे यैशमें उत्पन्न हुआ क्वेई भी व्यक्ति उपसर्ग (आकस्मिक रोग) आदि दोषोंको प्राप्त न होगा"
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.10296)
- **Original**: श्रीपराहरजी खोले--हे मुनिश्रेष्ठ
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.10297)
- **Original**: ऐसा कहकर बलभद्रजीके सहित माल्शकारसे पूजित हो तदगृहात्कृष्णो श्रीकृण्चचद्र निर्जगाम मुनिश्रेष्ठ मालाकारेण पूजित:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.10298)
- **Original**: उसके घरसे चल दिये
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.10299)
- **Original**: इति श्रीविष्णुपुराणे पहुमेंडशे एकोनिशो5ध्यायः
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.10300)
- **Original**: कफ फऔ -पफए बीसवाँ अध्याय क्ुब्जापर कृपा, धनुर्भड़, कुवबलयापीड और चाणूरादि मल्लॉका नाश तथा कंस-व्ध शीपराइर उगाच राजमार्गे ततः कृष्णस्सानुलेपनभाजनाम्‌ । दर्दर्श कुब्जामायान्ती नवयोबनगोचराम्‌
- **Translation**: 

---

