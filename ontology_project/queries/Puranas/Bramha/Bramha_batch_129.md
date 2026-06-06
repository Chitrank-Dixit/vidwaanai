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

### Verse 1 (Bramha 0.2561)
- **Original**: . श्वेत बोले--3* यासुदेवको नमस्कार है।
- **Translation**: 

---

### Verse 2 (Bramha 0.2562)
- **Original**: पुरुषोत्तमक्षेत्रपें भगवान्‌ भुसिंह तथा एवेतमाथवका माहात्प्य 123 सबको अपनी ओर खींचनेवाले संकर्षणको नमस्कार
- **Translation**: 

---

### Verse 3 (Bramha 0.2563)
- **Original**: नमस्कार है और वामनवाहन माधवको प्रणाम है। है। अत्यन्त दुतिमान्‌ प्रद्यप्र, कभी रुद्ध न होनेवाले
- **Translation**: 

---

### Verse 4 (Bramha 0.2564)
- **Original**: रमणीय, पूज्य तथा अव्यक्तस्वरूप भगवानूको अनिरुद्ध तथा नारायणको नमस्कार है। जिनके ' नमस्कार है। अतर्क्य, शुद्ध एवं भयहारी हरिको अनेक रूप हैं, जो विश्वरूप, विधाता, निर्गुण,
- **Translation**: 

---

### Verse 5 (Bramha 0.2565)
- **Original**: प्रणाम है। जो संसाररूपी समुद्रसे तारनेके लिये अतर्क्य, शुद्ध एवं उज्बल कर्मवाले हैं, उनको
- **Translation**: 

---

### Verse 6 (Bramha 0.2566)
- **Original**: नौकाके समान हैं, जो परम शान्त एवं चैतन्यस्वरूप नमस्कार है। जिनकी नाभिमें कमल है, जो
- **Translation**: 

---

### Verse 7 (Bramha 0.2567)
- **Original**: हैं, शिव, सौम्यरूप, रुद्र तथा उद्धारकर्ता हैं, उन पद्मगगर्भ ब्रह्माजीकी उत्पत्तिके कारण हैं, उनको
- **Translation**: 

---

### Verse 8 (Bramha 0.2568)
- **Original**: भगवानको नमस्कार है। जो संसारका संहार नमस्कार है। जिनका वर्ण कमलके समान है, जो
- **Translation**: 

---

### Verse 9 (Bramha 0.2569)
- **Original**: करनेवाले और उसे भोग प्रदान करनेवाले हैं, हाथमें भी कमल लिये रहते हैं, उनको नमस्कार
- **Translation**: 

---

### Verse 10 (Bramha 0.2570)
- **Original**: समस्त विश्व जिनका स्वरूप है और जो समस्त है। जिनके नेत्र कमलके समान हैं, जो सहस्रों
- **Translation**: 

---

### Verse 11 (Bramha 0.2571)
- **Original**: बिश्वकी सृष्टि करनेवाले हैं, उन भगवान्‌कों नेत्रोंसे युक्त और शिवस्वरूप हैं, उन्हें नमस्कार
- **Translation**: 

---

### Verse 12 (Bramha 0.2572)
- **Original**: नमस्कार है। 3 दिव्यरूप सोम, अग्नि और हैं। जिनके सहस्नों पैर और सहख्रों भुजाएँ हैं, उन
- **Translation**: 

---

### Verse 13 (Bramha 0.2573)
- **Original**: वायुस्वरूप भगवान्‌कों नमस्कार है। चन्द्रमा और मन्युरूप परमेश्वरको नमस्कार है। 3» वराहरूपधारी
- **Translation**: 

---

### Verse 14 (Bramha 0.2574)
- **Original**: सूर्यकी किरणें जिनके केश हैं, जो गौओं तथा भगवान्‌को नमस्कार है। जो बर देनेवाले, उत्तम
- **Translation**: 

---

### Verse 15 (Bramha 0.2575)
- **Original**: ब्राह्मणॉंका हित करनेवाले हैं, उन भगवान्‌को बुद्धिसे युक्त, वरिष्ठ, वरेण्य, शरणागतरक्षक और
- **Translation**: 

---

### Verse 16 (Bramha 0.2576)
- **Original**: प्रणाम है। 5» ऋकक्‍!स्वरूप पद और क्रमरूप अपनी महिमासे कभी च्युत न होनेवाले हैं, उन
- **Translation**: 

---

### Verse 17 (Bramha 0.2577)
- **Original**: भगवान्‌को प्रणाम है। ऋग्वेदके मन्त्रोंदरा जिनको भगवान्‌को प्रणाम है। 3> बालरूपधारी, बाल- , स्तुति होती है, ऋचाओंका जप जिनकी प्राप्तिका कमलके समान कान्तिमान्‌, बालसूर्य और चन्द्रमारूप
- **Translation**: 

---

### Verse 18 (Bramha 0.2578)
- **Original**: साधन है, उन भगवान्‌कों नमस्कार है। 3& नेत्रॉंबाले, मनोहर केशोंसे सुशोभित, बुद्धिमान्‌
- **Translation**: 

---

### Verse 19 (Bramha 0.2579)
- **Original**: यजुर्वेदको धारण करनेवाले और यजुर्वेदरूपधारी भगवान्‌ विष्णुकों प्रणाम है। केशवको नमस्कार
- **Translation**: 

---

### Verse 20 (Bramha 0.2580)
- **Original**: भगवान्‌को प्रणाम है। जिनका यजुर्वेदके मन्त्रोंसे है, नारायणको नित्य नमस्कार है। सर्वश्रेष्ठ माधव
- **Translation**: 

---

