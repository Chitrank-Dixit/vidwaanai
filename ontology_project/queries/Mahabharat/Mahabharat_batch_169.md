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

### Verse 1 (Mahabharat 0.1681)
- **Original**: नाम सार्थक हुआ। देवताओंको तो वह सदा भयभीत किये छीन लिया। इससे रुष्ट होकर कुबेस्ने शाप दिया कि 'यह
- **Translation**: 

---

### Verse 2 (Mahabharat 0.1681)
- **Original**: नाम सार्थक हुआ। देवताओंको तो वह सदा भयभीत किये छीन लिया। इससे रुष्ट होकर कुबेस्ने शाप दिया कि 'यह
- **Translation**: 

---

### Verse 3 (Mahabharat 0.1682)
- **Original**: रहता था। क+-ह ++-- देवताओंका रीछ और वानर-योनिमें उत्पन्न होना मार्कप्डेयजी कहते हैं--सदनच्तर राबणसे कष्ट पाये हुए
- **Translation**: 

---

### Verse 4 (Mahabharat 0.1682)
- **Original**: रहता था। क+-ह ++-- देवताओंका रीछ और वानर-योनिमें उत्पन्न होना मार्कप्डेयजी कहते हैं--सदनच्तर राबणसे कष्ट पाये हुए
- **Translation**: 

---

### Verse 5 (Mahabharat 0.1683)
- **Original**: आप ही उसके भयसे हमारी रक्षा कीजिये।' ब्रह्मिि, देवर्षथि तथा सिद्ध॑णण अग्निदेवको आगे करके
- **Translation**: 

---

### Verse 6 (Mahabharat 0.1683)
- **Original**: आप ही उसके भयसे हमारी रक्षा कीजिये।' ब्रह्मिि, देवर्षथि तथा सिद्ध॑णण अग्निदेवको आगे करके
- **Translation**: 

---

### Verse 7 (Mahabharat 0.1684)
- **Original**: अह्यजीने कहा--'अश्ने ! देवता या असुर उसे युद्धमें नहीं ब्रह्माजीकी झरणमें गये। अग्निने कहा, 'भगवन्‌ ! आपने जो
- **Translation**: 

---

### Verse 8 (Mahabharat 0.1684)
- **Original**: अह्यजीने कहा--'अश्ने ! देवता या असुर उसे युद्धमें नहीं ब्रह्माजीकी झरणमें गये। अग्निने कहा, 'भगवन्‌ ! आपने जो
- **Translation**: 

---

### Verse 9 (Mahabharat 0.1685)
- **Original**: जीत सकते। इसके लिये जो कार्य आवश्यक था, वह मैंने कर पहले बस्दान देकर विश्रवाके पुत्र महाबली रावणको अवध्य
- **Translation**: 

---

### Verse 10 (Mahabharat 0.1685)
- **Original**: जीत सकते। इसके लिये जो कार्य आवश्यक था, वह मैंने कर पहले बस्दान देकर विश्रवाके पुत्र महाबली रावणको अवध्य
- **Translation**: 

---

### Verse 11 (Mahabharat 0.1686)
- **Original**: दिया है; अब झीप्र ही उसका दमन हो जायगा। मैंने चतुर्भुज कर दिया है, वह अब संसारकी समस्त प्रजाको सता रहा है;
- **Translation**: 

---

### Verse 12 (Mahabharat 0.1686)
- **Original**: दिया है; अब झीप्र ही उसका दमन हो जायगा। मैंने चतुर्भुज कर दिया है, वह अब संसारकी समस्त प्रजाको सता रहा है;
- **Translation**: 

---

### Verse 13 (Mahabharat 0.1687)
- **Original**: भगवान्‌ विष्णुसे अनुरोध किया था, वे मेरी प्रार्थनासे संसारमें ,
- **Translation**: 

---

### Verse 14 (Mahabharat 0.1687)
- **Original**: भगवान्‌ विष्णुसे अनुरोध किया था, वे मेरी प्रार्थनासे संसारमें ,
- **Translation**: 

---

### Verse 15 (Mahabharat 0.1688)
- **Original**: 364 संक्षित्त महाभारत [ बनपर्च अबतार ले चुके हैं। वे ही रावणके दमनका कार्य॑ करेंगे।'
- **Translation**: 

---

### Verse 16 (Mahabharat 0.1688)
- **Original**: 364 संक्षित्त महाभारत [ बनपर्च अबतार ले चुके हैं। वे ही रावणके दमनका कार्य॑ करेंगे।'
- **Translation**: 

---

### Verse 17 (Mahabharat 0.1689)
- **Original**: देवताओंने भी अवतीर्ण होकर रीछ और वानरोंकी ख्त्रियोमें पुत्र फिर इञ्रको लक्ष्य करके कहा, 'इच्ध ! तुम भी सब
- **Translation**: 

---

### Verse 18 (Mahabharat 0.1689)
- **Original**: देवताओंने भी अवतीर्ण होकर रीछ और वानरोंकी ख्त्रियोमें पुत्र फिर इञ्रको लक्ष्य करके कहा, 'इच्ध ! तुम भी सब
- **Translation**: 

---

### Verse 19 (Mahabharat 0.1690)
- **Original**: उत्पन्न किये। वे सब वानर और रीछ यज्ञ तथा बरूसें अपने देवताओंके साथ पृथ्वीपर रीछ और वानरोंके रूपमें जन्म लो
- **Translation**: 

---

### Verse 20 (Mahabharat 0.1690)
- **Original**: उत्पन्न किये। वे सब वानर और रीछ यज्ञ तथा बरूसें अपने देवताओंके साथ पृथ्वीपर रीछ और वानरोंके रूपमें जन्म लो
- **Translation**: 

---

