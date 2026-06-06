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

### Verse 1 (Agni Puran 0.681)
- **Original**: प्रचार किया है। वे संख्यामें पच्चीस हैं। (उनके
- **Translation**: 

---

### Verse 2 (Agni Puran 0.682)
- **Original**: इन तन्‍्त्रोंक अनुसार मध्यदेश आदियमें उत्पन्न नाम इस प्रकार हैं--) आदिहयशीर्षतन्त्र,
- **Translation**: 

---

### Verse 3 (Agni Puran 0.683)
- **Original**: द्विज देवविग्रहोंकी प्रतिष्ठा करे। कच्छदेश, अलोक्यमोहनतन्त्र, वैभवतन्त्र, पुष्करतन्त्र, प्रह्मादतन्त्र,
- **Translation**: 

---

### Verse 4 (Agni Puran 0.684)
- **Original**: कावेरीतटवर्ता देश, कोंकण, कामरूप, कलिब्न, गार्ग्यतन्त्र, गालवतन्‍्त्र, नारदीयतन्त्र, श्रीप्रश्नतन्त्र,
- **Translation**: 

---

### Verse 5 (Agni Puran 0.685)
- **Original**: काञ्ली तथा काश्मीर देशमें उत्पन्न ब्राह्मण देवप्रतिष्ठा शाण्डिल्यतन्त्र, ईश्वरतन्त्र, सत्यतन्त्र, शौनकतन्त्र,
- **Translation**: 

---

### Verse 6 (Agni Puran 0.686)
- **Original**: आदि न करे। आकाश, वायु, तेज, जल एवं पृथ्वी -- उपलेपनकतार: सम्मारजबपराश्ष ये । कृष्णालये पतित्याण्यास्तेषां पुआस्तथा कुलम्‌
- **Translation**: 

---

### Verse 7 (Agni Puran 0.687)
- **Original**: येत चायतन॑ विष्णों: कारित॑ तरुत्कुलों>यम्‌ । पूंसा श्त॑ नावलोक्य. भवद्धिदुष्टचेतसा
- **Translation**: 

---

### Verse 8 (Agni Puran 0.688)
- **Original**: यस्तु॒ देवालय॑ विष्णोदास्शैलमय॑ ठथा । कारयेन्मृन्सयं वापि. सर्वपापै:. प्रमुच्यते
- **Translation**: 

---

### Verse 9 (Agni Puran 0.689)
- **Original**: अहन्पहनि कुलाऋं योेन यज्ले... यमहाफलस्‌ । प्राप्जोति तत्फल विष्णोर्य: कारयति केतनम्‌
- **Translation**: 

---

### Verse 10 (Agni Puran 0.690)
- **Original**: शतमागामि समतोत॑ तथा शत्म्‌ । कारयनू भगवद्धाम नयत्यच्चुतलोकताम्‌
- **Translation**: 

---

### Verse 11 (Agni Puran 0.691)
- **Original**: साप्तलोकमयो . किष्णुस्तस्थ यः कुस्ते गृहम्‌। तारपत्यक्षयौज्लोकानक्षग्पान्‌ प्रतिपद्यते
- **Translation**: 

---

### Verse 12 (Agni Puran 0.692)
- **Original**: इृष्टकाचयविन्यास्ो. यायत्त्यब्दानि तिहति। तावडपसहल्ाणि. तत्कतु्देथि. संस्थिति:
- **Translation**: 

---

### Verse 13 (Agni Puran 0.693)
- **Original**: प्रतिमाकृदू विष्णुलोक॑ स्थापकों लीयते हरौ। देवसच्प्रतिकृतिप्रतिष्ठकृततु गोचो
- **Translation**: 

---

### Verse 14 (Agni Puran 0.694)
- **Original**: (अग्निपु0 38
- **Translation**: 

---

### Verse 15 (Agni Puran 0.695)
- **Original**: 42--50 )
- **Translation**: 

---

### Verse 16 (Agni Puran 0.696)
- **Original**: ये पश्ममहाभूत पछरात्र हैं। जो चेतनाशुन्य एवं
- **Translation**: 

---

### Verse 17 (Agni Puran 0.697)
- **Original**: बनवाना चाहिये
- **Translation**: 

---

### Verse 18 (Agni Puran 0.698)
- **Original**: 9--13 3
- **Translation**: 

---

### Verse 19 (Agni Puran 0.699)
- **Original**: अज्ञानान्थकारसे आच्छन्न हैं, वे पञ्चण़त्रसे रहित हैं। जो मनुष्य यह धारणा करता है कि “मैं पापमुक्त परब्रह्म विष्णु हूँ'--वह देशिक होता है। वह समस्त बाह्य लक्षणों (वेष आदि)-से हीन होनेपर भी तन्त्रवेत्ता आचार्य माना गया है
- **Translation**: 

---

### Verse 20 (Agni Puran 0.700)
- **Original**: 6--8 3
- **Translation**: 

---

