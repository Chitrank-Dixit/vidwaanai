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

### Verse 1 (Markende Puran 0.3481)
- **Original**: 37 एभिस्तबैश्व मो नित्य स्तौघ्यते थः सपाहितः। तस्माहे सकलां बाधां नाश विध्याम्ययंशयम
- **Translation**: 

---

### Verse 2 (Markende Puran 0.3482)
- **Original**: 1. धा0-शम0। प्रभुकैटभनाश॑ च॑ पगहिपासुरणातनप्‌। क्रीत॑सिष्सन्ति ये तद्धद वध शुम्भनिशुष्भयों)
- **Translation**: 

---

### Verse 3 (Markende Puran 0.3483)
- **Original**: अएम्यां च॒ चतुर्देश्यां नवम्यां अकचेतस:। श्रोष्यन्ति जैस ये भक्‍त्या मम माहात्म्यमुत्तमम्‌
- **Translation**: 

---

### Verse 4 (Markende Puran 0.3484)
- **Original**: न तरेषां दुष्कृत करिस्लिद्‌ दुष्कृतोत्था न चापदः। भविष्यति न क््रिद्ध्॑ न चैवेष्टवियोजनम्‌
- **Translation**: 

---

### Verse 5 (Markende Puran 0.3485)
- **Original**: ज़त्रुतों न भय॑ त्स्य दस्युतों खा न साजत:। न शस्बानलतोबाघात्कदाचित्सप्भ्रविष्पति
- **Translation**: 

---

### Verse 6 (Markende Puran 0.3486)
- **Original**: 6 # तस्मान्मपैतन्माहात्य्य॑पठितव्य॑ सपाहिते:। ओतर्ये चर सदा भक्‍्त्या परे स्वस्त्पपन॑ हि ततू
- **Translation**: 

---

### Verse 7 (Markende Puran 0.3487)
- **Original**: उपसर्गानशेफंस्तु.._ महामारीसमुद्धवानू। तथा त्रित्िधमुत्पातं माहात्म्य॑ शमग्रेन्मम
- **Translation**: 

---

### Verse 8 (Markende Puran 0.3488)
- **Original**: यजैतत्पठयते समप्यड्नित्यपायतने मघ। सदा न तद्विपोधयापि सांनिध्य तत्न मे स्थितप्‌े
- **Translation**: 

---

### Verse 9 (Markende Puran 0.3489)
- **Original**: बलिपफ्रदाने पूजायामग्रिकार्य महोत्सवे। सर्व मर्मतव्यरित्मुच्याय अ्राव्यमेव ह्ञ।
- **Translation**: 

---

### Verse 10 (Markende Puran 0.3490)
- **Original**: 238 * संक्षत्त मार्कप्डयपुराण #768&5:4462::2:5%:5- 00008 0754 #54 3 6664ज+घ 2 शकतश्रप तक लश्ञ लक्षप अध 24 280886:523 23555 %5454464 4 #
- **Translation**: 

---

### Verse 11 (Markende Puran 0.3491)
- **Original**: 37.88 जानता$जानता वापि बलिपूजां तथा कृताम्‌। प्रसीक्षिाष्यर प्रीत्या बहिहोम॑ तथा कृताम्‌
- **Translation**: 

---

### Verse 12 (Markende Puran 0.3492)
- **Original**: शरत्काले महापूजा क्रियते या च सार्पिकी। तस्यां ममैतस्माहात्म्यं श्रुल्ता भक्तिसमन्वित:
- **Translation**: 

---

### Verse 13 (Markende Puran 0.3493)
- **Original**: ; फतत्सु चापि शस्वेषु संग्रामे भुशदारूणे। सर्वाजायाविनिर्म॒क्तो धनधान्यसुतान्वित:
- **Translation**: 

---

### Verse 14 (Markende Puran 0.3494)
- **Original**: प्रचुष्यो मत्यसादेन भविष्यति न संशय;
- **Translation**: 

---

### Verse 15 (Markende Puran 0.3495)
- **Original**: श्रुत्रा ममैतन्माहात्म्यं तशा चोत्पत्तय: शुभा:। पंराक्रपं च॑ युद्धेषु जायते निर्भयः पुमान्‌
- **Translation**: 

---

### Verse 16 (Markende Puran 0.3496)
- **Original**: रिपच: संक्षत्ं यान्ति कल्याणं चोपपद्चते। नन्दते च कुल पुंसां माहात्म्यं मम श्रृण्पत्तामू
- **Translation**: 

---

### Verse 17 (Markende Puran 0.3497)
- **Original**: शान्तिकर्मणि सर्वत्र तथा दुःस्थप्रदर्शने। ग्रहपीडास चोग्रासु माहात्य॑ थ्रूणुयान्यम
- **Translation**: 

---

### Verse 18 (Markende Puran 0.3498)
- **Original**: 98 छ उपसर्गा; ज्षमं यान्ति ग्रहपीडाक्ष दारुणा:। दुःस्वप्रं च॒ जुभिदंध सुसम्यप्रमुपजावते
- **Translation**: 

---

### Verse 19 (Markende Puran 0.3499)
- **Original**: बलग्रहाभिभूत्तानां बालानां शानिकारकम्‌
- **Translation**: 

---

### Verse 20 (Markende Puran 0.3500)
- **Original**: संघातभेदें चर नृणां मैत्रीकरणमुन्तमम्‌
- **Translation**: 

---

