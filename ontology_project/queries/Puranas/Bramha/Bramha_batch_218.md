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

### Verse 1 (Bramha 0.4341)
- **Original**: देवताओंके दूत हैं, उन आदिदेव भगवान्‌ अग्रिकी विरोधी होकर युद्ध करते रहे। दोनों ही अपने
- **Translation**: 

---

### Verse 2 (Bramha 0.4342)
- **Original**: मैं शरण लेती हूँ। जो शरीरके भीतर प्राणरूपमें पुत्र-पौत्रोंको साथ लेकर लड़ते थे। यह बलवान्‌
- **Translation**: 

---

### Verse 3 (Bramha 0.4343)
- **Original**: स्थित हैं और बाहर अन्नदातारूपमें विद्यमान हैं शत्रुओंके साथ बलवानोंका युद्ध था। उनमेंसे
- **Translation**: 

---

### Verse 4 (Bramha 0.4344)
- **Original**: तथा जो यज्ञके साधन हैं, उन धनंजय (अग्रिदेव)- उलूक अथवा कपोत-किसीकी भी जय-पराजय
- **Translation**: 

---

### Verse 5 (Bramha 0.4345)
- **Original**: की मैं शरण लेती हूँ।* नहीं होती थी। कपोतने यमराज तथा अपने
- **Translation**: 

---

### Verse 6 (Bramha 0.4346)
- **Original**: अग्रि बोले--पतिक्रते! मेरा यह अस्त्र अमोघ पितामह मृत्युकी आराधना करके याम्य-अस्त्र
- **Translation**: 

---

### Verse 7 (Bramha 0.4347)
- **Original**: है; अत: जिस लक्ष्यपर इसका विश्राम हो सके, प्रात्त किया, अत: वह सबसे अधिक शक्तिशाली
- **Translation**: 

---

### Verse 8 (Bramha 0.4348)
- **Original**: उसको बताओ। हो गया। इसी प्रकार उलूक भी अग्निकी आराधना
- **Translation**: 

---

### Verse 9 (Bramha 0.4349)
- **Original**: कपोतीने कहा--अग्निदेव! आपका अस्त्र करके अत्यन्त बलवान हो गया। वर पाकर दोनों
- **Translation**: 

---

### Verse 10 (Bramha 0.4350)
- **Original**: मुझपर ही विश्राम करे, मेरे पुत्र और पतिपर ही उन्मत्त हो गये थे, अत: फिर उनमें बड़ा
- **Translation**: 

---

### Verse 11 (Bramha 0.4351)
- **Original**: नहीं। मुझे मारकर आप सत्यवादी हों। आपको भंयकर युद्ध छिड़ गया। उसमें उलूकने कपोतके
- **Translation**: 

---

### Verse 12 (Bramha 0.4352)
- **Original**: नमस्कार है। ऊपर आग्रेय-अस्त्रका प्रहार किया। कपोतने भी
- **Translation**: 

---

### Verse 13 (Bramha 0.4353)
- **Original**: अग्रिदेवने कहा--पतिव्नते! तुम्हारे सुबचन उलूकपर यमपाश तथा यमदण्डका प्रयोग किया।
- **Translation**: 

---

### Verse 14 (Bramha 0.4354)
- **Original**: और पतिभक्तिसे मैं बहुत संतुष्ट हूँ। तुम्हारे स्वामी कपोतकी स्त्री हेति बड़ी पतिब्रता थी। उस
- **Translation**: 

---

### Verse 15 (Bramha 0.4355)
- **Original**: और पुत्नोंका अनिष्ट नहीं होगा। मैं उनकी रक्षाका महायुद्धमें अपने स्वामीके निकट अग्निको प्रण्यलित
- **Translation**: 

---

### Verse 16 (Bramha 0.4356)
- **Original**: वचन देता हूँ। यह मेरा आग्रेय-अस्त्र तुम्हारे देख वह दुःखसे विद्वल हो गयी। विशेषत:
- **Translation**: 

---

### Verse 17 (Bramha 0.4357)
- **Original**: पतिको, पुत्रोंकी तथा तुमको भी नहीं जलायेगा; पुत्रोंको अग्रिसे आबृत देख उसकी व्याकुलता
- **Translation**: 

---

### Verse 18 (Bramha 0.4358)
- **Original**: अत: तुम सुखपूर्वक लौट जाओ। * रूप॑ न दात॑ न परोक्षमस्ति यस्यात्मभू्त च पदार्थजातम्‌। अश्तन्ति हव्यानि च येन देवा: स्वाहापतिं यज्ञभुजं नमस्ये
- **Translation**: 

---

### Verse 19 (Bramha 0.4359)
- **Original**: मुखभू्त॑ च॒ देबानां देखानां हव्यवाहतम्‌ । होतारं चापि देयानां देवानां दूतमेव च
- **Translation**: 

---

### Verse 20 (Bramha 0.4360)
- **Original**: त॑ देवं शरणं याभि आदिदेब॑ विभावसुम्‌ । अन्तःस्थित: प्राणरूपो यहिश्षा्नप्रदो हि. य:
- **Translation**: 

---

