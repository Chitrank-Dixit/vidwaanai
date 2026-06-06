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

### Verse 1 (Agni Puran 0.6201)
- **Original**: उभयविपुलापूर्वक पुख-चपफ्लाका उदाहरण-- बिफुलाभिजातय॑शोद्धवापि रूपातिरिकरम्थापि । तिस्सार्यते गृहाद्‌ वललभाषि यदि भवाति मुखचफ्ला
- **Translation**: 

---

### Verse 2 (Agni Puran 0.6202)
- **Original**: 4. पथ्यापूर्वक जघनचपलाका उदाहरण -- यत्पादस्य कतिश्ठा 7 स्पृश्नति महीसतराभिका वाप । सा सर्व॑घूर्तओोग्या भवेदवश्य॑ जपतचपला
- **Translation**: 

---

### Verse 3 (Agni Puran 0.6203)
- **Original**: जघनचपलाका उदाहरण -- यस्या: पादाइगुष्ठ॑ व्यतीत्य याति प्रदेशिनी दीर्षा । बिपुले कुले प्रसूतापि सा ध्रुव॑ जपनचपला स्थात्‌
- **Translation**: 

---

### Verse 4 (Agni Puran 0.6204)
- **Original**: 'मकरध्वजसदनि दृश्यते स्फुट विलकलामएन॑ यस्या: । विपुलान्वयाभिजातापि जावते जघनचपलासौ
- **Translation**: 

---

### Verse 5 (Agni Puran 0.6205)
- **Original**: 5 विपुलापूर्वक महाचफ्लाका उदाहरण -- चध्यापूर्वक महाचफ्लाका उदाहरण-- हृदय हरान्ति तार्यो मुतेरापि भ्रृकराक्षविश्षेपै:। दोर्मुलवाभिदे्श निदर्शयसन्त्यो. महाचपला:
- **Translation**: 

---

### Verse 6 (Agni Puran 0.6206)
- **Original**: चिबुके कपोलदेशेउषि कृपिका दृश्य्ते स्मिते यस्या:। विपुलान्ययप्रसूतापि जायते सा महाचपला
- **Translation**: 

---

### Verse 7 (Agni Puran 0.6207)
- **Original**: पूर्वार्धक समान ही उत्तरार्ध भी हो, उसे “गीति"'
- **Translation**: 

---

### Verse 8 (Agni Puran 0.6208)
- **Original**: आठ गण हों तो “आर्यागीति" नामक छन्द होता नाम दिया गया है। तात्पर्य यह कि उसके
- **Translation**: 

---

### Verse 9 (Agni Puran 0.6209)
- **Original**: है। कोई विशेषता न होनेसे इसका उत्तरार्ध भी उत्तरार्धमें भी छठा गण मध्यगुरु (।5।) अथवा
- **Translation**: 

---

### Verse 10 (Agni Puran 0.6210)
- **Original**: ऐसा ही समझना चाहिये। यहाँ भी छठे गणमें सर्वलघु (।।।।) करना चाहिये। इसी प्रकार जहाँ
- **Translation**: 

---

### Verse 11 (Agni Puran 0.6211)
- **Original**: मध्यगुरु और सर्वलघु-इन दोनों विकल्पोंकी आर्याके उत्तरार्धके समान ही पूर्वार्थ भी हो, उसे
- **Translation**: 

---

### Verse 12 (Agni Puran 0.6212)
- **Original**: प्राप्ति थी, उसके स्थानमें केवल एक “लघु'का *उपगीति”' कहते हैं। आरयकि पूर्वोक्त क्रमको
- **Translation**: 

---

### Verse 13 (Agni Puran 0.6213)
- **Original**: विधान है
- **Translation**: 

---

### Verse 14 (Agni Puran 0.6214)
- **Original**: 9-10 ;ै
- **Translation**: 

---

### Verse 15 (Agni Puran 0.6215)
- **Original**: विपरीत कर देनेपर “उद्गीति"' नाम पड़ता है।। अब “मात्रा-उन्द” बतलाया जाता है। जहाँ सारांश यह कि उसमें पूर्वार्थको उत्तरार्धमें और
- **Translation**: 

---

### Verse 16 (Agni Puran 0.6216)
- **Original**: विषम, अर्थात्‌ प्रथम और तृतीय चरणमें चौदह उत्तरार्धको पूर्वार्धमें रखा जाता है। यदि पूर्वार्धमें
- **Translation**: 

---

### Verse 17 (Agni Puran 0.6217)
- **Original**: लघु (मात्राएँ) हों और सम--द्वितीय, चतुर्थ 1. पश्या-गीतिका उदाहरण -- अधुर॑ वीणारणित पकुमसुभगक्ष॒ कोकिलालाप: । गीति: पौरवधूनापधुता कुसुमायुधध॑ प्रबोधयति
- **Translation**: 

---

### Verse 18 (Agni Puran 0.6218)
- **Original**: आदिबिपुला-गीति -- इबमपरा खिपुला गीतिरुच्यते सर्वलोकहितहेतो:
- **Translation**: 

---

### Verse 19 (Agni Puran 0.6219)
- **Original**: यदनिष्टमात्मनस्तत्पोषु भवतापि मा क्षचित्‌ कारे
- **Translation**: 

---

### Verse 20 (Agni Puran 0.6220)
- **Original**: पथ्या महाचफ्ला-गीतिका उदाहरण -- कार्म चकास्ति गीतिमृंगीदृशां सौधुपातचपलानाम्‌। मुखं च मुक्तलण्ज॑ निरगलोल्लापमणितरमणीयम्‌ # महाविपुला-महाचफ्ला-गीतिका उदाहरण -- पद्केघुबल्लभ: पशञ्चमध्यनिस्तत्र भवति यदि विपुल:
- **Translation**: 

---

