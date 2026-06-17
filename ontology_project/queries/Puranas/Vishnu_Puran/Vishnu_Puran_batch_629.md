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

### Verse 1 (Vishnu Puran 0.12561)
- **Original**: 9 तावुभावपि चैवास्तां विजिगीषू परस्परम्‌ । केशिध्वजेन. खाण्डिक्यस्स्वराज्यादबरोपित:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.12562)
- **Original**: 10 पुरोधसा मन्त्रिभिश्न समवेतो$ल्पसाधन: । राज्यात्रिराकृतस्सो5थ दुर्गारण्यचरो5भवत्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.12563)
- **Original**: 19 इयाज सो5पि सुबहन्यज्ञाउ्ानव्यपाश्रयः । ब्रह्मविद्यामधिष्ठायतर्त्तु मृत्युमविद्यया
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.12564)
- **Original**: 12 वि> पु 15--- अख़िल्वरधार परमेश्वरको देख सकूँगा उस योगको मैं जानना चाहता हूँ; उसका वर्णन कोजिये
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.12565)
- **Original**: श्रीपराहरजी बोले--पूर्वकालमें जिस प्रकार इस योगक्ा केशिध्बजने महात्या ख्नाण्डिक्य जनकसे वर्णन किया था मैं तुम्हें कही बतल्मता हूँ
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.12566)
- **Original**: श्रीमैत्रेयजी बोले--ब्रह्मनू ! यह खाप्डिक्य और विद्वान्‌ केशिध्वज कौन थे ? और उनका योगसम्बन्धी संयाद किस कारणसे हुआ था 2
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.12567)
- **Original**: श्रीपराक्षरजी बोलले--पूर्वकालमें धर्मध्वज जनक नामक एक राजा थे। उनके अमितध्वज और कृतध्वज नामक दो पुत्र हुए । इनमें कृतध्यज सर्वदा अध्यात्मशास्ममें रत रहता था
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.12568)
- **Original**: कृतध्यजका पुत्र केशिध्वज नामसे विख्यात हुआ और अमितध्वजका पुत्र खाप्डिक्य जनक हुआ
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.12569)
- **Original**: पृथिवीमण्डलमें खाप्डिक्य कर्म-मार्गमें अल्यक्त निपुण था और केहिध्वज अध्यात्पलिद्याका विशेषज्ञ था
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.12570)
- **Original**: बे दोगों परस्पर एक-दूसरेकों पराजित करनेकी चेष्टामें लगे रहते थे। अन्‍्तमें, काालक्रमसे केविध्वजने स्व्ाण्डिक्यक्यरे राज्यच्युत कर दिया
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.12571)
- **Original**: राज्यभ्रष्ट होनेपर खाण्डिक्य पुरोहित और मन्त्रियोंके सहित धोड़ी -सी सामग्री लेकर दुर्गम वनोमें चल्म गया
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.12572)
- **Original**: केशिध्वज ज्ञाननिष्ठ था तो भी अविद्या (कर्म) द्वारा मृत्युको पार करनेके लिये ज्ञानदृष्टि रखते हुए उसने अनेकों चज्ञॉक्व्र अनुष्ठान किया
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.12573)
- **Original**: डडड अविष्णुपुराण (अण्6 एकदा वर्तमानस्य यागे योगविदां बर। धर्मभ्ेनुं जघानोग्रहशार्दूल्ले विजने बने
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.12574)
- **Original**: 13 ततो राजा ह॒तां श्रुत्वा धेनुं व्याघ्रेण चर्त्चिज: । प्रायक्षित्त स पप्नच्छ किमत्रेति विधीयताम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.12575)
- **Original**: 14 तेथप्यूचुर्न बयं बिद्यः कशेरु: पृच्छघतामिति । कशेरुरपि तेनोक्तस्तथैव प्राह भार्गवम्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.12576)
- **Original**: 15 झशुनकं पृच्छ राजेन्द्र नाहं बेडि स वेत्स्यति । स गत्बा तमपृच्छन्च सो5प्याह श्रृणु यन्मुने
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.12577)
- **Original**: 16 न कशेसुर्न चैवाहं न चान्य: साम्प्रतं भुवि । वेत््येक एव त्वच्तत्रु: खाण्डिक्यो यो जितस्त्ववा
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.12578)
- **Original**: 17 स॒ चाह त॑ व्रजाम्येष प्रष्टमात्मरिपुं मुने। प्राप्त एवं महायज्ञों यदि मां स हनिष्यति
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.12579)
- **Original**: 18 प्रायक्चित्तमशेषेण स चेत्पृष्टो वदिष्यति। ततश्चाविकलो यागो मुनिश्रेष्ठ भविष्यति
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.12580)
- **Original**: 19 अऔपराजसर उवाच इत्युक्त्वा रथमारुद्दा कृष्णाजिनधरों नृपः । बन॑ जगाम यत्रास्ते स खाण्डिक्यो महामति:
- **Translation**: 

---

