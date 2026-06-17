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

### Verse 1 (Vaivtpuran 6.2559)
- **Original**: देवता, महाविराट्‌ और स्वल्पविराटू-सभी उन
- **Translation**: 

---

### Verse 2 (Vaivtpuran 6.2560)
- **Original**: वेदज्ञा तथा द्विजोंकी पूजनीया हो गबी हैं। परम प्रभु परमात्माके अंश हैं। प्रकृति भी उन्हींका
- **Translation**: 

---

### Verse 3 (Vaivtpuran 6.2561)
- **Original**: परमात्मा श्रीकृष्णजी सेवा और तपका ही प्रभाव अंश कही गयी है। वे श्रीकृष्ण दो रूपोंमें विभक्त
- **Translation**: 

---

### Verse 4 (Vaivtpuran 6.2562)
- **Original**: है कि सरस्वतीकों समस्त विद्याकी अधिष्ठात्री हो जाते हैं-एक द्विभुज और दूसरे चतुर्भुज।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 6.2563)
- **Original**: माना जाता है। अखिल विद्वान्‌ उनकी उपासना चतुर्भुज श्रीहरि वैकुण्ठमें विराजते हैं और स्वयं
- **Translation**: 

---

### Verse 6 (Vaivtpuran 6.2564)
- **Original**: करते हैं। सनातनी महालक्ष्मी धन और सस्यकी द्विभुज श्रीकृष्णका गोलोकमें निवास है। ब्रह्मासे
- **Translation**: 

---

### Verse 7 (Vaivtpuran 6.2565)
- **Original**: अधिष्ठात्री देवी तथा सब सम्पत्तियोंकों देनेमें लेकर तृणपर्यन्त समस्त चराचर जगत्‌ (प्राकृत
- **Translation**: 

---

### Verse 8 (Vaivtpuran 6.2566)
- **Original**: समर्थ हुई हैं। इन्हींकी उपासिका होनेसे दुर्गाको सर्गके अन्तर्गत) है। जो-जो प्राकृतिक सृष्टि है, ,सब लोग पूजते हैं और वे सर्वेथ्री सबकी वह सब नश्वर ही है। इस प्रकार सृष्टिके
- **Translation**: 

---

### Verse 9 (Vaivtpuran 6.2567)
- **Original**: कामनाएँ पूर्ण कर देती हैं। इतना ही नहीं, वे कारणभूत परब्रह्म परमात्मा नित्य, सत्य, सनातन,
- **Translation**: 

---

### Verse 10 (Vaivtpuran 6.2568)
- **Original**: दुर्गतिनाशिनी दुर्गा इन्हींकी कृपासे समस्त गाँवोंकी स्वतन्त्र, निर्गुण, निर्लिप्त और प्रकृतिसे परे हैं;
- **Translation**: 

---

### Verse 11 (Vaivtpuran 6.2569)
- **Original**: ग्रामदेवी, सम्पूर्ण सम्पत्ति देनेमें समर्थ, सबके उनकी न कोई लौकिक उपाधि है और न कोई
- **Translation**: 

---

### Verse 12 (Vaivtpuran 6.2570)
- **Original**: द्वारा स्तुत्य और सर्वज्ञ हुई हैं। उन्होंने सर्वेश्वर भौतिक आकार। भक्तोंपर अनुग्रह करना उनका
- **Translation**: 

---

### Verse 13 (Vaivtpuran 6.2571)
- **Original**: शिवको जो पतिरूपमें प्राप्त किया है, वह उनकी स्वरूप है-सहज स्वभाव है। वे अत्यन्त
- **Translation**: 

---

### Verse 14 (Vaivtpuran 6.2572)
- **Original**: श्रीकृष्ण-सेवाका ही फल है। कमनीय हैं। उनकी अड्भकान्ति नूतन जलधरके श्रीकृष्णेक वामभागसे प्रकट हुई श्रीराधा समान है। उनके दो भुजाएँ हैं। हाथमें मुरली
- **Translation**: 

---

### Verse 15 (Vaivtpuran 6.2573)
- **Original**: श्रीकृष्णकी प्रेमसे आराधना और सेवा करके ही है। गोपों-जैसा वेष और किशोर अवस्था है।
- **Translation**: 

---

### Verse 16 (Vaivtpuran 6.2574)
- **Original**: उनके प्रेमकी अधिष्ठात्री तथा उन्हें प्राणोंसे भी वे सर्वज्ञ, सर्वसेव्य, परमात्मा एवं ईश्वर हैं। तुम
- **Translation**: 

---

### Verse 17 (Vaivtpuran 6.2575)
- **Original**: अधिक प्रिय हुई हैं। श्रीकृष्णकी सेवासे ही उनके स्वरूपकों ऐसा ही जानो। उन्होंने सबसे अधिक मनोहर रूप, सौभाग्य, मान, इन्हींके दिये हुए ज्ञानसे विराट्‌ पुरुष (विष्णु)-
- **Translation**: 

---

### Verse 18 (Vaivtpuran 6.2576)
- **Original**: गौरव तथा श्रीकृष्णके वक्ष:स्थलमें स्थान--उनका के नाभिकमलसे उत्पन्न ज्ञानस्वरूप ब्रह्मा अखिल
- **Translation**: 

---

### Verse 19 (Vaivtpuran 6.2577)
- **Original**: पत्नीत्व प्राप्त किया है। पूर्वकालमें राधाने शतश्ृद्ध ब्रह्माण्डकी सृष्टि करते हैं तथा सम्पूर्ण तत्त्वोंके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 6.2578)
- **Original**: पर्वतपर एक सहस्त दिव्य युगोंतक निराहार रहकर ज्ञाता मृत्यु्रय शिव संहारका कार्य सँभालते हैं।
- **Translation**: 

---

