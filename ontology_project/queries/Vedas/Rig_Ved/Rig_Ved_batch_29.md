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

### Verse 1 (Rig Ved 0.561)
- **Original**: हे जल समृह ! जीवन रक्षक ओषधियों को हमारे शरीर में स्थित करें, जिससे हम नीरोग होकर चिरकाल तक सूर्यदेव का दर्शन करते रहें
- **Translation**: 

---

### Verse 2 (Rig Ved 0.562)
- **Original**: 251. डदमाप: प्र बहत यत्कि च दुरितं मयि। यद्वाहमभिदुद्रोह यद्वा शेप उतानृतम्‌
- **Translation**: 

---

### Verse 3 (Rig Ved 0.563)
- **Original**: है जल देवो ! हम थाजकों ने अज्ञानवश जो दुष्कृत्य किये हों, जान- बूझकर किसी से द्रोह किया हो, सत्पुरुषों पर आक्रोश किया हो या असत्य आचरण किया हो तथा इस प्रकार के हमारे जो भी दोष हों, उन सबको बहाकर टूर करें
- **Translation**: 

---

### Verse 4 (Rig Ved 0.564)
- **Original**: 252. आपो अद्यान्वचारिषं रसेन समगस्महि। पयस्वानग्न आ गहि त॑ मा सं सृज वर्चसा
- **Translation**: 

---

### Verse 5 (Rig Ved 0.565)
- **Original**: आज हमने जल में प्रविष्ट होकर अवभृथ स्नान किया है, इस प्रकार जल में प्रवेश करके हम रस से 'आप्लावित हुए हैं। हे पयस्वान्‌ ! हे अग्निदेव ! आप हमें वर्वस्वी बनाएँ, हम आपका स्वागत करते हैं
- **Translation**: 

---

### Verse 6 (Rig Ved 0.566)
- **Original**: 253. स॑ मारने वर्चसा सृज सं प्रजया समायुषा
- **Translation**: 

---

### Verse 7 (Rig Ved 0.567)
- **Original**: बिद्युमें अस्य देवा इन्द्रो विद्यात्सह ऋषिभि:
- **Translation**: 

---

### Verse 8 (Rig Ved 0.568)
- **Original**: है अग्निदेव ! आप हमें तेजस्विता प्रदान करें । हमें प्रजा और दीर्घ आयु से युक्त करें । देवगण हमारे अनुष्ठान को जानें और इन्द्रदेव ऋषियों के साथ इसे जानें
- **Translation**: 

---

### Verse 9 (Rig Ved 0.569)
- **Original**: मै0 है सू0 रेड 29 [ सूक्त - 24 ] (ऋषि-शुन:शेप आजीगर्ति (कृत्रिम देवरात वैश्वामित्र)
- **Translation**: 

---

### Verse 10 (Rig Ved 0.570)
- **Original**: देवता-1 क (प्रजापति) 2 अग्नि, 3-4 सविता, 5 सविता अथवा भग, 6-15 वरुण
- **Translation**: 

---

### Verse 11 (Rig Ved 0.571)
- **Original**: छद- 1,2.6-15 त्रिष्टपु, 3-5 गायत्री
- **Translation**: 

---

### Verse 12 (Rig Ved 0.572)
- **Original**: ] 254. कस्य नून॑ कतमस्यामृतानां मनामहे चारु देवस्य नाम । को नो मह्या अदितये पुनर्दात्पितरं च दृशेयं मातरं च
- **Translation**: 

---

### Verse 13 (Rig Ved 0.573)
- **Original**: हम अआपर देवों में से किस देव के सुन्दर नाम का स्मरण करें ? कौन से देव हमें मह॒ती अदिति - पृथिवी को प्राप्त करायेंगे ? जिससे हम अपने पिता और माता को देख सकेंगे
- **Translation**: 

---

### Verse 14 (Rig Ved 0.574)
- **Original**: 255, अमनेर्वयं प्रथमस्यामृतानां मनामहे चारु देवस्य नाम । स नो मह्या अदितये पुनर्दात्पितरं च दूशेयं मातरं च
- **Translation**: 

---

### Verse 15 (Rig Ved 0.575)
- **Original**: हम अमर देवों में प्रथम अग्निदेव के सुन्दर नाम का मनन करें । वह हमें महती अदिति को प्राप्त करायेंगे, जिससे हम अपने माता-पिता को देख सकेंगे
- **Translation**: 

---

### Verse 16 (Rig Ved 0.576)
- **Original**: 256, अभि त्वा देव सवितरीशान वार्याणाम्‌। सदावन्भागमीमहे
- **Translation**: 

---

### Verse 17 (Rig Ved 0.577)
- **Original**: है सर्वदा रक्षणशील सवितादेव ! आप वरण करने योग्य धर्नों के स्वामी है, अत: हम आपसे ऐश्वर्यों के उत्तम भाग को माँगते हैं
- **Translation**: 

---

### Verse 18 (Rig Ved 0.578)
- **Original**: 257. यश्चिद्धि त इृत्था भग: शशमान: पुरा निद:। अद्विषो हस्तयोर्टथे
- **Translation**: 

---

### Verse 19 (Rig Ved 0.579)
- **Original**: हे सवितादेव ! आप तेजस्विता युक्त, निन्‍्दा रहित, द्वेष रहित, वरण करने योग्य धनों को दोनों हाथों से धारण करने वाले हैं
- **Translation**: 

---

### Verse 20 (Rig Ved 0.580)
- **Original**: 258. भगभक्तस्य ते वयमुदशेम तवावसा। मूर्धानं राय आरभे
- **Translation**: 

---

