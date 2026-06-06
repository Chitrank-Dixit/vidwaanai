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

### Verse 1 (Mahabharat 0.4941)
- **Original**: समय देवतालोग येरा एक ही काम सिद्ध कर दें; जैसे यक़ें बढ़ते चले आ रहे हैं ये अपने हैं या शहुओंके ? इसकी
- **Translation**: 

---

### Verse 2 (Mahabharat 0.4941)
- **Original**: समय देवतालोग येरा एक ही काम सिद्ध कर दें; जैसे यक़ें बढ़ते चले आ रहे हैं ये अपने हैं या शहुओंके ? इसकी
- **Translation**: 

---

### Verse 3 (Mahabharat 0.4942)
- **Original**: आवाहन करते ही इन्र आ पहुँचते हैं; उसी प्रकार अर्जुन भी पहचान कर लेना। युद्ध करते समये मुझे अपने-परायेका
- **Translation**: 

---

### Verse 4 (Mahabharat 0.4942)
- **Original**: आवाहन करते ही इन्र आ पहुँचते हैं; उसी प्रकार अर्जुन भी पहचान कर लेना। युद्ध करते समये मुझे अपने-परायेका
- **Translation**: 

---

### Verse 5 (Mahabharat 0.4943)
- **Original**: यहाँ आ जायें। विज्ञोक ! इस छिल्न-भिन्न होती ह.: ज्ञान नहीं रहता। कहीं ऐसा न हो कि अपनी ही सेनाको
- **Translation**: 

---

### Verse 6 (Mahabharat 0.4943)
- **Original**: यहाँ आ जायें। विज्ञोक ! इस छिल्न-भिन्न होती ह.: ज्ञान नहीं रहता। कहीं ऐसा न हो कि अपनी ही सेनाको
- **Translation**: 

---

### Verse 7 (Mahabharat 0.4944)
- **Original**: कौरब-सेनाकी ओर तो दृष्टि डाल, ये राजालोग क्यों भाग बाणोंसे आच्छादित कर डालूँ। विज्ञोक ! राजा युधिष्टिर
- **Translation**: 

---

### Verse 8 (Mahabharat 0.4944)
- **Original**: कौरब-सेनाकी ओर तो दृष्टि डाल, ये राजालोग क्यों भाग बाणोंसे आच्छादित कर डालूँ। विज्ञोक ! राजा युधिष्टिर
- **Translation**: 

---

### Verse 9 (Mahabharat 0.4945)
- **Original**: रहे हैं? मुझे तो स्पष्ट जान पड़ता है कि नस्प्रेष्ठ अजुन बाणोंके प्रह्रसे बहुत घबराये हुए हैं। इधर, अर्जुन उन्हें देखने
- **Translation**: 

---

### Verse 10 (Mahabharat 0.4945)
- **Original**: रहे हैं? मुझे तो स्पष्ट जान पड़ता है कि नस्प्रेष्ठ अजुन बाणोंके प्रह्रसे बहुत घबराये हुए हैं। इधर, अर्जुन उन्हें देखने
- **Translation**: 

---

### Verse 11 (Mahabharat 0.4946)
- **Original**: यहाँ आ पहुँचे, वे ही अपने बाणोंसे सम्पूर्ण सेनाको गये थे, सो अभीतक नहीं ल्लौटे। पता नहीं, राजा अबतक
- **Translation**: 

---

### Verse 12 (Mahabharat 0.4946)
- **Original**: यहाँ आ पहुँचे, वे ही अपने बाणोंसे सम्पूर्ण सेनाको गये थे, सो अभीतक नहीं ल्लौटे। पता नहीं, राजा अबतक
- **Translation**: 

---

### Verse 13 (Mahabharat 0.4947)
- **Original**: आच्छादित कर रहे हैं। कौरवॉपर मोह छा गया है, जीवित हैं या नहीं ? अर्जुनका भी समाचार नहीं मिला।
- **Translation**: 

---

### Verse 14 (Mahabharat 0.4947)
- **Original**: आच्छादित कर रहे हैं। कौरवॉपर मोह छा गया है, जीवित हैं या नहीं ? अर्जुनका भी समाचार नहीं मिला।
- **Translation**: 

---

### Verse 15 (Mahabharat 0.4948)
- **Original**: सब-के-सब भाग रहे हैं। रणमें हाहाकार मचा है। हाथी बढ़े इससे मुझे बड़ा खेद हो रहा है तो भी मैं झान्रुओंकी प्रचण्ड
- **Translation**: 

---

### Verse 16 (Mahabharat 0.4948)
- **Original**: सब-के-सब भाग रहे हैं। रणमें हाहाकार मचा है। हाथी बढ़े इससे मुझे बड़ा खेद हो रहा है तो भी मैं झान्रुओंकी प्रचण्ड
- **Translation**: 

---

### Verse 17 (Mahabharat 0.4949)
- **Original**: जोरोंसे चिग्घाड़ रहे हैं। सेनाका संहार करूँगा। तू मेरे रक्षपर रखे हुए सभी
- **Translation**: 

---

### Verse 18 (Mahabharat 0.4949)
- **Original**: जोरोंसे चिग्घाड़ रहे हैं। सेनाका संहार करूँगा। तू मेरे रक्षपर रखे हुए सभी
- **Translation**: 

---

### Verse 19 (Mahabharat 0.4950)
- **Original**: . विश्लोकने कहा--कुमार भीमसेन/! :क्रोधमें भरे हुए तस्कसोंकी जाँच कर ले, अब उसमें कितने बाण बाकी रह
- **Translation**: 

---

### Verse 20 (Mahabharat 0.4950)
- **Original**: . विश्लोकने कहा--कुमार भीमसेन/! :क्रोधमें भरे हुए तस्कसोंकी जाँच कर ले, अब उसमें कितने बाण बाकी रह
- **Translation**: 

---

