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

### Verse 1 (Vaivtpuran 23.1762)
- **Original**: 4442404///(//////8/4 8 /0
- **Translation**: 

---

### Verse 2 (Vaivtpuran 23.1763)
- **Original**: 6 6 6] लक्ष कोटि मनोहर आश्रम हैं, जिनसे वह अभीष्ट
- **Translation**: 

---

### Verse 3 (Vaivtpuran 23.1764)
- **Original**: बनमालासे वे विभूषित हैं। त्रिभंगी छबिसे युक्त धाम अत्यन्त दीप्तिमान्‌ एवं श्रीसम्पन्न दिखायी देता
- **Translation**: 

---

### Verse 4 (Vaivtpuran 23.1765)
- **Original**: और मणिमाणिक्यसे अलंकृत हैं। मोरपंखका है। उन सबके मध्यभागमें एक परम मनोहर आश्रम
- **Translation**: 

---

### Verse 5 (Vaivtpuran 23.1766)
- **Original**: मुकुट धारण करते हैं। उत्तम रतन्नमय मुकुटसे है, जो अकेला ही सौ मन्दिरोंसे संयुक्त है। वह
- **Translation**: 

---

### Verse 6 (Vaivtpuran 23.1767)
- **Original**: उनका मस्तक जगमगाता रहता है। रत्रोंके परकोटों तथा खाइयोंसे घिरा हुआ तथा पारिजातके
- **Translation**: 

---

### Verse 7 (Vaivtpuran 23.1768)
- **Original**: बाजूबंद, कंगन और मंजोरसे उनके हाथ-पैर वनोंसे सुशोभित है। उस आश्रमके भवनोंमें जो
- **Translation**: 

---

### Verse 8 (Vaivtpuran 23.1769)
- **Original**: सुशोभित हैं। उनके गण्डस्थल रत्नरमय युगल कलश लगे हैं, उनका निर्माण रत्रराज कौस्तुभमणिसे
- **Translation**: 

---

### Verse 9 (Vaivtpuran 23.1770)
- **Original**: कुण्डलसे अत्यन्त शोभा पाते हैं। उनकी दन्तपंक्ति हुआ है। इसलिये वे उत्तम ज्योति:पुञ्से जाज्वल्यमान
- **Translation**: 

---

### Verse 10 (Vaivtpuran 23.1771)
- **Original**: मोतियोंकी पाँतिका तिरस्कार करनेवाली है। वे रहते हैं। उन भवनोंमें जो सीढ़ियाँ हैं, वे दिव्य
- **Translation**: 

---

### Verse 11 (Vaivtpuran 23.1772)
- **Original**: बड़े ही मनोहर हैं। उनके ओठ पके हुए हीरोंके सार-तत्त्वसे बनी हुई हैं। उनसे उन
- **Translation**: 

---

### Verse 12 (Vaivtpuran 23.1773)
- **Original**: बिम्बफलके समान लाल हैं। उन्नत नासिका भवनोंका सौन्दर्य बहुत बढ़ गया है। मणीन्द्रसारसे
- **Translation**: 

---

### Verse 13 (Vaivtpuran 23.1774)
- **Original**: उनकी शोभा बढ़ाती है। सब ओरसे घेरकर खड़ी निर्मित वहाँके किवाड़ोंमें दर्पण जड़े हुए हैं। नाना
- **Translation**: 

---

### Verse 14 (Vaivtpuran 23.1775)
- **Original**: हुई गोपाड्नाएँ उन्हें सदा सादर निहारती रहती प्रकारके चित्र-विचित्र उपकरणोंसे वह आश्रम
- **Translation**: 

---

### Verse 15 (Vaivtpuran 23.1776)
- **Original**: हैं। वे गोपाड्रनाएँ भी सुस्थिर यौवनसे युक्त, मन्द भलीभाँति सुसज्जित है। उसमें सोलह दरवाजे हैं
- **Translation**: 

---

### Verse 16 (Vaivtpuran 23.1777)
- **Original**: मुस्कानसे सुशोभित तथा उत्तम रल्रोंके बने हुए तथा बह आश्रम रत्रमय प्रदीपोंसे अत्यन्त उद्धासित
- **Translation**: 

---

### Verse 17 (Vaivtpuran 23.1778)
- **Original**: आभूषणोंसे विभूषित हैं। देबेद्ध, मुनीन्द्र, मुनिगण होता रहता है। तथा नरेशोंके समुदाय और न्रह्मा, विष्णु, शिव, वहाँ बहुमूल्य रब्नोंद्वारा निर्मित तथा नाना
- **Translation**: 

---

### Verse 18 (Vaivtpuran 23.1779)
- **Original**: अनन्त तथा धर्म आदि उनकी सानन्द वन्दना प्रकारके विचित्र चित्रोंसे चित्रित रमणीय रत्नमय
- **Translation**: 

---

### Verse 19 (Vaivtpuran 23.1780)
- **Original**: किया करते हैं। वे भक्तोंके प्रियतम, भक्तोंके नाथ सिंहासनपर सर्वेश्वर श्रीकृष्ण बैठे हुए हैं। उनकी
- **Translation**: 

---

### Verse 20 (Vaivtpuran 23.1781)
- **Original**: तथा भक्तोंपर अनुग्रह करनेके लिये कातर अड्गकान्ति नवीन मेघ-मालाके समान श्याम है।
- **Translation**: 

---

