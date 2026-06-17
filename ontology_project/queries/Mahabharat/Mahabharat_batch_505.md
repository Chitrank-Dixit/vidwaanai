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

### Verse 1 (Mahabharat 0.5041)
- **Original**: घायल करते लगा। तब भीमसेनने क्रोधमें भरकर आपके जा पहुँचे। फिर तो झम्बरासुर और इक्के समान क्रोधमें भरे
- **Translation**: 

---

### Verse 2 (Mahabharat 0.5041)
- **Original**: घायल करते लगा। तब भीमसेनने क्रोधमें भरकर आपके जा पहुँचे। फिर तो झम्बरासुर और इक्के समान क्रोधमें भरे
- **Translation**: 

---

### Verse 3 (Mahabharat 0.5042)
- **Original**: पुत्रपर एक भयंकर झक्ति चलायी। उसे सहसा अपने ऊपर हुए उन दोनों बीरोंमें बड़ा भयंकर युद्ध छिड़ गया, दोनों ही
- **Translation**: 

---

### Verse 4 (Mahabharat 0.5042)
- **Original**: पुत्रपर एक भयंकर झक्ति चलायी। उसे सहसा अपने ऊपर हुए उन दोनों बीरोंमें बड़ा भयंकर युद्ध छिड़ गया, दोनों ही
- **Translation**: 

---

### Verse 5 (Mahabharat 0.5043)
- **Original**: आती देख आपके पुत्रने दस बाणोंसे काट डाला । उसके इस पणोंकी-बाजी लगाकर लड़ने लगे। इसी बीचमें भीमसेनने
- **Translation**: 

---

### Verse 6 (Mahabharat 0.5043)
- **Original**: आती देख आपके पुत्रने दस बाणोंसे काट डाला । उसके इस पणोंकी-बाजी लगाकर लड़ने लगे। इसी बीचमें भीमसेनने
- **Translation**: 

---

### Verse 7 (Mahabharat 0.5044)
- **Original**: दुष्कर कर्मको देख सभी सैनिक हर्षमें भरकर उसकी प्रशंसा अपनी फुर्ती दिखाते हुए दो क्षुगोंसे आपके पुत्रके धनुष और
- **Translation**: 

---

### Verse 8 (Mahabharat 0.5044)
- **Original**: दुष्कर कर्मको देख सभी सैनिक हर्षमें भरकर उसकी प्रशंसा अपनी फुर्ती दिखाते हुए दो क्षुगोंसे आपके पुत्रके धनुष और
- **Translation**: 

---

### Verse 9 (Mahabharat 0.5045)
- **Original**: करने लगे। परंतु भीमसेनका क्रोध और बढ़ गया। से ध्यूजाको...काट... डला, .. एक ...जाणसे... उसके .. ललाटवें
- **Translation**: 

---

### Verse 10 (Mahabharat 0.5045)
- **Original**: करने लगे। परंतु भीमसेनका क्रोध और बढ़ गया। से ध्यूजाको...काट... डला, .. एक ...जाणसे... उसके .. ललाटवें
- **Translation**: 

---

### Verse 11 (Mahabharat 0.5046)
- **Original**: उश्तकी ओर रोषधरी दृष्टिसे देख आगबबूला होकर कहने
- **Translation**: 

---

### Verse 12 (Mahabharat 0.5046)
- **Original**: उश्तकी ओर रोषधरी दृष्टिसे देख आगबबूला होकर कहने
- **Translation**: 

---

### Verse 13 (Mahabharat 0.5047)
- **Original**: छगे-- 'बीर दुः/झासन ! आज तूने तो मुझे बहुत घायल
- **Translation**: 

---

### Verse 14 (Mahabharat 0.5047)
- **Original**: छगे-- 'बीर दुः/झासन ! आज तूने तो मुझे बहुत घायल
- **Translation**: 

---

### Verse 15 (Mahabharat 0.5048)
- **Original**: किया, किंतु अब तू भी मेरी गदाका आघात सहन कर ।' यों
- **Translation**: 

---

### Verse 16 (Mahabharat 0.5048)
- **Original**: किया, किंतु अब तू भी मेरी गदाका आघात सहन कर ।' यों
- **Translation**: 

---

### Verse 17 (Mahabharat 0.5049)
- **Original**: कहकर उन्होंने दु/शासनका बध करनेके लिये अपनी भयंकर
- **Translation**: 

---

### Verse 18 (Mahabharat 0.5049)
- **Original**: कहकर उन्होंने दु/शासनका बध करनेके लिये अपनी भयंकर
- **Translation**: 

---

### Verse 19 (Mahabharat 0.5050)
- **Original**: गदा हाथमें ली और फिर कहा--दुरात्पन्‌! आज इस
- **Translation**: 

---

### Verse 20 (Mahabharat 0.5050)
- **Original**: गदा हाथमें ली और फिर कहा--दुरात्पन्‌! आज इस
- **Translation**: 

---

