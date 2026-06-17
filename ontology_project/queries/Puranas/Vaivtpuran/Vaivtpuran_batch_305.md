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

### Verse 1 (Vaivtpuran 13.12242)
- **Original**: सम्पत्ति प्राप्त होती है और चिरकालका खोया बीज! गुणातीत ! गुणस्वरूप ! गुणबीज ! गुणाधार!
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.12243)
- **Original**: हुआ नष्ट द्रव्य भी उपलब्ध हो जाता है। यदि गुणेश्व! आपको नमस्कार है। प्रभो! आप
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.12244)
- **Original**: कुमारी कन्या भक्तिभावसे एक वर्षतक प्रतिदिन अणिमा आदि सिद्धियोंके स्वामी हैं। सिद्धिकी
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.12245)
- **Original**: इस स्तोत्रको सुने तो निश्चय ही उसे श्रीकृष्णके भी सिद्धिरूप हैं। तपस्विन्‌! आप ही तप हैं [समान कमनीय कान्तिवाला गुणवान्‌ पति प्राप्त और आप ही तपस्याके बीज; आपको नमस्कार
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.12246)
- **Original**: होता है। है। जो अनिर्वचनीय अथवा निर्वचनीय वस्तु है, जलमें स्थित हुई राधिकाने श्रीकृष्णके वह सब आपका ही स्वरूप है। आप ही उन
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.12247)
- **Original**: चरणारविन्दोंका ध्यान एवं स्तुति करनेके पश्चात्‌ दोनोंके बीज हैं। सर्वबीजरूप प्रभो! आपको
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.12248)
- **Original**: जब आँखें खोलकर देखा तो उन्हें सारा जगत्‌ नमस्कार है। मैं, सरस्वती, लक्ष्मी, दुर्गा, गड्ढा
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.12249)
- **Original**: श्रीकृष्ममय दिखायी दिया। मुने ! तदनन्तर उन्होंने और बेदमाता सावित्री-ये सब देवियाँ जिनके
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.12250)
- **Original**: यमुनातटको वस्त्रों और द्रव्योंसे सम्पन्न देखा। चरणारविन्दोंकी अर्चनासे नित्य पूजनीया हुई हैं;
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.12251)
- **Original**: देखकर राधाने इसे तन्द्रा अथवा स्वप्रका विकार *गोलोकनाथ. गोपीश मदीश प्राणव्नभ । हे दीनबन्धो दीनेश सर्वेश्वर नमोउस्तु ते
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.12252)
- **Original**: गोपेश गोसमूहेश यशोदानन्दवर्धन । नन्दात्मज सदानन्द नित्यानन्द नमोउस्तु ते
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.12253)
- **Original**: शतमन्योरमन्युभग्र ब्रह्मदर्धवनाशक । कालीयदमन प्राणनाथ कृष्ण नमो5स्तु ते
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.12254)
- **Original**: शिवानन्तेशग. ब्रह्मेश..ब्राह्मणेश परात्पर । ब्रह्मस्वरूप ब्रह्म ब्रह्ममीज नमोउस्तु ते
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.12255)
- **Original**: चराचरतरोबींज गुणातीत शुणात्मक । गुणबीज गुणाधार गुणेश्वर नमोउस्तु ते
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.12256)
- **Original**: अधणिमादिकसिद्धीश सिद्धे:.. सिद्धिस्वरूपक । तपस्तपस्विस्तपसां बीजरूप तमोउस्तु ते
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.12257)
- **Original**: यदनिर्वयनीय॑ च वस्तु निर्वचनीयकम्‌ । तत्स्वरूप तयोबीज सर्वबीज नमो5स्तु ते
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.12258)
- **Original**: अहं सरस्वती. सक्ष्मीदुर्ग गज्जा श्रुतिप्रसू:
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.12259)
- **Original**: यस्य पादार्चनाश्रित्य॑ पूज्या तस्मैँ नमो नमः
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.12260)
- **Original**: स्पर्शे यस्थ धृत्यानां ध्यानेन च दिवानिशम्‌ । पवित्राणि च॑ तीर्थानि तस्मै भगवते नमः
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.12261)
- **Original**: इत्येवमुक्ला सा देवी जले संन्यस्य विग्रहम्‌ । मनः प्राणांश्व श्रीकृष्णे तस्थौ स्थाणुसमा सती
- **Translation**: 

---

