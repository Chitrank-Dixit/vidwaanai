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

### Verse 1 (Bramha 0.2181)
- **Original**: तत्क्षमस्वापराध॑ मे यदि तेउस्ति दया मयि। कृतापराधे5पि हरे क्षमां कुर्यन्ति साधव:
- **Translation**: 

---

### Verse 2 (Bramha 0.2182)
- **Original**: तस्मात्बसीद देवेश भक्तस्नेह समाश्रित: । स्तुतोडउसि यनन्‍्मया देव भक्तिभावेन चेतसा
- **Translation**: 

---

### Verse 3 (Bramha 0.2183)
- **Original**: साज़ूं भबतु तत्सव॑ ब्रासुदेव नमोस्तु ते
- **Translation**: 

---

### Verse 4 (Bramha 0.2184)
- **Original**: 39-59)
- **Translation**: 

---

### Verse 5 (Bramha 0.2185)
- **Original**: 106 # संक्षिप्त बअह्मपुराण कर मूर्ख, कृतप्र, मानी, दुष्टबुद्धि तथा अभक्त मनुष्यको
- **Translation**: 

---

### Verse 6 (Bramha 0.2186)
- **Original**: नाश करनेवाले तथा परोंसे भी पर हैं। उनसे कभी इसका उपदेश न दे। जिसके हृदयमें भक्ति
- **Translation**: 

---

### Verse 7 (Bramha 0.2187)
- **Original**: भिन्न किसी भी बस्तुकी सत्ता नहीं है। वे हो, जो गुणवान्‌, शीलवान्‌, विष्णुभक्त, शान्त तथा
- **Translation**: 

---

### Verse 8 (Bramha 0.2188)
- **Original**: ही सबकी सृष्टि, पालन और संहार करनेवाले श्रद्धापूर्वक अनुष्ठान करनेवाला हो, उसीको इसका
- **Translation**: 

---

### Verse 9 (Bramha 0.2189)
- **Original**: हैं। वे ही समस्त संसारमें सारभूत हैं। मोक्ष- उपदेश देना चाहिये। सुख देनेवाले जगदुरु भगवान्‌ श्रीकृष्णमें यहाँ जो निर्मल हृदयबाले मनुष्य उन परम सूक्ष्म
- **Translation**: 

---

### Verse 10 (Bramha 0.2190)
- **Original**: जिनकी भक्ति नहीं होती, उन्हें विद्यासे, अपने नित्य पुराणपुरुष मुरारि श्रीविष्णुभगवान्‌का ध्यान ' गुणोंसे तथा यज्ञ, दान और कठोर तपस्यासे करते हैं, वे मुक्तिके भागी हो भगवान्‌ विष्णुमें
- **Translation**: 

---

### Verse 11 (Bramha 0.2191)
- **Original**: क्या लाभ हुआ। जिस पुरुषकी भगवान्‌ प्रवेश कर जाते हैं-ठीक उसी तरह, जैसे
- **Translation**: 

---

### Verse 12 (Bramha 0.2192)
- **Original**: पुरुषोत्तमके प्रति भक्ति है, वही संसारमें धन्य, मन्त्रोंद्ारा यज्ञाग्रिमें हवन किया हुआ हविष्य
- **Translation**: 

---

### Verse 13 (Bramha 0.2193)
- **Original**: पवित्र और विद्वान्‌ है। वही, यज्ञ, तपस्या और भगवान्‌ विष्णुकों प्राप्त होता है। एकमात्र वे गुणोंके कारण श्रेष्ठ है तथा यही ज्ञानी, दानी देवदेव भगवान्‌ विष्णु ही संसारके दुःखोंका
- **Translation**: 

---

### Verse 14 (Bramha 0.2194)
- **Original**: और सत्यवादी है।* 4] राजाको स्वप्रमें और प्रत्यक्ष भी भगवान्‌का दर्शन, भगवत्प्रतिमाओंका निर्माण, स्थापन और यात्राकी महिमा ब्रह्मजी कहते हैं--मुनिवरो ! इस प्रकार स्तुति
- **Translation**: 

---

### Verse 15 (Bramha 0.2195)
- **Original**: स्वप्रमें अपने शद्बु, चक्र और गदा धारण करनेवाले करके राजाने समस्त कामनाओंको पूर्ण करनेवाले
- **Translation**: 

---

### Verse 16 (Bramha 0.2196)
- **Original**: स्वरूपका दर्शन कराया। राजा इन्द्रुप्नने बड़े सनातन पुरुष जगन्नाथ भगवान्‌ वासुदेवको प्रणाम
- **Translation**: 

---

### Verse 17 (Bramha 0.2197)
- **Original**: प्रेमसे भगवान्‌का दर्शन किया। वे शद्भु और चक्र किया और चिन्तामग्र हो पृथ्वीपर कुश और वस्त्र
- **Translation**: 

---

### Verse 18 (Bramha 0.2198)
- **Original**: धारण किये हुए थे। उन्होंने शार्ड्र नामक धनुष बिछाकर भगवान्‌का चिन्तन करते हुए वे उसीपर
- **Translation**: 

---

### Verse 19 (Bramha 0.2199)
- **Original**: और बाण भी धारण कर रखे थे। उनका स्वरूप सो गये। सोते समय उनके मनमें यही संकल्प था
- **Translation**: 

---

### Verse 20 (Bramha 0.2200)
- **Original**: प्रलयकालीन सूर्यक समान देदीप्यमान हो रहा कि सबकी पीड़ा दूर करनेवाले देवाधिदेव भगवान्‌
- **Translation**: 

---

