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

### Verse 1 (Rig Ved 0.10381)
- **Original**: वे ऑन्निदेव आहुतियों के अधिषति और वे ही दिवोदास के शत्रुओं के संहारक हैं । हे याजको ! वे अग्निदेव रक्षक एवं सर्वज्ञ हैं । हम स्तुतियों द्वारा अग्निदेव का आवाहन करते हैं
- **Translation**: 

---

### Verse 2 (Rig Ved 0.10382)
- **Original**: 4513. स हि विश्वाति पार्थिवा रयिं दाशन्महित्वना।वन्वन्नवातो अस्तृत:
- **Translation**: 

---

### Verse 3 (Rig Ved 0.10383)
- **Original**: जो अग्नदेव अपराजित, शत्रुनाशक और अहिंसित हैं । वे अग्निदेव ही अपनी सामर्थ्य से हमें पृथ्वी पर श्रेष्ठ धन-ऐश्वर्य प्रदान करते है
- **Translation**: 

---

### Verse 4 (Rig Ved 0.10384)
- **Original**: 4514 स प्रलवन्नवीयसाम्ने घुम्नेन संयता। बृहत्ततन्थ भानुना
- **Translation**: 

---

### Verse 5 (Rig Ved 0.10385)
- **Original**: हे अग्निदेव ! आप इस विस्तार वाले अन्तरिक्ष को अपने संयमित एवं नवीन तेज से वैसे ही प्रकाशित कर रहे हैं, जैसे कि पहले प्रकाशित करते थे
- **Translation**: 

---

### Verse 6 (Rig Ved 0.10386)
- **Original**: 4515, प्र व: सखायो अग्नये स्तोम॑ यज्ञ च धृष्णुया। अर्च गाय च वेधसे
- **Translation**: 

---

### Verse 7 (Rig Ved 0.10387)
- **Original**: हे ऋत्विजो ! आप ईश्वर के समान शक्तिमान्‌ और शत्रुविनाशक अग्निदेव को आहुतियों एवं उत्तम स्तुतियों द्वारा प्रसन्न करें
- **Translation**: 

---

### Verse 8 (Rig Ved 0.10388)
- **Original**: 4516, स॒ हि यो मानुषा युगा सीदद्धोता कविक्रतु: । दूतश्न हव्यवाहन:
- **Translation**: 

---

### Verse 9 (Rig Ved 0.10389)
- **Original**: 22 ऋग्वेद संहिता भाग - 2 जो अग्निदेव मेधावी, हविवाहक एवं यज्ञकर्म में देवटूत और देवों का आवाहन करते हैं, वे अग्निदेव हमारे इस यज्ञ में कुशाओं पर प्रतिष्ठित हों
- **Translation**: 

---

### Verse 10 (Rig Ved 0.10390)
- **Original**: 4517. ता राजाना शुचित्रतादित्यान्मारुतं गणम्‌
- **Translation**: 

---

### Verse 11 (Rig Ved 0.10391)
- **Original**: वसो यक्षीह रोदसी
- **Translation**: 

---

### Verse 12 (Rig Ved 0.10392)
- **Original**: है अग्निदेव ! आप इस यज्ञ में आएँ और प्रसिद्ध, शुभकर्म करने वाले मित्रावरुण, मरुत्‌ एवं द्यावा-पृथिवों के लिए यजन करें । आप श्रेष्ठ निवास्त प्रदान करते हैं
- **Translation**: 

---

### Verse 13 (Rig Ved 0.10393)
- **Original**: 4518. बस्यी ते अग्ने सन्दृष्टिरिषयते मर्त्याय। ऊर्जो नपादमृतस्य
- **Translation**: 

---

### Verse 14 (Rig Ved 0.10394)
- **Original**: है अग्निदिव ! आप अमर एवं बलशाली हैं । आप की सतेज दृष्टि (कृपा) अन्न की इच्छा वाले याजकों को अन्न-धन प्रदान कराती है
- **Translation**: 

---

### Verse 15 (Rig Ved 0.10395)
- **Original**: 4519. क्रत्वा दा अस्तु श्रेष्ठोउद्य त्वा वन्वन्त्सुरेक्णा:
- **Translation**: 

---

### Verse 16 (Rig Ved 0.10396)
- **Original**: पर्त आनाश सुवृक्तिम्‌
- **Translation**: 

---

### Verse 17 (Rig Ved 0.10397)
- **Original**: है अभ्विदेव ! आज याजक आपकी सेवा (यज्ञ) करने वाले एवं श्रेष्ठकर्म करने वाले बनें । वे सदेव हो उत्तम सम्भाषण करें
- **Translation**: 

---

### Verse 18 (Rig Ved 0.10398)
- **Original**: 4520. ते ते अग्ने त्वोता इषयन्तो विश्वमायु:। तरन्तो अर्यो अरातीर्वन्वन्तो अर्यों अराती:
- **Translation**: 

---

### Verse 19 (Rig Ved 0.10399)
- **Original**: है अग्निदेव ! आपकी स्तुति करने वाले आपकी सुरक्षा में रहकर, शत्रुओं की सेना को जीतकर , शत्रुओं का नाश करते हैं एवं पूर्ण आयु तक अन्नादि सहित सुखों से पूर्ण जीवन व्यतीत करते हैं
- **Translation**: 

---

### Verse 20 (Rig Ved 0.10400)
- **Original**: 4521. अग्निस्तिग्मेन शोचिषा यासद्विश्व॑ न्यश्त्रिणम्‌। अग्निनों बनते रयिम्‌
- **Translation**: 

---

