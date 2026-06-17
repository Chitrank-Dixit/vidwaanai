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

### Verse 1 (Vishnu Puran 0.8941)
- **Original**: 61 सुराश्ष सकलास्स्वांदैरवतीर्य महीतले । कुर्वन्तु युद्धमुत्मत्तै: पूर्वोत्पन्नैर्महासुरै:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.8942)
- **Original**: 62 ततः क्षयमशेषास्ते दैतेबा धरणीतले। प्रयास्यन्ति न सन्देहो मददुक्पातबिचूर्णिता:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.8943)
- **Original**: 63 वसुदेवस्थ या पत्नी देवकी देवतोपमा। तत्रायमष्टमो गर्भो मल्केशों भविता सुराः
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.8944)
- **Original**: 64 अवतीर्य च तत्रायं॑ कैस॑ घातयिता भुवि। कालनेमिं समुद्धृतमित्युक्त्वान्तर्दधे हरिः
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.8945)
- **Original**: 65 अदृश्याय ततस्तस्मै ग्रणिपत्य महामुने । प्रेस्पृष्टं॑ सुरा जग्मुरबतेरुश्ष॒ भूतले
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.8946)
- **Original**: 66 कंसाय चाष्टपो गर्भो देवक्या धरणीधरः । भ्रविष्यतीत्याचचक्षे भगवाजन्नारदो पुनिः
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.8947)
- **Original**: 67 कंसो5पि तदुपश्रुत्य॒नारदात्कुपितस्ततः । देवकी बसुदेव॑ चर गृहे गुप्तावधारयत्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8948)
- **Original**: 68 वसुदेवेन कंसाय तेनैवोक्ते यथा पुरा। तथैब बसुदेवोषपि पुत्रमर्पितवान्द्विज
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.8949)
- **Original**: 69 हिरण्यकरिपो: पुत्राष्पद्गर्भा इति विश्रुता: । विष्णुप्रयुक्ता तान्निद्रा क्रमादर्भानयोजयत्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.8950)
- **Original**: 70 योगनिद्रा महामाया वैष्णवी मोहित यया । अविद्यया जगत्सर्व॑ तामाह भगवान्हरि:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.8951)
- **Original**: 71 श्रीभगवानुवाच निद्रे गच्छ ममादेशात्याताछतलसंश्रयान्‌। एकैकत्वेन षड्गर्भानदेवकीजठरं॑ नय
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.8952)
- **Original**: 72 हतेषु तेषु कंसेन शेषाख्यों5शस्सतो मम । अंज्ांशेनोदरे तस्यास्सप्तमः सम्भविष्यति
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.8953)
- **Original**: 73 अ्रीपराशरजी बोले--हे महामुने । इस प्रकार स्तुति किये जानेपर भगवान्‌ परमेश्वरने अपने इ्याम और श्रेत दो केश ठखाड़े
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.8954)
- **Original**: और देवताओंसे बोले--'मेरे ये दोनों केश पृथिंयीपर अबतार लेकर पृथिवीके भाररूप काशको दूर करेंगे
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.8955)
- **Original**: सब देनगण अपने-अपने ओशॉसे पृथियीपर अवतार लेकर अपनेसे पूर्व डटान्न हुए उन्मतत दैत्योंके साथ युद्ध करें
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.8956)
- **Original**: तब निःसन्देह पृथियीतलपर सम्पूर्ण दैल्यगण मेरे दृष्टिपातसे दलित होकर क्षीण हो जायेंगे
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.8957)
- **Original**: यस्तुदेखजोको जो देवोके समान देवकी नामकी भार्यो है उसके आठवें गर्भसे मेरा यह (ज््याम) केज् अवतार छेगा
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.8958)
- **Original**: और इस प्रकार यहाँ अबवार ठेकर यह कालनेमिके अवतार कंसका ब् करेगा ।' ऐसा कहकर ओऔ्रीहरि अन्तर्धान हो गये
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.8959)
- **Original**: हे महासुने ! भगवानके अदृश्य हो जानेपर उन्हें प्रघाम करके देवगण सुमेरुषर्ततपर चले गये और फिर पुृथिवीपर अयतीर्ण हुए
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.8960)
- **Original**: डुसी समय भगवान्‌ नारदजीने कैससे आकर वहा कि देवकौके आठवें गर्भमें भगवान्‌ धरणीघर जन्म लेंगे
- **Translation**: 

---

