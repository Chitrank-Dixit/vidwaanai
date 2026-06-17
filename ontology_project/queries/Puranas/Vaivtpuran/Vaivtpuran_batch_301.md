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

### Verse 1 (Vaivtpuran 13.12162)
- **Original**: अर्थका तथा 'वाकार' दाता अर्थका वाचक है। स्तवन करती थीं, जो सम्पूर्ण अभीष्ट फलोंको
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.12163)
- **Original**: वे देवी कल्याणसमूह तथा उत्कृष्ट वस्तुको देनेवाली हैं। देनेवाली हैं; इसलिये 'शिवा' कही गयी हैं। वे जब सारा जगत्‌ घोर एकार्णवमें डूब गया
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.12164)
- **Original**: शिव अर्थात्‌ कल्याणकी मूर्तिमती राशि हैं;
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.12165)
- **Original**: * भ्रीकृष्णजन्मखण्ड « 537 न] ]]]]]ऋ]422420000(4(/4 8
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.12166)
- **Original**: । 44444. इसलिये भी उन्हें 'शिवा' कहा गया है। 'शिव'
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.12167)
- **Original**: विधाताको दिव्य कबचकी प्राप्ति हुई। उस श्रेष्ठ शब्द मोक्षका बोधक है तथा 'आकार' दाताका।
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.12168)
- **Original**: कबचको पाकर निश्चय ही वे निर्भय हो गये। वे देवी स्वयं ही मोक्ष देनेवाली हैं; इसलिये
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.12169)
- **Original**: फिर ब्रह्माने महेश्वको उस समय स्तोत्र और “शिवा' कही गयी हैं। 'अभय' का अर्थ है
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.12170)
- **Original**: कबचका उपदेश दिया, जब कि त्रिपुरासुरके साथ भ्रयनाश और “आकार' का अर्थ है दाता। वे
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.12171)
- **Original**: युद्ध करते समय रथसहित भगवान्‌ शंकर नीचे तत्काल अभय-दान करती हैं; इसलिये ' अभया'
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.12172)
- **Original**: गिर गये थे। उस कवचके द्वारा आत्मरक्षा करके कहलाती हैं। 'मा' का अर्थ है राजलक्ष्मी और
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.12173)
- **Original**: उन्होंने निद्राकी स्तुति की। फिर योगनिद्राके 'या' का अर्थ है प्राप्ति करानेवाला। जो शीघ्र
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.12174)
- **Original**: अनुग्रह और स्तोत्रके प्रभावसे वहाँ शीघ्र ही ही राजलक्ष्मीकी प्राप्ति कराती हैं; उन्हें 'माया'
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.12175)
- **Original**: वृषभरूपधारी भगवान्‌ जनार्दन आये। उनके साथ कहा गया है। 'मा' मोक्ष अर्थका और 'या' प्राप्ति
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.12176)
- **Original**: शक्तिस्वरूपा दुर्गा भी थीं। वे भगवान्‌ शंकरको अर्थका वाचक है। जो सदा मोक्षकी प्राप्ति कराती
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.12177)
- **Original**: विजय देनेके लिये आये थे। उन्होंने रथसहित हैं, उनका नाम “माया' है। वे देवी भगवान्‌ शंकरकों मस्तकपर बिठाकर अभय दान दिया नारायणका आधा अक्ज़ हैं। उन्हींक समान
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.12178)
- **Original**: और उन्हें आकाशमें बहुत ऊँचाईतक पहुँचा तेजस्विनी हैं और उनके शरीरके भीतर निवास
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.12179)
- **Original**: दिया। फिर जयाने शिवकों विजय दी। उस समय करती हैं; इसलिये उन्हें 'नारायणी' कहते हैं।
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.12180)
- **Original**: ब्रह्मासत्र हाथमें ले योगनिद्रासहित श्रीहरिका *सनातन' शब्द नित्य और निर्गुणका वाचक है।
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.12181)
- **Original**: स्मरण करते हुए भगवान्‌ शंकरने स्तोत्र और जो देवी सदा निर्गुणा और नित्या हैं; उन्हें
- **Translation**: 

---

