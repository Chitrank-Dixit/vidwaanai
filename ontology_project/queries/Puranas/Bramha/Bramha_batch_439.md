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

### Verse 1 (Bramha 0.8761)
- **Original**: दिखायी नहीं देता। वेदोंके पारगामी तत्त्वज्न थधच्चीसवें तत्त्व परमात्मामें स्थित हो जाता है, उस
- **Translation**: 

---

### Verse 2 (Bramha 0.8762)
- **Original**: विद्वानोंने उसे तमसे दूर--अज्ञानान्धकारसे परे समय उसकी सम्यक्‌ स्थिति बतायी जाती है।
- **Translation**: 

---

### Verse 3 (Bramha 0.8763)
- **Original**: बताया है। वह निर्मल एवं लिड्भरहित है। यही एकत्व और नानात्व दोनों रूपोंमें उस परमात्माका
- **Translation**: 

---

### Verse 4 (Bramha 0.8764)
- **Original**: योगियोंका योग है। इसके सिवा योगका और ही दर्शन होता है। तत्त्ववेत्ता पुरुष एकत्व और
- **Translation**: 

---

### Verse 5 (Bramha 0.8765)
- **Original**: क्‍या लक्षण हो सकता है। इस प्रकार साधना नानात्व दोनोंके पार्थक्यकों भलीभाँति जानता है।
- **Translation**: 

---

### Verse 6 (Bramha 0.8766)
- **Original**: करनेवाला योगी सबके द्रष्टा अजर-अमर मनीषी पुरुष तत्त्वोंकी संख्या पच्चीस बतलाते हैं;
- **Translation**: 

---

### Verse 7 (Bramha 0.8767)
- **Original**: परमात्माका दर्शन करता है। यहाँतक मैँने तुम्हें परंतु उनमें पतच्चीसाँ तत्त्व परमात्मा है, जो
- **Translation**: 

---

### Verse 8 (Bramha 0.8768)
- **Original**: योग-दर्शनका यथार्थस्वरूप बतलाया। तत्त्वोंसे विलक्षण है। अब सांख्यका वर्णन करता हूँ, यह बिचार- राजन्‌! योगीका प्रधान कर्तव्य है ध्यान; ध्यान
- **Translation**: 

---

### Verse 9 (Bramha 0.8769)
- **Original**: प्रधान दर्शन है। राजन्‌! प्रकृतिबादी विद्वान मूल ही योगियोंका सबसे बड़ा बल है। योगविद्याके ' प्रकृतिको अव्यक्त कहते हैं। उससे दूसरा तत्त्व ज्ञाता विद्वान्‌ पुरुष मनकी एकाग्रता और प्राणायाम--ये
- **Translation**: 

---

### Verse 10 (Bramha 0.8770)
- **Original**: प्रकट हुआ, जो ' महत्तत्त्व” कहलाता है। महत्तत्त्वसे ध्यानके दो भेद बतलाते हैं। योगीको सब
- **Translation**: 

---

### Verse 11 (Bramha 0.8771)
- **Original**: अहंकार नामक तीसरे तत्त्वकी उत्पत्ति सुनी गयी प्रकारकी आसक्तियोंका त्याग करके मिताहारी
- **Translation**: 

---

### Verse 12 (Bramha 0.8772)
- **Original**: है। सांख्य-दर्शनके ज्ञाता बिद्वान्‌ अहंकारसे सूक्ष्म और जितेन्द्रिय होना चाहिये। वह रात्रिके पहले
- **Translation**: 

---

### Verse 13 (Bramha 0.8773)
- **Original**: भूतोंका-पश्च-तन्मात्राओंका प्रादुर्भाव बतलाते हैं। और पिछले भागमें मनको परमात्मामें लगाकर
- **Translation**: 

---

### Verse 14 (Bramha 0.8774)
- **Original**: इन आठोंको प्रकृति कहते हैं; इनसे सोलह अन्त/करणमें उनका ध्यान करें। मिथिलेश्वर!
- **Translation**: 

---

### Verse 15 (Bramha 0.8775)
- **Original**: तत्त्वोंकी उत्पत्ति होती है, जो 'विकृति' कहलाते सम्पूर्ण इन्द्रियोंकों मनके द्वारा स्थिर करके
- **Translation**: 

---

### Verse 16 (Bramha 0.8776)
- **Original**: हैं। पाँच ज्ञानेन्द्रियाँ, पाँच कर्मेन्द्रियाँ, ग्यारहवाँ मनको भी बुद्धिमें स्थापित कर दे और पत्थरकी
- **Translation**: 

---

### Verse 17 (Bramha 0.8777)
- **Original**: मन तथा पाँच स्थूलभूत--ये ही सोलह विकार भाँति अविचल हो जाय, तभी उसे योगयुक्त
- **Translation**: 

---

### Verse 18 (Bramha 0.8778)
- **Original**: हैं। ये प्रकृति और बिकृति मिलकर चौबीस तत्त्व कहते हैं। जिस समय उसे सुनने, सूँघने, स्वाद
- **Translation**: 

---

### Verse 19 (Bramha 0.8779)
- **Original**: होते हैं। सांख्यदर्शनमें तत्त्वोॉंकी इतनी ही संख्या लेने, देखने और स्पर्श करनेका भी भान नहीं
- **Translation**: 

---

### Verse 20 (Bramha 0.8780)
- **Original**: मानी गयी है। सांख्यमार्गपर स्थित और सांख्यविधिके रहता, जब मनमें किसी प्रकारका संकल्प नहीं
- **Translation**: 

---

