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

### Verse 1 (Sama Ved 0.361)
- **Original**: 120. त्वभिन्द्र बलादधि सहसो जात ओजस:
- **Translation**: 

---

### Verse 2 (Sama Ved 0.362)
- **Original**: त्वं सन्वृषन्वृषेदेिसि
- **Translation**: 

---

### Verse 3 (Sama Ved 0.363)
- **Original**: हे इन्द्रदेव ! आप महान्‌ शक्तिशाली हैं । अपने साहस, बल और सामर्थ्य के कारण सबसे सिद्ध श्रेष्ठ हुए हैं । श्रेष्ठ फलों की वर्षा करने में आप समर्थ हैं
- **Translation**: 

---

### Verse 4 (Sama Ved 0.364)
- **Original**: 129. यज्ञ इन्द्रमवर्धयद्यद्धूमि व्यवर्तयत्‌ । चक्राण ओपशं दिवि
- **Translation**: 

---

### Verse 5 (Sama Ved 0.365)
- **Original**: जिस यज्ञ प्रक्रिया ने पृथ्वी को आकाश में लटकाकर, घुमाते हुए रखा है, उस यज्ञ ने इद्धदेव का यशवर्धन भी किया है
- **Translation**: 

---

### Verse 6 (Sama Ved 0.366)
- **Original**: [ पृथ्वी का आकाश में पृषना पश्चिम वालों के लिये नवीन खोज हो सकती है, वेदज़ों के लिए नहीं
- **Translation**: 

---

### Verse 7 (Sama Ved 0.367)
- **Original**: गीता पें कहा जया है- सृष्टि यज़सहित बनायी गयी है । इस क्रवा से उतरी व्यापक यज्ञ का स्वरूप स्पष्ट होता है ।] 122, यदिन्द्राहं यथा त्वमीशीय वस्व एक इत्‌ । स्तोता मे गोसखा स्यात्‌
- **Translation**: 

---

### Verse 8 (Sama Ved 0.368)
- **Original**: हे इद्धदेव ! जिस प्रकार आप सारे ऐश्वर्य के स्वामो हैं, वैसा यदि मैं बन जारऊँ , तो मेरी स्तुति करने चार+ शो आदि, धन-धान्य से युक्त हो जाएँ
- **Translation**: 

---

### Verse 9 (Sama Ved 0.369)
- **Original**: [हों ऐज्वर्य पिलते पर उसका उपयोग अधाउप्रस्तों का अभाव पिटाने के लिये किये जाने का संकेत हैं ।]
- **Translation**: 

---

### Verse 10 (Sama Ved 0.370)
- **Original**: सामवेद-संहिता 123. पन्य॑पन्यमित्सोतार आ धावत मद्याय । सोम॑ं वीराय शूराय
- **Translation**: 

---

### Verse 11 (Sama Ved 0.371)
- **Original**: हे सोम- शोधन में रत याजको ! पराक्रमी, शूरवीर इन्द्रदेव के लिए आनन्ददायी सोम अर्पित करो
- **Translation**: 

---

### Verse 12 (Sama Ved 0.372)
- **Original**: 3124. इदं बसो सुतमन्ध: पिबा सुपूर्णमुदरम्‌ । अनाभयित्ररिमा ते
- **Translation**: 

---

### Verse 13 (Sama Ved 0.373)
- **Original**: हे निर्भय इद्धदेव ! आप अभिषुत सोम को ग्रहण करें, जिससे आप तृप्त हों । आपको आनन्दित करने के लिए यह सोप अर्पित है
- **Translation**: 

---

### Verse 14 (Sama Ved 0.374)
- **Original**: इति प्रथम:खण्ड:
- **Translation**: 

---

### Verse 15 (Sama Ved 0.375)
- **Original**: #जऊक के
- **Translation**: 

---

### Verse 16 (Sama Ved 0.376)
- **Original**: द्वितीय: खण्ड:
- **Translation**: 

---

### Verse 17 (Sama Ved 0.377)
- **Original**: 125. उदघेदभि श्रुतामघं वृषभं नर्यापसम्‌ । अस्तारमेषि सूर्य
- **Translation**: 

---

### Verse 18 (Sama Ved 0.378)
- **Original**: ज़गत्‌ विख्यात, ऐश्वर्य-सम्पन, शक्तिशाली, मानव पात्र के हितैषी और (दुष्टों पर) अस्त्रों से प्रहार करने वाले ये उदीयमान सूर्य (इन्द्र) देव हैं.
- **Translation**: 

---

### Verse 19 (Sama Ved 0.379)
- **Original**: 126. यदद्य कच्च वृत्रहन्नुदगा अभि सूर्य । सर्व तदिद्ध ते वशे
- **Translation**: 

---

### Verse 20 (Sama Ved 0.380)
- **Original**: हे बृत्र के संहारक, अभी उदय हुए (सूर्य) इन्द्रदेव ! (आपसे प्रकाशित होने वाला) वह सब कुछ आपके अधिकार में है
- **Translation**: 

---

