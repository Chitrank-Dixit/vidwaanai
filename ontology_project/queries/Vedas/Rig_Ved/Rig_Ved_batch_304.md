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

### Verse 1 (Rig Ved 0.6061)
- **Original**: अम्निदेव यज्ञ में प्रज्बलित होकर केश रूप ज्वाला वाले, पविश्रकारक और स्तुत्य हैं, उनसे हम इष्ट फल की याचना करते हैं
- **Translation**: 

---

### Verse 2 (Rig Ved 0.6062)
- **Original**: 2661. पृथुपाजा अमर्त्यों घ्तनिर्णिक्स्वाहुत: । अग्निर्यज्ञस्थ हव्यवाट्‌
- **Translation**: 

---

### Verse 3 (Rig Ved 0.6063)
- **Original**: महान्‌ तेजस्वी, अजर-अमर, घृतवत्‌ तेजोमब, भली- भाँति जिनका आवाहन और पूजन किया गया है, ऐसे अम्निदेव, यज्ञ में समर्पित हवियों को धारण करने वाले हैं
- **Translation**: 

---

### Verse 4 (Rig Ved 0.6064)
- **Original**: 2662. त॑ सबाधों यतख्नुत्न इत्था थधिया यज्ञवन्त:। आ चक्रुरग्निमूतये
- **Translation**: 

---

### Verse 5 (Rig Ved 0.6065)
- **Original**: विघ्न-बाधाओं को दूर करके यज्ञ सम्पन्न करने वाले, यज्ञ के साधनों से युक्त ऋत्विजों ने अपनी रक्षा के लिए हव्यपूरित खुचा को आगे बढ़ाकर स्तुतियों के साथ अग्निदेव को समर्पित किया । इस प्रकार उन्हें अपने अनुकूल बनाया
- **Translation**: 

---

### Verse 6 (Rig Ved 0.6066)
- **Original**: 2663. होता देवो अपर्त्य: पुरस्तादेति मायया। विदथानि प्रचोदयन्‌
- **Translation**: 

---

### Verse 7 (Rig Ved 0.6067)
- **Original**: देवों का आवाहन करने वाले, अविनाशो, प्रकाशमान अग्निदेव, याजकों को सत्कर्म की प्रेरणा देते हुए शीघ ही प्रकट होते हैं
- **Translation**: 

---

### Verse 8 (Rig Ved 0.6068)
- **Original**: 2664. वाजी वाजेषु धीयतेउध्वरेषु प्र णीयते। विप्रो यज्ञस्य साधन:
- **Translation**: 

---

### Verse 9 (Rig Ved 0.6069)
- **Original**: संग्राम में बलशालो अग्निदेव को, शत्रु नाश करने के निमित स्थापित करते हैं । यह ज्ञान-सम्पन्न अग्निदेव यज्ञादि श्रेष्ठ कर्मों को सिद्ध करने वाले साधन रूप हैं
- **Translation**: 

---

### Verse 10 (Rig Ved 0.6070)
- **Original**: 2665, धिया चक्रे बरेण्यो भूतानां गर्भमा दधे
- **Translation**: 

---

### Verse 11 (Rig Ved 0.6071)
- **Original**: दक्षस्थ पितरं तना
- **Translation**: 

---

### Verse 12 (Rig Ved 0.6072)
- **Original**: वे अग्निदेव सब यज्ञ कर्मों में प्रकट होने के कारण श्रेष्ठ हैं और सब प्राणियों में संव्याप्त हैं । विश्व पालक अग्निदेव को वेदी स्वरूपिणी दक्ष-पुत्री यज्ञादि के निमित्त धारण करती हैं
- **Translation**: 

---

### Verse 13 (Rig Ved 0.6073)
- **Original**: 2666. नि त्वा दथे वरेण्य॑ दक्षस्थेव्या सहस्कृत । अग्ने सुदीतिमुशिजम्‌
- **Translation**: 

---

### Verse 14 (Rig Ved 0.6074)
- **Original**: है अग्विदेव ! आप घर्षण-बल (अरणि-मन्थन) से प्रकट होने वाले, श्रेष्ठ, तेजस्वी घृतादि हविष्यात्न की कामना करने वाले और वरण करने योग्य हैं। आपको वे दो रूपों वाली दक्ष पुत्री 'इला' धारण करती हैं
- **Translation**: 

---

### Verse 15 (Rig Ved 0.6075)
- **Original**: 2667. अग्नि यन्तुरमप्तुरमृतस्य योगे बनुषः। विप्रा वाजै: समिन्धते
- **Translation**: 

---

### Verse 16 (Rig Ved 0.6076)
- **Original**: मेधाबों साधकगण जगनियन्ता, जल-प्रेरक अग्निदेव को हविष्यात्र द्वारा सम्यक्‌ रूप से प्रदीप्त करते हैं
- **Translation**: 

---

### Verse 17 (Rig Ved 0.6077)
- **Original**: 2668. ऊर्जो नपातमध्यरे दीदिवांसमुप द्यवि । अग्निमील्ठे कविक्रतुम्‌
- **Translation**: 

---

### Verse 18 (Rig Ved 0.6078)
- **Original**: बलों को धारण करने वाले, घ्युलोक को प्रकाशित करने वाले अग्निदेव की हम इस यज्ञ में स्तुति करते हैं
- **Translation**: 

---

### Verse 19 (Rig Ved 0.6079)
- **Original**: 2669. ईल्ेन्यो नमस्यस्तिरस्तमांसि दर्शतः । समग्निरिध्यते वृषा
- **Translation**: 

---

### Verse 20 (Rig Ved 0.6080)
- **Original**: स्तुत्य, प्रणम्य, अन्थकार नाशक, दर्शनीय और शक्तिशाली हे अग्विदेव ! आप आहुतियों द्वारा भली प्रकार प्रज्वलित संवर्धित किये जाते हैं
- **Translation**: 

---

