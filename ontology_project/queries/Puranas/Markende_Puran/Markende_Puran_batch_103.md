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

### Verse 1 (Markende Puran 0.2041)
- **Original**: घोड़ेपर सवार हो वहाँसे अकेले ही एक घने उन प्रबल शत्रुओंने उस समय महाधाग राजा कल अली 80 आ ट सुरथपर आक्रमण कर दिबा
- **Translation**: 

---

### Verse 2 (Markende Puran 0.2042)
- **Original**: अपार्लर्बलिभिर्दृष्टेदुर्बलस्थ दुरात्मभि:
- **Translation**: 

---

### Verse 3 (Markende Puran 0.2043)
- **Original**: कोशो बल ज्ञापट्ठतं तम्नापि स्थपुरे त्तः
- **Translation**: 

---

### Verse 4 (Markende Puran 0.2044)
- **Original**: ततो मृगयात्याजेन हइतस्वाम्ब: स भूपति:। एकाकी हब्रमारुझ जगाप्त गहन॑ जनम्‌
- **Translation**: 

---

### Verse 5 (Markende Puran 0.2045)
- **Original**: स्‌ तत्राश्मममद्राक्षीद्‌ द्विजवर्यस्थ मेश्वसः। प्रशान्तश्रापदाकीर्ण मुनिशिष्योपशोभितम्‌
- **Translation**: 

---

### Verse 6 (Markende Puran 0.2046)
- **Original**: तस्थौ कंचिल्म काल॑ च मुनिना त्तेन सत्कृत: । इतप्लतश्न विन्नरंस्तस्मिन्मुनिवरा भ्रमे
- **Translation**: 

---

### Verse 7 (Markende Puran 0.2047)
- **Original**: सो5चिन्तयन्नदा त्तत्र ममत्याकृषचेतन:
- **Translation**: 

---

### Verse 8 (Markende Puran 0.2048)
- **Original**: म्रत्पूर्व: पालितं पूर्च म्या ही पुरं हि तत्‌
- **Translation**: 

---

### Verse 9 (Markende Puran 0.2049)
- **Original**: मदभूर्त्वस्तैरसट्यूसैध॑र्मत: पाल्यतते न वा। न॑ जाते स॑ प्रधानों में शूरहस्ती सदामदः
- **Translation**: 

---

### Verse 10 (Markende Puran 0.2050)
- **Original**: मष्त वैरिवशं यात्र: कान्‌ भोगानुपलफ्यते। - ये भमानुगता निर्त्य प्रसादभनभोजने:
- **Translation**: 

---

### Verse 11 (Markende Puran 0.2051)
- **Original**: जजजलमें चले गये
- **Translation**: 

---

### Verse 12 (Markende Puran 0.2052)
- **Original**: वहाँ उन्होंने विप्रवर मेथा अनुबूर्त्ति ध्रुवं तेठड्य कुब॑नत्बन्यमहीभूताम्‌। मुनिका आश्रम देखा, जहाँ कितने ही हिंसक जीव असप्यग्व्ययशीलैस्त: कुर्बद्ध: सतर्त व्ययम्‌
- **Translation**: 

---

### Verse 13 (Markende Puran 0.2053)
- **Original**: [ अपनी स्वाभाविक हिंसावृत्ति छोड़कर] परम संचित: सो5तिदु:खेन क्षयं कोशो गपिष्यति। शात्तभावसे रहते थे। मुनिके बहुत-से शिष्य उस एतच्चान्चच्य सततं चिन्तबामास्र पार्थिव:
- **Translation**: 

---

### Verse 14 (Markende Puran 0.2054)
- **Original**: वंनकी शोभा चढ़ा रहे थै
- **Translation**: 

---

### Verse 15 (Markende Puran 0.2055)
- **Original**: वहाँ जानेपर तब विप्राश्रमाध्याशे वैश्यपेक छुदर्श सः। मुतिने उनका सत्कार क्रिया और ते उन मुनिश्रेष्ठके स पृष्टस्तेन कस भो हेतुआणमने5त्र कः
- **Translation**: 

---

### Verse 16 (Markende Puran 0.2056)
- **Original**: आशन्रपपर इधर उधर चिचरते हुए कुछ कालतक सशोक इब कस्मान्ष्वं दुर्मना इव लक्ष्यसे
- **Translation**: 

---

### Verse 17 (Markende Puran 0.2057)
- **Original**: वहाँ रहे
- **Translation**: 

---

### Verse 18 (Markende Puran 0.2058)
- **Original**: फिर ममतासे आकृष्टचित्त होकर इत्याक्र्ण्य ब्रचस्तस्य भूपते: प्रणयोदितम्‌
- **Translation**: 

---

### Verse 19 (Markende Puran 0.2059)
- **Original**: उस आश्रमर्में इस प्रकार चिन्ता करने लगे-- 6, पाटान्तर--मर/एयाकुशटानस; ।
- **Translation**: 

---

### Verse 20 (Markende Puran 0.2060)
- **Original**: +मसशा अस्तंपका ता सुरक्ष और समराप्मिक्ों भगवतीकी सहिसा स़ुलाता + 179 ###520 5543 5558. 6:755 55542 8 9 75723:5647 #* 22556 "05:22 :5## 17186 87 रु 7:2556#6#/* 33566 #&7 *चूर्वकालमें मेंरे पूर्वजोंने जिसका पालन किया था,
- **Translation**: 

---

