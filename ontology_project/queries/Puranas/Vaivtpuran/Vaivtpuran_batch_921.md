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

### Verse 1 (Vaivtpuran 543.16734)
- **Original**: अभक्तालापदीम्ताग्रिज्यालाया: कलयापि च । अड्डुरं शुष्कर्ता याति पुनः सेकेन वर्धते
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.16735)
- **Original**: तस्मादभक्तसज़ूं . च स्रावधानं परित्यज । यथा दृष्ठा कालसप॑ नरो भीतः: पलायते
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.16736)
- **Original**: यशोदे च॒ प्रयत्नेन स्वात्मनः: पुत्रमौश्ररम्‌
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.16737)
- **Original**: भजस्व परया भकत्या परमात्मानमीश्वरम्‌
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.16738)
- **Original**: राम नाग़यणानन्त मुकुन्द मधुसूदन
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.16739)
- **Original**: कृष्ण केशव कंसारें हरे वैकुण्ठ यामन
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.16740)
- **Original**: इत्येकादश नापथानि पठेदू. वा पाठयेदिति
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.16741)
- **Original**: जन्मकोटिसहस्सराणां.. पातकादेव मुच्यते
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.16742)
- **Original**: (1115। 13-20) * राशब्दो विश्ववचनों मश्चापौश्वरवाचक: । विश्वानामीश्ररो यो हि. तेन राम: प्रकीर्तित: #
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.16743)
- **Original**: रमते रमया साध॑ तेन रामं॑ विदुर्बुधा:
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.16744)
- **Original**: रमाणां रमणस्थानं राम॑ रामबिदो विदु:
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.16745)
- **Original**: राश्वेति लक्ष्मीबचनो मश्वापीश्ररवाचक: । लक्ष्मीपतिं गति राम॑ प्रवदन्ति मनीषिण:
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.16746)
- **Original**: नाग्रां सहस्त॑ दिव्यानां स्मरणे यत्फल॑ भवेत्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.16747)
- **Original**: तत्फल॑ लभते नून॑ रामोच्चारणमात्रत:
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.16748)
- **Original**: (111। 18-21) ! सारूप्यमुक्तिवचनों नोरेति च विदुबुंधा:
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.16749)
- **Original**: यो देवो5प्यायनं तस्थ स च नारायण: स्मृतः
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.16750)
- **Original**: नाराश्ल कृतपापाश्चाप्ययनं गमन॑ स्मृतम्‌ ।.यतो हि गमन॑ तेषां सो5यं नारायण: स्मृतः
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.16751)
- **Original**: सकृन्नारायणेत्युक्चा. पुपानु कल्पशतत्रयम्‌ । गड्जादिसर्वतीर्थेंषच. स्रातों भवति . निश्चितम्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.16752)
- **Original**: नारं च॒ मोक्षणं पुण्यमयन॑ ज्ञानमीप्सितम्‌ । तयोर्ज्ञान भवेद्‌ यस्मात्‌ सो5यं नारायण: प्रभुः
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.16753)
- **Original**: (1115। 22-25)
- **Translation**: 

---

