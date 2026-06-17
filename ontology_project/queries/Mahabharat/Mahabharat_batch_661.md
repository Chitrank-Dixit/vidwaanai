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

### Verse 1 (Mahabharat 0.6601)
- **Original**: भुझे जो यह पाक्भौतिक मनुष्य-झरीर मिलता है, इसको जन्प महर्षि गौतम बनमें चले गये और चिर्कारी 'हाँ' करके भी
- **Translation**: 

---

### Verse 2 (Mahabharat 0.6601)
- **Original**: भुझे जो यह पाक्भौतिक मनुष्य-झरीर मिलता है, इसको जन्प महर्षि गौतम बनमें चले गये और चिर्कारी 'हाँ' करके भी
- **Translation**: 

---

### Verse 3 (Mahabharat 0.6602)
- **Original**: देनेवाली मेरी माता ही है। संसारके समस्त दुःखी जीवॉको अपने स्वभावके अनुसार बहुत देरतक उसपर विचार करता
- **Translation**: 

---

### Verse 4 (Mahabharat 0.6602)
- **Original**: देनेवाली मेरी माता ही है। संसारके समस्त दुःखी जीवॉको अपने स्वभावके अनुसार बहुत देरतक उसपर विचार करता
- **Translation**: 

---

### Verse 5 (Mahabharat 0.6603)
- **Original**: मातासे ही सान्वना मिलती है। जबतक माता जीवित रहती है, रहा। उसने सोचा--“क्या उपाय करूँ, जिससे पिताकी
- **Translation**: 

---

### Verse 6 (Mahabharat 0.6603)
- **Original**: मातासे ही सान्वना मिलती है। जबतक माता जीवित रहती है, रहा। उसने सोचा--“क्या उपाय करूँ, जिससे पिताकी
- **Translation**: 

---

### Verse 7 (Mahabharat 0.6604)
- **Original**: मनुष्य अपनेको सनाथ समझता है। उसके मरनेपर यह आज्ञाका पालन भी हो जाय और माताका वध भी न हो।
- **Translation**: 

---

### Verse 8 (Mahabharat 0.6604)
- **Original**: मनुष्य अपनेको सनाथ समझता है। उसके मरनेपर यह आज्ञाका पालन भी हो जाय और माताका वध भी न हो।
- **Translation**: 

---

### Verse 9 (Mahabharat 0.6605)
- **Original**: अनाथ-सा हो जाता है। पुत्र और पौत्रोंसे युक्त सौ बर्षका बुड़ढा धर्मके बहाने यह मुझपर बड़ा भारी संकट आ पड़ा । भला अन्य
- **Translation**: 

---

### Verse 10 (Mahabharat 0.6605)
- **Original**: अनाथ-सा हो जाता है। पुत्र और पौत्रोंसे युक्त सौ बर्षका बुड़ढा धर्मके बहाने यह मुझपर बड़ा भारी संकट आ पड़ा । भला अन्य
- **Translation**: 

---

### Verse 11 (Mahabharat 0.6606)
- **Original**: ही क्‍यों न हो, यदि उसकी माता जीवित हो तो बह उसके पास असाथु पुरुषोंकी भाँति मैं भी इसमें डूबनेका साहस कैसे
- **Translation**: 

---

### Verse 12 (Mahabharat 0.6606)
- **Original**: ही क्‍यों न हो, यदि उसकी माता जीवित हो तो बह उसके पास असाथु पुरुषोंकी भाँति मैं भी इसमें डूबनेका साहस कैसे
- **Translation**: 

---

### Verse 13 (Mahabharat 0.6607)
- **Original**: दो बर्षक बालकका-सा ही आनन्द उठाता है। बेटा समर्थ हो या करूँ ? पिताकी आज्ञाका पालन परम धर्म है, साथ ही
- **Translation**: 

---

### Verse 14 (Mahabharat 0.6607)
- **Original**: दो बर्षक बालकका-सा ही आनन्द उठाता है। बेटा समर्थ हो या करूँ ? पिताकी आज्ञाका पालन परम धर्म है, साथ ही
- **Translation**: 

---

### Verse 15 (Mahabharat 0.6608)
- **Original**: असमर्थ, हष्ट-पुष्ट हो या दुर्बल, माता हमेशा उसकी रक्षामें माताकी रक्षा करना भी अपना प्रधान थर्म है। पुत्र तो पिता
- **Translation**: 

---

### Verse 16 (Mahabharat 0.6608)
- **Original**: असमर्थ, हष्ट-पुष्ट हो या दुर्बल, माता हमेशा उसकी रक्षामें माताकी रक्षा करना भी अपना प्रधान थर्म है। पुत्र तो पिता
- **Translation**: 

---

### Verse 17 (Mahabharat 0.6609)
- **Original**: रहती है। माताके समान विधिपूर्वक पालन-पोषण करनेवारठा और माता दोनोंके अधीन होता है। अतः क्‍या करूँ, जिससे
- **Translation**: 

---

### Verse 18 (Mahabharat 0.6609)
- **Original**: रहती है। माताके समान विधिपूर्वक पालन-पोषण करनेवारठा और माता दोनोंके अधीन होता है। अतः क्‍या करूँ, जिससे
- **Translation**: 

---

### Verse 19 (Mahabharat 0.6610)
- **Original**: दूसरा कोई नहीं है। जब मातासे बिछोह हो जाता है, उस समय मेरा ही धर्म मुझे कहटमें न डाले। पिता स्वय॑ अपने झील,
- **Translation**: 

---

### Verse 20 (Mahabharat 0.6610)
- **Original**: दूसरा कोई नहीं है। जब मातासे बिछोह हो जाता है, उस समय मेरा ही धर्म मुझे कहटमें न डाले। पिता स्वय॑ अपने झील,
- **Translation**: 

---

