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

### Verse 1 (Bramha 0.2381)
- **Original**: भागी होते हैं, बह भी मेरा ही स्वरूप है। मैं ही शिव, चन्द्रमा, प्रजापति कश्यप, धाता,
- **Translation**: 

---

### Verse 2 (Bramha 0.2382)
- **Original**: दान, उग्र तपस्या और अहिंसा--ये मेरे बनाये हुए विधाता और यज्ञ हूँ। अग्नि मेरा मुख, पृथ्वी
- **Translation**: 

---

### Verse 3 (Bramha 0.2383)
- **Original**: विधानके अनुसार ही विहित माने जाते हैं और चरण, चन्द्रमा और सूर्य नेत्र, चुलोक मस्तक,
- **Translation**: 

---

### Verse 4 (Bramha 0.2384)
- **Original**: मेरे ही स्वरूपमें इनकी स्थिति है। जिनकी आकाश और दिशाएँ कान तथा जल स्वेद है।
- **Translation**: 

---

### Verse 5 (Bramha 0.2385)
- **Original**: ज्ञानशक्ति मेरे द्वारा अभिधूत हो जातो है, वे दिशाओंसहित आकाश मेरा शरीर और वायु मेरे
- **Translation**: 

---

### Verse 6 (Bramha 0.2386)
- **Original**: इच्छानुसार चेष्टा नहीं कर पाते। वेदोंका सम्यक्‌ मनमें स्थित है। मैंने पर्यात दक्षिणावाले अनेकों
- **Translation**: 

---

### Verse 7 (Bramha 0.2387)
- **Original**: स्वाध्याय करके भाँति-भाँतिके यज्ञोंद्वाए यजन यज्ञोंका अनुष्ठान किया है। पृथ्वीपर वेदके विद्वान्‌
- **Translation**: 

---

### Verse 8 (Bramha 0.2388)
- **Original**: करनेवाले शान्तचित्त एवं क्रोधपर विजय पानेवाले देवयज्ञ्में स्थित मुझ विष्णुका ही यजन करते हैं।
- **Translation**: 

---

### Verse 9 (Bramha 0.2389)
- **Original**: ब्राह्मण मुझे प्राप्त करते हैं। पापाचारी, लोभी, स्वर्गकी इच्छा रखनेवाले मुख्य-मुख्य क्षत्रिय और
- **Translation**: 

---

### Verse 10 (Bramha 0.2390)
- **Original**: कृपण, अनार्य तथा मनकों वशमें न रखनेवाले वैश्य भी यज्ञके द्वारा मेरी आराधना करते हैं। मैं
- **Translation**: 

---

### Verse 11 (Bramha 0.2391)
- **Original**: मनुष्योंको मैं कभी नहीं मिल सकता। जिनके ही शेषनाग होकर चारों ओरके समुद्रों और
- **Translation**: 

---

### Verse 12 (Bramha 0.2392)
- **Original**: अन्त/करण शुद्ध हैं, उन्हें प्राप्त होनेवाला महान्‌ मेरुपर्वतसहित समस्त पृथ्बीको अकेला ही धारण
- **Translation**: 

---

### Verse 13 (Bramha 0.2393)
- **Original**: फल मुझे हो समझो। कुयोगसेवी मूढ़ मनुष्योंके करता हूँ। पूर्वकालमें बाराहरूप धारण करके मैंने
- **Translation**: 

---

### Verse 14 (Bramha 0.2394)
- **Original**: लिये मैं अत्यन्त दुर्लभ हूँ। संतशिरोमणे! जब- ही जलमें डूबी हुई इस पृथ्वीका अपनी शक्तिसे
- **Translation**: 

---

### Verse 15 (Bramha 0.2395)
- **Original**: जब धर्मकी हानि और अधर्मका उत्थान होता है उद्धार किया था। द्विजश्रेष्ट] मैं हो बड़वानल
- **Translation**: 

---

### Verse 16 (Bramha 0.2396)
- **Original**: तब-तब मैं अपनेको प्रकट करता हूँ।* हिंसापरयण होकर समुद्रका जल पीता और मेघरूपसे उसकी
- **Translation**: 

---

### Verse 17 (Bramha 0.2397)
- **Original**: दैत्य तथा भयंकर राक्षस, जो बड़े-बड़े देवताओंके वर्षा करता हूँ। ब्राह्मण मेरा मुख, क्षत्रिय मेरी
- **Translation**: 

---

### Verse 18 (Bramha 0.2398)
- **Original**: लिये भी अवध्य हैं, जब इस संसारमें जन्म लेते भुजाएँ, वैश्य जाँघ और शूद्र चरण हैं। ऋग्वेद, हैं, तब मैं पुण्यात्मा पुरुषोंके घरोंमें अबतार लेता यजुर्वेद, सामबेद और अधथर्ववेद मुझसे हो प्रकट
- **Translation**: 

---

### Verse 19 (Bramha 0.2399)
- **Original**: हूँ। मनुष्य-देहमें प्रवेश करके समस्त बाधाओंका होते और फिर मुझमें ही प्रवेश कर जाते हैं।
- **Translation**: 

---

### Verse 20 (Bramha 0.2400)
- **Original**: शमन करता हूँ। देवता, मनुष्य, गन्धर्व, नाग तथा ज्ञानपरायण संन्यासी, संयमशील जिज्ञासु तथा
- **Translation**: 

---

