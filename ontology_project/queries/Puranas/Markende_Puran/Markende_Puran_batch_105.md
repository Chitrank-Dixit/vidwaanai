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

### Verse 1 (Markende Puran 0.2081)
- **Original**: वहीं। इस समय घस्में वे कुशलसे रहते हैं अथवा उन्हें कोई कष्ट हैं ?#29--24
- **Translation**: 

---

### Verse 2 (Markende Puran 0.2082)
- **Original**: बे मेरे पुत्र कैसे हैं? क्या वे सदाचारी हैं अथवा दुराचारी हो गये हैं
- **Translation**: 

---

### Verse 3 (Markende Puran 0.2083)
- **Original**: साजोवाब
- **Translation**: 

---

### Verse 4 (Markende Puran 0.2084)
- **Original**: 26 2 चैर्निरस्तों भर्वाल्लुब्ीः पुतन्रदारादिधिर्धने:
- **Translation**: 

---

### Verse 5 (Markende Puran 0.2085)
- **Original**: तेषु कि भवतः स्नेहपनुबक्षाति मानसम्‌# 28
- **Translation**: 

---

### Verse 6 (Markende Puran 0.2086)
- **Original**: राजाने पूछा--
- **Translation**: 

---

### Verse 7 (Markende Puran 0.2087)
- **Original**: जिन लोभी स्त्री-पूत्र आंदिने धनके कारण तुम्हें चरसे निकाल दिया, उनके प्रत्ति तुम्होिर चित्तमें इतना स्नेह क्‍यों हैं 7
- **Translation**: 

---

### Verse 8 (Markende Puran 0.2088)
- **Original**: र7--+28
- **Translation**: 

---

### Verse 9 (Markende Puran 0.2089)
- **Original**: ब्ैश्व उकाच
- **Translation**: 

---

### Verse 10 (Markende Puran 0.2090)
- **Original**: 29 # एवमेतद्वांथा प्राह भवानस्मदगत॑ बच:
- **Translation**: 

---

### Verse 11 (Markende Puran 0.2091)
- **Original**: कि करोषि ने यश्चात्ति मम्त निप्ुरतां मनः। ये; संत्यज्य पितृस्नेह धनलुव्यैर्निराकृतः
- **Translation**: 

---

### Verse 12 (Markende Puran 0.2092)
- **Original**: 180 #ह 44 #4 44445 फशशफकफण >मण'ज 7 + लक 4 हह 68462 :2522::055000 744 8 ## 2 8 22/220432 95744 645 शत कणज पतिस्वजनहार्द नर हार्दि तेप्वेत्न पे मनः। किमेतन्नाभिजानामि जानम्नपि महामते
- **Translation**: 

---

### Verse 13 (Markende Puran 0.2093)
- **Original**: य्रत्पेमप्रतर्ण चित्त विगुणेष्वपि स्न्धुयु। तेषां कृते मे नि:श्नास्रो दौर्मचस्थं च जायते
- **Translation**: 

---

### Verse 14 (Markende Puran 0.2094)
- **Original**: करोपि कि बत्र मनस्तेष्वप्रीतियु निधुरम्‌
- **Translation**: 

---

### Verse 15 (Markende Puran 0.2095)
- **Original**: वैश्य बोलां--
- **Translation**: 

---

### Verse 16 (Markende Puran 0.2096)
- **Original**: आप मेरे त्रिषयमें जो थात कहते हैं, चह सब ठौक हैं
- **Translation**: 

---

### Verse 17 (Markende Puran 0.2097)
- **Original**: किंतु क्या करूँ, मेरा मन निष्व॒रता नहाँ भ्राएण करता। जिन्होंने धनके लोभमें पड़कर पिताके प्रति स्तेह,
- **Translation**: 

---

### Verse 18 (Markende Puran 0.2098)
- **Original**: पत्निके प्रैतिं प्रेम तथा आत्मोष जगके प्रति अनुरागको तिलाझञलि दे मुझे घरसे निकाल दिया है, उन्हींके ग्रति मेरे इदयमें इत्तना स्नेह है। महापते ! गुणहीन वन्धुओके प्रति भी जो मेरा चित्त इस प्रकार प्रेमपणन हो रहा हैं, यह क्‍या हैं--इस बातको मैं जानकर भी नहों जात पात।। उनके लिये मैं लंबी साँसें ले रहा हूँ और मेरा इृदय अत्यन्त दुःखित हो रहा है
- **Translation**: 

---

### Verse 19 (Markende Puran 0.2099)
- **Original**: 31--33
- **Translation**: 

---

### Verse 20 (Markende Puran 0.2100)
- **Original**: उन ल्ोगोपें प्रेमका' सर्वथा अथाव है त्तो भी उनके प्रति जो मेरा मन निह्ठुर नहीं हो यात्रा, इसके लिये क्या करूँ
- **Translation**: 

---

