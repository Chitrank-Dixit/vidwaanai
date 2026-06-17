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

### Verse 1 (Vaivtpuran 13.11302)
- **Original**: ही कुलदेवता। संसारकी सृष्टि, पालन और संहार भीगे नहीं थे। शरीर भी आर्द्र नहीं था। भाल-
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.11303)
- **Original**: करनेवाले भी आप ही हैं। अग्नि, वरुण, चन्द्रमा, देशमें चन्दन और नेत्रोंमें अक्षनका थ्रुज्जार भी लुप्त
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.11304)
- **Original**: सूर्य, यम, कुबेर, वायु, ईशानादि देवता, ब्रह्मा, नहीं हुआ था। समस्त आभूषणोंसे अलंकृत,
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.11305)
- **Original**: शिव, शेष, धर्म, इन्द्र, मुनीन्द्र, मनु, मानव, दैत्य, सिरपर मोरपंखका मुकुट धारण किये और अधरोंसे
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.11306)
- **Original**: यक्ष, राक्षस, किन्नर तथा अन्य जो-जो चराचर मुरली लगाये अच्युत श्रीकृष्ण ब्रह्मतेजसे प्रकाशित
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.11307)
- **Original**: प्राणी हैं, वे सब-के-सब आपकी ही विभूतियाँ हो रहे थे। यशोदा अपने लालाको देखते ही
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.11308)
- **Original**: हैं। उन सबके आविर्भाव और लय आपकी छातीसे लगाकर मुस्करा उठीं और उनके
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.11309)
- **Original**: इच्छासे ही होते हैं। गोविन्द! हमें अभय दीजिये मुखारविन्दकों चूमने लगीं। उस समय उनके नेत्र
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.11310)
- **Original**: और इस अग्रिका संहार कीजिये। हम आपकी और मुख प्रसन्नतासे खिल उठे थे। नन्‍द, बलराम
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.11311)
- **Original**: शरणमें आये हैं। आप हम शरणागतोंको बचाइये। तथा रोहिणीजीने बारी-बारीसे श्यामसुन्दको
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.11312)
- **Original**: यों कहकर बे सब लोग श्रीकृष्णके हर्षपूर्वक हृदयसे लगाया। सब लोग एकटक हो
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.11313)
- **Original**: चरणकमलोंका चिन्तन करते हुए खड़े हो गये। गोविन्दके श्रीमुखका दर्शन करने लगे। प्रेमसे अंधे
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.11314)
- **Original**: श्रीकृष्णजी अमृतमयी दृष्टि पड़ते ही दावानल हुए सम्पूर्ण ग्वालबालोंने श्रीहरिका आलिब्जन
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.11315)
- **Original**: दूर हो गया। फिर तो वे ग्वालबाल मोदमग्न होकर किया। गोपाडुनाएँ नेत्र-चकोरोंद्वार उनके मुखचन्धकी
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.11316)
- **Original**: नाचने लगे। क्यों न हो, श्रीहरिके स्मरणमात्रसे मधुर सुधाका पान करने लगीं। सब विपत्तियाँ नष्ट हो जाती हैं। जो प्रातःकाल इतनेमें ही वहाँ सहसा वनके भीतरी
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.11317)
- **Original**: उठकर इस परम पुण्यमय स्तोत्रका पाठ करता भागको दावानलने आवेष्टित कर लिया। उन
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.11318)
- **Original**: है, उसे जन्म-जन्ममें कभी अग्रिसे भय नहीं सबके साथ गौओंका समुदाय भी उस दाबाग्रिसे
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.11319)
- **Original**: होता। शत्रुओंसे घिर जानेपर, दावानलमें आ घिर गया। वनके भीतर चारों ओर पर्वतोंके
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.11320)
- **Original**: जानेपर, भारी विपत्तिमें पड़नेपर तथा प्राणसंकटके समान आगकी ऊँची-ऊँची लपटें उठने लगीं।
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.11321)
- **Original**: समय इस स्तोत्रका पाठ करके मनुष्य सब यह देख सबने अपना नाश निकट ही समझा।
- **Translation**: 

---

