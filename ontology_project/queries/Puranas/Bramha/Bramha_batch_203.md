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

### Verse 1 (Bramha 0.4041)
- **Original**: अपना वरद हाथ रखिये। हो। परमात्मन्‌! आपको नमस्कार है। मुक्तिदाता!
- **Translation**: 

---

### Verse 2 (Bramha 0.4042)
- **Original**: समस्त कामनाओंको पूर्ण करनेवाले शद्भु- आपकी जय हो। आप ही मुक्ति हैं। भोग प्रदान
- **Translation**: 

---

### Verse 3 (Bramha 0.4043)
- **Original**: चक्र-गदाधर भगवान्‌ विष्णुने इस प्रकार स्तुति करनेवाले केशव! आपकी जय हो। लोकप्रद
- **Translation**: 

---

### Verse 4 (Bramha 0.4044)
- **Original**: करनेवाले धन्वन्तरिसे वर माँगनेको कहा। तब परमे7र! आपकी जय हो। पापोंका नाश करनेवाले
- **Translation**: 

---

### Verse 5 (Bramha 0.4045)
- **Original**: राजाने विनीत होकर कहा--'मैं देवताओंका राजा लोके श्वर! आपकी जय हो। भक्तवत्सल! आपकी
- **Translation**: 

---

### Verse 6 (Bramha 0.4046)
- **Original**: होना चाहता हूँ।' “तथास्तु' कहकर भगवान्‌ जय हो, जय हो। चक्र धारण करनेवाले परमेश्वर ' वहाँसे अन्तर्धान हो गये और राजा धन्वन्तरिने आपको प्रणाम हैं। मानदाता! आपकी जय हो।
- **Translation**: 

---

### Verse 7 (Bramha 0.4047)
- **Original**: क्रमश: उन्नति करते हुए देवेन्द्रपद प्रात किया। आप ही मान हैं। विश्ववन्दित देव! आपकी जय
- **Translation**: 

---

### Verse 8 (Bramha 0.4048)
- **Original**: पूर्वजन्ममें किये हुए अनेक कर्मोंके परिणामबश हो। धर्मदाता! आपको जय हो। आप धर्मस्वरूप ' इन्द्रको तीन यार अपने पदसे भ्रष्ट होना पड़ा। हैं। संसारसे पार लगानेवाले परमात्मन्‌! आपको
- **Translation**: 

---

### Verse 9 (Bramha 0.4049)
- **Original**: वृत्रासुरका वध होनेपर नहुषके द्वारा इन्द्रका पद
- **Translation**: 

---

### Verse 10 (Bramha 0.4050)
- **Original**: 200 * संक्षिप्त ब्रह्मपुराण « छीना गया। इसके बाद इद्धने सिन्धुसेनकी हत्या
- **Translation**: 

---

### Verse 11 (Bramha 0.4051)
- **Original**: कार्यकी सिद्धि नहीं होती। अपना धर्म पूर्ण न कर डालो। अत: उस पापसे भी उनके पदकी
- **Translation**: 

---

### Verse 12 (Bramha 0.4052)
- **Original**: होनेपर कौन-सा अनिष्ट नहीं होता।' यों हानि हुई। तीसरी बार अहल्याके साथ समागम
- **Translation**: 

---

### Verse 13 (Bramha 0.4053)
- **Original**: कहकर मैंने उनके पूर्वजन्मका वृत्तान्त भी करनेके कारण तथा अन्य कारणोंसे भी उन्हें
- **Translation**: 

---

### Verse 14 (Bramha 0.4054)
- **Original**: बतलाया। “पूर्वजन्ममें इन्द्र राजा आयुके पुत्र पदष्रष्ट होना पड़ा। इन्द्र उन बातोंको याद करके
- **Translation**: 

---

### Verse 15 (Bramha 0.4055)
- **Original**: धन्वन्तरि थे। उनकी तपस्यामें तम नामक राक्षसने चिन्ताजनित संतापसे उदास रहा करते थे। तदनन्तर
- **Translation**: 

---

### Verse 16 (Bramha 0.4056)
- **Original**: विध्न डाल दिया, फिर भगबान्‌ विष्णुने उस एक दिन उन्होंने बृहस्पतिजीसे पूछा--'वागीश्वर।
- **Translation**: 

---

### Verse 17 (Bramha 0.4057)
- **Original**: बिध्तका निवारण किया। इस तरह इनके पूर्वजन्मोंमें क्या कारण है कि बीच-बीचमें मुझे अपने
- **Translation**: 

---

### Verse 18 (Bramha 0.4058)
- **Original**: ऐसे वृत्तान्त अनेक हो सकते हैं। उन्हींके फलसे राज्यसे भ्रष्ट होना पड़ता है? इस प्रकार पदभ्रष्ट
- **Translation**: 

---

### Verse 19 (Bramha 0.4059)
- **Original**: इन्हें कभी-कभी अपने राज्यसे वज्चित रहना होनेकी अपेक्षा तो निर्धन हो जाना ही अच्छा है।
- **Translation**: 

---

### Verse 20 (Bramha 0.4060)
- **Original**: पड़ता है।' कर्मोंकी गहन गतिकों कौन ठीक-ठौक जानता
- **Translation**: 

---

