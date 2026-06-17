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

### Verse 1 (Mahabharat 0.3991)
- **Original**: दिया था। अक्ति अर्जुनपर ही छोड़नेका निक्षय किया था तो अबतक
- **Translation**: 

---

### Verse 2 (Mahabharat 0.3991)
- **Original**: दिया था। अक्ति अर्जुनपर ही छोड़नेका निक्षय किया था तो अबतक
- **Translation**: 

---

### Verse 3 (Mahabharat 0.3992)
- **Original**: प्रतराष्ने कह्ा--सक्षय ! इसमें कर्ण;-दुर्योधनः और उनपर छोड़ी क्‍यों नहीं ? झकुनिका तथा सबसे अढ़कर तुम्हारा अन्याय है। तुप सब भगवान्‌ श्रीकृष्ण बोले--सुर्षोधन, दुःझासन, झकुनि और
- **Translation**: 

---

### Verse 4 (Mahabharat 0.3992)
- **Original**: प्रतराष्ने कह्ा--सक्षय ! इसमें कर्ण;-दुर्योधनः और उनपर छोड़ी क्‍यों नहीं ? झकुनिका तथा सबसे अढ़कर तुम्हारा अन्याय है। तुप सब भगवान्‌ श्रीकृष्ण बोले--सुर्षोधन, दुःझासन, झकुनि और
- **Translation**: 

---

### Verse 5 (Mahabharat 0.3993)
- **Original**: ल्ओेगोंको मालूप था कि वह झक्ति केवछ एक बीसकोःमार जयद्रथ--ये सब मिलकर यही सलाह दिया कस्ते थे कि
- **Translation**: 

---

### Verse 6 (Mahabharat 0.3993)
- **Original**: ल्ओेगोंको मालूप था कि वह झक्ति केवछ एक बीसकोःमार जयद्रथ--ये सब मिलकर यही सलाह दिया कस्ते थे कि
- **Translation**: 

---

### Verse 7 (Mahabharat 0.3994)
- **Original**: सकती है, इन्द्र आदि देवता भी उस्तकी चोट बरदाइत नहीं कर “कर्ण ! तुम अर्जुनके सिवा दूसरे किसीपर झक्तिका प्रयोग न
- **Translation**: 

---

### Verse 8 (Mahabharat 0.3994)
- **Original**: सकती है, इन्द्र आदि देवता भी उस्तकी चोट बरदाइत नहीं कर “कर्ण ! तुम अर्जुनके सिवा दूसरे किसीपर झक्तिका प्रयोग न
- **Translation**: 

---

### Verse 9 (Mahabharat 0.3995)
- **Original**: सकते । तो भी कर्णने उस्ते श्रीकृष्ण अथवा अर्जुनपर क्यों नहीं करना। उनके मारे जानेपर पाण्डकष और सृक्षय स्वयं ही नष्ट
- **Translation**: 

---

### Verse 10 (Mahabharat 0.3995)
- **Original**: सकते । तो भी कर्णने उस्ते श्रीकृष्ण अथवा अर्जुनपर क्यों नहीं करना। उनके मारे जानेपर पाण्डकष और सृक्षय स्वयं ही नष्ट
- **Translation**: 

---

### Verse 11 (Mahabharat 0.3996)
- **Original**: छोड़ा ? (तुमलोग युद्धके समय क्‍यों नहीं याद दिलाते/थे:23 हो जायैंगे।' युयुधान ! कर्ण भी उनसे ऐसा ही करनेकी
- **Translation**: 

---

### Verse 12 (Mahabharat 0.3996)
- **Original**: छोड़ा ? (तुमलोग युद्धके समय क्‍यों नहीं याद दिलाते/थे:23 हो जायैंगे।' युयुधान ! कर्ण भी उनसे ऐसा ही करनेकी
- **Translation**: 

---

### Verse 13 (Mahabharat 0.3997)
- **Original**: सञय बोले--भहाराज ! हमलोोग तो रोज ही: रातमें। उसे अ्तिज्ञा कर चुका था, उस्रके इृदयमें सदा अर्जुनके व्य
- **Translation**: 

---

### Verse 14 (Mahabharat 0.3997)
- **Original**: सञय बोले--भहाराज ! हमलोोग तो रोज ही: रातमें। उसे अ्तिज्ञा कर चुका था, उस्रके इृदयमें सदा अर्जुनके व्य
- **Translation**: 

---

### Verse 15 (Mahabharat 0.3998)
- **Original**: ऐसा करनेकी सरूाह देते थे, पर आतःकाल होते: ही देवलश करनेका विचार रहा भी कर्ता था, परंतु मैं ही उसे मोहमें
- **Translation**: 

---

### Verse 16 (Mahabharat 0.3998)
- **Original**: ऐसा करनेकी सरूाह देते थे, पर आतःकाल होते: ही देवलश करनेका विचार रहा भी कर्ता था, परंतु मैं ही उसे मोहमें
- **Translation**: 

---

### Verse 17 (Mahabharat 0.3999)
- **Original**: कर्णकी तथा दूसरे योद्धओंकी भी बुद्धि मारी जाती डाल देता था। यही कारण है, जिससे उसने अर्जुनपर
- **Translation**: 

---

### Verse 18 (Mahabharat 0.3999)
- **Original**: कर्णकी तथा दूसरे योद्धओंकी भी बुद्धि मारी जाती डाल देता था। यही कारण है, जिससे उसने अर्जुनपर
- **Translation**: 

---

### Verse 19 (Mahabharat 0.4000)
- **Original**: थी। हाथमें झक्तिके रहते हुए भी: जो उसने ओऔकृष्णा/या शक्तिका प्रहार नहीं किया। सात्पके ! वह झाक्ति अर्जुनके
- **Translation**: 

---

### Verse 20 (Mahabharat 0.4000)
- **Original**: थी। हाथमें झक्तिके रहते हुए भी: जो उसने ओऔकृष्णा/या शक्तिका प्रहार नहीं किया। सात्पके ! वह झाक्ति अर्जुनके
- **Translation**: 

---

