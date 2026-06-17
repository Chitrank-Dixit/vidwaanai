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

### Verse 1 (Vaivtpuran 13.11502)
- **Original**: (21। 90-95)
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.11503)
- **Original**: + श्रीकृष्णजन्मखण्ड « 511 55555 55% 45 $ 5 5 55 5 5 5 क 5 $ 5 4 $ 5 5 5 5 हक 888 8 9 88 89888 885 8688 ##8##8%# 68 5888 4588 8
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.11504)
- **Original**: 8888 व्यवस्था होती है, उसके बाद जीव प्रकट होता
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.11505)
- **Original**: ब्रह्माेओंका उन निर्गुण परमात्मा श्रीहरिके एक है। बारंबार ऐसा होनेसे ही इस नियत व्यवस्थाको
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.11506)
- **Original**: निमेषमें ही पतन हो जाता है; ऐसे परमात्माके स्वभाव कहते हैं। स्वभावसे कर्म होता है और
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.11507)
- **Original**: रहते हुए इन्द्रकी पूजा विडम्बनामात्र है। कर्मके अनुसार जीवधारियोंको सुख-दुःखका
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.11508)
- **Original**: नारद! यों कहकर श्रीकृष्ण चुप हो गये। भोग प्राप्त होता है। यातना, जन्म-मरण, रोग-
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.11509)
- **Original**: उस समय सभामें बैठे हुए महर्षियोंने भगवान्‌की शोक, भय, उत्पत्ति, विपत्ति, विद्या, कविता, यश,
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.11510)
- **Original**: भूरि-भूरि प्रशंसा की। नन्दके शरीरमें रोमाझ् हो अपयश, पुण्य, स्वर्गवास, पाप, नरकनिवास,
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.11511)
- **Original**: आया। वे हर्षसे उत्फुल्ल हो सभामें बैठे-बैठे भोग, मोक्ष और श्रीहरिका दास्‍्य-ये सब
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.11512)
- **Original**: नेत्रोंसे अश्रु बहाने लगे। मनुष्य यदि अपने पुत्रोंसे मनुष्योंको कर्मके अनुसार उपलब्ध होते हैं। ईश्वर [पराजित हों तो वे आनन्दित ही होते हैं। सबके जनक हैं। शील और कमोंका अभ्यास
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.11513)
- **Original**: श्रीकृष्णकी आज्ञा मान नन्दजीने स्वस्तिवाचन विधाताके लिये भी फलदाता होता है। सब कुछ
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.11514)
- **Original**: किया और क्रमश: सब ब्राह्मणों एवं मुनियोंका ईश्वरकी इच्छासे ही सम्भव होता है। बिराट्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.11515)
- **Original**: वरण किया। उन्होंने आदरपूर्वक गिरिराज गोवर्धनकी, पुरुषसे प्रकृति, पद्मतत्त्व, जगतू, कूर्म, शेष, धरणी
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.11516)
- **Original**: समागत मुनीश्वरॉंकी, विद्वान्‌ ब्राह्मणोंकी तथा तथा ब्रह्मासे लेकर कीटपर्यन्त सम्पूर्ण चराचर
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.11517)
- **Original**: गौओं और अग्निकी सानन्द पूजा कौ। पूजाकी पदार्थोका निर्माण हुआ है। जिनकी आज्ञासे वायु
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.11518)
- **Original**: समाप्ति होनेपर उस यज्ञ-महोत्सवमें नाना प्रकारके कूर्मको, कूर्म शेषको, शेष अपने मस्तकपर
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.11519)
- **Original**: बाद्योंका तुमुल नाद होने लगा। जय-जयकारके वसुधाकों और वसुधा सम्पूर्ण चराचर जगत्‌कों
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.11520)
- **Original**: शब्द, शद्भुध्यनि तथा हरिनामकीर्तन होने लगे। धारण करती है; जिनके आदेशसे जगतके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.11521)
- **Original**: मुनिवर गर्गने बेदोंके मड्गरलकाण्डका पाठ किया। प्राणस्वरूप समीरण सदा तीनों लोकोंमें बहते
- **Translation**: 

---

